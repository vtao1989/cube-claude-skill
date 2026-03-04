# Introduction to CUBE Voyager control statements

CUBE Voyager operates by reading control statements from a
script (job) file. All control statements have the same general format. Each
statement begins with a control word to tell the program what type of statement
it is. Following the control word and one, or more, spaces, are keywords and
their values. A keyword is always followed by an equals (=) sign, and then the
value(s) to be associated with the keyword. There may be as many keywords as
are applicable to the control type. A statement can be continued onto the next
line by breaking it after a valid operator for the statement. If the last
character on the statement (prior to any comments) is a valid operator for the
statement, the statement MUST continue onto the next line. Valid continuation
characters are: comma and mathematical and logical operators: ( , + - / \* ^
& | = ); the character must be one that is in proper context for the
statement.

Example

```
COMP a = b + c = ; invalid: = is not in proper context
COMP a = b + c + ; valid: + is logical at this point
d + e / f ; continuation of previous line
ZDATI=myfile, z=2-4, emp=21-30 pop=40- ; valid: - is logical here
48, ; valid: , is logical here
sfdus = 51-55 & ; invalid: & doesnât fit here
mfdus= 61-65
```

**Parent topic:** [General Syntax](GUID-DE2905C2-9EEC-4ED6-99F8-BA2EDA9B6ADF.html)

|
|  |
|
|  |
