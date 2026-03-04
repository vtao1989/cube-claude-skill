# CUBE 7 Voyager Cluster Changes Summary

The new topology of a cluster system involves a "Cluster
Manager" process on each node that controls communications with other "Cluster
Managers" on other nodes, and with it's own collection of "slave" nodes.

There is no longer any need to manually start slaves on
each node - that is handled by the Cluster Manager and is configured in the
initial Pilot script. The Cluster Manager on the node the "master" node is
executing on will contact each of the required Cluster Manager nodes and start
the required number of nodes on each.

Error detection has been improved - if any nodes fail, they
trigger a failure for all nodes in the run and the entire run will cleanly
exit.

Slaves are now simply allocated an ID, and no specification
of "process name" and number is required - any node from the pool that can
perform the task is used. Intrastep tasks simply request the number of nodes
desired. This ensures that multiple requests for the same node are now no
longer possible.

A separate wait function has been implemented for Pilot for
multi-step operations - "BARRIER". WAIT4FILES still exists, but as it only
operates on files, it no longer functions as a wait for cluster operations to
complete.

![](GUID-FBCB26A0-22B3-4DFB-91A1-2A59B6359492-low.jpg)

**Parent topic:**  [CUBE 7 Cluster](GUID-FD716A57-7ABC-4A28-AD21-864024D61908.html)

|
|  |
|
|  |
