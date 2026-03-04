# Setting up Pre/Post processing networks

To run your imported model using CUBE Voyager, your CUBE 7
formatted networks and datasets need to be converted back to the appropriate
Voyager supported file formats. CUBE 7 supports visualization of the CUBE .net
file formats and there might not be a need to convert the output networks to
CUBE 7 formats unless the output networks need to be further edited. The
conversion process (both ways) can be scripted and automated as part of your
model run process. CUBE 7 comes with a converter utility which can be called
inside a CubePy program to handle the conversions. An example implementation of
the pre/processing is provided in the attached CUBE 7 project below:

[CUBE\_Pre\_Post\_Process\_example](HTTPS://COMMUNITIES.BENTLEY.COM/PRODUCTS/BETAS/CUBE-CE-V7-0-EARLY-ACCESS/M/CUBE-CE-V7-0-FILES)

To find out how to set up a CubePy program check the
tutorial:
[Adding CubePy programs](GUID-8BD83231-32D9-4049-94AF-1674D40158D9.html)

Note: When opening your
CUBE 6 networks (.net) in CUBE 7, by default the map will be set to use spatial
Reference EPSG: 3857 WGS 84 / Pseudo-Mercator, since CUBE 6 .net networks do
not have any spatial reference associated with them. You can change the default
spatial reference by going to:
Tools > Options > GIS
and set the SRID corresponding to the network (use the SRID in your input CUBE
database file). For a list of supported spatial reference ids, please refer to
[https://spatialreference.org/](HTTPS://SPATIALREFERENCE.ORG/)

**Parent topic:**  [Moving to CUBE 7](GUID-7C6798F6-C733-4659-BDF2-22E58E4FB12C.html)

|
|  |
|
|  |
