"""
Scraper for Bentley CUBE 7 documentation.

Key findings:
- All GUID pages are static HTML (no JS rendering needed)
- Full topic list: suitehelp_topic_list.html (384 pages)
- Content selector: div.mainbody
- Title: in <title> tag or meta content="..." name="DC.Title"

Usage:
    pip install -r requirements.txt
    python scraper.py
"""

import re
import time
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

BASE_URL = "https://docs.bentley.com/LiveContent/web/CUBE%207-v1/en/"
TOPIC_LIST_URL = BASE_URL + "suitehelp_topic_list.html"
OUTPUT_DIR = Path("output")
FAILED_LOG = Path("failed.txt")

REQUEST_DELAY = 0.5  # seconds between requests

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


def get_page(session: requests.Session, url: str) -> str | None:
    """Fetch a page and return its HTML, or None on failure."""
    try:
        resp = session.get(url, timeout=20, headers=HEADERS)
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        print(f"  FETCH ERROR {url}: {e}")
        return None


def extract_guid_links(html: str, base_url: str) -> list[str]:
    """Extract all GUID-*.html links from HTML, returning absolute URLs."""
    soup = BeautifulSoup(html, "html.parser")
    seen = set()
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if re.match(r"GUID-[A-F0-9\-]+\.html$", href, re.IGNORECASE):
            abs_url = urljoin(base_url, href)
            if abs_url not in seen:
                seen.add(abs_url)
                links.append(abs_url)
    return links


def parse_page(html: str, url: str) -> tuple[str, str]:
    """
    Parse a GUID page and return (title, markdown_content).
    """
    soup = BeautifulSoup(html, "html.parser")

    # Title: prefer DC.Title meta, fallback to <title>
    title = ""
    dc_title = soup.find("meta", attrs={"name": "DC.Title"})
    if dc_title and dc_title.get("content", "").strip():
        title = dc_title["content"].strip()
    if not title:
        title_tag = soup.find("title")
        if title_tag:
            title = title_tag.get_text(strip=True)
    if not title:
        title = url.split("/")[-1].replace(".html", "")

    # Content: div.mainbody
    mainbody = soup.find("div", class_="mainbody")
    if not mainbody:
        # fallback: article tag
        mainbody = soup.find("article")
    if not mainbody:
        return title, f"# {title}\n\n*(No content found)*\n"

    # Convert to Markdown
    content_html = str(mainbody)
    text = md(
        content_html,
        heading_style="ATX",
        bullets="-",
        strip=["script", "style"],
    )
    # Collapse excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return title, text.strip() + "\n"


def url_to_filename(url: str) -> str:
    basename = url.split("/")[-1]
    return re.sub(r"\.html$", ".md", basename, flags=re.IGNORECASE)


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    session = requests.Session()

    print(f"Fetching topic list from: {TOPIC_LIST_URL}")
    topic_list_html = get_page(session, TOPIC_LIST_URL)
    if not topic_list_html:
        print("ERROR: Could not fetch topic list. Aborting.")
        return

    all_urls = extract_guid_links(topic_list_html, BASE_URL)
    print(f"Found {len(all_urls)} pages in topic list.")

    # Also discover any additional links by crawling (belt-and-suspenders)
    # We'll add newly found URLs not already in the list
    visited: set[str] = set()
    queue: list[str] = list(all_urls)
    index_entries: list[tuple[str, str]] = []
    failed: list[str] = []

    while queue:
        url = queue.pop(0)
        if url in visited:
            continue
        visited.add(url)

        filename = url_to_filename(url)
        print(f"[{len(visited)}/{len(visited) + len(queue)}] {filename}")

        html = get_page(session, url)
        if html is None:
            failed.append(url)
            time.sleep(REQUEST_DELAY)
            continue

        title, markdown = parse_page(html, url)

        # Save file
        output_path = OUTPUT_DIR / filename
        output_path.write_text(markdown, encoding="utf-8")
        index_entries.append((title, filename))

        # Discover additional links not already queued
        new_links = extract_guid_links(html, url)
        added = 0
        for link in new_links:
            if link not in visited and link not in queue:
                queue.append(link)
                added += 1
        if added:
            print(f"  +{added} new links discovered (queue: {len(queue)})")

        time.sleep(REQUEST_DELAY)

    # Write index.md
    index_lines = ["# CUBE 7 Documentation Index\n"]
    for title, filename in index_entries:
        index_lines.append(f"- [{title}]({filename})")
    (OUTPUT_DIR / "index.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")

    print(f"\n{'='*50}")
    print(f"Done. {len(index_entries)} pages saved to {OUTPUT_DIR}/")
    print(f"Index: {OUTPUT_DIR}/index.md")

    if failed:
        FAILED_LOG.write_text("\n".join(failed) + "\n", encoding="utf-8")
        print(f"Failed ({len(failed)}): see failed.txt")
    else:
        print("No failures.")


if __name__ == "__main__":
    main()
