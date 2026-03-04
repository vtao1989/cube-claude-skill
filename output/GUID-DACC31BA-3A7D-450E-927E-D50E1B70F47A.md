# Utilities

This section describes:

- [Cluster executable](GUID-DACC31BA-3A7D-450E-927E-D50E1B70F47A.html#GUID-DACC31BA-3A7D-450E-927E-D50E1B70F47A__LI_BDA3EDA3BD7042E6A97C02859D962274)
- [Utility functions](GUID-DACC31BA-3A7D-450E-927E-D50E1B70F47A.html#GUID-DACC31BA-3A7D-450E-927E-D50E1B70F47A__LI_A2792C3C77404A77AB0E16F61A3ACC3D)

Cluster executable

You may use the cluster.exe utility program to start
multiple processing nodes on the local machine. In this section there is
information on:

- [Cluster Dialog Box](GUID-DACC31BA-3A7D-450E-927E-D50E1B70F47A.html#GUID-DACC31BA-3A7D-450E-927E-D50E1B70F47A__LI_D16BEB6207EE496C8B16C3759AEF0571)
- [Running Cluster from the Command Line](GUID-DACC31BA-3A7D-450E-927E-D50E1B70F47A.html#GUID-DACC31BA-3A7D-450E-927E-D50E1B70F47A__LI_4328BE6FF3FA47E9A5258169FCAF97BF)
- [Starting processing nodes in CUBE Cluster](GUID-DACC31BA-3A7D-450E-927E-D50E1B70F47A.html#GUID-DACC31BA-3A7D-450E-927E-D50E1B70F47A__LI_0CF4029C6A8E4AFB8A3D6EB355D3400C)

Cluster Dialog Box

Go to File
 > Tools
 > Cluster Node
Managementto open the Cluster Node Management dialog
box.

![](GUID-BC2DADBD-43D3-4532-87A6-E5D537C36F17-low.png)

- Select the
  Work Directory and
  Process ID of the desired Cluster processes.
  Click
  Browse to pick a folder from the local system,
  or remote network.
- Under
  Process List, enter the applicable Process
  IDs.
- In
  Time to Wait for Response, enter the number of
  seconds CUBE Cluster should wait for a response from a node before determining
  that the node is unavailable.
- Click
  List Nodes
  to return the status of all processing nodes within the
  chosen Work Directory.
- Click
  Start Nodes to start all listed processing
  nodes (remote or local). Or, click
  Start Selected to only start the selected
  node(s).
- Click
  Close Nodes to close all listed processing
  node (remote or local). Or, click
  Close Selected to only close the selected
  node(s).
- Check
  Hide New Nodes
  to minimize cluster nodes to the system tray. The nodes
  will be hidden after they are Started. This is the same as clicking Hide on the
  associated Voyager instance. Hiding is useful when the user wishes to minimize
  window clutter.

Running Cluster from the Command Line

You can also run this program from a Windows command line.
Therefore, you can run the program from either a .bat batch file or from a CUBE
Voyager \* command call. The syntax for the command line is:

```
Cluster [ProcID] [ProcList] [Start/Starthide/Close/List]
[Exit]
```

These command line options correspond to the Cluster dialog
box shown above.

Starting processing nodes in CUBE
Cluster

Prior to starting a distributed-processing run using CUBE
Cluster, individual instances of CUBE Voyager must be running and set to wait
mode with the appropriate script file name and work directory for the run. A
CUBE Cluster processing node corresponds to a single, properly configured
instance of CUBE Voyager running and waiting. Processing nodes can either be
additional processors on the local computer (local nodes) or processors on
remote computers connected to the main computer over a local network (remote
nodes). You can start an instance of CUBE Voyager manually by running the
Voyager.exe program in the CUBE Voyager program directory and setting the
script and working directory, or by running the Cluster.exe program as
described in
[Cluster executable](GUID-DACC31BA-3A7D-450E-927E-D50E1B70F47A.html#GUID-DACC31BA-3A7D-450E-927E-D50E1B70F47A__LI_BDA3EDA3BD7042E6A97C02859D962274).

You cannot start instances of CUBE Voyager on remote nodes
over a network. You must start remote nodes directly on the remote machines.
Typically, you must physically go to each machine and run either the
Voyager.exe or the Cluster.exe program on that machine. Alternatively, you can
use the
COMMPATH keyword to send information to active
instances of CUBE Voyager, which are open and running on remote processing
nodes. Use
COMMPATH to send changes in script and working
directory names to waiting instances of CUBE Voyager without having to
physically visit each machine and make changes manually.

You use COMMPATH only for initial
communication with the node. The node will switch its work directory to be the
same as the main process before running the multistep distributed process.
After completing the steps, the node reverts to waiting for the communication
file in the
COMMPATH directory. Bentley recommends starting an
instance of CUBE Voyager on each remote processor that you will use, setting
the work directory to a common path like z:wait, and leaving them run. Then,
you can use this value as the COMMPATH
keyword value.

Utility functions

A number of utility functions were added to the CUBE
Voyager system to allow more flexibility in performing distributed processing:

- FilesExist(âfile1|file2|file3â¦â) â This function will
  check for the existence of one or more files. The function takes one string
  argument (constant or variable) and if there are more than one file to check,
  they are put into one string and separated by â|â. The return value is the
  number of files that exist. If none of the files exist, then the return value
  will be zero. This can be use instead of the Wait4Files command if you only
  want to check if a node is done but donât want to wait for it to get done.
- NumReadyNodes(âProcessIDâ,âProcessListâ) â This
  function will check for availability of a list of CUBE Cluster nodes. The
  second argument is a string with the list of process numbers to check. The
  return value is the number of ready nodes. For example,
  NumReadyNodes(âTestDistâ,â1-5,10,15-20â) or
  NumReadyNodes(MyProcess,MyProcessList)
- FirstReadyNode(âProcessIDâ,âProcessListâ) â This
  function will check for availability of a list of CUBE Cluster nodes and return
  the process number of the first available node. The second argument is a string
  with the list of process numbers to check. The processes are checked in the
  input order and can go from low to high or high to low so if the list is â6-2â
  and all processes (2-6) are available, the result will be 6. For example,
  FirstReadyNode(âTestDistâ,â1-5,10,15-20â)

  The following is an example for using the NumReadyNodes
  function when there are two separate groups of CUBE Cluster nodes that may be
  available to participate in a DP run, the script wants to select the one with
  the most available nodes:

  ```
  IF (NumReadyNodes(âDP1â,â1-10â) > NumReadyNodes(âDP2â,â11-20â))
  MyProcessID=âDP1â
  MyProcessList=â1-10â
  ELSE
  MyProcessID=âDP2â
  MyProcessList=â11-20â
  ENDIF
  RUN PGM=Matrix
  DistributeIntraStep ProcessID=@MyProcessID@, ProcessList=@MyProcessList@
  ```

**Parent topic:** [CUBE Cluster](GUID-413908B0-27A9-4741-AD3D-477817641737.html)

|
|  |
|
|  |
