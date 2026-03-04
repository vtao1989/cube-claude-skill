# Control statements

This section describes the control words available in the
Network program.

[ABORT](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__ABORT_unique_1) - Abort current program and CUBE Voyager

[ARRAY](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__ARRAY_unique_1) - Declare user arrays

[BREAK](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__BREAK_unique_2) - Break out of stack processing for current data
record

[COMP](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__COMP_unique_3) - Compute variables from expressions

[COMPARE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__COMPARE) - Compare network records

[CONTINUE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__CONTINUE_unique_2) - Continue at end of loop statement

[CROSSTAB](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__CROSSTAB) - Tabulate / cross tabulate variable values

[DELETE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__DELETE) - Delete this record

[EXIT](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__EXIT_unique_2)- Terminate current phase

[FILEI](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__FILEI_unique_3) - Input files

[FILEO](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__FILEO_unique_3) - Output files

[IF â¦ ELSEIF â¦ ELSE â¦ ENDIF](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__ELSEIF_unique_2)- Define IF ENDIF block

[LOOP â¦ ENDLOOP](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__ENDLOOP_unique_1)

[MERGE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__MERGE)

[PARAMETERS](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__PARAMETERS_unique_3)

[PLOT](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__PLOT)

[PLOTTER](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__PLOTTER)

[PRINT](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__PRINT_unique_3)

[PROCESS â¦ ENDPROCESS](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__PROCESS_unique_1)

[REPORT](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__REPORT_unique_3)

[SORT](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__SORT_unique_2)

[SPDCAP](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__SPDCAP_unique_1)

ABORT

Aborts the Network program and CUBE Voyager. Keywords
include:

[MSG](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__AMSG)

Use
ABORT to quit the Network program at with a
"fatal" return code. Use this statement if you can determine from the data that
you desire no further processing.

MSG - |S| - Optional message to be
printed along with the
ABORT message. For readability, Bentley recommends
100 characters or less.

Example

```
IF (a > 1000) ABORT MSG='Must be the wrong Network'
```

ARRAY

Declares user single dimension arrays. Keywords include:

[VAR](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__AVAR_unique_1)=size

Use
ARRAY to allocate user arrays that are to be used
in the process. An array is different than a variable in that it represents
vectored data. Values stored in arrays must be numeric. Arrays cannot store
string values. When an array is referenced, it should include an index [], and
if the index exceeds the size, the program may fatally terminate. Arrays can be
useful for different processes; the most common use may be to store information
for specific zones. ARRAY statements are not dynamic (stack oriented); they are
allocated prior to any stack operations.

VAR
- |I| -
VAR is the name of the variable that is to be
allocated according to the specified size.
VAR must be a unique name. The size following the
keyword is the highest index possible for
VAR. Size may be either a numeric constant, or a
special name. Special names are: ZONES, NODES, and LINKS if there is a binary
input network. NODES and LINKS should not be used if links are to be added to
the network. Arrays are cleared when they are allocated.

Example

```
ARRAY abc=100, xyz=100

ARRAY AN=LINKS, BN=LINKS, VMT=LINKS
; NETI must be a binary network
```

BREAK

Breaks out of stack processing for current data record.

When a data record is being subjected to the operations in a
phase block, and the operation is
BREAK, the remainder of the block operations are
bypassed and the next data record is processed. Most likely, BREAK
would be used in conjunction with an IF statement. However,
if
BREAK is encountered within a
LOOP, stack processing jumps to the statement
after the associated
ENDLOOP statement.

Example 1

```
if (a=1-500 || b=1-500) BREAK ; do not process centroid links.
if (a.x > b.x) ; bypass the links that go from right to left
  BREAK
endif
```

Example 2

```
/* this example finds the index where subtotal of ARRAY1 exceeds 1000 */
loop index=1,_zones
  _total = _total + array1[index]
  if (_total>1000) BREAK
endloop
list=âINDEX =â,index ; BREAK jumps to here
```

COMP

Computes a value for a variable. Functions include:

[SPEEDFOR (lanes,spdclass)](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__SPEEDFOR)

[CAPACITYFOR (lanes,capclass)](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__CAPACITYFOR)

Usage is:

`Variable = Expression`

COMP statements specify that new
variables are to be created or that existing variables are to have new values
computed for them. During any phase other than the SUMMARY, any name that
appears on the left side of the equals sign will be placed into the output
network record, unless it is a working variable (begins with an underscore).
There may be more than one variable computed on a statement, but there must be
comma between an expression and the next variable=expression. The statement
need not begin with
COMP.

The expression will be solved and the results stored in the
named variable. The phase for which this
COMP statement is coded will establish which
variables may be included within the expression, and where the results can be
stored. The maximum length of the name is 15 characters. This limit includes
the "\_" prefix of temporary variables.

A normal numerical expression is required. If the expression
results in a string, the mode of the target (named) variable will be set to
string instead of numeric. A variableâs mode should be consistent throughout
the application. The program tries to detect any possible changes, or misuse of
variable modes, but it might not detect all inconsistencies. If a variable is
misused as to mode, unpredictable results could occur. It might be prudent to
have a standard naming convention for string variables, such as always
beginning with the same letter.

The expression may contain function names with their
arguments. To obtain speed and/or capacity values from the SPDCAP tables, the
SPEEDFOR and CAPACITYFOR
functions are utilized. They are coded as:

SPEEDFOR(lanes,spdclass) - Returns
the speed from the SPEED table for the designated number of lanes and spdclass.

CAPACITYFOR(lanes,capclass) -
Returns the capacity times the lanes for the designated number of lanes and
capclass.

In the
SPEEDFOR and
CAPACITYFOR functions, the first argument is the
number of lanes and the second argument is the class. If the lanes value is
less than 1, or greater than 9, the function value of lanes will be reset
accordingly. Thus, if
`CAPACITYFOR (88...)`were specified, lanes would be reset to 9, and the capacity
extracted for that value would be multiplied by 9. Similarly, if the second
argument is less than 1, or greater than 99, the internal value will be reset
to the appropriate limit.

Example

```
i=0
j = a / i, k=j*2+3*i
newb = nodecode(b)
sumab = newb+newa
cdist = sqrt((a.x-b.x)^2 + (a.y-b.y)^2)
_LinkSpeed = SPEEDFOR(Lanes,Facility*10+Area)
```

COMPARE

Compares network records. Keywords and sub-keywords
include:

- [RECORD](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__CRECORD)

  - [LIST](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__CLIST)
  - [TITLE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__CTITLE)

COMPARE statements are dynamic and
are used to compare the records of either the link or node portion of two
networks. At the end of the phase (NODEMERGE or LINKMERGE), a summary of the
comparison is reported. The LIST parameter controls the listing of individual
differences. To make this statement function properly, the
`MERGE RECORD=T` statement should be coded.

In addition to a summary report,
COMPARE also returns a value indicating the result
after the comparison of each record. The value is stored in a temporary
variable: \_COMPARE. The meaning of the returned value is as follows:

n - n
attributes are different between two records.

0 - No differences between two records.

-1 - Record not found in file one.

-2 - Record not found in file two.

There may be multiple
COMPARE statements in a single application.

- RECORD
  - |IP| - Indicates which LINKI or NODEI set of records is
  to be compared. Two numbers, separated by a dash, must be coded. This keyword
  may occur only one time on a
  COMPARE statement.
  - LIST - I| - Indicates how many
    of the links with differences are to be listed to the print file. The default
    is 0. If LIST=100, then only the first 100 links with differences will be
    listed. If a link exists in one file but not in the other, a single line is
    generated. But, if the record keys match, each variable for which there is a
    difference will be listed on a separate line with the values from both files
    and the difference.
  - TITLE - |S| - Optional title
    to print with the summary report. It is suggested that the value be embedded
    within quotes.

Example 1

```
LINKI[1] = current.net
LINKI[2] = future.net
COMPARE RECORD=1-2
```

The following is a sample output in the print file:

```
COMPARE 1 vs. 2:
          1=2   ------- 1 < 2 -------   ------- 1 > 2 -------
Variable  Cnt   Cnt   Min   Max   Ave   Cnt   Min   Max   Ave    Ave
--------  ---   ---   ---   ---   ---   ---   ---   ---   ---    ---
A         321    --    --    --    --     7    --    --    --     --
B         321    --    --    --    --     7    --    --    --     --
LANES      --   321     1     1    -1    --    --    --    --     -1
DISTANCE   --   321     1     1    -1    --    --    --    --     -1
SPDCLASS   --   321     2     2    -2    --    --    --    --     -2
CAPCLASS   --   321   1.23  1.23  -1.23  --    --    --    --  -1.23
NAME       --   321    --    --    --    --    --    --    --     --
```

The
1=2 column lists the number of records where the
records are the same. The
1<2
set of columns lists the number of records where the values
for the listed variables are lower in file 1 than in file 2, and the
1>2 set lists the summary where file 1 values
are greater than file 2, The final
AVE column lists the average difference for the
variable, using only records where there is a difference. The
Min and
Max differences show the range of differences for
the variable.

Example 2

```
RUN PGM=NETWORK
  NETI=NET1.NET, NET2.NET
  NETO=NET3.NET
  MERGE RECORD=T
  PHASE=LINKMERGE
    COMPARE RECORD=1-2, LIST=20 ; compare link record 1 with 2
    IF (_COMPARE=-2) CMPFLAG=1 ; link in NET1, not in NET2
    IF (_COMPARE=-1) CMPFLAG=2 ; link in NET2, not in NET1
    IF (_COMPARE>0) CMPFLAG=3 ; link in both but different
ENDRUN
```

Example 2 illustrates how to use
\_COMPARE to flag the links in the merged network. The
CMPFLAG attribute can be used in selection expressions in Viper to post the
comparison results.

CONTINUE

Immediately jumps to the end of a loop, bypassing all stack
statements until the associated end of loop. If it is within a loop, control
passes to the appropriate
ENDLOOP statement. Otherwise (not in a loop),
stack processing for the record is terminated.

Example

```
LOOP _L1=1,3
  IF (!(condition)) CONTINUE
ENDLOOP
IF (condition) CONTINUE  ; no more processing for this data record
LOOP _L2=_K1,_K2,_KINC
   LOOP _L3=_L2,_L2+5
      IF (condition) CONTINUE ; jump to ENDLOOP for _L3
   ENDLOOP
ENDLOOP
```

CROSSTAB

Cross tabulates variables. Keywords and subkeywords
include:

[COL](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__CRCOL)

- [RANGE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__COLRANGE)

[COMP](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__CRCOMP)

- [FORM](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__CRFORM)

[ROW](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__CRROW)

- [RANGE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__ROWRANGE)

[VAR](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__CRVAR)

- [FORM](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__VARFORM)

Use the
CROSSTAB control statement to accumulate a tabular
summary from the network. Use the
VAR keyword to specify the variables you want
tabulated. Use the
ROW keyword along with the RANGE subkeyword and
the
COL
keyword along with the RANGE subkeyword to specify the
tableâs dimensions. If you omit either
ROW or
COL, the report collapses into only one column or
one row. Although the
CROSSTAB
statement can include several instances of the
VAR keyword, the statement tabulates all the
variables to the same specifications. Use the
COMP keyword to generate additional reports after
network generation using the values from the tabulated variables. For example;
if the statement includes
`VAR = VehDist`,
`VehTime`, then including
`COMP = VehDist / VehTime`would produce a table of average speeds.

Note: The program does not automatically produce totals because
your ranges may overlap. You can produce totals and subtotals with appropriate
use of
RANGE values. See below for a description of the
process used in placing values in the appropriate range slots.

CROSSTAB Keywords

- COL - |S| - Name of the variable
  that will be used for the column definition of the report.
  - RANGE - |RV50| - Same as for
    ROW
    (RANGE)\*\*, but applies to the
    COL variable. Care should be taken to not
    cause the reported line to be too long (limit the number of column ranges).
- COMP - |NV| - Expression that can
  be used to generate a report that is some combination of the reports generated
  by the
  VAR
  variables on this statement. The only variable names that
  may appear in the
  COMP expressions are the VAR variables that are
  on this statement. There may be up to ten
  COMP
  expressions on a statement.
- FORM - |S| - Specifies the format
  for the COMP\*\*\*\* reports. The standard CUBE Voyager
  FORM
  syntax is used. If
  FORM is not coded for any COMP\*\*\*\*, the program
  will supply "7cs." The format applies to the COMP\*\*\*\* that it is coded with,
  and to all subsequent COMP\*\*\*\* variables until a new value is encountered. The
  first format will be back-filled to apply to any prior COMP\*\*\*\* variables.
- ROW - |S| - Name of the variable
  that will be used for the row definition of the report.
  - RANGE - |RV50| - Series of
    ranges (and increments) for stratifying the row variable for use in the report.
    A range as either one, two, or three numbers. If more than one number, the
    values are separated by dashes. The three values are low, high, and increment.
    The program establishes ranges for stratifying the
    ROW
    variable values. Each range has a lower limit, an upper
    limit, and an increment. If there is no upper limit, the program makes the
    upper limit equal to the lower limit. If there is no increment, the program
    assumes one row. If there is an increment, the program generates a row for each
    increment, starting at the lower limit, and progressing until the upper limit
    is reached. There are certain problems associated with stratifying non-integer
    data; they are discussed below.
- VAR - |SV10| - Name(s) of the
  variable(s) that are to be tabulated. The value of each variable will be
  accumulated into the cells of the generated table(s). A separate report will be
  generated for each variable named. There may be up to ten
  VAR keywords on a statement.
  - FORM - |S| - Format to use
    when printing the accumulated values in the table. The standard CUBE Voyager
    FORM syntax is used. If
    FORM is not coded for any VAR, the program
    will supply "7cs." The format applies to the VAR that it is coded with, and to
    all subsequent
    VAR variables until a new value is
    encountered. The first format will be back-filled to apply to any prior
    VAR variables.

Range classification strategy

The
ROW RANGE and
COL RANGE values are stored as single- precision
numbers, and the actual variable values are computed and stored as
double-precision floating-point numbers. Single precision provides accuracy to
about six, or seven, significant digits, whereas double precision provides
accuracy to up to fifteen, or sixteen, digits. Because computers do arithmetic
on a binary basis, numbers which seem to be easily described in base 10 cannot
always be represented exactly in the computer. For example: the number 0.01 is
a definite number in base 10, but it can only be approximated in base 2. If the
program compares a variable to a range limit, it might fail due to this
limitation of the computer. The comparison result may differ, depending upon
the floating point capabilities of the computer.

Another concern is the definition of limits. If
RANGE
is 1-10, should a value of 0.9999999999 be included in it? If
RANGE is 1-10-1, should a value of 10.001 be
included, and which range should the value of 2.0001 fall into? To address all
these concerns, the program is designed to check for
RANGE
satisfaction based upon an integer representation of both the
RANGE limits and the data.

You can control the level of precision when specifying the
RANGE values. The level of precision is set by the
maximum number of decimal places in any of the
RANGE values (low-high-increment). The
RANGE values and the ROW and COL variable values
are factored and integerized (rounded) according to the decimal digits. If a
single
RANGE (no increment) is used, the program checks
the value against the limits as: if the value is greater than, or equal to, the
lower
RANGE, and less than, or equal to, the higher
value, the value satisfies the range. If a
RANGE with an increment is used, a similar initial
check is made to determine if the value fits within the outer
RANGE limits. If the value fits with the range,
the increment index is computed (in integer) as: ((value-lo) / inc) + 1.

Examples may best illustrate this process.

| RANGE | Internal Range | Integer Value | Value | Index |
| --- | --- | --- | --- | --- |
| 1-10 | 1-10 | 0.99 | 1 | - |
| 1-10-1 | 1-10-1 | 1.50 | 2 | 2 |
| 1-10-1 | 1-10-1 | 1.45 | 1 | 1 |
| 1-10-1.0 | 10-100-10 | 1.45 | 15 | 1 |
| 1-10-0.5 | 10-100-5 | 1.45 | 15 | 2 |
| 1-3-0.5 | 10-30-5 | 3.00 | 30 | 5 |
| 1-3-0.3 | 10-30-3 | 1.29 | 13 | 2 |
| 1-3-0.3 | 10-30-3 | 3.01 | 30 | 7 |
| 1-3-0.3 | 10-30-3 | 3.001 | 30 | 7 |

There is a caveat with this process. The maximum integer
revised value for either
RANGE or
ROW is 2,147,483,647. For this reason, the program
may adjust the number of decimal digits if either RANGE limit would exceed the
maximum after revising.

Example

```
CrossTab    VAR=DIST, _CNT,
            ROW=VC, RANGE=0.5-1.2-0.1, 0.5-1.2, 1.2-2.5-0.5, 2.5-9999,
            COL=LANES, RANGE=1-7-1, 1-3, 4-7, 1-7, 1-100-5,
CrossTab    VAR=VMT FORM=6.1c, VAR=VHT, FORM = 6.2c,
            ROW=CLASS, RANGE=1-50-1,
            COL=LANE, RANGE=1-10,
            COMP=sqrt(VMT)+10*(min(1000,VHT)),
            COMP=VMT / VHT,
            FORM=8.3 ; weird example & ave trip length
```

DELETE

Deletes data record.

When a data record is being subjected to the operations in a
phase block, and the operation is
DELETE, the remainder of the block operations are
bypassed, and the record is removed from the network. Most likely,
DELETE would be used in conjunction with an IF
statement.

Example

```
If (a=2150-2199 || b=2150-2199) DELETE
;remove all links connected to nodes 2150-2199
```

EXIT

Exits current phase.

Use
EXIT to exit the current phase. The remaining
input records to the phase will not be read.

Example

```
IF (a > 1000) EXIT; no reason to process beyond this link.
```

FILEI

Note: See [FILEI](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__FILEI) on for general information about
FILEI and for important limitations when using
Application Editor.

FILEI inputs data files. Keywords and subkeywords include:

- [GEOMI](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__GEOMI)

  - [AFIELD](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__FAFIELD)
  - [BFIELD](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__FBFIELD)
  - [SEQFIELD](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__FSEQFIELD)
- [LINKI](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__LINKI)

  - [COMBINE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__COMBINE)
  - [DETAILS](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__FDETAILS)
  - [EXCLUDE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__FEXCLUDE)
  - [RENAME](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__FRENAME)
  - [REV](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__FREV)
  - [SELECT](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__FSELECT)
  - [START](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__FSTART)
  - [STOP](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__FSTOP)
  - [TRIPSXY](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__FTRIPSXY)
  - [VAR](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__FVAR)
- [LOOKUPI](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__LOOKUPI_unique_1)
- [NETI](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__NETI_unique_1)- Alias for LINKI, above
- [NODEI](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__NODEI)- Uses the same subkeywords as LINKI (above), except REV and
  TRIPSXY

The
FILEI
statement specifies the input files that contain the network
data. You may designate up to ten
NODEI, ten
LINKI and ten
GEOMI files in a FILEI
statement (GEOMI support GIS inputs; see next page).

Upon recognizing a
LINKI file as a binary file, the program
automatically assumes a corresponding
NODEI
file. To preclude the program from using the node data in the
automatic
NODEI
file (not recommended), provide a
NODEI file with the same index as the
LINKI
file.
NODEI files that have the same index as a
binary-network
LINKI file must precede the
LINKI file.

On the other hand, you may list non-binary
LINKI
and
NODEI files in any order. CUBE geodatabase
networks have associated link and node stand-alone feature classes. If a
LINKI file is a CUBE geodatabase network, the
automatic corresponding
NODEI file is the networkâs node stand-alone
feature class.

Upon reading input files, the program truncates field names
longer than 15 characters. If truncation results in duplicate field names, the
program automatically renames fields to avoid duplicate names.

If you code value limits for a variable (with
MIN=, MAX=), the program
only checks those limits during the INPUT phase. If the limits are exceeded,
the program rejects the record as an error and does not process the record. The
program does not edit input record keys before stack processing. You can decide
how to handle records with invalid keys. After stack processing, the program
ensures that key values range from 1 to the number of nodes. If a key is
outside this range, the program lists the record as an error. If the input file
contains many extraneous records (invalid data records-possible if coming from
a GIS DBF with extra data), you can check the key (N, A,
or
B) and
DELETE the record, or recode the key.

NETWORK also includes the
GEOMI keyword to input Shape and Geodatabase
geometry sources.
GEOMI has three advantages over using
LINKI as geometry source:

It eliminates the need to read and merge a GDB network into
the final network if it is needed as a geometry source only.

It allows using shape files as geometry source since
LINKI does not allow shape files as input.

It will not merge the data fields or data records into the
base network because it is not a
LINKI.

FILEI Keywords

GEOMI - |KFV10| - Input file(s) to
NETWORK to act as link geometry source for output GDB networks and shape files.
GEOMI
may be indexed with up to ten shapefile (\*.shp) or
Geodatabase sources.

The
GEOMI index can be 1, even when there is already a
LINKI[1] specified. If there is a
[LINKI](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__LINKI) GDB network and a
GEOMI GDB/SHP specified with the same index, the
GEOMI data will be used as the geometry source â
thus it will override
LINKI
if both are specified.

The source of the link geometry is specified in the
LINKMERGE phase by setting the GEOMETRYSOURCE variable.

For an example of usage, see Example 2.

Note: You can force Network to search a geometry source in both
the forward and reverse directions. This is useful for matching 1-way links
with their corresponding geometries coded in the reverse direction. Simply list
the file twice as the first two
GEOMI
inputs.
GEOMETRYSOURCE must be unspecified or 2. Network
will search first in one direction, and if the link match is not found, it will
check the opposite direction.

- AFIELD - |S| - A node field name.
  Default is âAâ.
- BFIELD - |S| - B node field name.
  Default is âBâ.
- SEQFIELD - |S| - True shape
  sequence number field name. Default is none.

LINKI - |KFV10| - Name of file or
files that contains link-based records (may be indexed up to ten files). The
file format can be:

- ASCII
- DBF
- MDB data table
- CUBE geodatabase network
- Link stand-alone feature
  class in a geodatabase network
- Recognized binary network.

The program will try to detect what type of file it is. If
it cannot identify the file as a DBF, MDB, CUBE geodatabase network, or a
binary network, it will assume ASCII. If it detects that the file is a
MINUTP binary network, the variables DIST, SPDC,
CAPC, and LANE will automatically be renamed to
DISTANCE, SPDCLASS, CAPCLASS, and
LANES, respectively.

Since most applications will input binary networks or CUBE
geodatabase networks, you can use the keyword
[NETI](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__NETI_unique_1)as an alias for
LINKI. If the
LINKI file and the
NODEI file are DBF or MDB format then at a
minimum, the
LINKI
file must have a field named A and a field named B and the
NODEI file must have a field named N. If these
fields in the DBF or MDB do not use this naming convention, then the
RENAME keyword below can be used to rename the
variables on input.

Note: A valid network in CUBE Voyager/TP+ need not have
coordinate variables on the node records. If the network is to be viewed/edited
in CUBE then it must have variables named
X and
Y on the node records to hold the coordinate
data.

COMBINE - |?| - Flag that indicates
whether multiple link or node records exist on the input data file. The
following subkeywords can be used to specify how to combine attributes values
across multiple link or node records.

FIRST, LAST, AVE, SUM, MAX, MIN, CNT,
AVEX0

The descriptions of these keywords are identical to those
described for the
MERGE
statement.

The default for any variables not combined will be
consistent with the value of
PARAMETERS REPL\_DUPL. If
REPL\_DUPL is true, the unlisted vars will be set
to
LAST, otherwise to
FIRST.

Example of usage:

```
FILEI LINKI=linki.dat, vars=
v1,v2,v3,v4,v5,v6,v7,v8 combine=t,
ave=v1,v3,v4 ave=v6,v8

FILEI NODEI=node.dat, vars=n,x,y, combine=t,
first=x, last=y
```

- DETAILS - |?| - Flag that
  indicates if you would like to keep the full iteration results from an input
  loaded Tranplan network on the output file and have the iteration specific
  attributes available as li. variables during the run.
- EXCLUDE - |SV| - Name(s) of
  variable(s) excluded from the file. Only relevant if the file is a DBF or
  binary network file and you do not want certain variables from the file, or if
  the input is defined as a series of variables (in delimited format â not with
  BEG/LEN), and you do not want to extract certain
  variables from the input records.
- RENAME - |SP| - Use to rename a
  variable from the input file. The format is
  `RENAME=oldname-newname`; both names must be specified.
  Names can be swapped on one statement; to swap names for V1 and V2:
  `RENAME=V1-temp1,V2-V1,temp1-V2`.
- REV
  - |I| - Parameter that can be used in conjunction with
  files that are ASCII or DBF to specify if an input record is to represent a
  single directional link or if it is to be considered as two links (A-B and B-
  A, with the B-A values being the same as the A-B values). Under normal
  conditions, an input record represents a single directional link from A to B.
  The REV parameter is used only if:
- There is no REV variable on
  the record.
- There is a REV variable on
  the record, but its value is neither 1 nor 2.

If there is a
`VAR=REV` defined for the link data records, the value of
the
REV should be a 1 or a 2. If the value is not a 1
or a 2, the reversibility of the link is determined by the value assigned to
this keyword. The only valid values for this keyword are 1 and 2; the default
is 1. The record variable defined as
REV will be treated as any other link variable,
but it will
not be written to the output network (the
NETO will not contain a variable named
REV ).

- SELECT - |s| - Used only with
  ASCII input when it is desired to select only certain records from the file.
  The syntax is the same as for
  START. SELECT is processed after any
  STOP statement, and before any editing.
- START - |s| - Used only with ASCII
  input where the first valid data record follows some identifying header record.
  The expression value must be enclosed within parenthesis (), and the only valid
  variable is
  RECORD, which is the actual data record. The
  primary purpose is to allow the user to specify that there is a header, and how
  to identify it. The expression should contain a
  SUBSTR function to extract the header.
  START is used to position the file before actual
  data records are read.
- STOP - |s| - Used in a manner
  similar to the
  START keyword, but is associated with a trailer
  record.
  STOP is processed immediately after a record is
  read, and before any field editing.
- TRIPSXY - |F| - Name of a file
  that contains TRIPS X-Y data. This keyword is only required for TRIPS networks.
- VAR - |SV| - Name of a variable to
  be extracted from the file. Name lengths may not exceed 15 characters; case is
  ignored.

To read variables from fixed-format text files, use the
BEG and
LEN subkeywords.

To read character-string variables from free-format text
files, use the subkeywords
TYP and
LEN, or append (C) or (Cn) to the variable name,
where n specifies the number of characters.

To read character-string variables from fixed-format text
files, use the TYP, BEG, and
LEN subkeywords.

If the file is ASCII, and the variable is to be extracted
from specific positions on each file record,
BEG and
LEN will have to be specified. The program assumes
that ASCII files are free format and all fields are separated by white space, a
comma, or some combination of both. Examples of free-form records:

```
1  2  3
1, 2, 3
1 ,          2  3
1      ,2,3
```

All four of the above illustrated records contain three
fields: 1, 2, and 3.

Subkeywords of
VAR include:

- BEG - |I| - Designates the beginning
  of the field in the input records. The first column of the record is designated
  as 1.
- LEN - |I| - Designates the length of
  the field that begins at position
  BEG.
- TYP - |S| - May be used to specify
  that the format of the variable is not numeric. An "A" means that the variable
  is alphanumeric. If
  `TYP=A` is specified for free format input, the
  LEN must also be specified, or it will default
  to 1. TYP A variable values on free format input must be enclosed within quote
  or literal marks (ââ¦â or "â¦"), if they contain special characters (other than
  alphanumeric characters: a-z, 0-9).
- MIN - |R| - May be used to specify a
  minimum allowable value for the field. If the input value of the variable is
  less than this value, the variable will be rejected as an error.

VAR may also be specified with
parameters directly (without the above subkeywords). If the field following the
variable name is a number, this format is automatically triggered. The total
format is name,beg,len,min,max,typ. All these fields must be numeric, or null.
A null field is specified by coding two commas with nothing between them. The
parameter list is considered as exhausted when a non-numeric field is
encountered. Typ must be coded as 1 to indicate that the variable is to be an
alphanumeric field.

Example:
`VAR=A,1,5,B,6,5` (A is in columns 1-5 and B is in 6- 10).
If the first two numbers that follow the name are separated by a dash, the
numbers indicate the actual columns of the data record where the field is
located.

For example:
`VAR=A,1-5,B,6-10` (A is in columns 1-5, and B is in
columns 6-10). If both forms may be used to specify variable (numeric format,
followed by any of the sub-keywords); the keyword values will override the
positional numbers.

LOOKUPI
- |KFV999| - Name of file containing records for a lookup
function implemented with the LOOKUP control statement.

Equivalent to the
[FILE](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__FILE) keyword of the LOOKUP control statement. You must index
LOOKUPI.

NETI - |KFV10| - Alias for
[LINKI](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__LINKI).

NODEI - |KFV10| - Name of a file or an
MDB and element that contains node-based records.

NODEI may take a standalone node
shapefile as an input. The shapefile must have an associated DBF file. NETWORK
will create a new DBF with all fields and data as the original shapefile. It
will also add X&Y fields to contain the associated point coordinates.

See
[LINKI](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__LINKI) for comments regarding file detection.
NODEI uses the same keywords as
LINKI except
REV and
TRIPSXY.

Example:

```
RUN PGM=NETWORK
FILEI LINKI[1]="LINKS.DBF"
FILEI NODEI[1]="NODES.SHP"
; shape file should include the node number ; field 'N' must be specified
FILEO NETO="HIGHWAY.NET"
ENDRUN
```

Example 1

This section contains some examples of
FILEI LINKI and
FILEI NODEI usage.

```
LINKI[1]=\demo\demo20.dat exclude=dist,tsin  ; file is binary network
NODEI[1]=C:\DEMO\DEMOXY.DAT VAR=N,X,Y        ; file is ASCII
NODEI[2]=\demo\demo21.dat, LINKI[2]=\demo\?07.dat,
       var=a,beg=1,len=5,
       var=b,beg=6,len=5,
       var=dist,beg=14,len=4,
       var=rev,beg=35,len=1
LINKI[3]=freeform.fil, VAR=a,b,name,21,5,,,1,section,0,5
;section follows name in free form
nodei[4]=c:\citya\nets\linka.dbf, linki[4] = c:\citya\nets\nodea.dbf
LINKI[8]=Mixed_Node_and_Link.lxy, var=a,b,distance,
       start=(substr(record,1,2)=='LD'),
       stop=(substr(record,1,2)=='XY')
NODEI[8]=Mixed_Node_and_Link.lxy, var=n,x,y,
       start=(substr(record,1,2)=='XY'),
       stop=(substr(record,1,2)=='LD')
```

Example 2

This example specifies a shapefile Geometry source, then
link and node shape outputs matching that geometry. The associated DBF file
will be from the LINKO/NODEO process. Note that the GEOMI index is 1, even with
LINKI[1] specified. The GEOMI data will be used as the geometry source.

```
RUN PGM=NETWORK
FILEI LINKI[1]="2005HWYLOAD.NET"
FILEI GEOMI[1]="SHAPES\LINK3.SHP"
FILEO LINKO="SHAPES\LINK4.SHP" FORMAT=SHP INCLUDE=A,B,DISTANCE,CAPACITY,SPEED,TIME
FILEO NODEO="SHAPES\NODE4.SHP" FORMAT=SHP
phase=linkmerge
   GEOMETRYSOURCE=1
ENDRUN
```

FILEO

Generates output filesâa network file, link file, and node
file. Keywords and subkeywords include:

- [LINKO](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__LINKO)

  - [DELIMITER](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__LI_2124A7167A854A67A20BC2E4739D49CE)
  - [EXCLUDE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__LI_A5FCAB802B8547329BE6C595A7E03C67)
  - [FORM](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__LINKOFORM)
  - [FORMAT](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__LINKOFORMAT)
  - [INCLUDE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__LINKOINCLUDE)
  - [VARFORM](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__LINKOVARFORM)
- [NETO](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__NETO_unique_1)

  - [EXCLUDE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__LI_9F6B1C48338342758A948FF2915E1331)
  - [FORMAT](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__NETOFORMAT)
  - [INCLUDE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__NETOINCLUDE)
  - [LEFTDRIVE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__LI_AEE8E4F549204E33885DEE876B79DBFD)
- [NODEO](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__NODEO)- Uses the same subkeywords as LINKO (above).
- [PRINTO](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__PRINTO_unique_2)

  - [APPEND](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__FAPPEND)

FILEO Keywords

LINKO - |KF| - Name of a non-CUBE
Voyager output file in which the program writes link records.

May be any of the formats described by the
[FORMAT](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__NETOFORMAT) subkeyword, or otherwise, a geodatabase/element
name. This is a CUBE geodatabase network, or table, stored in an MDB file
(personal geodatabase) or GDB (file geodatabase). Designate the file name
followed by a backslash and the CUBE geodatabase network/table name.

Note: Networks stored in personal (MDB) geodatabases are limited
to a maximum of 255 fields, including the default geodatabase network fields
(OBJECTID, SHAPE, SHAPE\_LENGTH, A, B, GEOMTERYSOURCE, etc).

- DELIMITER - |S|
  - Character used as the delimiter in SDF and TXT files. To specify special
  characters (, - / + \* = ;), enclose within quote marks or specify using its
  decimal equivalent (for example, tab is code 9). The default value is a comma;
  but there is no default value for TXT files.
- EXCLUDE - |SV|
  - Similar to
  [EXCLUDE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__missing-elem-id--NETOEXCLUDE) under NETO.
- FORM - |S| - Sets the print
  format of all variables written to the file. Usually specified as w.d to
  indicate the maximum field width and number of decimal places to preserve. See
  [Defining a numeric print format](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__DEFININGNUMERICPRINT) and
  [Defining a character print format](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__DEFININGCHARACTERPRINT). Optional format codes are
  usually not appropriate for use on this statement.
- FORMAT - |S| - Sets the file
  format of the
  LINKO file. Possible values are:
  - TXT - File of ASCII
    records in which all the data fields are written in a fixed format.
  - SDF - File of ASCII
    records in which the data fields are written in variable length, and separated
    by a delimiter.
  - CS1 - File of comma
    separated values with one header row. The header row contains comma separated
    field names.
  - CS2 - File of comma
    separated values with two header rows. The first header row contains two comma
    separated values [number of fields and number of records] and the second header
    row contains comma separated field names.
  - DBF - Industry-standard
    database file. If there is a ? in the name, and there is no filename extension
    to the
    LINKO
    value, an extension of this value will be appended to
    the filename. If a DBF is written, and a designated
    FORM does not provide adequate width and
    decimal space for a field value, the program will try to adjust the field form
    within typical database rules to fit the value into the field space.
  - SHP - Industry-standard
    shapefile. The file extension must be .shp.

NETWORK will write the shape file with geometry from the
geometry source(s) but the associated DBF file will be from the
LINKO process. This will allow using the
[INCLUDE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__LINKOINCLUDE) and
[EXCLUDE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__missing-elem-id--LINKOEXCLUDE) keywords to limit the fields written to the shape
file DBF.

When an associated node shape file is specified using
LINKO
[NODEO](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__NODEO)
FORMAT=SHP, it must reside in the same folder as
the link shapefile. Otherwise, both files will be consolidated to the
LINKO folder.

For more on usage with the SHP FORMAT, see [Example 2](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__FILEOEXAMPLE2).

- INCLUDE - |SV| - See INCLUDE
  under
  NETO. INCLUDE variables may have a format
  appended to their names in a manner similar to
  VARFORM. The same variable may be included
  multiple times.

When used with INCLUDE, a scriptâs
output network file (LINKO) must be created after
linking its input network file ([LINKI](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__LINKI) or
NETI
).

- VARFORM - |SV| - Sets the
  format for specific variables. Specify a variable name with its desired format
  appended in parenthesis. For example,
  `VARFORM=A(4.0), B(4.0)` sets A and B to be formatted as
  4 characters wide with no decimal places. If the file format is SDF, the
  program deletes leading spaces. Only specify this keyword for variables that
  require specific formats.

When setting a variableâs format, the program first
determines a default format. Then, the program applies the formats as they
appear on the statement. Therefore, if the same variable appears with both a
VARFORM subkeyword and an
INCLUDE subkeyword, the latest appearance
prevails. Similarly, the latest FORM prevails for any variables not explicitly
named in a
VARFORM and/or
INCLUDE subkeyword.

NETO - |KF| - Name of the standard
output network that the program writes. The
NETO can be a binary CUBE Voyager/TP+ network.
Alternatively,
NETO can point to a CUBE geodatabase network
stored in an MDB file (personal geodatabase) or GDB (file geodatabase) by
designating the file name followed by a backslash and the CUBE geodatabase
network name.

Note: Networks stored in personal (MDB) geodatabases are limited
to a maximum of 255 fields, including the default geodatabase network fields
(OBJECTID, SHAPE, SHAPE\_LENGTH, A, B, GEOMTERYSOURCE).

- EXCLUDE - |S| -
  List of variables excluded from the output network. Listed variables that exist
  in both node and link records are excluded from both records. To exclude a
  variable from only the link records, add the LO. prefix to the variable name.
  To exclude a variable from only the node records, add the NO. prefix to the
  variable name. CUBE Voyager ignores listed variables that do not exist in any
  of the input files, and does not issue a warning.

Do not use with the INCLUDE
subkeyword.

- FORMAT
  - |S| - Specifies the file format for writing the output
  network. Normally, this is not specified; the program will write the file as a
  standard CUBE Voyager binary network.

If the
NETO keyword specifies an MDB/element name, the
program writes the output as a CUBE geodatabase network in the MDB file under
the element name. The program also creates two stand-alone feature classes in
the MDB file,
element\_Node and
element\_Link, and a table,
element\_SPDCAP, that contains the indices and
values from the internal speed and capacity table. The output CUBE geodatabase
network will contain the additional link and node attribute,
GEOMETRYSOURCE, which contains the input file
number from which the geometry will be applied (for more information on
GEOMETRYSOURCE see
[Built-in variables](GUID-5AF1421D-6629-4614-820B-514AF97CEEDA.html#GUID-5AF1421D-6629-4614-820B-514AF97CEEDA__BUILTINVARIABLES_unique_1)).

Specify
`FORMAT=MINUTP` to write a MINUTP network. MINUTP string
variables are truncated to 80 characters. Specify
`FORMAT=TRIPS TRIPSXY=fname` to write a TRIPS network and
its associated XY file.

- INCLUDE - |S| - List of
  variables included in the output network. If you use this subkeyword, the
  output network only includes the listed variables.

When
INCLUDE
is used, the
FILEO NETO statement should be declared below the
FILEI [LINKI](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__LINKI) statement.

Example 1

```
FILEI LINKI[1]="C:\MYMODEL\INPUT.NET"
FILEO NETO="C:\MYMODEL\OUTPUT.NET",
INCLUDE=LANES
```

In the case of Application Editor, create the
NETO
file reference before creating the
LINKI/NETI reference. This will make the
NETI/LINKI and
NETO statements appear in the order discussed
above.

Do not use with
EXCLUDE subkeyword.

- LEFTDRIVE - |?|
  - Flag that indicates whether the program writes a flag in the output network
  file to indicate whether vehicles drive on the left in the network. This is
  primarily for use in JUNCTION modeling in the Network program; it does not have
  any affect on any [PLOT](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__PLOT) statements in Network. This keyword is not necessary
  if the lowest numbered
  LINKI file had the
  LEFTDRIVE
  parameter set, or if
  [PARAMETERS LEFTDRIVE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__PLEFTDRIVE) is specified. The setting of the
  NETO value follows the rules:

If
PARAMETERS LEFTDRIVE is specified, use that value.

Else if
NETO LEFTDRIVE is specified, use that value.

Else if lowest LINKI contains a
LEFTDRIVE value, use that value.

Else do not set this value.

NODEO - |KF| - Name of a non-CUBE
Voyager output file in which program writes node records. Its subkeywords are
the same as those for [LINKO](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__LINKO).

May be any of the formats described by the
[FORMAT](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__LINKOFORMAT) subkeyword under the
LINKO keyword, or may be an MDB/element name.

Note: Networks stored in personal (MDB) geodatabases are
limited to a maximum of 255 fields, including the default geodatabase network
fields (OBJECTID, SHAPE, N, GEOMTERYSOURCE, etc).

PRINTO
- |KF| - Name of the file where the program directs output
from a
PRINT statement using
`PRINT PRINTO=#`.

- APPEND - |?| - See APPEND under
  [PRINT](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__PRINT).

The program produces output files by combining data from
the input files. Use the
[MERGE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__MERGE) statement to specify how to process duplicate
records. Unless you specifically exclude fields with the
EXCLUDE subkeyword, the output files will contain
the fields from all the input files, even if you do not merge the files and the
output file contains no data from a particular input file.

When writing output files, the program generates an output
network first even if
NETO is not specified. The program derives both
LINKO and
NODEO from the output network; the link and node
files are subsets of the output network. Consequently, if you specify
NETO
and exclude a link variable, then that link variable will not
be available for
LINKO.

Example 1

```
FILEO NETO=MY.NET
NETO=DEMOMINU.DAT, FORMAT=MINUTP, EXCLUDE=TEMP1, TEMP2
NODEO=TEXTNODE FORMAT=TXT, FORM=8.0 INCLUDE=A,B,DIST,SPEED,SPDCAP(2)
LINKO=LINK FORMAT=DBF VARFORM=VC(6.3)
```

Example 2

This example specifies a shapefile Geometry source, then
link and node shape outputs matching that geometry. The associated DBF file
will be from the LINKO/NODEO process.

```
RUN PGM=NETWORK
FILEI LINKI[1]="2005HWYLOAD.NET"
FILEI GEOMI[2]="SHAPES\LINK3.SHP"
FILEO LINKO="SHAPES\LINK4.SHP" FORMAT=SHP
INCLUDE=A,B,DISTANCE,CAPACITY,SPEED,TIME
FILEO NODEO="SHAPES\NODE4.SHP" FORMAT=SHP
phase=linkmerge
   GEOMETRYSOURCE=2
ENDRUN
```

IF â¦ ELSEIF â¦ ELSE â¦ ENDIF

Performs certain operations based on conditions.

Code IF condition blocks like
standard CUBE Voyager specifications. Enclose the
IF
and
ELSEIF selections within parenthesis; the
selections can reference any variables that are valid for the current phase.
See
[IF â¦ ELSEIF â¦ ELSE â¦ ENDIF](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__missing-elem-id--IFELSE%20) for more details.

Example

```
PHASE=INPUT, FILE=NI.1
IF (N==5)
.
ELSEIF (N=1,3, 8-42 && X<3000 || Y=1-500,800-900)
.
ELSE
.
ENDIF
ENDPROCESS
IF (I < (K*3/6 +J) ) DELETE
```

LOOP...ENDLOOP

Controls a general variable loop.

```
LOOP LVAR=Lbeg,Lend,Linc ;
...
ENDLOOP
```

where:

- LVAR is the name of the loop control variable.
  LVAR is not protected during the loop;
  computational, program, and other
  LOOP statements can alter its value.
  LVAR must be followed by
  Lbeg, and optionally, by
  Lend and
  Linc.
- Lbeg
  is a numeric expression that initializes
  LVAR.
- Lend
  is a numeric expression that is computed and stored when the
  LOOP
  statement is first processed.
  LVAR is incremented by
  Linc, and compared with Lend when the
  ENDLOOP statement is processed. If
  Lend
  is not specified, it is assumed no comparison is to be made
  (rather meaningless loop).
- Linc is a numeric expression that is computed and stored
  when the
  LOOP statement is first processed. The value is
  added to
  LVAR before the
  ENDLOOP comparison is made. If
  Linc
  is not specified, it will be set to 1 (-1 if
  Lbeg and
  Lend are both constants and
  Lbeg < Lend; a backwards loop).

Note: All variables in a
LOOP statement expression (Lbeg, Lend, Linc) must begin with the underscore
character â\_â to prevent confusion with record variables.

Use
LOOPâ¦ENDLOOP blocks to repeat of a series of
statements. LOOP initializes a variable(LVAR);
ENDLOOP compares the contents of the variable to
another value (Lend), and branches back to the
statement following the LOOP statement if the comparison
fails.
LOOP blocks may be nested; they may not overlap
IF blocks. The logic is as follows:

- At
  LOOP:
  - Initialize
    LVAR to
    Lbeg.
  - Compute the value for
    Lend.
  - Compute the value for
    Linc (default to 1 if missing).
  - Proceed to next
    statement.
- At
  ENDLOOP:
  - If
    Lend not specified, jump to next
    statement.
  - Add
    Linc to
    LVAR.
  - Compare
    LVAR
    to
    Lend.
  - Either jump back to
    statement following associated
    LOOP, or drop through.

The
Lend and
Linc
variables are processed somewhat differently than in the other
programs; they are computed at the
LOOP statement and can not be modified by other
statements. This helps to protect against possible endless loops. The loop will
be processed at least one time regardless of Lend
and Linc values. Most uses will
involve constants. Because
LVAR values can be expressions,
Lbeg,
Lend, and Linc
must be separated by commas (standard white-space delimiting
cannot be interpreted properly). If an expression is used, it is suggested that
it be enclosed in either parentheses or quote marks.

Example

```
LOOP _pass=1,10 ; perform 10 passes
...
ENDLOOP
LOOP _xyz=_abc*_def,_ghi+_jkl,_mno/_pqr
  LOOP _abc=_xyz,_xyz+2,2 ; nested LOOP
  ...
  ENDLOOP
ENDLOOP

LOOP _jj=10,3,-2.5 ; perform 3 passes -- 10, 7.5, 5.0
...
ENDLOOP
```

MERGE

Specifies record and variable merging. Keywords include:

[RECORD](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__MRECORD)

[AVE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__MAVE)

[AVEX0](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__MAVEX0)

[CNT](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__MCNT)

[FIRST](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__MFIRST)

[LAST](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__MLAST)

[MAX](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__MMAX)

[MIN](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__MMIN)

[SUM](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__MSUM)

Use
MERGE to specify how to merge records from
different files, and how to combine variables in a merged record. Note that
merging records and combining variables are independent processes.

Use the
RECORD keyword to indicate whether to merge data
in duplicate records when encountering identical keys during the NODEMERGE or
LINKMERGE phases.

Use the other keywords to specify the method for determining
data values for specific variables when merging data in duplicate records from
different input files. (Duplicate records from the same file may not occur in
the MERGE phase.) Each resulting record will have a cell for every variable
specified in any input file or any
COMP statement.

MERGE Keyword - Selecting Records

RECORD - |?| - Flag that indicates
whether to merge duplicate records:

- False - Include only the
  records that exist in the
  [FILEI](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__FILEI_unique_3)with the lowest index [].
- True -
  `Default value`. Include any unique record included.

If you input two networks (NETI[1] and NETI[2]) and
`RECORD=FALSE`, the program only processes the links that
are in NETI[1].

Use the following keywords to indicate how to obtain the
value of variables when merging records. The program only obtains variable
values from file records that contain the variable. Only list a variable with
one keyword; the program uses the
FIRST keyword for variables not listed with any
keyword.

MERGE Keywords - Technique

AVE - |SV| - Average of all records.

AVEX0 - |SV| - Average of all
records, where the value from the file records is not 0.

CNT - |SV| - Count of the records that
contain the variable.

FIRST - |SV| - Directly from the
record from the FILEI with the lowest index[].

LAST - |SV| - Directly from the record
from the FILEI with the highest index [].

MAX
- |SV| - Maximum value of all the records.

MIN - |SV| - Minimum value from all the
records.

SUM
- |SV| - Sum of all the records.

Example

```
MERGE RECORD=TRUE FIRST=CAPCLASS,SPDCLASS, LAST=LANES, AVE=DISTANCE,
SUM=COUNT
```

Illustration for sample input files (â indicates variable
not defined for file):

```
FILEI
LINKI[1]=FILE1,VAR=A,B,DISTANCE,SPDCLASS,CAPCLASS,LANES
FILEI LINKI[2]=FILE2,VAR=A,B,COUNT
FILEI LINKI[3]=FILE3,VAR=A,B,DISTANCE,LANES

LINKI[]   A    B    DISTANCE   SPDCLASS   CAPCLASS   LANES   COUNT
1         101  102  10.1       11         11         1       --
1         105  106  12.5       12         12         3       --
2         101  102  --         --         --         --      1000
2         102  103  --         --         --         --      1000
3         101  102  11.5       --         --         2       --
3         102  103  12.6       --         --         2       --
3         104  105  1.0        --         --         3       --
```

Order as seen in LINKMERGE, after being processed in the
INPUT phase.

```
LINKI[]   A    B    DISTANCE   SPDCLASS   CAPCLASS   LANES   COUNT
1         101  102  10.1       11         11         1       --
2         101  102  --         --         --         --      1000
3         101  103  11.5       --         --         2       --
2         102  103  --         --         --         --      2000
3         102  103  12.6       --         --         2       --
3         104  105  1.0        --         --         3       --
2         105  106  12.5       --         --         3       --
MERGE RECORD=FALSE ; Resulting file:

A    B    DISTANCE   SPDCLASS   CAPCLASS   LANES   COUNT
101  102  10.1       11         11         1       1000
105  106  12.5       12         12         3       0
MERGE RECORD=TRUE FIRST=COUNT, AVEX0=DISTANCE
 ; Resulting file:

A    B    DISTANCE   SPDCLASS   CAPCLASS   LANES   COUNT
101  102  10.8       11         11         1       1000
102  103  12.6       0          0          2       2000
104  105  1.0        0          0          3       0
105  106  12.5       12         12         3       0
```

PARAMETERS

Specifies basic parameter values. Keywords include:

[LEFTDRIVE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__PLEFTDRIVE)

[LIST\_ERRS](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__LISTERRS)

[MAX\_IP\_ERRS](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__PMAXIPERRS)

[NODES](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__PNODES)

[REPL\_DUP](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__PREPLDUP)

[SHAPEANGLE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__PSHAPEANGLE)

[SORTANGLE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__SORTANGLE)

[ZONES](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__PZONES_unique_1)

PARAMETERS Keywords

LEFTDRIVE - |?| - Used to force a
LeftDrive switch into the
NETO. By default, this value is not set. See
FILEO NETO LEFTDRIVE in
[FILEO](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__FILEO_unique_3) for more details.

LIST\_ERRS - |KI| - Specifies how
many records with data errors will be listed before turning off the error
listing. Default value is 20.

MAX\_IP\_ERRS - |KI| - Specifies
how many records with data errors are allowed. If this value is exceeded, the
program will terminate with a fatal condition. Default value is 20.

Records with errors are not skipped, unless the error is in
the key (for example, node number). The bad fields will be set to 0, unless the
error is a limits error.

NODES - |KI| - Specifies the highest
node number to be allowed in the network. This need not be specified (by
default, the program detects the highest number); but if it is specified, any
node numbers that exceed this value are considered errors.

The value specified must be greater than 0; values up to
the license node limit are allowed.

REPL\_DUP - |K?| - Switch that
indicates how to process records from an input file with matching node numbers.
If this switch is true, the later record will replace any previously read
records. Default value is false.

This keyword applies to each NODEI or LINKI file as it is
read within any PHASE=INPUT. (Any nonbinary file will automatically be
processed within an input phase; binary files should not have duplicate
records.) The
MERGE control statement is used to determine how
duplicate links from different inputs are to be processed during the MERGE
phases. To obtain a listing of duplicate links, specify `REPORT
DUPLICATES=T`.

SHAPEANGLE - |K?| - Use shape to
determine link angles. Default is False. By default, link angles are calculated
using straight lines. If a shape file is specified as a GEOMI input, which has
the A and B node fields, then setting this parameter will enable the
calculation of link angles using the shapes in the GEOMI input.

SORTANGLE - |K?| - Option to allow
sorting the relative angle of the legs with respect to the current leg, to make
it easier to process the list of inbound/outbound links. Default is False. For
N and A, the legs are sorted based on the inbound relative angles. For B, the
legs are sorted based on the outbound relative angles. Inbound sorting is used
for A node, since it will be useful to look at the turns into the A node and
similarly outbound sorting is used for B node, since it will be useful to look
at the turns out of the B node.

ZONES - |KI| - Specifies the number
of zones in the network. This is required only if the number of zones cannot be
determined from the LINKI and NODEI files, or it is desired to alter the number
of zones. By default, the program detects the value.

The value must be greater than 0 and less than 20000. A
temporary variable \_ZONES is initially set equal to this
value, and can be used in
COMP and
IF
expressions. If
ZONES is used in a
COMP statement, it will become a variable in the
output network. If this parameter value is not supplied (or is not available
from an input binary network), the program will set it to the highest node
number in a monotonic string beginning at 1.

All the values on this statement are trigger keys;
the PARAMETERS control word need not be specified. Each
keyword could begin a new statement.

Example

```
PARAMETERS repl_dup=n
MAX_IP_ERRS=10
nodes=35000 zones=2203
```

PLOT

Selects links/nodes for plotting.

[DRAWA](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__DRAWA)

[DRAWLINK](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__DRAWLINK)

[LINKPOST](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__LINKPOST)

[NODEPOST](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__NODEPOST)

PLOT statements in the LINKMERGE
phase control plotting. After the program completes the LINKMERGE stack for a
link, it processes the final values for the
PLOT keywords that may have been applied to the
link. If there are no
DRAWLINK values present, the link is not processed
for plotting. If there are DRAWA and/or
NODEPOST values, they are saved until all the
links from the current A-node are completed. When the A-node is completed, the
node values are saved for post processing, so that node symbols will be
prominent on the display.

If there is a
LINKPOST value, but there is no
DRAWLINK value, the
LINKPOST
value is ignored. The situation for nodes is different; a
node can be posted without a symbol.

A PLOT statement may be specified on a short IF statement,
but it must begin with one of the keywords.

PLOT Keywords

DRAWA - |S4| - Specifies the
characteristics for drawing a symbol for the A-node of the link. Possible
values are:

- Color â A value as described
  in
  [PLOTTER](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__PLOTTER).
- Size â Size of the symbol.
- Symbol â Centered on the
  node, can be Circle, Rectangle, or Triangle.
- Fill

DRAWLINK
- |KS4| - Specifies the characteristics for drawing this
link: color, size, and style. Color is a value as shown in the PLOTTER
description, below. Size is the width of the line; current Windows drivers do
not allow both size and style at the same time (style is changed to solid if a
width is specified). Possible styles are: Solid, Dash, Dot, DashDot,
DashDotDot. If PLOTTER BANDWIDTH is specified and the bandwidth variable has a
value, Size and Style are ignored. It is recommended that Size usually be left
null.

LINKPOST - |S| - Specifies the
color that this link is to be posted with.

NODEPOST - |S2| - Specifies the
color and size of the variables that are to be posted for this Anode. (See
NODEPOSTVARS under
[PLOTTER](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__PLOTTER) for information about which variables are to be
posted.)

Example

See
[Examples and FAQ](GUID-6B29A589-C26B-4AE9-BA0D-3CD02DFA925D.html)

PLOTTER

Specifies plotting parameters

- [BANDWIDTH](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__BANDWIDTH)

  - [FILL](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__BFILL)
  - [TAPER](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__BTAPER)
- [DEVICE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__DEVICE)
- [FILE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__FILE_unique_1)
- [FOOTER](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__FOOTER)

  - [ALIGN](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__FALIGN)
  - [FONT](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__FFONT)
- [HEADER](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__HEADER)

  - [ALIGN](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__HALIGN)
  - [FONT](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__HFONT)
- [LEGEND](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__LEGEND)

  - [FONT](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__LFONT)
  - [LINE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__LLINE)
  - [SYMBOL](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__LSYMBOL)
- [LINKOFFSET](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__LINKOFFSET)
- [MAPSCALE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__MAPSCALE)
- [MAPWINDOW](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__MAPWINDOW)
- [MARGINS](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__MARGINS)
- [PLATESIZE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__PLATESIZE)
- [POSTLINKVAR](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__POSTLINKVAR)

  - [FONT](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__PFONT)
  - [POST](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__PPOST)
- [POSTNODEVAR](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__POSTNODEVAR)

  - [FONT](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__POSTFONT)

The
PLOTTER
statement specifies the configuration for plotting link
and/or node information. See
["Plotting"](GUID-F974D638-B07C-4609-8EFC-62EEAD395456.html#GUID-F974D638-B07C-4609-8EFC-62EEAD395456__PLOTTING) for some information about getting your printer
device installed and its basic configuration established. The printer driver
properties are established by left-clicking the desired printer and then
modifying the properties as desired. The orientation (portrait or landscape)
determines how the plot will be generated, and the size determines the plate
size of the drawing.

PLOTTER Keywords

BANDWIDTH - |S| - Specifies the
variable that is to be used to control the drawing of bandwidths along drawn
links. Usually, a temporary variable should be designated. The variable must be
scaled appropriately, or the plot will be unreadable.

- FILL - |S| - Specifies if the band
  is to be filled in or left empty. On raster plotters, this value should be
  specified as solid, but on pen plotters, solid could require excessive time for
  generating and actually drawing the plot. The possible values are: Solid and
  None. The default is None.
- TAPER - |I| - Specifies that the
  ends of the bands are to be tapered towards the nodes rather than being
  perpendicular to the link. In grid plots where Fill is not used, a taper of 45
  might be more presentable. Any integer value from 0 to 45 (degrees) may be
  specified.

DEVICE - |S| - Name of the printer
driver that is to be selected and written to. The name must match the name of
the printer as it appears in the Printers dialog box. Case is not essential. If
the name has spaces in it, the value must be enclosed within quotes so that the
spaces can be considered as part of the name. There must be a
DEVICE specified; otherwise the program will not
know anything about the printer.

FILE - |F| - Used if it is desired to
write the printer information to a file, rather than directly to the printer.
This is recommended for devices that are normally not connected directly to the
processing computer. If
FILE
is not specified, the output will be written directly to the
printer device. If
FILE
is specified, actual printing (or plotting) is performed by
copying the file directly to the port that is connected to the device.

FOOTER
- |S16| - Specifies lines of text that are to be printed at
the bottom of the plot page. There may be up to 16 footers. The program will
add one additional footer to identify the software and the licensee after the
user footers are printed. If none of the footers has specified a date, the date
and time will be added included in the identification line. Tokens may be
specified in the footers; when they are present the token is replaced by a
value. The tokens and their replacements are:

| Token | Replacement |
| --- | --- |
| [date] | MM/DD/YY |
| [idate] | MMM DD YYYY |
| [time] | HH.MM |
| [times] | HH.MM.SS |
| [window] | X=xxxxx-xxxxx Y=yyyyy-yyyyy |
| [scale] | Scale=xxxxx |

- ALIGN - Specifies how the footers
  should be aligned on the plot. The value can be: Left, Right, or Center.
  ALIGN
  must be placed after a
  FOOTER or
  FONT value; if more headers are to be specified
  after
  ALIGN, the FOOTER[]= must
  be specified.
- FONT - Specifies the font
  characteristics of the footers. There may be up to nine values following
  FONT, but currently, only the first three are
  used. The values are (position), name, size, color.

HEADER
- |S16| - Specifies lines of text that are to be printed at
the top of the plot page. There may be up to 16 headers. Since headers most
likely have special characters in them, it is recommended that each header be
enclosed within quote marks ("â¦"). The highest index for a header sets the
number of header lines that will be printed. Example: if only one header is
specified, say HEADER[6]="â¦", 6 lines will be printed, with the first 5 being
blank.

- ALIGN - |S| - Specifies how the
  headers should be aligned on the plot. The value can be: Left, Right, or
  Center.
  ALIGN must be placed after a
  HEADER or
  FONT value; if more headers are to be specified
  after
  ALIGN, the
  HEADER[]= must be specified.
- FONT
  - |S4| - Specifies the font characteristics of the headers.
  There may be up to nine values following FONT, but currently, only the first
  three are used. The values are (position), name, size, color.

LEGEND
- |S| - Specifies the position for additional user text is to
be printed on the plot page. There are four possible legend positions:

- TopLeft
- TopRight
- BottomLeft
- BottomRight

Note: The four positions can also be designated as TL, TR, BL,
and BR, or 1, 2, 3, and 4. See
[Examples and FAQ.](GUID-6B29A589-C26B-4AE9-BA0D-3CD02DFA925D.html)

The legends are placed within the plot window area, and
their areas are not written into by network drawing. The coding rules are
similar to those for HEADER and FOOTER, but you can also enter symbols on each
line. Legends are primarily for identifying the characteristics of the network
drawing. Each LEGEND may have its own font characteristics; they will be used
for the text for all lines in the legend. Each LINE can have its own symbol.

- FONT - |S9| - Specifies the font
  characteristics for the text in this legend. See
  HEADER
  [FONT](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__HFONT) for details.
- LINE - |S16| - Text to be printed
  at the specified line of the legend.
- SYMBOL - |S4| - Specifies the
  symbol that is to precede the LINE text. There should be four values specified
  for the symbol: name, size, color, and fill color.

Name - See DRAWA under PLOT for valid symbol names. If a
sample line style is to be drawn, see DRAWLINK under PLOT for valid names.

Size The size of the symbol, or the length of the line.

Color Standard color designation.

Fill Standard color designation if the symbol is to be
filled with a color.

LINKOFFSET - |R| - Specifies the
distance (in inches) that the links are to be drawn from the normal centerline.
This allows two-way links to be more visually presented. If this keyword is not
used, or the value is 0, the high-to-low node link will overwrite the low-to-
high link.

MAPSCALE - |R| - Specifies a scale
factor to be used to convert coordinate units to inches. The value is expressed
as coordinate units/inch. If the value is not specified, a scale factor will be
computed from known information. Note that when a factor is specified, the
MAPWINDOW will be used mainly to orient the center
of the plot.

MAPWINDOW
- |R4| - Specifies two opposite corners of the map window to
be selected. The map window is specified in map coordinate units. If no window
is specified, the program uses the minimum and maximum coordinates from the
network. The plot will be scaled to fit within the map window. The 4 required
values are specified as X1,Y1, X2,Y2. Any part of the network that exceeds the
limits of the window will not be drawn. If
MAPSCALE is not specified, the scale factor will
be calculated to fit the window within the page. The center of the map window
will be placed in the center of the plotting window.
MAPWINDOW will most likely not directly correlate
with the plotting window; the program may adjust one of the dimensions if it is
necessary.

MARGINS - |R4| - Specifies the
margins that surround the plot window on the printed page. If the selected
device is a printer that is selected with Letter size (8.5 x 11 inches), a
normal margins would be 0.25 inches. If it were desired to leave more space
around the plotted window (say 1 inch on the left and 1.5 inches on the right),
`MARGINS=0.75,1.25` would be used. To make the top margin
1.5 inches and the bottom margin 2 inches,
`MARGINS[3]=1.25, 1.75` would be used. You can do this
with one keyword:
`MARGINS = 0.75,1.25,1.25,1.75.`

By judicial use, the plot window can be placed anywhere on
the page that is desired.

PLATESIZE - |R2| - Specifies the
maximum plot plate (page) size. It should not be greater than the dimensions
specified in the device properties; if it is, the output might be cropped. This
keyword is used primarily to make a plate that is smaller than the basic
dimensions of the device. The plate will be oriented at the upper left corner
of the printed page. Nothing will be printed outside the rectangle defined by
this The MARGINS values can be used to position the printed window within the
plate. In general, this need not be specified; the MARGINS values can be used
to establish the dimensions of the plot window. Two values must be entered: the
width (x dimension), and the height (y dimension). They are expressed in
inches. PLATESIZE is not normally used.

POSTLINKVAR - |S4| - Specifies
the variables that are to be posted along links that are drawn and designated
for posting by a
PLOT LINKPOST
value. Up to four variables can be selected. The same
variables will be posted for all links; it is not possible to vary the
variables. It is not recommended that different variables be posted on
different links, but it is possible for the user to cause this to happen by
specifying variables that are modified as desired in the stack statements. The
number of desired decimal places for the posting of the variable can be
appended to the variable name in parentheses, for example,
`POSTLINKVAR=VC(3)` to post VC ratio with 3 decimal
places.

- FONT - |S4| - Specifies the font
  characteristics for link posting. The standard font designations are specified,
  but the color is ignored; the
  PLOT DRAWLINK statements set color.
- POST
  - |S| - Specifies how link post text is to be printed when
  it is too long for the link. The possible selections are:

Fit - Omit the text; it doesnât fit.

All - Print it, regardless if it overruns the link.

AutoSize - Decrease the font size until it fits, or is too
small.

AutoSize(ss) - Same as AutoSize, but the optional (ss)
indicates the minimum size to allow.

POSTNODEVAR - |S4| - Specifies
the variables that are to printed to the upper left of a node that is
designated for posting by a
PLOT NODEPOST value.

- FONT - |S4| - Specifies the font
  characteristics for node posting. The standard font designations are specified,
  but the color is ignored; the
  PLOT NODEPOST statements set color. The font
  size can be overwritten on a node-by-node basis.

Font specifications

You can control all text that is to be printed on the plot.
In general, you can specify the name of the font, the size, and the color. The
font name must be recognized (and available), or the printer driver will
substitute a font of its choosing. If no font is specified, the program will
supply the name "ARIAL." The size is always specified as absolute, in inches;
changing to a different size printer will not alter the size the text. If no
size is specified, the program will supply a value of 0.01. The color can be
specified in various ways: by a standard name, or a numeric value to index
color mix. Colors are processed in Windows by using a number that is a
combination of the three colors (red green and blue). You can create the
internal number by specifying an integer number (not too likely), a hexadecimal
value (very common process), or by a string of digits preceded by a color
indicator. Three bytes are used to store the intensity of each of the colors;
the values can range from 0 to 255. To use the mixing string, the string must
begin with one of the letters (RGB) followed by a number in the range of 0-255,
and more color strings, if desired. The order of the strings is irrelevant. To
enter the hexadecimal value, the string must begin with 0x and be followed by a
string of hexadecimal values (0-f ). The table below indicates the standard
colors and their various representations. If there is no color for the font, a
color will be chosen by the printer driver. For pen plotters, the driver will
translate the color number to a pen number. The pen color correlation is
determined by the properties of the driver. You may have to experiment to
obtain which pen is selected for each color used.

| Color | Decimal | HexValue | R#G#B# |
| --- | --- | --- | --- |
| black | 0 | 0x000000 | â |
| red | 255 | 0x0000ff | r255 |
| green | 49152 | 0x008000 | g128 |
| blue | 16711680 | 0xff0000 | b255 |
| yellow | 65535 | 0x00ffff | r255g255 |
| purple | 8388736 | 0x800080 | r128b128 |
| aqua | 16776960 | 0xffff00 | g255b255 |
| gray | 8421504 | 0x808080 | r128g128b128 |
| silver | 12632256 | 0xc0c0c0 | r192g192b192 |
| lime | 65280 | 0x00ff00 | g255 |
| white | 16777215 | 0xffffff | r255g255b255 |
| none | -1 | â | â |

Example

See
[Examples and FAQ](GUID-6B29A589-C26B-4AE9-BA0D-3CD02DFA925D.html)

![](GUID-1FF58007-A0C0-4FD3-97CC-CA3B0BCC6F00-low.png)

PRINT

Formats and prints a line of information. Please see PRINT
for more details.

Example

```
PRINT LIST=A(4),B(5),DISTANCE(6.2) ABCDE(6.3), FORM=LRCD,
  LIST=SPEED, TIME1 ;Note: this line is a continuation

LIST= N(5), X, Y
PRINT FORM=6.0CDLR LIST=A,B,DISTANCE, T0, SPDCLASS FILE=PRINTFIL.002
```

PROCESS â¦ ENDPROCESS

Specifies a
PROCESS and
ENDPROCESS block. Keywords and sub- keywords
include:

- [PHASE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__PHASE)

  - [FILEI(comp)](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__PHASEFILEI)

PROCESS Keywords

- PHASE - |KS| - Indicates the phase
  to which the statements which follow it are to be applied. The end of the phase
  block is established when an ENDPROCESS or another
  PROCESS statement is encountered. The value for
  PHASE must be either INPUT, NODEMERGE,
  LINKMERGE, or SUMMARY.
  - FILEI
    - |F| - Used only with
    `PHASE=INPUT`, and indicates that the block
    statements are to be applied only when the specified FILEI file is being
    processed. Normally, only DBF and ASCII files are processed in the INPUT phase,
    but if a FILEI with a different mode is specified, the file will be processed
    in the INPUT phase. The value must be NI.# or LI.#, to indicate a file from
    NODEI[#], or LINKI[#] that was previously specified on a FILEI statement.

Normally, a
PROCESS statement contains only the above keywords
and values, and the operations to be performed on the designated file during
the phase follow on additional control statements. The
ENDPROCESS
statement can alternatively be specified as
ENDPHASE; that is more consistent if the
PROCESS control is triggered by
PHASE=.

Bentley recommends using
PROCESS/ENDPROCESS blocks be used to contain all
operational (stack) statements. That way there is no confusion about what is
intended. If there is no specific
PHASE=LINKMERGE statement, any stack statements
that are not explicitly within a
PROCESS block, will be executed in the LINKMERGE
phase. Even if there are
PROCESS blocks surrounded by stack statements, all
the stack statements will be executed during the LINKMERGE phase. The program
will skip over the
PROCESS
block.

There are some rules about PROCESS
blocks:

- There may be only one
  `PHASE=NODEMERGE`
- There may be only one
  `PHASE=LINKMERGE`
- If there is a`PHASE=LINKMERGE` statement, there may not be stack statements that are
  not explicitly within a
  PROCESS block. In other words, once a LINKMERGE
  phase has been designated, all stack statements must be with an explicitly
  stated PHASE.

Example 1

```
; Re-code node numbers for LINKI[1] and NODEI[1] using a
; lookup function. The 2nd PROCESS statement also acts as
; an ENDPROCESS statement, but an ENDPROCESS is required
; after the 2nd PROCESS.

PHASE=INPUT FILEI=NI.1
    N = NODECODE(N);
PHASE=INPUT FILEI=LI.1;
    A = NODECODE(A), B = NODECODE(B)
ENDPROCESS
```

Example 2

```
PHASE=LINKMERGE
IF (LI.1.DIST != LI.2.DIST) LIST='Distances Differ for link:',
    LIST=A(5) B(6), FORM=6.2, LI.1.DIST, LI.2.DIST
ENDPHASE
```

REPORT

Defines report specifications. Keywords include:

[ALL](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__ALL)

[CAPACITY](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__CAPACITY)

[DEADLINKS](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__DEADLINKS)

[DUPLICATES](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__DUPLICATES)

[FILEI](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__REPORTFILEI)

[FILEO](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__REPORTFILEO)

[INPUT](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__INPUT)

[MERGE](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__REPORTMERGE)

[SPEED](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__SPEED_unique_1)

[UNCONNECTED](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__UNCONNECTED)

REPORT Keywords

ALL - |?| - Set all the
following reports to this value (not usually recommended). Default value is F.

CAPACITY - |?| -
Capacity tables. Default value is F.

DEADLINKS
- |?| - Links that are missing either an entry or exit link.
Such links cannot be used by any path processing. Additional file processing
may be required. Default value is F.

DUPLICATES - |?| -
Duplicate links that are detected during PHASE=INPUT. Default value is F.

FILEI - |?| -
Internal specifications for the input files (use for debugging only). Default
value is F.

FILEO
- |?| - Internal specifications for the allocation of output
variables use for debugging only). Default value is F.

INPUT
- |?| - Summary statistics following input phases. Default
value is F.

MERGE - |?| -
Summary statistics following every phase. Default value is T.

SPEED
- |?| - Speed tables. Default value is F.

UNCONNECTED - |?| -
List of zones that do not have links into and out of them. Default value is T.

All reports must be specified with a logical value of true
or false. The default value is true.

Example

```
REPORT FILEI=Y, FILEO=Y; normally not specified.
REPORT SPEED=Y, UNCONNECTED=N
REPORT ALL=true, fileo=false, filei=false
```

SORT

Sorts user-defined arrays. Keywords include:

ARRAY

NUMRECS

See
[SORT](GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531.html#GUID-0776F0F6-CB16-4D4F-8AC6-CFABFE50B531__SORT) for more information about this standard CUBE Voyager
statement.

Example

```
ARRAY  AN=LINKS, BN=LINKS, VMT=LINKS         ; NETI must be a binary network
PHASE=LINKMERGE
  _L = _L + 1
  AN[_L] = A
  BN[_L] = B
  VMT[_L] = V_1 * DISTANCE
ENDPHASE
/* note:
The User has to keep count of the records entered into the arrays If links are deleted, the number of entries will be less than the original number of links.
*/
PHASE=SUMMARY
  SORT ARRAY=-VMT, AN,BN, NUMRECS=_L
  LOOP _K=1,30 ; only want to see the highest 30
      LIST=AN[_K](6),BN[_K](6),VMT[_K](10.2c)
  ENDLOOP
ENDPHASE
```

SPDCAP

Revises speed and capacity tables. Keywords include:

[CAPACITY](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__SPDCAPCAPACITY)

[LANES](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__SPDCAPLANES)

[SPEED](GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E.html#GUID-57CABDC5-C6B1-4B85-8499-6F4A7D4CFE3E__SPDCAPSPEED)

SPDCAP Keywords

CAPACITY -
|RV\*99| - Capacity in vehicles per lane per hour. Actual link capacity is
obtained by multiplying the link capacity based upon its capacity
classification (CAPCLASS) value by the number of LANES.
All values must be 0-9999, inclusive. The capacity array is initialized to 20
times the index number, for all lane stratification:
`CAPACITY[1]=20, CAPACITY[2]=40...`.

LANES - |IV| - Lane
stratification that any following
CAPACITY and/or
SPEED values are to apply to.
LANES
may be interspersed with other keywords and values on the
statement. All values must be 1-9, inclusive.

SPEED - |RV\*99| -
Speed to be applied to the link. All values must be 0-3276.7, inclusive. The
speed array is initialized to the index number, for all lane stratification
(SPEED[1â¦99]=1,2,â¦99). Speed is maintained with one decimal place.

A network contains an array of capacity and speed data.
Each array is dimensioned with ninety-nine values for each of nine lane
stratification, and contains 891 values. When an array is accessed, the program
uses the number of lanes (LANES) as the row index, and
the capacity and/or speed classification (CAPCLASS,
SPDCLASS) as the column index to obtain a value for a link. If
CAPACITY or
SPEED is encountered prior to a
LANES keyword on the statement, LANES will be
preset to 1-9.
CAPACITY and
SPEED are entered as vector data, and may be
indexed to set a specific loading place, and may have null fields to skip the
revision of certain columns. The
SPEEDFOR and
CAPACITYFOR functions can be used to obtain values
for these tables.

Example

```
;Set entire table to 50,
; then revise the values for 20,21, and 24 for lanes 1,3,8
SPDCAP CAPACITY=99*50, LANES=1,3,8, CAPACITY[20]=300,400,,,700
SPDCAP LANES=2,4-9, SPEED=20.5,30.3,50.6,,,88.2, LANES=5,SPEED[15]=15
SPDCAP SPEED=30, LANES=2-8; Inappropriate; the LANES will not be used.
```

**Parent topic:**  [Network Program](GUID-7B7F2E2B-1D37-43F4-B390-965753B42391.html)

|
|  |
|
|  |
