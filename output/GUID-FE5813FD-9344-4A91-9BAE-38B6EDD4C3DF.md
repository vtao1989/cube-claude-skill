# TURNFCTR

Type = Real(+)

Default = 1.0

The weighting factor to use for the turning counts contribution to the
cost function in dynamic estimation. This corresponds to Î± in Equation Set 9.
The default value of
TURNFCTR=1 in essence gives the turning count
contribution an equal weighting as that of the screenline count term. However,
it is likely the case that the cost contribution of the two terms vary to some
extent, and so the user should pay attention to the output turn costs to adjust
this parameter accordingly. For example, if the cost from the screenline count
is 10 times the cost of the turning count and the user wishes to keep the two
terms on an equal footing in the estimation then they should increase
TURNFCTR
to 10.0. On the other hand, the user may see turning counts
playing only a small role in the estimation and so may wish to leave the turn
weight as the default or even decrease it.

**Parent topic:**  [Parameters](GUID-BE49B418-D604-498C-9957-1B26EC5E26EF.html)

|
|  |
|
|  |
