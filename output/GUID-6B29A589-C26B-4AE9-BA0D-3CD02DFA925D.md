# Examples and FAQ

This section contains examples of the Network program and a link to the
FAQ chapter.

[Example
1: Listing links to the print file](GUID-6B29A589-C26B-4AE9-BA0D-3CD02DFA925D.html#GUID-6B29A589-C26B-4AE9-BA0D-3CD02DFA925D__EXAMPLE1_unique_5)

[Example
2: Merging link records from multiple ASCII files](GUID-6B29A589-C26B-4AE9-BA0D-3CD02DFA925D.html#GUID-6B29A589-C26B-4AE9-BA0D-3CD02DFA925D__EXAMPLE2_unique_3)

[Example
3: Dumping link and node records to DBF files excluding select fields](GUID-6B29A589-C26B-4AE9-BA0D-3CD02DFA925D.html#GUID-6B29A589-C26B-4AE9-BA0D-3CD02DFA925D__EXAMPLE3_unique_2)

[Example
4: Building network from inline data records](GUID-6B29A589-C26B-4AE9-BA0D-3CD02DFA925D.html#GUID-6B29A589-C26B-4AE9-BA0D-3CD02DFA925D__EXAMPLE4_unique_1)

[Example
5: Simple link plot](GUID-6B29A589-C26B-4AE9-BA0D-3CD02DFA925D.html#GUID-6B29A589-C26B-4AE9-BA0D-3CD02DFA925D__EXAMPLE5_unique_1)

[Example
6: Complex plot](GUID-6B29A589-C26B-4AE9-BA0D-3CD02DFA925D.html#GUID-6B29A589-C26B-4AE9-BA0D-3CD02DFA925D__EXAMPLE6_unique_1)

[Frequently
asked questions](GUID-6B29A589-C26B-4AE9-BA0D-3CD02DFA925D.html#GUID-6B29A589-C26B-4AE9-BA0D-3CD02DFA925D__FAQ_unique_3)

Example 1: Listing links to the print
file

```
run pgm=NETWORK ; List the links in a network
    neti=demo20.net
    list=a,b
endrun
```

Example 2: Merging link records from multiple
ASCII files

```
run pgm=NETWORK ; merge two ASCII files with different links
    linki[1]=demo07.dat,var=a,2,4, b,7,4, dist,14,4, v1,2,4, v2,2,4
    linki[3]=demo07m.dat,rev=2,
        var=a,2,4, b,7,4, dist2,14,4, rev,35,1, v1,2,4, v2,2,4
    nodei[1]=c:\demo\demoxy.dat,var=n,x,y
    merge record=true, AVE=dist
    report all=no
    zones=19
    phase=LINKMERGE
      if (li.1.a == 0) list=' LI[1] missing link:', a,b
      if (li.3.a == 0) list=' LI[3] missing link:' a,b
   endphase
endrun
```

Example 3: Dumping link and node records to DBF
files excluding select fields

```
run pgm=NETWORK     ; write DBFs for nodes and links,
                    ; but exclude many variables from input
  neti=test.Hnt
  neto=test.tpn,
      EXCLUDE=  SCENARIO  STATUS  NAME  TPCAP1  TPCAP2  TIPRTP  CNT,
      EXCLUDE=  FIELDOPT  TCNUMBER  COUNTY  USER  DATE  OCOUNTA  OCOUNTP,
      EXCLUDE=  OCOUNTD  OSPEEDA  OSPEEDP  OSPEEDD,
      EXCLUDE=  OSPEEDX  OSPEEDY  ECOUNTA  ECOUNTP  ECOUNTD  ECOUNTY,
      EXCLUDE=  ESPEEDA  ESPEEDP  ESPEEDD  ESPEEDY  COMMENT6  COMMENT1,
      EXCLUDE=  ATYPE
  nodeo=testxy
  linko=testld
  if (STATUS=='D' || ft==15) delete
endrun
run pgm=NETWORK ;now look at the results from the link DBF
      linki=testld.dbf
      nodei=testxy.dbf,exclude=xcoor,ycoor
      If (a>b && lanes > 4) list=a,b,lanes
endrun
```

Example 4: Building network from inline data
records

```
copy file=3pth.lxy ; copy data from inline to a file
LD
1    1     10   1000   60   60   4   1   S23456
2    1     11   2000   60   60   8   1
3    1     12   2500   60   60   6   1
4    10    2    0      0    60   4   1
5    11    2    0      0    60   8   1
6    12    2    0      0    60   6   1
XY
1  1   100  200
2  10  200  300
3  11  200  200
4  12  200  100
5  2   300  200
endcopy
id=this is my ID... pagewidth=80
RUN PGM=NETWORK ; now build a network from the inline data
  merge record=y
  nodes=20 zones=2 nodei[3]=3pth.lxy,var=n1,n,x,y,
    start=(substr(record,1,2)=='XY'),
    stop=(substr(record,1,2)=='LD')
  linki[2]=3pth.lxy,var=n3,a,b,dist,tsva1,spdc1,capc1,lane1,string1,typ=a,
     start=(substr(record,1,2)=='LD') ,
     stop=(substr(record,1,2)=='XY')
  list=a,b,dist
ENDRUN
```

Example 5: Simple link plot

```
; Sample Quickie plot with no parameters: draw links only
RUN PGM=NETWORK      ; sample quick link plot
    NETI = C:\DEMO\DEMO20.DAT
    PLOTTER DEVICE = "HP 7475A", FILE=f:\sample.plt
    DRAWLINK=0xffff
ENDRUN
```

Example 6: Complex plot

```
;This sample illustrates various capabilities of plotting.
RUN PGM=NETWORK
  NETI = C:\DEMO\DEMO20.DAT
  PLOTTER { ; SETUP Plotter
      DEVICE="HP LASERJET 4"
      POSTLINKVAR=A,B,_AB,_STR
          FONT='COURIER',0.10,YELLOW,BOLD
          POST=AUTOSIZE(.05)
      POSTNODEVAR=A, FONT='COURIER',.10 LINKOFFSET=0.01
      BANDWIDTH=_BANDWIDTH FILL=SOLID TAPER=45
      HEADER= "This is header 1",
              "This is header 2",
              align=center, font='courier' ,0.1,green
      FOOTER="Footer 1"
      FOOTER[3]="Footer 3"
      FOOTER[5]='Shows various date tokens: [date]  [idate]'
      FOOTER[7]='Shows various time tokens: [time]  [times]',
      FOOTER[7]='Shows window and scale tokens: [window] [scale]'
          align=right font='Courier',0.15,green
      LEGEND=TopLeft, font='courier',.10,blue,italics,
          LINE[1]=TL.LINE1,symbol=triangle,.15,red
          LINE[5]=tl.line5,symbol=Dash,.15,red
      LEGEND=TR, font='courier',.20,blue,italics,
          LINE[1]=TR.LINE1,symbol=triangle,.5,red
          LINE[3]=tr.TRne3,symbol=rectangle,.08,red
      LEGEND=3, font='courier',.10,red,italics,
          LINE[1]=BL.LINE1,symbol=circle,.10,red
          LINE[5]=BL.line5,symbol=dashdot,.15,red
      LEGEND=BottomRight font='courier',.15,purple,italics,
          LINE[2]=BR.LINE2,symbol=triangle,.15,red
  }
; Plotting Controls
  if (a<=19 || b<=19) _BANDWIDTH = lane/10
  _AB = A*100 + B
  _STR = str(_ab/100,5,2)
  DRAWLINK=RED,,SOLID, LINKPOST=GREEN
  IF (A.X == B.X || A.Y == B.Y) LINKPOST=BLUE; FLAT|VERTICAL LINES
  DRAWA=BLUE,0.20,CIRCLE,YELLOW
  NODEPOST=r123b220g100,.1
  IF (A>=30 && A <40) LINK=GREEN,,DASH ; reset the color of these links
; set node postings and symbols
  IF (A<=5) DRAWA=RED,0.10,CIRCLE,WHITE NODEPOST=0XFF00FF
  IF (A>5 && A<=10) DRAWA=RED ,0.40 CIRCLE NODEPOST=G255
  IF (A>10 && A<20) DRAWA=R255,0.15,RECTANGLE,BLACK NODEPOST=R255
ENDRUN
```

Frequently asked questions

Please see [FAQ -
Network in Frequently Asked Questions.](GUID-B5B400F2-F9D2-45E7-9704-332285F59926.html)

**Parent topic:**  [Network Program](GUID-7B7F2E2B-1D37-43F4-B390-965753B42391.html)

|
|  |
|
|  |
