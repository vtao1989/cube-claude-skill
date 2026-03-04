# GIS Editor Overview

GIS Editor is the mapping window that allows to visualize
and edit highway networks, transit and non-transit data, polygon layers and
other geosapatial data. Through GIS Editor it is possible to customize each
layer's visualization and save the overall map, with all the added layers and
its settings, as a .cube-map.

GIS Editor can be accessed by
File > New > Map.
This will open a New Map tab where you can start adding and editing layers.

Alternatively whenever you attempt to open a geospatial
data file (.SQLite, .NET,.GDB, .SHP) CUBE will automatically try to open it in
GIS Editor. Opening these data types can be done through

- File > Open > Select
  the geospatial Data File
- Drag and Drop a geospatial
  data file from File Explorer
- Opening a geosapatial data
  file in a project from File Browser

Customizing a map through symbols, labels, charts, base
maps and other capabilities like trip distribution maps and shortest path
rendering is available through GIS Editor. For more information and video
tutorials on these topics see
[Mapping](GUID-AC06BFFC-7004-4E72-B0A2-80E7A6B557CB.html)

Additionally it is possible to use Lua Expressions and
other network functions in the GIS Layer Properties window, for Rendering and
Labeling your maps.

Network Editing

GIS Editor allows to create, remove and edit network
components like links and nodes, as well as transit lines and non-transit legs
for transit/non transit networks. For more detailed instructions and videos on
how to edit networks see
[Highway Network Editing](GUID-0CE4BDAE-15B1-4D1A-8AF3-6728B14472F6.html)and [Transit Network Editing](GUID-91547DB6-3C38-46C8-9A76-6D8628FEA7C7.html)

Note: Only CUBE database
files (.SQLite) networks can be modified through GIS Editor. See the File
Editing section in
[File Formats in CUBE 7](GUID-9F262E99-CBF5-4613-989E-74A5B6E7F39C.html)for more information

You can also access and edit individual component's
information (attributes) through the Feature Table, which will display that
particular element's data whenever it has been selected in the map.

**Parent topic:** [GIS Editor](GUID-ECB5431B-B41F-4FA5-9C2D-2E4E01CAD7AB.html)

|
|  |
|
|  |
