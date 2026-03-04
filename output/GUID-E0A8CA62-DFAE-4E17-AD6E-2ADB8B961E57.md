# CUBE 7 Cluster Sample Scripts

Intrastep

This first example demonstrates a run on 3 hosts, including the local
host.

```
REPORT_SCRIPT_LOCATION LOCATION_ID='Starting script'

CLUSTER RUNID="Intrastep Test",
  SERVER="LOCALHOST" NUMNODES=2,
  SERVER="TESTHOST1" NUMNODES=2,
  SERVER="192.168.1.18" NUMNODES=2,
  WAIT=60, NOHIDE=T

REPORT_SCRIPT_LOCATION LOCATION_ID='Performing loop'

LOOP I=0,10,1

RUN PGM=MATRIX PRNFILE="MCMAT00N.PRN" STEP_ID='Matrix'
DISTRIBUTEINTRASTEP MAXPROCESSORS=6, MinGroupSize=20,SavePrn=T
FILEI MATI[1] = ".\inputs\TSKIM0TMP.MTX"
FILEO MATO[1] = ".\TSKIMAVG_R05.MTX",
  MO=1-2;,NAME=PeakSkim,OffpkSkim

PAR ZONEMSG=100

FILLMW MW[1]=MI.1.1,2

MW[1]=MW[1]+1
MW[2]=MW[2]+1

ENDRUN

ENDLOOP

REPORT_SCRIPT_LOCATION LOCATION_ID=âScript End'
```

Multistep

This example uses multi-step to concurrently run two highway steps.

```
CLUSTER RUNID="Multistep Test",
  SERVER=LOCALHOST" NUMNODES=6,
  WAIT=60,NOHIDE=T

DistributeMULTISTEP ALIAS='MULTI_1'

RUN PGM=HIGHWAY PRNFILE="Model\SCHWY01A.PRN" MSG='Highway Assignment for Peak Period'
FILEI NETI = "Input_Data\HIGHWAY_0001.NET"
FILEI MATI[1] = "Input_Data\PKHOURTRIPS.MAT"
FILEI MATI[2] = "Input_Data\FORECASTEDTRUCK.MAT"
FILEO NETO = "Base\LOADED_PEAK.NET"

   ;--- set convergence method and criteria
   PARAMETERS COMBINE=EQUI, ENHANCE=0
   PARAMETERS RELATIVEGAP=0.00001 GAP=0.00001, MAXITERS=5

   DistributeIntraStep MaxProcessors=2 

   ZONESMSG=1
   ;--- set capacity and group links
   PROCESS PHASE=LINKREAD
      C = LI.CAP
      LINKCLASS = LI.FUNC_CLASS
      IF (LI.FUNC_CLASS == 1,1.5) LINKCLASS=1  ; Freeways, tollways & HOV
      IF (LI.FUNC_CLASS == 2-3)   LINKCLASS=2  ; Ramps & expressways
      IF (LI.FUNC_CLASS == 4-5)   LINKCLASS=3  ; Arterial streets
      IF (LI.FUNC_CLASS == 6)     LINKCLASS=4  ; Local / collector
      IF (LI.FUNC_CLASS == 9-10)  LINKCLASS=10 ; Connectors /dummy
      IF (LI.NAME='HOV') ADDTOGROUP=1
      IF (LI.NAME='RAILACCESS') ADDTOGROUP=9
   ENDPROCESS

   PROCESS PHASE=ILOOP
       MW[1]=MI.1.1
       MW[2]=MI.1.2
       MW[3]=MI.2.1
   	; SOV, EI/EE, TRUCK ASSIGNMENT
       PATHLOAD PATH = COST, VOL[1]=MW[1], vol[3]=MW[3], EXCLUDEGROUP=1,9
       ; HOV
       PATHLOAD PATH = COST, VOL[2]=MW[2], EXCLUDEGROUP=9 ASSIGNMENT
  ENDPROCESS

   PROCESS PHASE=ADJUST
    function {
       V=VOL[1]+VOL[2]+VOL[3]
       TC[1] = T0 *(1+0.18*(V/C)^8.5) ; Freeways, tollways & HOV
       TC[2] = T0 *(1+1.00*(V/C)^5.0) ; Ramps & expressways
       TC[3] = T0 *(1+0.70*(V/C)^5.0) ; Arterial streets
       TC[4] = T0 *(1+1.40*(V/C)^5.0) ; Local / collector
       TC[10]= T0                     ; centroid connectors
       COST=TIME+60*li.toll/5.25      ; cost function
       }
   ENDPROCESS                                                     
ENDRUN

EndDistributeMULTISTEP
DistributeMULTISTEP ALIAS='MULTI_2'

RUN PGM=HIGHWAY PRNFILE="MODEL\SCHWY01B.PRN" MSG='Highway Assignment for Off-Peak Period'
FILEI NETI = "Input_Data\HIGHWAY_0001.NET"
FILEI MATI[1] = "Input_Data\PKHOURTRIPS.MAT"
FILEI MATI[2] = "Input_Data\FORECASTEDTRUCK.MAT"
FILEO NETO = "Base\LOADED_OFFPEAK.NET"

   ;--- set convergence method and criteria
   PARAMETERS COMBINE=EQUI, ENHANCE=0
   PARAMETERS RELATIVEGAP=0.00001 GAP=0.00001, MAXITERS=5

   DistributeIntraStep MaxProcessors=2 

   ZONESMSG=1
   ;--- set capacity and group links
   PROCESS PHASE=LINKREAD
      C = LI.CAP*5
      LINKCLASS = LI.FUNC_CLASS
      IF (LI.FUNC_CLASS == 1,1.5) LINKCLASS=1  ; Freeways, tollways & HOV
      IF (LI.FUNC_CLASS == 2-3)   LINKCLASS=2  ; Ramps & expressways
      IF (LI.FUNC_CLASS == 4-5)   LINKCLASS=3  ; Arterial streets
      IF (LI.FUNC_CLASS == 6)     LINKCLASS=4  ; Local / collector
      IF (LI.FUNC_CLASS == 9-10)  LINKCLASS=10 ; Connectors /dummy
      IF (LI.NAME='HOV') ADDTOGROUP=1
      IF (LI.NAME='RAILACCESS') ADDTOGROUP=9
   ENDPROCESS

   PROCESS PHASE=ILOOP
       MW[1]=MI.1.1*5
       MW[2]=MI.1.2*5
       MW[3]=MI.2.1*5
   	; SOV, EI/EE, TRUCK ASSIGNMENT
       PATHLOAD PATH = COST, VOL[1]=MW[1], vol[3]=MW[3],  EXCLUDEGROUP=1,9
       ; HOV
       PATHLOAD PATH = COST, VOL[2]=MW[2], EXCLUDEGROUP=9 ASSIGNMENT
   ENDPROCESS

   PROCESS PHASE=ADJUST
    function {
       V=VOL[1]+VOL[2]+VOL[3]
       TC[1] = T0 *(1+0.18*(V/C)^8.5) ; Freeways, tollways & HOV
       TC[2] = T0 *(1+1.00*(V/C)^5.0) ; Ramps & expressways
       TC[3] = T0 *(1+0.70*(V/C)^5.0) ; Arterial streets
       TC[4] = T0 *(1+1.40*(V/C)^5.0) ; Local / collector
       TC[10]= T0                     ; centroid connectors
       COST=TIME+60*li.toll/5.25      ; cost function
       }
   ENDPROCESS                                                     
ENDRUN

EndDistributeMULTISTEP
BARRIER IDLIST='MULTI_1','MULTI_2', CheckReturnCode=T, PrintFiles=Merge

```

**Parent topic:**  [CUBE 7 Cluster](GUID-FD716A57-7ABC-4A28-AD21-864024D61908.html)

|
|  |
|
|  |
