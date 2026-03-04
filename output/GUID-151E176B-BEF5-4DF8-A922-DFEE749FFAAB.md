# MEMOPT1

Type = Logical

Default = T

Perform level-1 memory optimizations for dynamic
estimation. This option requires at least 12\*NPKT\*(PKTLNG+2) bytes of available
memory, where NPKT is the number of packets and PKTLNG is the largest packet
size in the
Cube Avenue-generated packet log file. These values
can be found in the header of the packet log file. Enabling this option allows
the packet log file to be processed in memory which is substantially faster
than file-based processing, but may require a large amount of memory. If the
user encounters a
FILE\_ERROR=199 (see Â[File error
codes](GUID-2A561428-A116-4166-9BD0-A8F23D2B69B4.html)Â on page 84), they should ensure that they have enough available
memory and uncheck this option if necessary.

**Parent topic:** [Options](GUID-10019297-039D-47CE-BC92-61F1C3D829EA.html)

|
|  |
|
|  |
