# Phases

The Public Transport program executes its main
processesâdata processing and modelingâwithin a series of phases. You control
all the phases and can initiate additional, context-sensitive computations
within them. The phases, presented in the order they would normally be
implemented, are:

- [NODEREAD](GUID-99C2FBB8-963E-4D2D-A21C-FF9CBE4B335D.html#GUID-99C2FBB8-963E-4D2D-A21C-FF9CBE4B335D__NODEREAD) â Computes node based variables.
- [LINKREAD](GUID-99C2FBB8-963E-4D2D-A21C-FF9CBE4B335D.html#GUID-99C2FBB8-963E-4D2D-A21C-FF9CBE4B335D__LINKREAD_unique_2) â Computes link based variables.
- [DATAPREP](GUID-99C2FBB8-963E-4D2D-A21C-FF9CBE4B335D.html#GUID-99C2FBB8-963E-4D2D-A21C-FF9CBE4B335D__DATAPREP) â Prepares the public transport network for
  modeling.
- [MATI](GUID-99C2FBB8-963E-4D2D-A21C-FF9CBE4B335D.html#GUID-99C2FBB8-963E-4D2D-A21C-FF9CBE4B335D__MATI_unique_2) â Computes trips for loading.
- [SELECTIJ](GUID-99C2FBB8-963E-4D2D-A21C-FF9CBE4B335D.html#GUID-99C2FBB8-963E-4D2D-A21C-FF9CBE4B335D__SELECTIJ)
- [SKIMIJ](GUID-99C2FBB8-963E-4D2D-A21C-FF9CBE4B335D.html#GUID-99C2FBB8-963E-4D2D-A21C-FF9CBE4B335D__SKIMIJ) â Extracts skims and select link results, saving
  them, generally in working matrices.
- [MATO](GUID-99C2FBB8-963E-4D2D-A21C-FF9CBE4B335D.html#GUID-99C2FBB8-963E-4D2D-A21C-FF9CBE4B335D__MATO_unique_2) â Manipulates and reports skim, select-link, and
  loading-analyses matrices.

The NODEREAD, LINKREAD, MATI, and MATO phases provide data
manipulation facilities, and are secondary to the main functions of the Public
Transport program. They are optional.

You specify the exact configuration for the Public
Transport program to run through a combination of phases and control
statements.

Control statements provide information and instructions to
the program. In the Public Transport program, control statements are either
static or dynamic. Static statements may be present anywhere in the job stream;
the program evaluates them once. Dynamic statements may be present only within
phases; the program evaluates them as encountered, during the execution of the
phases.

Only context-sensitive dynamic control statements are
available to the phases; a list of valid statements is provided with the
description of each phase. See
[Control Statements](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A) for more information. You only must code
phases that contain control statements; you need not code empty or null phases.
Specify phases in a script as follows:

```
PHASE=DATAPREP
  ;Generate access/egress legs
  GENERATE
  ...
  ...
  ;End of GENERATE
ENDPHASE
```

Regardless of the functionality selected for any run of the
Public Transport program, a requirement is that a network, basic or public
transport, is always input. This is read and set up at the start of each run;
no user intervention is required.

A diagram showing how the phases would be used in a typical
public transport model follows:

![](GUID-6528A8D6-DC74-4653-9139-FA9B5A90942B-low.png)

NODEREAD

In the NODEREAD phase, you can compute node-based
information from the input networkâs node attributes with NETI. This
information is for use primarily in the DATAPREP phase but is available in
later phases if the DATAPREP phase is active.

The control statements within the NODEREAD phase are
executed once per node. Only one NODEREAD phase is permitted per run.

The computed variables may be scalars or vectored by node.
The use of a vectored variable produces an array containing a computed value
for each node. Vectored variables have the case insensitive prefix "nw".

The evaluated expression may contain any valid variables,
numeric or string, and node based variables from the input network. Input node
variable names must have the case insensitive prefix "ni".

An example of a computed node variable is:

```
NW.XplusY = NI.X+NI.Y
```

Computed variables are available for the duration of the
run but not saved back to the network.

See Example 2: Preparing a public transport network from
TRIPS link data for an example of this phase.

Control statements available in this
phase

- [ABORT](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__ABORT_unique_3)
- [BREAK](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__BREAK_unique_4)
- [COMP](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__COMP_unique_6)
- [CONTINUE](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__CONTINUE_unique_4)
- [EXIT](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__EXIT_unique_4)
- [GOTO](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__GOTO_unique_3)
- [IFâ¦ ELSEIF â¦ ELSE â¦ ENDIF](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__ELSEIF_unique_4)
- [LOOP â¦ ENDLOOP](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__ENDLOOP_unique_3)
- [PRINT](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__PRINT_unique_6)

Public Transport variables available in this
phase

- ZONES

LINKREAD

In the LINKREAD phase, you can compute link-based
information from the input networkâs link attributes with NETI. This
information is for use primarily in the DATAPREP phase but is available in
later phases if the DATAPREP phase is active.

The control statements within the LINKREAD phase are
executed once per link. Only one LINKREAD phase is permitted per run.

The computed variables may be scalars or vectored by link.
The use of a vectored variable produces an array containing a computed value
for each link. Vectored variables have the case insensitive prefix "lw".

The evaluated expression may contain any valid variables,
numeric or string, and node based variables from the input network. Input link
variable names must have the case insensitive prefix "li".

An example of a computed link variable is:

```
LW.GCTime=LI.Time*1.5
```

Computed variables are available for the duration of the run
but not saved back to the network.

See Example 2: Preparing a public transport network from
TRIPS link data for an example of this phase.

Control statements available in this
phase

- [ABORT](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__ABORT_unique_3)
- [BREAK](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__BREAK_unique_4)
- [COMP](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__COMP_unique_6)
- [CONTINUE](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__CONTINUE_unique_4)
- [EXIT](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__EXIT_unique_4)
- [GOTO](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__GOTO_unique_3)
- [IFâ¦ ELSEIF â¦ ELSE â¦ ENDIF](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__ELSEIF_unique_4)
- [LOOP â¦ ENDLOOP](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__ENDLOOP_unique_3)
- [PRINT](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__PRINT_unique_6)

Public Transport variables available in this
phase

- ZONES
- LINKNO

DATAPREP

The DATAPREP phase invokes the Public Transport network
development process and provides the mechanism for generating and/or reading
nontransit legs.

You can develop nontransit legs with one or more
[GENERATE](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__GENERATE) control statements, or you can produce them
externally to the Public Transport program and input them in this phase.

You can compute data for nontransit leg generation from the
input network with the
[COMP](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__COMP_unique_6) statement.

See
[Public transport network development](GUID-00336599-ED4B-4F9B-A2FF-C8B5BB751F53.html#GUID-00336599-ED4B-4F9B-A2FF-C8B5BB751F53__PUBLICTRANSPORTNETWORKDEV) for examples of this
phase.

Control statements available in this
phase

- [ABORT](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__ABORT_unique_3)
- [BREAK](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__BREAK_unique_4)
- [COMP](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__COMP_unique_6)
- [CONTINUE](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__CONTINUE_unique_4)
- [EXIT](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__EXIT_unique_4)
- [GENERATE](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__GENERATE)
- [GOTO](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__GOTO_unique_3)
- [IFâ¦ ELSEIF â¦ ELSE â¦ ENDIF](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__ELSEIF_unique_4)
- [LINKLOOP â¦ ENDLINKLOOP](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__LINKLOOP_unique_1)
- [LOOP â¦ ENDLOOP](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__ENDLOOP_unique_3)
- [PRINT](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__PRINT_unique_6)

Public Transport variables available in this
phase

- ZONES

MATI

The MATI phase produces working matrices, (MW[#]), from
FILEI[MATI](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__MATI_unique_3) matrices (MI.#.name), although
[COMP](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__COMP_unique_6) statements can also compute working matrices.

The MATI phase is executed for each origin zone, I, before
the route evaluation, skimming, loading, and loading analyses processes are
done for each zone pair, I-J.

This phase provides a flexible mechanism for generating and
manipulating one row of a matrix at a time. You might use this phase to:

- Examine the matrix input with
  FILEI [MATI](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__MATI_unique_3), one row at a time, and determine if there is anything
  specific about zone I that could affect further processing for that zone. For
  example, if
  MATI points to a highway network matrix, and
  the matrix indicates that there is no highway access for zone I, you might set
  a variable for zone I and test in the SELECTIJ phase.
- Compute a row of trips, from an origin zone (I) to all
  zones (J), using the
  [COMP](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__COMP_unique_6) statement and the built-in ROW functions, and save the
  trips in a working matrix, MW[#], for subsequent loading. You can also do this
  in the SELECTIJ phase, but for a zone pair at a time. The working matrix is
  designated for loading with
  PARAMETERS [TRIPSIJ](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__TRIPSIJ)[userclass].
- Input matrices external to the Public Transport program
  with
  FILEI [MATI](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__MATI_unique_3), and then manipulate, report, and save those matrices
  with
  FILEI [MATO](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__MATO_unique_3). You can merge highway skims with skims extracted in
  the Public Transport program run.

The working matrix may be reported with the PRINTROW
statement. With the BREAK statement, you can use the MATI phase to select zones
for processing.

See
[Public transport loading](GUID-00336599-ED4B-4F9B-A2FF-C8B5BB751F53.html#GUID-00336599-ED4B-4F9B-A2FF-C8B5BB751F53__PUBLICTRANSPORTLOADING) for an example of this phase.

Control statements available in this
phase

- [ABORT](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__ABORT_unique_3)
- [BREAK](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__BREAK_unique_4)
- [COMP](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__COMP_unique_6)
- [CONTINUE](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__CONTINUE_unique_4)
- [EXIT](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__EXIT_unique_4)
- [GOTO](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__GOTO_unique_3)
- [IFâ¦ ELSEIF â¦ ELSE â¦ ENDIF](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__ELSEIF_unique_4)
- [JLOOP â¦ ENDJLOOP](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__JLOOP_unique_1)
- [LOOP â¦ ENDLOOP](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__ENDLOOP_unique_3)
- [PRINT](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__PRINT_unique_6)
- [PRINTROW](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__PRINTROW_unique_3)

Public Transport variables available in this
phase

- ZONES
- USERCLASS
- I
- J

SELECTIJ

The SELECTIJ phase selects pairs of zones, I-J, for
bypassing the route-evaluation process.

The
 [ROUTEI](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__ROUTEI) and
 [ROUTEO](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__ROUTEO) subkeywords I, J, and
SELECTBYMAT provide the first line of selection
but they do not control specific I-J combinations. The SELECTIJ phase allows a
finer selection of specific I-J combinations, although if the I-J combination
is precluded by the values on the
ROUTEI and
ROUTEO, that I-J pair is not available to this
phase.

The Public Transport program executes the SELECTIJ phase
prior to the route-evaluation process for the I-J pair. (Route evaluation is a
time consuming process, therefore judicious use of this phase can have a
significant impact on overall processing time.)

Only zone pairs for evaluated routes are available for the
skimming, loading, and loading analyses processes.

This phase can compute the trips to be loaded for each I-J
pair. For example:

```
PHASE=SELECTIJ
  if(I < 10) CONTINUE
  if(J > 10) BREAK
  TRIPSIJ=MI.1.1 * 0.75
  PRINT LIST=I,J,TRIPSIJ
ENDPHASE
```

In this fragment of code, the I-J pairs loaded range from
I=10-ZONES to J=1-9. The trips to be loaded are computed from the input trip
matrix and reported.

Control statements available in this
phase

- [ABORT](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__ABORT_unique_3)
- [BREAK](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__BREAK_unique_4)
- [COMP](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__COMP_unique_6)
- [CONTINUE](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__CONTINUE_unique_4)
- [EXIT](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__EXIT_unique_4)
- [GOTO](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__GOTO_unique_3)
- [IFâ¦ ELSEIF â¦ ELSE â¦ ENDIF](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__ELSEIF_unique_4)
- [PRINT](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__PRINT_unique_6)
- [PRINTROW](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__PRINTROW_unique_3)

Public Transport variables available in this
phase

- ZONES
- USERCLASS
- I
- J

SKIMIJ

The SKIMIJ phase extracts skims and select-link outputs with
special functions described in "Select-link functions", then saves them,
generally in working matrices with the
COMP MW[#] statement.

The Public Transport program invokes SKIMIJ for each zone
pair, I-J, immediately after route evaluation.

See
[Public transport skimming](GUID-00336599-ED4B-4F9B-A2FF-C8B5BB751F53.html#GUID-00336599-ED4B-4F9B-A2FF-C8B5BB751F53__PUBLICTRANSPORTSKIMMING) for an example of this phase.

MATO

In the MATO phase, the Public Transport program revises,
combines, reports and writes work matrices to the FILEO MATO files.

The program executes this phase once for each origin zone,
I, after completing the route evaluation, skimming, loading, and loading
analyses processes for all destination zones of that origin zone.

Generally, you use the MATO phase with the matrices
produced by the skimming and loading analyses phases, but you can also process
other working matrices similarly.

You can manipulate matrices with the COMP statement and a
set of built-in ROW functions, and create a report with the PRINTROW statement.
With the BREAK statement, you can use the MATO phase to select zones for
processing.

See
[Public transport skimming](GUID-00336599-ED4B-4F9B-A2FF-C8B5BB751F53.html#GUID-00336599-ED4B-4F9B-A2FF-C8B5BB751F53__PUBLICTRANSPORTSKIMMING) for an example of this phase.

Control statements available in this
phase

- [ABORT](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__ABORT_unique_3)
- [BREAK](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__BREAK_unique_4)
- [COMP](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__COMP_unique_6)
- [CONTINUE](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__CONTINUE_unique_4)
- [EXIT](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__EXIT_unique_4)
- [GOTO](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__GOTO_unique_3)
- [IFâ¦ ELSEIF â¦ ELSE â¦ ENDIF](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__ELSEIF_unique_4)
- [JLOOP â¦ ENDJLOOP](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__JLOOP_unique_1)
- [LOOP â¦ ENDLOOP](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__ENDLOOP_unique_3)
- [PRINT](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__PRINT_unique_6)
- [PRINTROW](GUID-E3125DB1-766F-47E3-A219-78C544D2988A.html#GUID-E3125DB1-766F-47E3-A219-78C544D2988A__PRINTROW_unique_3)

Public Transport variables available in this
phase

- ZONES
- USERCLASS
- I
- J

**Parent topic:**  [Public Transport](GUID-A90E32B1-BFB1-40F1-A921-7BC202F0A562.html)

|
|  |
|
|  |
