# Standard control statements

This section discusses details about specific control
statements. Topics include:

- [Control statement introduction (general syntax)](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__CONTROLSTATEMENTINTRO)
- [COMP](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__COMP)
- [CONSOLE](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__CONSOLE)
- [FILEI](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__FILEI)
- [FILEO](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__FILEO)
- [GLOBAL](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__GLOBAL)
- [ID](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__missing-elem-id--ID%20)
- [IF â¦ ELSEIF â¦ ELSE â¦ ENDIF](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__missing-elem-id--IFELSE%20)
- [LOG](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__missing-elem-id--LOG%20)
- [LOOKUP](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__LOOKUP)
- [PRINT](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__PRINT)
- [PRINTROW](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__PRINTROW)
- [READ](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__missing-elem-id--READ%20)
- [SORT](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__SORT)

Control statement
introduction (general syntax)

Many programs will share the same type of control
statements; however, the data entered on them may vary between programs. This
section briefly describes the common format of statements that are used in many
of the CUBE Voyager programs. All statements follow the format that the
statement type is identified by the first word that appears on it. Usually, the
first word is the ControlWord. However, in some cases it is more expedient
(and/or convenient) for the user to start the statement with one of the special
keywords that is acceptable for that type of statement.

Those keywords (termed ÂtriggerÂ keywords) are identified
in their respective program detailed descriptions. The general format for
describing Control Statements in this document is:

ControlWord

Key1 Key1 Key1 (Key2 Key2 (Key3 Key3) ) Key1 (Key2) â¦

ControlWord is the statement type and must be the first
keyword on each statement, unless the statement contains "trigger" keys, and
the first keyword is a trigger keyword followed by an equals sign. See the
keyword description below for details about trigger keys, denoted by K within
the |â¦|.

- Key1 - A keyword that must be
  followed by an equals sign and appropriate value(s).
- Key2
  - A keyword that is valid only if it follows the values
  for its Key1, an equal level Key2, or any key3 or key4 (for the same Key1).
- Key3 - A keyword that is valid
  only if it follows the values for its Key2, an equal level Key3, or a key4 (for
  the same Key2).

The parenthesis () are used only to indicate the key level;
they are not coded on the statement. A keyword must always be followed by an
equals sign and appropriate value(s).

The following example illustrates the hierarchy of control
statement description:

CTLWRD

AAA BBB (CCC DDD) EEE FFF (GGG (HHH III) JJJ (KKK) )

This description indicates that AAA, BBB, EEE, and FFF are
all valid keywords. They must be followed directly by an equals sign and the
associated values, and may appear any place a keyword is allowed. CCC and DDD
are valid level 2 keywords, and may appear only following the values for either
BBB, CCC, or DDD. GGG may follow the values for FFF, GGG, HHH, III, JJJ, and
KKK. HHH and III are level 3 keywords, and may appear only following the values
for GGG, HHH, or III. KKK is also a level 3 keyword and may appear only after
the values for JJJ or KKK.

- AAA=3 BBB=5 DDD=2 EEE=25,FFF=Y -
  Valid
- AAA=3 DDD=2 BBB=5 - Invalid: DDD
  must follow BBB or CCC
- KKK=27 - Invalid: KKK must follow
  JJJ
- FFF=Y HHH=5 - Invalid: HHH must
  follow GGG
- BBB=5 CCC=6 DDD=7 CCC=8 BBB=9 -
  Valid

COMP

COMP statements are used to
dynamically assign values to variables and/or matrices.
COMP statements contains one, or more, keywords
with associated numerical and/or character expressions. Each expression results
in a number or a character string; its mode is usually determined by the first
term in the expression. If the first term is a number, or numeric variable, it
is a numeric expression, or if the first term is a character function or
literal character string (beginning with a quote), it is a character
expression. Every term within the expression must be known to the expression at
the time the COMP statement is to be compiled. Often a variable is defined by
its presence as a keyword in another
COMP statement. If there are multiple expressions
on a
COMP statement, they are solved in left to right
order.

```
K = j + 2    ; defines K as a numeric variable.
name='     ' ; declares name as a variable that is 4 characters long.
namx=substr(name,1,3)+'abcde'+str(k,4,1) ; declares namx as a character
variable that is 12 characters long.
```

All numeric variables that are declared by the user in this
manner are internally treated as double precision floating point variables.

Some programs (mostly those involving zonal matrices) may
allow the use of
INCLUDE and
EXCLUDE keywords on the
COMP statement. When the statement contains
either, or both, of these keywords, it means that the statement will be
subjected to a zonal filter before being processed. The zonal filter will refer
to either I (origin zone) or J (destination zone); the program definition will
clarify which. If an
INCLUDE is present, the zone number will be
checked against the zones in the
INCLUDE list. If it fails the
INCLUDE list specifications, the statement is
bypassed. Then, if there is an
EXCLUDE, the zone is checked with the
EXCLUDE list. If it meets the
EXCLUDE list specifications, the statement is
bypassed.

CONSOLE

A CONSOLE statement is used to set certain switches relative
to dynamic display of messages in the message area of the window.

- CONSOLE ONLINE=Y - Causes all
  subsequent text written to the standard print media to also be written to the
  console.
- CONSOLE ONLINE=N - Turns off the
  ONLINE=Y switch
- CONSOLE MESSAGE=text - Causes
  text to be written to the console.

FILEI

FILEI tells the program which input
files to process. In most cases, if there is no
FILEI statement, the program will assume a default
statement, or simulate certain required defaults. Typical keywords on a
FILEI statement are
NETI, MATI, and
ZDATI. When the program accepts
FILEI vectored keywords, such as
MATI in various programs, the keyword may contain
[i]. If [i] is not specified, [1] is assumed. Most times the statement may
begin with the keyword itself, thus eliminating the need to code
FILEI. The exact format of the
FILEI statement will vary between programs.

```
FILEI MATI=?01.mat, ?02.mat, ?03.mat,
NETI=??.mat
MATI[1]=?01.mat, MATI[2]=?02.mat, MATI[3]=?03.mat NETI=??.mat
; this would be the same as the above FILEI statement.
```

Some
FILEI
keywords may allow sublevel keywords that are associated with
the file keyword. In some programs, all
FILEI statements must be in the beginning of the
control stream, because later control statements may reference variables that
are to come directly from the files. The documentation for each program will
indicate where the
FILEI statements are valid. Generally, programs
delay opening
FILEI files until absolutely necessary, but it is
wise to form the habit of placing all
FILEI statements first in the control stream.

Hint: It is relatively easy to miscode
FILEI statements by either omitting or including
line delimiters. For example:

```
FILEI MATI[1]=...   ; this is single FILEI statement
MATI[2]=...         ; this is a single FILEI statement
MATI[5]=...,        ; this is a FILEI statement with continuation
Abc=def             ; but this is probably an invalid FILEI continuation
```

Note: Application Editor automatically writes all
FILEI statements to the script file when you
define input file boxes. If you use Application Editor, do not manually edit
the file path or file name elements of the
FILEI statements, as both the script file and
the applicationâs .app file stores this information. Editing the file path or
file name will result in a mismatch between the file that the script uses when
it runs and the file Application Editor opens when you double-click an input
file box. (See Application Editor, in the CUBE Base Reference Guide.)

FILEO

FILEO is the counterpart to
FILEI; it names the output files that the program
writes. If there is no
FILEO statement, some programs will generate an
appropriate statement. The exact format of the
FILEO statement varies between programs.

Note: Application Editor automatically writes all
FILEO statements to the script file when you
define content for output file boxes. If you use Application Editor, do not
manually edit the file path or file name elements of the
FILEO statements, as both the script file and
the applicationâs .app file stores this information. Editing the file path or
file name will result in a mismatch between the file the script writes during
runs and the file Application Editor opens when you double-click an output file
box. (See Application Editor, in the CUBE Base Reference Guide.)

GLOBAL

Alters the size of a page on the standard print media.
Keywords include:

- [PAGEHEIGHT](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__PAGEHEIGHT)
- [PAGEWIDTH](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__PAGEWIDTH)

The keywords are trigger keywords; you need not specify
"GLOBAL".

GLOBAL keywords

PAGEHEIGHT - |KI| -
Resets the maximum number of lines on a page, so that the system knows when to
start a new page with appropriate headers. The value must be in the range 10-
32767. Hint: If the print file is going to be viewed primarily on-line (instead
of actually being printed), it is suggested that PAGEHEIGHT be set to a large
number to reduce the number of interspersed page headers. The PAGExxxx values
can also be set when CUBE Voyager is initially launched from its menu.

PAGEWIDTH - |KI| -
Resets the maximum number of characters to be printed on a single line. Usually
this value is either 80 or 132 to accommodate most character printers. It only
comes into play when certain reporting processes need to know the width of a
print line, so it can form the report properly. The value must be in the range
50-250.

If these parameters are specified, they remain in effect
through subsequent programs until revised.

Example ââââ

```
PAGEHEIGHT=32767 ; preclude insertion of page headers
```

ID

An
ID
statement is used to revise the page headings for each
printed page. The length of the
ID text will be truncated to 60 characters. The
ID is specified as: ID=newid string. The ID is
revised in one of two ways: with the ID statement, and (in some programs) by a
COMP ID=text expression.
ID statements in CUBE Voyager Pilot program are
dynamic; they cause the ID to be revised when the
statement is processed in the CUBE Voyager operations stack.
ID statements in the application programs cause
the
ID to be revised only when the statement is
encountered in the statement reading and editing phase prior to actual program
execution. This can cause the sign-on
ID to be revised at a time different than what
might be expected. Because of this situation, it is suggested that
ID statements be used before a
RUN statement. That way, the sign-on page for the
application program will contain the desired
ID.

Example of improper ID location ââââââââââââââââ

```
RUN PGM=MATRIX
ID=this is the MATRIX ID
ENDRUN
RUN PGM=HIGHWAY
ID=this is the HIGHWAY ID
ENDRUN
```

In this situation, the first page (sign-on) for the Matrix
application will not contain the "this is the MATRIX ID" as its header, but the
first page of the Highway section would contain it. If the
RUN
and
ID statements were reversed, the sign-on
IDs would be correct.

When
ID is specified as the destination in a
COMP statement, the
ID can be computed, and it is revised at that time
(but will not be reflected in the headers until a new page is required). In the
COMP statement, parts of the
ID can be computed. This would most likely be used
in a CUBE Voyager loop situation:

Example of computing the ID ââââââââââââââ

```
LOOP PASS=1,5
COMP ID='This is Pass'+str(PASS,2,0)
RUN PGM=
...
ENDRUN
ENDLOOP
```

Example âââââ

```
ID=This is the new Page Header
```

IF â¦ ELSEIF â¦ ELSE â¦
ENDIF

IF statements control the flow of
user defined operations for those programs that provide for them.
IF is followed by a selection expression enclosed
within (â¦). The expression is evaluated and will result in a true or false
condition. For each
IF statement, there must be a matching
ENDIF later in the input stream. Between the
IF and its matching
ENDIF, optionally, there may be any number of
ELSEIF statements, and one
ELSE statement. The
ELSEIF statement has the same format as the
IF
statement. Program flow is determined by the results of the
condition evaluations of the
IF
and
ELSEIF statements, and the
ELSE statement. Flow is outlined as:

- IF/ELSEIF expression is true â
  The statements following the statement are executed until an
  ELSEIF, ELSE, or
  ENDIF is encountered. The next statement
  executed is the one following the associated
  ENDIF statement.
- IF/ELSEIF expression is false â
  The next statement to be executed is the next associated
  ELSEIF, ELSE, or
  ENDIF statement.

Example âââ-

```
IF (I<0)
s1...
ELSEIF ( I>=0 & I<5 )
s2...
ELSEIF (I==8)
s3...
ELSE
s4...
ENDIF
```

For varying values of I, the statements would be executed
as:

- -1 - S1
- 3 - S2
- 9 - S3
- >9 - S4

If, in the example, there was no
ELSE statement, then any time I is greater than 8,
no statements between the
IF and the
ENDIF statement would be executed.

A variation of the
IF statement (sometimes referred to as a simple or
short
IF) is one in which a single control statement is
appended after the
IF expression. In such cases, the program
automatically generates the required
ENDIF. This shortcut statement is provided to help
reduce the amount of coding required.
Note: if a short
IF is used and the statement appended to the
statement is not acceptable in that context or is mis-structured, the error
diagnostic stated about the line may be somewhat confusing. This is because the
system can not always fully ascertain exactly what the problem is. It is
diagnosing an
IF statement, but the appended statement has
errors, so it doesnât know exactly where to place the blame because it is
diagnosing the
IF statement at the time. Note that there is no
corresponding short
ELSEIF statement and no control statements may
directly follow
ELSEIF or
ELSE or
ENDIF statements on the same line or they will be
ignored by the processor.

```
IF ( i == 1) counter=0
IF ( i == zones) print ...
IF (j==3 & k==5) k=3    ; This statement will be OK, ENDIF generated
     cnter = cnter + 1  ; and this is OK
ENDIF                   ; This will fail, because there is no associated IF
IF (j==3 & k==5) k=3,   ; This statement will be OK
    cnter = cnter + 1   ; and this will continue it
; Generated the ENDIF here
ENDIF                   ; So, this will be an error
```

LOG

Writes values to the log file. Keywords include:

- [PREFIX](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__PREFIX)
- [VAR](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__VAR)

CUBE Voyager maintains a file called the log file; it has a
filename with an extension of .VAR. Whenever a
RUN statement is encountered, CUBE Voyager updates
the values in the .VAR file with the values for all the variables that CUBE
Voyager is maintaining plus the values that were logged by any programs. If a
program is requested to
LOG any values, the program appends values to the
.VAR file, and CUBE Voyager retrieves the values when the program terminates.

The values in the .VAR file can be accessed in two
different ways: 1.) in CUBE Voyager, the variable can be accessed directly; 2.)
in other programs, the values can be retrieved by the use of the @â¦@ token
process. In the latter case, the value from the .VAR is substituted directly
into the control statement as it is read. A
LOG statement is used to have a program write
values to the .VAR file. The variables in the .VAR file can be retrieved by
other CUBE Voyager programs (including the Pilot program) in the same job.
Examples may help to clarify this process.

```
RUN PGM=MATRIX      ; (CUBE Voyager tests the value from MATRIX):
    ZONES=5
    MW [1] = 1
    TOTMW1 = TOTMW1 + ROWSUM (1)
    LOG VAR=TOTMW1
ENDRUN
IF (MATRIX.TOTMW1 == 0) ABORT MSG='Nothing in MW1'
RUN PGM=HIGHWAY     ; (HIGHWAY obtains a value from MATRIX):
    .
    X = @MATRIX.TOTMW1@
    .
ENDRUN
```

The records that are written to the file are written as
PREFIX.VAR=value. The current version of CUBE Voyager truncates .VAR string
values with embedded or trailing spaces at the first space when it reads the
values. This is scheduled for revision in a subsequent release of the system.

PREFIX
- |S| - Sets the prefix of the logged variable(s). This
string is added to the start of the names of all variables that follow
PREFIX. If
PREFIX is not specified, the program name will be
used. This could be confusing if different applications of the same program log
the same values.

VAR - |S| - Indicates which
variables will have their values written to the .VAR file.

Example ââââ

```
RUN PGM=MATRIX
   .
LOG  PREFIX=MATRIX1, VAR=TOTMW1, AVEMW
LOG  VAR=GRANDTOTAL  ; will be written as MATRIX1.GRANDTOTAL=#####
```

LOOKUP

A LOOKUP statement is used to define a lookup function and
to enter data for the function. Keywords and subkeywords include:

- [FAIL](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__FAIL)
- [FILE](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__FILE)
- [INTERPOLATE](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__INTERPOLATE)
- [LOOKUPI](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__LOOKUPI)
- [NAME](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__NAME)

  - LOOKUP
  - RESULT
- [NEAREST](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__NEAREST)
- [R](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__R)
- [SETUPPER](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__SETUPPER)
- [SIZE](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__SIZE)
- [TOLERANCE](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__TOLERANCE)

The statements are not dynamic; they are processed at the
appropriate time by the program, prior to their actual use. Lookup functions
are referenced from within numerical expressions. When the function is
referenced in an expression, the correct number of arguments enclosed within
parenthesis must follow it. The function returns a single value to the
expression solver. A lookup array is allocated and initialized with the data
referenced by the
LOOKUPI, FILE or
R
keywords. In most cases, a lookup statement will define a
single set of lookup data, but if a
LOOKUP subkeyword follows the
NAME, the function will be defined as one that
requires at least two arguments (curve number and the value to be searched
for). This latter format is useful for entering friction factors for use in the
Distribution program. Data referenced by
LOOKUPI or
FILE keywords can be either in DBF, MDB, or
delimited ASCII format.

A new wizard feature has been added to CUBE to automate the
coding of a
LOOKUP function when linking a DBF file to a
LOOKUPI file box in Application Editor. See "Job
Script Editor Window," in the CUBE Base Reference Guide for information about
this wizard.

The following lists the Keyword, Subkeyword, Type and
Description:

LOOKUP keywords

- FAIL - |RV3| - Defines
  the results to be returned by the function if the lookup value is not contained
  within the data.

  By default, if the value is less than the lowest value
  in the table, the result for the lowest value in the table is returned, unless
  `FAIL[1]`is explicitly specified. If the value is greater than the
  highest value in the table, the result for the highest value in the table is
  returned, unless
  `FAIL[2]` is specified. If the value is not found
  within the data,
  `FAIL[3]`(default value is 0) is returned. If a call to the function
  has more arguments than is required, the argument following the required
  arguments is the value that will be returned if the lookup fails for any
  reason. Note that versions prior to 1.5.5 did not return the extreme results of
  the data for low and high failure; they returned
  FAIL[1] and
  FAIL[2], respectively. If
  FAIL[1-2] were not specified, they were set to
  0.
- FILE - |F| - Name of
  the file that contains the data to be associated with the function. This
  keyword must be specified, unless
  R or
  LOOKUPI is specified.
  FILE, R, and
  LOOKUPI are mutually exclusive.
- INTERPOLATE -
  |?| - Indicates if the returned function value is to be the result of
  interpolating between rows in the lookup table. The default value is false,
  meaning that there must be a direct match in the table.
- LIST - |?| - Indicates
  if the program is to format and list the lookup table.
- LOOKUPI - |I| - The
  # of the
  FILEI LOOKUPI[#] file where this
  LOOKUP statement is to obtain values. Note
  that
  FILE, LOOKUPI and
  R are mutually exclusive. The data formats
  supported for
  LOOKUPI= and
  FILE= when referencing data from an external
  file are ASCII and DBF. ASCII data MUST be delimited with either spaces or
  commas.
- NAME - |S| - Name of
  the lookup function that the statement defines.
- NAME -
  LOOKUP - |S| - Used when data for one, or more, curves is to be
  obtained from a single data record. The
  LOOKUP keyword must be indexed [1-n], and its
  value must be followed by
  RESULT=value. The values provided for the
  LOOKUP and
  RESULT keywords are either the field numbers
  in the input data (ASCII, DBF, or MDB data) or the field names when the input
  data is in DBF or MDB format. The
  LOOKUP
  index indicates the curve number and the
  LOOKUP value indicates which column or field
  in the input data file holds the lookup values for the indexed curve. The value
  following the RESULT keyword indicates the field number or name on the data
  record where the return value for the curve on the
  LOOKUP index is to be found. The use of the
  LOOKUP keyword implies that the call to the
  lookup function must contain at least two arguments (a curve number, and a
  value to be searched for). For example on the
  LOOKUP statement with NAME=FUNC1, LOOKUP[1]=1
  RESULT=2, a call to this function like X=FUNC1(1,5) implies for curve 1 (first
  argument in the function call), lookup a value of 5 (second argument of the
  function call) in the data field defined by the
  LOOKUP value (the first field in this example)
  and return the value from the field in the data file defined by the
  RESULT value (the second field in this
  example). The returned value from the function would be placed in the variable
  X.
- NAME -
  RESULT - |S| - Field number or name of the field from the data
  record that contains the result to be returned when the function is called.
- NEAREST - |?| -
  Specifies that the function should return a value based on the nearest value
  found in the table to the lookup value when an exact match cannot be found.
- R - |SV| - Used in place
  of the
  FILE or
  LOOKUPI keywords to enter data records for the
  function. If
  R is specified,
  FILE or
  LOOKUPI may not be specified.
  FILE, LOOKUPI and
  R are mutually exclusive. Any number of
  R records can be entered. The string values
  following
  R represent data records that are in the same
  format as the
  FILE records would be. Each
  R value must be enclosed within single quote
  marks ââ¦â. A single R= may specify the entire file, or
  multiple
  R= records may be entered. See
  [Example: Double value function](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__EXAMPLEDOUBLEVALUE) â Typical friction factor
  curves for an example showing the use of
  LOOKUP to define friction factor curves for
  the usage of
  R= to read data directly from the body of the
  script file.
- SETUPPER - |?| -
  Specifies that the function is to simulate an upper limit for a lookup row when
  only a single value is entered for the row. This option is useful when the data
  is input with single values, and the function can not find an exact match, and
  it is to return a value based upon the lower of two ranges. For example, a
  curve is entered with single values that begin at 1 and increment through 10 by
  1. A lookup for 1.5 would fail. If INTERPOLATE were rue,
  the return value would be computed, otherwise the return would be error. In
  such cases, if
  SETUPPER
  were true, the result for 1 would be returned.
  SETUPPER takes precedence over
  INTERPOLATE, and only comes into play for rows
  without both limits explicitly provided.
- SIZE - |I| - Optional
  variable that specifies the total number of entries in a
  LOOKUP array. The value should be the number
  of resulting values to be searched for multiplied by the number of records. As
  of v4.1 of CUBE Voyager and TP+ systems, this keyword is no longer required as
  the memory allocation process is now automated to optimize within the resources
  of the computer it is using. However, it is maintained to insure backward
  compatibility with previous versions of the software. |
- TOLERANCE - |R| -
  Specifies a tolerance to be applied to the lookup value. This can be useful
  when the lookup value is the result of a computation and due to processor
  differences there may be differences in the level of precision associated with
  the result.

Lookup functions are referenced in numerical and selection
expressions. When a function is referenced, it is supplied a lookup argument
within parenthesis, and the function returns a value for the argument. The
returned value is obtained by searching the lookup function data table for the
lookup argument. The table is composed of rows of data.

If the
LOOKUP
subkeyword is in effect, the call to the function requires at
least two arguments: the lookup curve number and the lookup argument.
Otherwise, the function requires only one argument: the lookup argument. If the
function can not find a match for the lookup curve number,
FAIL[3] is returned, regardless of the value of
INTERPOLATE. If the argument is less than the
lowest value for the lookup number the return value is set to
FAIL\*\*[1]. If the argument is higher than the highest value,
the return value is set to \*\*FAIL\*\*[2]. If the value is not found in any range,
the return value is set to \*\*FAIL\*\*[3] unless \*\*INTERPOLATE is set
to true. If interpolation is used, the return value is the result of
interpolating between the high limit of the lower row and the low limit of the
upper row.

For either a single or double value function (functional
call with 1 or 2 arguments) and additional argument value can be provided. If
this optional argument is provided ANY failure will not return the
FAIL value defined by the
FAIL keyword or its default values but the value
for this optional argument will be the returned value on any failure. This in
effect gives you the ability to override the default
FAIL values for specific situations.

Possible data records include:

- Data records when LOOKUP subkeyword is NOT used and data
  source is ASCII:

  Each data record must have at least two fields delimited
  by white space, or commas or may be separate fields on a DBF file. The first
  field on a record is the lookup result, and the fields following it are the
  lookup values. If two numbers are separated by a dash, they form the low and
  high limits of a row. Numbers not separated by dashes are entered as both the
  low and high limits of a row. Ranges may not overlap, but the upper limit of a
  row may be equal to the lower limit of the next row. If the argument matches a
  high limit of a row and the low limit of the next row, the result is obtained
  from the upper row. (For example, first row limits=1-2, second row limits =2-3.
  The result for 2 would be obtained from the second row.)
- Data records when LOOKUP subkeyword is not used and
  data source is DBF or MDB:

  Only the first two fields on the DBF or MDB lookup file
  will be used. The first field is the lookup result and the second field is the
  lookup value. The first two fields should be numeric fields but character
  fields are ok as long as the content can be converted to numerics, otherwise
  the program will report a lookup input error.
- Data records when LOOKUP subkeyword is used:

  Each data record may have any number of fields
  delimited by white space, or commas or may be separate fields on a DBF or MDB
  file. The data for each LOOKUP is obtained from the record according to the
  field numbers or names specified for the LOOKUP and RESULT keywords. If either
  field number exceeds the number of fields on the record, there is no row
  generated for that curve. If both fields exist, they form a row with the low
  and high limits equal to the value from the LOOKUP field.

When the lookup format designates multiple curves, special
consideration is given to blank fields. Blank fields are not treated as zeroes,
but indicate there is no data point. For example, assume the following records:

```
T, v1, v2, v3
1, 101, 201, 301
2, 102, 202, 302
3, 103, , 303
4, 104, 204
5, , , 305
```

There will be no data points for T=3,V2, T=4,V3, T=5,V1,
and T=5,V2. The V1 curve will have points for T=1-4, the V2 curve will have
points for T=1-2,4, and V3 will have points for T=1-3, 5. The result for a
lookup of T=3 in V2, will depend upon the options of the
LOOKUP statement (SETUPPER,
INTERPOLATE, or none).

Be aware that this situation exists only for comma
delimited and dbf data; space delimited records donât have any way to designate
null fields; the first empty field indicates the end of the record, and no more
points appear on the record. With space delimited records, the T=3 record would
appear as "3 103 303", which would be interpreted as points for V1 and V2; V3
would be blank.

Example: Single value
function

```
COPY FILE=C:\LOOK1.DAT ; this is the data for the function
1    2 3 4-8 23
15   50
2    1
3    9-10
ENDCOPY
LOOKUP NAME=DISTRICTS, FILE=C:\LOOK1.DAT LIST=Y
```

The lookup table will be represented as:

|  |  |  |
| --- | --- | --- |
| Lower Limit | Upper Limit | Result Value |
| 1 | 1 | 2 |
| 2 | 2 | 1 |
| 3 | 3 | 1 |
| 4 | 8 | 1 |
| 9 | 10 | 3 |
| 23 | 23 | 1 |
| 50 | 50 | 15 |

DISTRICTS(6) results in the value 1.

DISTRICTS(9) results in 3.

DISTRICTS(50) results in 15.

Example: Single
value function using LOOKUPI

```
FILEI LOOKUP[1]=C:\LOOK1.DAT
LOOKUP NAME=DISTRICTS, LOOKUPI=1 LIST=Y
```

Example: Double value
function â Typical friction factor curves

The traditional format for friction factors has been one in
which the first field on an input data record is the time value, and the
subsequent fields are the factors for the various purposes that are being
distributed. This example illustrates that typical process. Because the CUBE
Voyager distribution process is generic, it is possible to have times that are
below the minimum time and greater than the highest time. The normal (default)
process would return a 0 for those values (from the
FAIL values), but that may not be what is
expected. In most situations, users may wish to have values for times that
extend beyond the limits of the values entered.

For example: a table might have factors for times from 1
through 100, but there are zone-to-zone times that are greater than 100
minutes. The time matrix might also have very large values, or possibly zero,
for zone-to-zone movements for which there is no path (inaccessible). Thus, if
a time of 110 is encountered, the friction factor obtained from the lookup
would be the
FAIL[2] value; this may not be what was wanted. A
similar situation would occur if the time were less than 1, but greater than 0.
To circumvent these potential problems, be sure to include a record for a very
low time value (say 0.01), and a record for the highest time value that you
feel is reasonable. The factors of the two first records should be the same,
and the factors for the last records should also be the same.

The lookup values can be set so that only trips within a
certain item range can be distributed. The limits of the curve would control
this operation; a friction value of 0 will preclude distribution between the
zones.

```
LOOKUP   NAME=FF,                ; typical Friction Factor table
         LOOKUP[1]=1, RESULT=2,  ; Curve 1 lookup value is in field 1
                                 ; Result (FF) for curve 1 is in field 2
         LOOKUP[2]=1, RESULT=3,  ; Curve 2 lookup value is in field 1
                                 ; Result (FF) for curve 2 is in field 3
         LOOKUP[3]=1, RESULT=4,  ; Curve 3 lookup value is in field 1
                                 ; Result (FF) for curve 3 is in field 4
         FAIL=2000,1,0,          ; return 2000 if any lookup < 0.01
                                 ; return 1 if any lookup > 120
         INTERPOLATE=Y,          ; interpolate to obtain values
R= '0.01 1200  1000  800',
   '1    1200  1000  800',
   '3     300   500',
   '4     100   100  100',
   '5      50',
   '120    50   100  100'
FFX = FF(1,3)                    ; RESULT = 300
FFX = FF(3,150,888)              ; RESULT = 888 since 150 > highest value
in field 1
FFX = FF(2,2)                    ; RESULT = 750
/* to find 2 in field 1, you must interpolate between 1 and 3
   then interpolate on same basis between 1000 and 500 in field 3
*/
```

The lookup table will be represented as:

|  |  |  |  |
| --- | --- | --- | --- |
| Curve # | Lower Limit | Upper Limit | Result Value |
| 1 | 0.01 | 0.01 | 1200 |
| 1 | 1 | 1 | 1200 |
| 1 | 3 | 3 | 300 |
| 1 | 4 | 4 | 100 |
| 1 | 5 | 5 | 50 |
| 1 | 120 | 120 | 50 |
| 2 | 0.01 | 0.01 | 1000 |
| 2 | 1 | 1 | 1000 |
| 2 | 3 | 3 | 500 |
| 2 | 4 | 4 | 100 |
| 2 | 120 | 120 | 100 |
| 3 | 0.01 | 0.01 | 800 |
| 3 | 1 | 1 | 800 |
| 3 | 4 | 4 | 100 |
| 3 | 120 | 120 | 100 |

Example: Double
value function â LOOKUP with DBF LOOKUPI file

```
FILEI LOOKUPI[1] = "C:\CUBETOWN\TAZ\TAZ.DBF"
LOOKUP LOOKUPI=1, ;references the input DBF file
NAME=TAZ, ;name for this function
LOOKUP[1]=TAZ, RESULT=ACRES, ;lookup a value in TAZ return
;a the value from ACRES
LOOKUP[2]=TAZ, RESULT=POPULATION,
LOOKUP[3]=TAZ, RESULT=AGE_5_14,
LOOKUP[4]=TAZ, RESULT=AGE_15_17,
LOOKUP[5]=TAZ, RESULT=ENROL_ELEM,
LOOKUP[6]=TAZ, RESULT=ENROL_HS,
LOOKUP[7]=TAZ, RESULT=TOTAL_JOBS,
LOOKUP[8]=TAZ, RESULT=RET_JOBS,
LOOKUP[9]=TAZ, RESULT=SERV_JOBS,
LOOKUP[10]=TAZ, RESULT=OTH_JOBS,
INTERPOLATE=F
; example of use: v=TAZ(10,25)
; look for 25 in the TAZ field and returns the OTH_JOBS value
```

Example: Double value function â Using LOOKUP to
get constants and populate internal arrays with the values

```
FILEI ZDATI[1] = "C:\MTA_GEN\STEP1.DBF"
FILEI LOOKUPI[1] = "C:\MTA_GEN\CFACS.DAT"
cc=zi.1.cc ;cc = county code (1=LA,2=OR,3=RV,4=SB,5=VN)
; lookup county correction factors O&D Survey
LOOKUP LOOKUPI=2 LIST=Y NAME=CFAC,
LOOKUP[1]=1, RESULT=2,
LOOKUP[2]=1, RESULT=3,
LOOKUP[3]=1, RESULT=4,
LOOKUP[4]=1, RESULT=5,
LOOKUP[5]=1, RESULT=6,
INTERPOLATE =N
; dimension user arrays to 5
array c0=5 cv=5 c2=5
; fill arrays for factors by county
LOOP cc=1,5
c0[cc]=CFAC(cc,1)
cv[cc]=CFAC(cc,2)
c2[cc]=CFAC(cc,3)
ENDLOOP
/* ;external LOOKUPI file in this example
1 3.4108 3.4137 3.7070 3.4132 3.2278
2 0.6088 0.6767 0.6505 0.6389 0.6759
3 0.5665 0.6518 0.5778 0.5757 0.6642
*/
```

Example: Double value function â Using LOOKUP
with DBF data in a trip Distribution application

```
RUN PGM=DISTRIBUTION PRNFILE="DISTRIBUTION.PRN"
FILEI ZDATI[1] = "TRIP ENDS.DBF"
FILEI MATI[1]  = "TRAVEL TIMES.MAT"
FILEI LOOKUPI[1] = "FRICTIONFACTORS.DBF"
FILEO MATO[1]  = "PERSON TRIP TABLE.MAT",
      MO=1-4, NAME='Home_Based','NonHome_Based','School','EI_Trips'
; Set a maximum number of iterations and convergence criterion
PARAMETERS MAXITERS=99, MAXRMSE=5
; Link the input production and attraction values to internal variables
SETPA   P[1]=ZI.1.P1,  A[1]=ZI.1.A1,
        P[2]=ZI.1.P2,  A[2]=ZI.1.A2,
        P[3]=ZI.1.P3,  A[3]=ZI.1.A3,
        P[4]=ZI.1.P4,  A[4]=ZI.1.A4
; Put the travel time matrix into a working matrix for distribution
MW[20]=MI.1.TIME
; Put the friction factors into a LOOKUP for distribution
LOOKUP LOOKUPI=1,
       NAME=FRICTIONFACTORS,
         LOOKUP[1]=TRVLTIME, RESULT=HOMEBASED,
         LOOKUP[2]=TRVLTIME, RESULT=NONHOME,
         LOOKUP[3]=TRVLTIME, RESULT=SCHOOL,
         LOOKUP[4]=TRVLTIME, RESULT=EXT_INT,
       INTERPOLATE=T
; Distribute trips using a standard gravity model formulation
GRAVITY PURPOSE=1, LOS=MW[20], FFACTORS=FRICTIONFACTORS
GRAVITY PURPOSE=2, LOS=MW[20], FFACTORS=FRICTIONFACTORS
GRAVITY PURPOSE=3, LOS=MW[20], FFACTORS=FRICTIONFACTORS
GRAVITY PURPOSE=4, LOS=MW[20], FFACTORS=FRICTIONFACTORS
ENDRUN
```

Where the FRICTIONFACTOR.DBF file contains:

![](GUID-3868489B-FDA1-4326-B545-96507DB42078-low.png)

PRINT

Formats data items and writes them as a single line to the
standard printed output, a file, or both. Keywords and subkeywords include:

- [CFORM](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__CFORM)
- [CSV](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__CSV)
- [FILE](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__PRINTFILE)

  - [APPEND](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__FILEAPPEND)
  - [PRINT](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__FILEPRINT)
  - [REWIND](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__FILEREWIND)
- [FORM](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__FORM)
- [LIST](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__PRINTLIST)
- [PRINTO](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__PRINTO)

  - [PRINT](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__PRINTOPRINT)
  - [REWIND](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__PRINTOREWIND)

The size limit of a single data item (or print field)
written a
PRINT statement is 50,000 characters. This
facilitates transferring large amounts of data between files, for example.
Certain print modes, however, restrict the field width â see
[Defining a numeric print format](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__DEFININGNUMERICPRINT), and
[Defining a character print format](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__DEFININGCHARACTERPRINT).

The program prints one line for each PRINT statement. The
length of the printed line is determined by the formatting of each listed item.

PRINT keywords

- CFORM - |S| -
  Optional. Default format for
  subsequently appearing character strings, except for literal values, specified
  with the
  LIST keyword. Explicit formats defined for
  particular items take precedence. This default format is effective until the
  program reads the next
  CFORM value. See
  [Defining a character print format](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__DEFININGCHARACTERPRINT). Default value is 0.
- CSV
  - |?| -
  Optional. Flag indicating whether to
  print the output file in CSV format (with commas between the LIST items).
  Possible values:
  - T - Print in CSV format, with commas between each
    LIST item
  - F - Do not print in CSV format

  Default value is F.
- FILE
  - |F| -
  Optional. File where the program
  writes the formatted list.

  If not specified, the program writes the standard
  printed output file. If specified, the program writes only to the specified
  file unless subkeyword
  PRINT is set to T.

  The program writes each formatted list to one record.
  Thus, the end-of-file character is at the end of the last record. You might
  need to add a "\n" to the end of the file if you concatenate the file with
  another file.
- FILE - APPEND - |?|
  -
  Optional. Flag indicating whether to
  overwrite or append to the specified file. Possible values:
  - T â Append the formatted list to the specified
    file.
  - F â Overwrite the existing file when writing the
    formatted list.

  Note: If set to T for a file at least once in a step, then
  all
  PRINT
  statements executed at that step will append to that
  file, even if other statements set
  APPEND to F.

  Default value is F.
- FILE - PRINT - |?| -
  Optional. Flag indicating whether to
  write record to standard printed output in addition to specified file. Possible
  values:
  - T â Write the record to the standard printed output
    in addition to the specified file
  - F â Only write the record to the specified file

  Default value is F.
- FILE - REWIND - |?|
  -
  Optional. Flag indicating whether the
  program repositions to the start of the file before writing contents. Possible
  values:
  - T â Reposition to start of file before writing
    formatted list. Program overwrites previous contents.
  - F â Write to the current position in the file.

  REWIND is dynamic; therefore, you
  can control the rewinding on each
  PRINT
  statement.

  Default value is F.
- FORM - |S| -
  Optional. Default format for
  subsequently appearing numbers specified with the
  LIST
  keyword. Explicit formats defined for particular items
  take precedence. This default format is effective until the program reads the
  next
  FORM value. See
  [Defining a numeric print format](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__DEFININGNUMERICPRINT)

  Default value is 10.2.
- LIST - |KS|
  - Optional. List of items (variables, strings,
  and expressions) to format and write to a printed line. Enclose expressions in
  parentheses. Specify no more than 500 items.

  To assign an explicit format to a particular item in the
  list, place the format in parentheses next to the item. The format only applies
  to that item. See
  [Defining a numeric print format](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__DEFININGNUMERICPRINT) and
  [Defining a character print format](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__DEFININGCHARACTERPRINT).

  For example:

  ```
  I, J, ITEM1(6), 'abcde', (sqrt(4))(8C), 'i='(8R), I(L).
  ```

  Append appropriate subscripts to any array and matrix
  variables in the list. If you do not specify a subscript, the program will
  supply one, depending on the variable, program, and phase. Subscripts may be
  constants, variables, or valid expressions. For example:
  `P[i*3-1]`.

  Note: `MW[n]` normally implies
  `MW[n][J]`, where J is the current value of J.

  The
  PRINT statement recognizes four special
  character strings as special control characters:
  - "\n" â new line control
  - "\f" â new page control
  - "\t" â tab control
  - "\" â ignore new line control

  For example, a literal string may contain the newline
  character string ("\n" ; lowercase), to generate a new line at that location
  (the \n will not be printed).

  As long as a
  PRINT statement has at least one
  LIST item, the program automatically inserts a newline character
  prior to the first item. You can override the automatic newline character by
  making the first LIST item a literal string that begins
  with the "\" characters. The \ will not be printed, and the printing will
  continue from the current line position.

  Note: Because special
  characters are treated as these special controls, problems can arise when
  printing strings for a system path due to the "\" character. For example, upon
  reading
  `LIST="C:\n2020\output\"` the program would treat
  the embedded \n as the newline control and insert a new line at the location.
  Because the special control is case sensitive and directory folder names are
  not, you can avoid this issue by using LI`ST="C:\N2020\output"`.

  In some cases, you might prefer to form character
  variables using the string functions of a
  COMP character expression and include those
  variables in the list. The string functions might provide some flexibility that
  is better suited to the specific task.
- PRINTO - |I| - Optional. Index number of the FILEO PRINTO file where
  the program writes this output. Setting the Index to 0 will send the output to
  the "User Progress Messages" box in Task Monitor.
- PRINTO -
  PRINT- |?| -
  Optional. Flag that indicates whether
  to write record to standard printed output in addition to specified PRINTO
  file. Possible values:
  - T â Write the record to the standard printed output
    in addition to the specified file.
  - F â Only write the record to the specified file

  Default value is F.
- PRINTO - REWIND
  - |?| -
  Optional. Flag indicating whether the
  program repositions to the start of the file before writing contents. Possible
  values:
  - T â Reposition to start of file before writing
    formatted list. Program overwrites previous contents.
  - F â Write to the current position in the file.

  REWIND is dynamic; therefore, you
  can control the rewinding on each
  PRINT statement.

  Default value is F.

Examples

- Report a mixture of numeric and character variables.

  ```
  PRINT FORM=0 LIST=I,  J, TOTAL(6.2CS)  'ABCDE'(6.3),
  FORM=LRCD,
        LIST=N, JLOOP_J;
  ```
- Use
  LIST keyword without the control statement
  name.

  ```
  LIST= I(6) J(6) TOTAL1, TOTAL2, TOTAL3
  FILE=PRINTFIL.001, APPEND=T
  ```
- Output to file and rewind file at the end.

  ```
  PRINT FORM=6.0CDLRS LIST=I, J, TOTAL1, TOTAL2
  FILE=PRINTFIL.002,  REWIND=T
  ```
- Interpret
  `sqrt(6)` as a variable "sqrt" with
  `form=6`

  ```
  PRINT FORM=LRS LIST= 'I =',  I,  ' J=',  J,  '
  MW[1]=',  MW[1][1],  MW[1][2], MW[1][3],
            time+dist/sqrt(xyz), (sqrt(6))
  ```
- Output directly to CSV format

  ```
  FILEO PRINTO[1]=c:\data\mydata.csv
  If (I=1) PRINT CSV=T LIST='I','J','TIME','COST','DISTANCE'  PRINTO=1
  PRINT CSV=T LIST=I(6.0L),J(6.0L),MW[1](8.4L),MW[2](8.4L),MW[3](5.2L)
  PRINTO=1
  ```

Defining a numeric print format

You can specify numeric print formats with the
[FORM](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__FORM) keyword or the
[LIST](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__PRINTLIST) keyword. For either keyword, you code numeric print
formats as:

w.dBCDELRST

where:

- w â Total field width.
  Maximum value is 30. If you specify a value greater than 30, the program uses a
  width of 30.
- d â Number of digits
  printed after the decimal point. The program sets
  d to 0 if the format begins with
  w and you do not specify
  d. Maximum value is 15. If you
  specify a value greater than 15, the program uses 15 digits after the decimal
  point.
- B â Display zero-value numbers as blanks. B overrides
  D, if both are coded.
- C â Insert commas into numbers.
- D â Display zero-value numbers as a pair of
  right-justified dashes.
- E â Display numbers in scientific format. Field width
  must be at least 9, otherwise the program resets the format to the default
  value
  `10.2`. The smallest format is
  `9.1E`, which prints as
  `+1.2E+123`. If you set
  d to 0, the program uses the maximum
  decimal (w-8). If there are more post-decimal
  digits than this maximum value, then the program reduces the post-decimal
  digits to
  w-8. You may specify B or D along
  with E; the program ignores other format codes when you specify E.
- L â Trim numbers on the left and print the result
  beginning with the left-most digit. The result will be left justified and only
  as long as required.
- R â Replace a numberâs trailing 0s (right side of
  decimal point) with spaces. The program replaces zeros after normal formatting
  and removes decimal point if there is no trailing 0.
- S â Insert a space before the digits of any numbers
  formatted with L.
- T â Truncate numbers on the left if they cannot fit the
  field width. Normally, the program formats such numbers with all asterisks.

All characters are optional. The BCDELRST characters (case
insensitive) may be in any order, but must follow
w.d, if
w and
d
are specified. The program ignores characters other than B and
D specified with E. Bentley recommends that you use a varying length format
unless you must align reported values. The program attempts to accommodate
fixed formats: When values do not fit the specified field width, the program
drops commas, and then reduces the number of decimal places; finally, the
program reformats with scientific notation (1E+ppp), if possible, otherwise the
program truncates.

If printing an unknown range of values, specify a width
adequate to accommodate all possible ranges. For delimited output,
`FORM=16.4LRS` is probably adequate. When printing fixed
fields, do not specify L, R, and S.

Defining a character
print format

You can specify character print formats with the
CFORM keyword or the
LIST keyword. For either keyword, you code
character print formats as:

w.dCDBTLR

where:

- w â Total field width. Set to 0 to indicate that the
  field width depends on the string length. Specify w anywhere in the format
  string; any number not preceded by a period specifies w. If a format string
  specifies multiple w values, the program uses the last value.

Note:

If the format specifies L, w must be wide enough to
accommodate the string.

- d â Number of leading spaces printed (or dashes, if D
  specified). Specify
  d anywhere in the format string; any
  digit preceded by a period specifies
  d. If a format string specifies
  multiple
  d values, the program uses the last
  value. Valid values range from 0 through 15. The default value is 0.
- C â Center-justify text item. Program applies T first.
  C overrides L or R.
- D â Print dashes (-) in the
  d characters preceding the field.
- B â Replace blanks with underscore characters (\_).
- T â Trim leading or trailing spaces from text item. If L
  is specified, delete leading spaces. If R is specified, delete trailing spaces.
  If both L and R are specified, delete leading and trailing spaces and
  center-justify text item.
- L âLeft-justify text item.
- R â Right-justify text item (truncating beginning
  characters if length exceeds field width).

All characters are optional. The CDBTLR characters (case
insensitive) may be in any order. Bentley recommends using a varying length
format unless you must align reported values. The program attempts to
accommodate fixed formats. When text does not fit the specified field width,
the program truncates.

PRINTROW

Formats and prints all cells or selected cells of a matrix
row to the main print file. Keywords include:

- [BASE1](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__BASE1)
- [FORM](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__PRINTROWFORM)
- [J](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__missing-elem-id--J%20)
- [MAXPERLINE](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__MAXPERLINE)
- [MW](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__MW)
- [TITLE](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__TITLE)

Row formatting can be quite voluminous; use this statement
judiciously.

None of the
PRINTROW keywords are "trigger" keys. You must
code all on a
PRINTROW statement.

- BASE1 - |?| -
  Optional. Flag indicating row format
  when using non-varying print format (that is,
  FORM
  does not contain L). Possible values:
  - T â Begin every printed line with a zone number
    ending in 1.
  - F â Begin each printed line with appropriate zone
    number based on
    FORM
    and page width.

  MAXPERLINE takes
  precedence over
  BASE1: if
  MAXPERLINE is specified and is not modular
  ten,
  BASE1 has no effect.

  For example:

  ```
  PRINTROW MW=1-2, 8 FORM=LRD TITLE='form=LRD'
  PRINTROW MW=1-21 FORM=8 BASE1=Y MAXPERLINE=10
  ```
- FORM
  - |S| -
  Optional. Default format for row
  values. See "[Defining a numeric print format](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__DEFININGNUMERICPRINT)".

  Default value is 20.5LRD

  The default value (20.5LRD) provides efficient reporting
  while maintaining precision. (The L in the format value triggers
  varying-formatted numbers separated by a single space.) Three spaces precede
  zone values ending in 1, providing one distinction. For printing traditional
  integer boxes, set
  FORM to 7D.

  See also "[PRINT](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__PRINT)".
- J - |P| - Optional. List
  of zone numbers formatted for printing. Program sets excluded zones (those not
  listed) to zero.

  Specify the list as a set of single numbers or
  dash-separated pairs of numbers that give a range. Delimit each number or pair
  with a comma.

  For example `J=1,3-5,10,12-20`selects zones 1,3 through 5, 10, and 12 through 20 for
  printing.

  Valid values range from 1 to the number of zones.
  Default value is all zones.
- MAXPERLINE - |I| -
  Optional. Maximum number of columns
  printed on a line.

  By default, program allows any number of values to be
  printed on a line, provided line length does not exceed the standard page
  width. If
  MAXPERLINE is specified, program ignores page
  width.
- MW - |IP| -
  Optional. List of work matrices to
  print. Program prints matrices in ascending order, regardless of specified
  order.

  Specify the list as a set of single numbers or
  dash-separated pairs of numbers that give a range. Delimit each number or pair
  with a comma.

  For example `MW=1,3-10,13`selects work matrices 1,3 through 10, and 13 for printing.

  Default value is no work matrices.
- TITLE - |S| -
  Optional. Title printed at the beginning of each MW. The program truncates
  titles longer than fourteen characters.

  Enclose the value within quotes ('â¦') or literal marks
  ("â¦").

  You may specify only one title per
  PRINTROW statement, even if printing multiple
  MWs.

  By default, the program prints no title.

For neat-appearing reports, Bentley suggests specifying
FORM without the LD, setting
BASE1 to true, and setting
MAXPERLINE to some integral of 10.

Example

```
PRINTROW mw=1-2,8 form=LRD title='form=LRD'
PRINTROW mw=1-21 form=6D base1=y maxperline=10
```

READ

Switches reading of control statements to a different file.
Keywords include:

- [FILE](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__READFILE)
- [newstring](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__READNEWSTRING)
- [oldstring](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__READOLDSTRING)

The format is:

`READFILE=filename,oldstring=newstring,oldstring=newstring,....`

- FILE - File to be
  read. When the end of file is encountered on that file, reading of control
  statements will continue with the statement following this
  READ statement.
- newstring
  - Character string that will replace
  oldstring
  in the records in
  FILE that contain
  oldstring.
  newstring
  is case sensitive; it will be replaced directly.
- oldstring
  - Character string (not case sensitive) that is to be
  replaced by newstring. As each record is read from the
  file, it is scanned to see if
  oldstring
  exists in it. If it does, the string is replaced with
  newstring, and the scan is continued. If
  either
  oldstring
  or
  newstring contains any special characters it
  must be enclosed with ââ¦â. It is suggested that strings always be enclosed
  within 'â¦', but it is not mandatory.

READ statements can be nested up to
five levels. A nested
READ may not point to a file that is already in
the nest. There is no specific limit to the length and number of replacement
strings. The replacement process is designed to not allow a replacement string
to replace an earlier replacement. Replacements are done in the left to right
order as specified in the
READ statement.

READ statement is processed
differently, depending on, if it is used in a PILOT script or as part of a
Voyager program, such as MATRIX. When the
READ statement is used in a PILOT script, Voyager
checks for the existence of the
READ file, before starting the run. If the file
did not exist Voyager will fail. Any variables declared within the file will be
set before the start of the run. When
READ statement is inside other programs such as
MATRIX, HIGHWAY, etc., the READ files are checked and the statements inside the
files are
READ only during the run.

Example

```
READ FILE=BUSLINES, 'MODE=5' = 'MODE=3'
```

SORT

Sorts an array, or series of arrays. Keywords include:

- [ARRAY](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__SORTARRAY)
- [NUMRECS](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__NUMRECS)

The format is:

```
SORT ARRAY=name, name,... NUMRECS=x
```

- ARRAY
  - |S| - Names of the arrays to be sorted. All names must
  be declared in an ARRAY statement or as a DBI AUTOARRAY
  name. A name may be preceded by a "+" or "-" sign to indicate the order of sort
  to be applied for that array (within the series of arrays). If a leading + sign
  is used, the sign and name must be enclosed within quotes (for example,
  â`+myarray`â). A "+" means ascending, and a Â-Â means
  descending. If there is no sign for the first name, ascending is assumed. Signs
  need not be specified, but if they are, a signed array may not follow an array
  without a sign. Unsigned arrays are carried along in parallel with the sorted
  records. All the arrays in a
  SORT statement must be declared with the same
  size.

  For example, if one wanted to see a sorted listing of
  the number of households per zone, two arrays would be required: ZONENO and HH.
  The
  SORT statement would be SORT ARRAY=-HH,ZONENO.
  This would sort the HH array in a descending order and keep the ZONENO array
  records parallel to it.
- NUMRECS - |S| -
  Specifies the number of records to sort; it may be either the name of a
  variable, or an integer number. It may not exceed the length of the arrays.

Example 1

```
SORT ARRAY=A,B,C
  ; Sort on ascending values in A, carry B & C along with A
SORT ARRAY=-A,B,C
  ; same as above, but sort order for A is descending
SORT ARRAY=-A,'+B',-C,D,E
  ; sort on descending on A, ascending B, descending C
SORT ARRAY=-A,B,'+C'
  ; ***  ERROR ***  signed name (+C) follows unsigned (B)
```

Example 2 (Matrix, Fratar, Distribution,
Generation)

```
ARRAY ZONENO=ZONES, HH=ZONES, INCOME=ZONES
.
.
ZONENO[I] = I
HH[I] = ZI.1.HH[I]
INCOME[I] = ZI.1.INCOME[I]
.
.
SORT ARRAY=-INCOME,-HH,ZONENO
LIST=' Zone Income HHs'
JLOOP
  PRINT FORM=8, LIST=ZONENO[J], INCOME[J], HH[J]
ENDJLOOP
```

Example 3 (Network)

```
ARRAY AN=LINKS, BN=LINKS, VMT=LINKS ; NETI must be a binary network
PHASE=LINKMERGE
  _L = _L + 1
  AN[_L] = A
  BN[_L] = B
  VMT[_L] = V_1 * DISTANCE
ENDPHASE
/* note:
The User has to keep count of the records entered into the arrays
If links are deleted, the number of entries will be less than the
original number of links.
*/
PHASE=SUMMARY
  SORT ARRAY=-VMT, AN,BN, NUMRECS=_L
  LOOP _K=1,30 ; only want to see the highest 30
      LIST=AN[_K](6),BN[_K](6),VMT[_K](10.2c)
  ENDLOOP
ENDPHASE
```

**Parent topic:** [General Syntax](GUID-DE2905C2-9EEC-4ED6-99F8-BA2EDA9B6ADF.html)

|
|  |
|
|  |
