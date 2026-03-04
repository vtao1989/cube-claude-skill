# A note on CPU cores and memory in parallel computing

For the purposes of a discussion of the
Analyst Drive program, we will discuss two types of
cores,
Physical and
Virtual. A physical core is one that is actually
present on a CPU, while a virtual core represents a thread process which can
use a physical CPU core. CPUs that employ hyperthreading can have more virtual
cores than physical CPU cores. This can be beneficial as the virtual core can
perform a computation on a physical core while another virtual core may be busy
fetching data and is not ready to execute and would otherwise leave the core
idle. We will also discuss two types of memory,
shared and
distributed. Shared memory is local to a processor
(or several processors) and has cache coherence, meaning that all CPU cores
that use the same shared memory can access all shared data. You can think of
your desktop or laptop computer as a shared memory computer. On the other hand,
a distributed memory computer has disjoint memory sets; thus a CPU core on such
a system cannot share information with another core without using some type of
message passing.

Most modern computing clusters have hybrid memories; in
other words: shared memory within some processors of a single compute node, and
several disjoint compute nodes which make up the cluster. This is important
information to consider when running a modern parallel program. The
Analyst Drive program employs simple threading for
shared memory systems so that the benefits of parallelism with cache coherence
can be realized, providing large benefits even on a simple desktop or laptop
computer with a multicore CPU. At a higher level,
Analyst Drive is built using a message passing library
so that it can use the parallelism available to distributed memory clusters,
but at the same time can be used on a shared memory system. While the shared
memory threads defined by the
[NCORES](GUID-E23E89B8-1CBA-41D1-A643-788A7C2CC72B.html) parameter are lightweight and dynamic (they are
created and destroyed as needed), the distributed memory threads of the
[MPICORES](GUID-539DD601-CF95-495D-8993-D058970BF046.html) parameter are heavy and static. These threads
launch separate processes and will remain active throughout the life of the
program. When running Analyst Drive for a single user class problem it is
optimal to set
[NCORES](GUID-E23E89B8-1CBA-41D1-A643-788A7C2CC72B.html)to the number of virtual cores present on the computer. When
running
Analyst Drive with the
[MPICORES](GUID-539DD601-CF95-495D-8993-D058970BF046.html) parameter in addition to
[NCORES](GUID-E23E89B8-1CBA-41D1-A643-788A7C2CC72B.html), the optimal choice depends on the computer setup and
the number of user classes to be run.

This choice can be a challenging decision to the
inexperienced user. In the next section,
[Performance metrics with NCORES and MPICORES](GUID-3FBC41FD-7835-48E5-B5CD-F413FA6F147E.html), guidance is
provided through the examination of some performance metrics for a set of cases
that use the two parameters.

**Parent topic:**  [Notes and Best
Practices](GUID-0A491153-77C8-4A0A-A09B-F4D79A7F7BA1.html)

|
|  |
|
|  |
