# Application of the Matrix API with CubePy

The Matrix API is primarily a file-based API, working with
CUBE 7 Matrix files. CUBE 7 Matrix files are HDF5 format matrices.

CUBE Matrix files store multiple square matrices, with
dimension that is given by the number of zones, in transportation terms, as
zones x zones matrices. It is also possible to associate multiple zonal
references to the matrices, to provide a meaningful string or numeric reference
to the zone index.

The CubeMatrix is indexed by "int", which is a 32-bit signed
int. Technical zone limit is therefore 232/2 (maximum integer for
the index).

**[Opening a CUBE Matrix
file with the CubeMatrixFile Class](GUID-44666D61-7D18-4C90-92F8-A545758A1E31.html)**

**[Connecting to a matrix
with the CubeMatrix Class](GUID-0C56A2E2-E0BD-4705-BF83-D7DA1B265088.html)**

**[Create a multi-tab
matrix](GUID-E2EC7E22-7DA0-467D-BEC2-F5AB9F20C801.html)**

**[Handling Matrix
Attributes](GUID-309A7B91-D6D8-4E90-A3B9-B8DE500B2E72.html)**

**Parent topic:** [CubePy for Beginners](GUID-72BBF685-9C8E-41E8-87BF-862F8F834752.html)

|
|  |
|
|  |
