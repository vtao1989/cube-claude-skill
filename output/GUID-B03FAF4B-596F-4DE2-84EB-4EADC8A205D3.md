# Including Partial Trip Data

To include partial trip data in the estimation procedure
one must link a partial trip data file for each user class being estimated. In
application manager, the
Analyst Drive module block has been updated with
positions provided for including partial trip data files which can be seen in
[Figure 19](GUID-7EA1B617-55BA-45CD-AB09-6E2AE3983371.html).

![](GUID-A6FFD57F-997F-4819-A84D-15EF2535E4C1-low.png)

Figure 18: Example Partial Trip Data
File

Additionally, the user may wish to adjust the
[PARTFCTR](GUID-093D3973-9A09-4ECC-9F0D-7927450E4658.html)parameter which scales the partial trip data contribution to the
cost function in the same manner as the
[TURNFCTR](GUID-FE5813FD-9344-4A91-9BAE-38B6EDD4C3DF.html) parameter does for dynamic estimation with turning
counts. Increasing
[PARTFCTR](GUID-093D3973-9A09-4ECC-9F0D-7927450E4658.html) will increase the cost function contribution to
the partial trip count data in the estimation procedure and hence the program
will be weighted more toward matching these counts in relation to the other
counts on an all else equal basis.

**Parent topic:**  [Using Partial Trip
Data in Analyst Drive](GUID-F3E60FC1-1A51-4310-9D62-F2F02C6D918C.html)

|
|  |
|
|  |
