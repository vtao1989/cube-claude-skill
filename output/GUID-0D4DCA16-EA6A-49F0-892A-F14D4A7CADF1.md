# OD matrix file

A single input matrix file should be provided to the
Analyst Drive program. The matrix input file will
define the proper ordering of the user classes being estimated, and
consequently the order for the listing of screenline and ICP files that must be
followed in the control file or the
Application Manger diagram block. When using
confidence matrices, they must be contained in the same matrix file, and the
tab number of the confidence matrix should immediately follow the corresponding
OD matrix tab number. As a simple example, if there are two user classes and
confidence matrices are to be included in the input matrix file then the first
tab of the OD matrix file would correspond to the OD matrix of user class one,
the second tab to the confidence matrix corresponding to the first OD matrix,
the third tab would be the OD matrix for user class two and then the fourth tab
would correspond to the confidence matrix for user class two. When using the
[CONFMAT](GUID-E195EAE8-D5ED-4873-AC1B-BF2F187D9C46.html)=T option, all OD matrices must have a confidence
matrix. Note that one can include confidence matrices with input OD matrices
but choose not to use them in the estimation process by selecting the
[USECONF](GUID-5646C0C4-C3E6-4DBD-9B3F-1272327C770E.html)=F option.

**Parent topic:**  [Input files for static
estimation](GUID-C9DFFA8E-1425-4026-9E22-D901AE7B286C.html)

|
|  |
|
|  |
