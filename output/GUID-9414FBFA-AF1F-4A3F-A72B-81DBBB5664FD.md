# FAQ - FRATAR

How do I specify SETPA with
both target values and growth factors for the same purpose?

This has to be done using separate SETPA statements. See
the following example:

```
; assuming gf() and tot() are previously defined lookup functions
; zone 3 is specified using growth factor
; other zones are specified using target values

setpa pgf[1]=gf(1,j), agf[1]=gf(2,j), include=3
setpa p[1]=tot(1,j), a[1]=tot(2,j), exclude=3
setpa mw[1]=mi.1.1
```

**Parent topic:** [Frequently Asked
Questions](GUID-078814F3-A213-4C26-8689-7528F1915945.html)

|
|  |
|
|  |
