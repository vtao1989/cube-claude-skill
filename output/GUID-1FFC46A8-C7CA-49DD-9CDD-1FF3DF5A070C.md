# Partial Trip Data Preparation

The partial trip data file format is similar to the dynamic
screenline files with a couple of exceptions. First, it must include two nodes
corresponding to paired detector locations similar to nodes A and B as in the
screenline case but here the two nodes are not required to be directly
connected on the network. We will refer to these detector nodes as DNode A and
DNode B to avoid confusion with the connected screenline and turncount nodes.
The other key difference is the inclusion of a scaling factor for each partial
trip data set corresponding to a paired detector location, this value
corresponds to
S in Equation 11. Once the user has identified all
detector pairs and their corresponding scaling factors, they may set up the
dynamic partial trip data file using corresponding counts for each time
interval. The general format for a partial trip data file using the equation
notation above can thus be given as

![](GUID-2BB20CD1-19EB-48B6-999B-BBA6CC192682-low.png)

where t=time segment, and N=total number of time segments.

The confidence values
Vc are optional. Note that unlike the screenline and
turncount case, confidence values for partial trip data counts must take into
consideration the validity of the scaling factor in addition to any uncertainty
in the count itself. An example partial trip data file is provided in Figure
18.

**Parent topic:**  [Using Partial Trip
Data in Analyst Drive](GUID-F3E60FC1-1A51-4310-9D62-F2F02C6D918C.html)

|
|  |
|
|  |
