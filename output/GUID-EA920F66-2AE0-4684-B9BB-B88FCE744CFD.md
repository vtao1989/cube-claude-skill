# TOL

Type = Real(+)

Default = 0.0

Range = 0.0-0.0001

Convergence tolerance; this is the minimum Î± value that can be achieved
before convergence, where Î± is the step length used in the conjugate gradient
step of the estimation algorithm. In most cases, this value should be set
rather low. If the user wishes to rely more on the
[MAXITER](GUID-1A4B526D-0A32-4F91-8267-21D57A1B78D1.html)
parameter for terminating the program, it should be left as the default value
of 0.0. Note that using any tolerance value greater than 0.0 can cause the
program to terminate before finding the minimum value of the cost function, and
so is only recommended to be set for problems which run excessively large
numbers of iterations due to slow convergence in which case terminating the
program early is beneficial from a time cost standpoint.

**Parent topic:**  [Parameters](GUID-BE49B418-D604-498C-9957-1B26EC5E26EF.html)

|
|  |
|
|  |
