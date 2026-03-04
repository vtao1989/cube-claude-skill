# Troubleshooting

| Error | Details |
| --- | --- |
| File sharing lock count exceeded | This is an error message from Microsoft Access indicating the number of locks required to perform a transaction exceeds the maximum number of locks per file. This value can be modified using the CUBE installer (License agreement > "Advanced Options" > "Max Locks Setting"). 200000 is the recommended default value, but this may need to be increased when dealing with larger recordsets. There are other options for modifying this setting here: support.microsoft.com/kb/815281 |
| InsertBufferedFeatureException | InsertBufferedFeatureException occurs when strings longer than 252 characters are being imported into a field. In this case, CUBE will automatically truncate the strings (with the last three characters being "â¦"). |

**Parent topic:**  [Public Transport](GUID-A90E32B1-BFB1-40F1-A921-7BC202F0A562.html)

|
|  |
|
|  |
