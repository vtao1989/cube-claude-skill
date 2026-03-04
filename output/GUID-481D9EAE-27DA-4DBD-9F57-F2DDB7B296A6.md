# Signal-controlled intersections

This section describes signal controls. Topics include:

- [Overview of signals](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__OVERVIEW)
- [Generic keywords](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__GENERICKEYWORDS)
- [Geometric keywords](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__GEOMETRICKEYWORDS)
- [Geometric signals example](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__GEOMETRICSIGNALS)
- [Saturation flow signals example](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__SATURATIONFLOWSIGNALS)

Overview of signals

Signalized intersections are controlled by sets of traffic
lights. At any given time, vehicles making a particular movement through the
intersection will see a particular signal aspect:

- In the U.K., red, green, amber, red amber, flashing
  amber.
- In the U.S., green, yellow, red, green.

Modelers reclassify the aspect into effective green (when
the traffic can go) and effective red (when the traffic stops). Note that
effective green begins and ends later than actual green (due to reaction
times).

A set of signal aspects for all movements through an
intersection is called a phase. Note that the total duration of all the phases
should be significantly less than the duration of the signal cycle. The
difference is primarily due to two factors: lost time while the signals are
changing phase and pedestrian phases.

CUBE Voyager offers two ways of modeling the capacity of
signals. There is a detailed model of junction geometry, which has been
calibrated to traffic conditions in the U.S.(Geometric / HCM model), and there
is a model which requires saturation flows to be estimated or measured
externally, which has been calibrated to traffic conditions in the
U.K.(Saturation Flow model). The detailed model also imposes more constraints
on the allowed signal phasing than the saturation flow only model.

CUBE Voyager offers four signal intersection types, i.e.
signal saturation flows, signal geometric (HCM), adaptive signal saturation
flows, and adaptive signal geometric (HCM).

- Signal, Saturation Flows model:
  It is developed to model capacities, queues, delays and LOS at fixed time
  signal controlled isolated intersections. The user inputs include geometric
  characteristics of the intersection, signal timing arrangements, and demand
  flow information. The methodology is based on the Catlingâs delay method and
  the TRRL (Transport and Road Research Laboratory, UK) Report 105.
- Signal, Geometric (HCM) model: It
  addresses the capacities, queues, delays and LOS for lane groups and the LOS
  for intersection approaches and the intersection as a whole at signalized
  intersections. Each lane group is analyzed separately in the HCM model. It
  considers a wide variety of prevailing conditions, including the amount and
  distribution of traffic movements, traffic composition, geometric
  characteristics, and details of intersection signalization. The methodology is
  based on the HCM 2000 signal model.
- Adaptive Signal, Saturation Flows
  model: It is an advanced model based on the Signal, Saturation
  Flows model. The model optimizes the signal timing based on the intersection
  geometric characteristics, signal parameter bounders and demand flow
  information. The methodology tries to iteratively fit delay parabolas based on
  three distinct and reasonable signal timing plans, i.e. phase timings and cycle
  time, and picks the plan at the minimum delay point, until no delay reduction
  could be reached. The delay is calculated by the Catlingâs delay method. The
  methodology was inspired by the TRANSYT model.
- Adaptive Signal, Geometric (HCM)
  model: The model is similar as the Adaptive Signal, Saturation
  Flows model, except the delay is calculated by the HCM 2000 method.

The above intersection types output not only delay,
capacity, queue and LOS, but also low flow delay. The low flow delay is a
measure commonly used by European users. It is the additional travel time
experienced by drivers of each movement at low degree of saturation (flow to
capacity ratio << 1). According to Catlingâs delay method, the delay at
low degree of saturation is almost equal to that occurring when the traffic
intensity is uniform. The low flow delay is calculated as the inverse of the
capacity for Saturation Flows models, and is calculated as the half cycle time
times the square of the red time proportion for Geometric (HCM) models.

A left turn (right turn when
LEFTDRIVE=T) which sees a green phase will either
be protected (that is, no opposing flow is running) or permitted (that is, the
vehicles must give way to some oncoming traffic). Both methodologies can model
both permitted and protected phases.

CUBE Voyager does not offer any model of "right turn on
red" although this is allowed in many areas of the U.S. (The
LEFTDRIVE=T equivalent, "left turn on red", is not
permitted in the U.K.) This is best handled by introducing a dummy link into
the network, allowing the right-turners to bypass the signal control, and
omitting some lane(s) from the definition of the approach.

References

- Catling, I. (1977). A time-dependent approach to
  junction delays.
  Traffic Engineering and Control,
  18(11), pp. 520-523, 526.
- Kimber, R. M., Mcdonald, M., Hounsell, N. B. (1986).
  The prediction of saturation flows for single
  road junctions controlled by traffic signals. Transport and Road
  Research Laboratory Report RR 67.
- Burrow, I. J. (1987).
  OSCADY: a computer program to model capacities,
  queues and delays at isolated traffic signal junctions. Transport and
  Road Research Laboratory Report RR 105.
- Kimber, R.M. and M.C. Semmens (1983).
  Traffic signal junctions: a track appraisal of
  conventional and novel design. Transport and Road Research Laboratory
  Report RL 1063.
- Transport Research Laboratory. TRANSYT.
  [http://www.trl.co.uk/Transyt.htm](HTTP://WWW.TRL.CO.UK/TRANSYT.HTM)
- Transportation Research Board. Highway Capacity Manual
  2000.

Generic keywords

This section describes generic keywords used for signals:

- [CANSHARELEFT](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__CANSHARELEFT)
- [CANSHARERIGHT](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__CANSHARERIGHT)
- [CYCLETIME](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__CYCLETIME)
- [EXCLUSIVELANES](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__EXCLUSIVELANES)
- [LANEADJUST](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__LANEADJUST)
- [PHASE and ACTUALGREEN](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__PHASEACTUALGREEN)
- [PHASES](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__PHASES)
- [SATFLOWPERLANE](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__SATFLOWPERLANE)
- [SINGLELANE](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__SINGLELANE)

Note: These keywords are case insensitive. For example,
capitalizing as
CanShareLeft might improve readability.

CANSHARELEFT

This keyword specifies that there is a shared lane to the
left of the exclusive lanes for this movement (that is, the movement can share
with the movement to its left). Note that this keyword does not mean "can share
with left turners" unless either the movement is
THROUGH or the movement is on the minor leg of a
three-arm junction.

If a movement has
CANSHARELEFT = T coded, then there must be a
movement to this movementâs left and the movement to this movementâs left must
have
CANSHARERIGHT
= T coded.

If
SINGLELANE = T then
CANSHARELEFT should not be coded.

CANSHARERIGHT

This keyword specifies that there is a shared lane to the
right of the exclusive lanes for this movement (that is, the movement can share
with the movement to its right). Note that this keyword does not mean "can
share with right turners" unless either the movement is
THROUGH or the movement is on the minor leg of a
three-arm junction.

If a movement has
CANSHARERIGHT = T coded, then there must be a
movement to this movementâs right, and the movement to this movementâs right
must have
CANSHARELEFT = T coded.

If
SINGLELANE = T then
CANSHARERIGHT
should not be coded.

CYCLETIME

This real-valued keyword is required for all signals. Its
value is the length of the signal cycle in seconds.

The cycle time must be strictly greater than the sum of all
the coded green times.

At actuated signals, the
CYCLETIME value is taken to be part of the example
feasible solution and the subkeywords
MAXIMUM
and
MINIMUM
may be used to supply constraints. For example:

Actual Cycle = 120, Minimum = 60, Maximimum=180,

If no constraints are placed on the cycle time at an
adaptively modeled signal, the constraints will be deduced from the constraints
on the individual green times.

EXCLUSIVELANES

This integer-valued keyword gives the number of lanes, on
the specified approach, which are reserved for the exclusive use of vehicles
making the specified movement.

If
SINGLELANE = T, then
EXCLUSIVELANES should not be coded.

LANEADJUST

Set
LANEADJUST to Y at a signal to invoke the HCM2000
capacity calculations.

Set
LANEADJUST to N at a signal if you are supplying
saturation flows.

PHASE and
ACTUALGREEN

These keywords occur in pairs; every occurrence of the
integer- valued keyword,
PHASE must be followed by a single occurrence of
the real-valued keyword
ACTUALGREEN. There should be one such pair for
each phase of the signals during which vehicles move (that is, all-red and/or
pedestrian phases should not be coded).

The values of the
PHASE keyword should form a continuous sequence,
starting at one and increasing, without gaps, until the number of phases is
reached. Every phase must be mentioned in a
PHASE keyword for some movement at the
intersection.

The value of the
ACTUALGREEN keyword is the duration, in seconds,
of the effective green-time associated with the phase. The effective green time
is the period during which vehicles move across the stop line. It starts
shortly after the signals change to green (because the vehicle drivers must
react to the change in signal aspect) and continues through the following
red/yellow. The
CYCLETIME must greater than the summation of the
ACTUALGREEN.

If the signal is being modeled adaptively, then the
keywords maximum (required) and minimum (optional) may be used to specify
constraints, and the coded value of ACTUALGREEN is taken to be part of the
example feasible solution. If no minimum is applied, CUBE Voyager may remove
the phase altogether (that is, set green-time to zero).

PHASES

The keyword
PHASES is integer-valued but, conceptually, it
consist of either one phase number (that is, digit) or of two phase numbers
(that is, two digits). The vehicles making the movement see a green signal
aspect when the specified phase(s) is/are running and red otherwise.

Note that the (node-level) keyword
PHASE is used to define phases and the
(movement-level) keyword
PHASES associates movements with the defined
phases.

At geometrically specified signals, then any two-digit
phase specifications must specify contiguous phases. No such restriction is
required when saturation flows are coded.

SATFLOWPERLANE

This real-valued keyword allows the specification of
saturation flows in pcu (vehicles) per hour per lane.

Saturation flows at signals are the flows that would be
observed if the movement had a continuous green all other movements had no flow
and no green.

Saturation flow at a priority junction (two-way
yield-controlled intersection) is defined similarly, except that no signal
aspects are involved.
SATFLOWPERLANE is only applicable to Saturation
flow model. The suggested value is 1700 pcu/h for THROUGH and UNOPPOSED
movements and 1279 pcu/h for OPPOSED movements.

SINGLELANE

The logical-valued keyword is used to indicate that an
approach consists of a single lane. It is applicable to many junction types:

- Signal-controlled intersection:

  - Geometric Data -
    SINGLELANE may be coded.
  - Saturation Flows -
    SINGLELANE may be coded.
- All-way stop-controlled intersection:
  SINGLELANE
  may not be coded; code
  NUMBEROFLANES = 1.
- Two-way stop-controlled intersection:

  - SINGLELANE
    may not be coded; code
    NUMBEROFLANES = 1.
  - Use
    FOURLANEMAJOR to describe major road.
- Priority intersection (two-way yield- controlled
  intersection):

  - Geometric Data
    - SINGLELANE may be coded for minor arms. Major road
    width in meters, not lanes.
- Roundabout:

  - Saturation Flows
    -
    SINGLELANE
    may be coded.
  - Empirical -
    SINGLELANE may not be coded.
  - Gap Acceptance -
    SINGLELANE may not be coded.

Coding
`SINGLELANE=Y` for an approach precludes the use of
EXCLUSIVELANES, CANSHARERIGHT, or
CANSHARELEFT on that approach.

At two-way stop-controlled intersections and priority
junctions, a minor arm that does not have
`SINGLELANE=Y` explicitly coded, has two lanes.

Geometric
keywords

This section describes geometric keywords:

- [AVERAGELANEWIDTH](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__AVERAGELANEWIDTH)
- [CONFLICTINGBIKE](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__CONFLICTINGBIKE)
- [BUSBLOCKAGE](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__BUSBLOCKAGE)
- [CENTRALBUSINESSDISTRICT](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__CENTRALBUSINESSDISTRICT)
- [DELAYEQUATION](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__DELAYEQUATION)
- [EXITLANES](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__EXITLANES)
- [FREEENTRYLENGTH](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__FREEENTRYLENGTH)
- [FREETURNEXITLENGTH](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__FREETURNEXITLENGTH)
- [FREETURNFOLLOWUP](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__FREETURNFOLLOWUP)
- [FREETURNGAP](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__FREETURNGAP)
- [GRADE](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__GRADE)
- [NODEFACTOUNOPPOSE](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__NODEFACTOUNOPPOSE)
- [NODEFACTOOPPOSE](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__NODEFACTOOPPOSE)
- [PARKINGMANEUVERS](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__PARKINGMANEUVERS)
- [PEDESTRIANFLOW](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__PEDESTRIANFLOW)
- [PEDESTRIANPHASE](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__PEDESTRIANPHASE)
- [PHASES](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__GKPHASES)
- [UNITEXTENSION](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__UNITEXTENSION)
- [VEHICLELENGTH](GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6.html#GUID-481D9EAE-27DA-4DBD-9F57-F2DDB7B296A6__VEHICLELENGTH)

Note: Keywords are case insensitive. For example, capitalizing
as
AverageLaneWidth might improve readability.

AVERAGELANEWIDTH

This real-valued keyword describes the mean lane width, in
meters or feet, of an approach to a geometrically modeled signalized junction.
If no value is provided, a default of 3.6m is used.

The average lane width must be in the range from 2.4m to
4.8m. If the value falls outside this range, the approach should be recoded to
have more or fewer lanes, as appropriate.

CONFLICTINGBIKE

The flow of bicycles in from the curb-side lane in units of
bicycles per hour. Bicycle traffic which weaves with turning traffic in advance
of the stop line should be excluded from this value, because these bicycles do
not interact with the other vehicles while they are still within the
intersection.

The diagram below illustrates the relevant bicycle flow for
right hand rule of the road. In the diagram, the crossed box is the bicycle
conflict zone where right turning traffic may be impeded by any bicycles
crossing the intersection. The
CONFLICTINGBIKE is the flow of bicycles through
this region.

![](GUID-DBA50A98-D85B-436D-BDB3-408928DAD0E4-low.png)

BUSBLOCKAGE

The real values supplied to this keyword are number of buses
stopping per hour. The first element refers to the normal curb side of the
road; the second refers to the other side of the road (for example, if there is
a tram line in the center of the road or there is a bus stop on the offside of
a one-way street). Only buses stopping within 75 meters (246 feet) of the stop
line (either upstream or downstream) should be included.

This keyword is only applicable at geometrically modeled
signals.

CENTRALBUSINESSDISTRICT

Note: You can also use the abbreviation, CBD.

CENTRALBUSINESSDISTRICT is a
logical-valued keyword which may be applied at geometrically-modeled fixed-time
signals. Coding
`CENTRALBUSINESSDISTRICT=Y`causes all calculated capacities to be 90% of the value that
would be obtained otherwise.

DELAYEQUATION

Selects the delay modeling methodology applied to the
capacities calculated by the HCM2000 signal capacity modeling methodology. The
keyword accepts the values "HCM" or "Catling" (case-insensitive). By default,
The HCM delay equations are invoked.

EXITLANES

The number of lanes traveling away from the modeled
intersection. This key may occur on the same arm as the
EXITONLY keyword but is invalid for a one-way link
that travels towards the intersection.

CUBE Voyager only uses this value for pedestrian and
bicycle modeling.

Note: If exit lanes are omitted from an arm that pedestrians
cross, the capacity of movements entering the arm may be reduced significantly.

FREEENTRYLENGTH

This keyword defines the length in the entry leg measured
from the stop line to the earliest point when a free turn vehicle can enter the
free turn pocket or channel in the current unit (meter or feet. See Data file
settings). If this value is greater than zero and the turn is coded as
exclusive, then it is considered a free turn. Default to 0 for not a free turn.
The Intersection Data Editor only takes values with 2 decimal places. If
provided with more than 2 decimal places, the values will be rounded up with 2
decimal places.

FREETURNEXITLENGTH

This keyword defines the length in the exit leg measured
from the earliest point to the latest point a free turn vehicle can merge into
the main flow of traffic in the current unit (meter or feet). It only becomes
effective when calculating the statistics for free right-turn movements. It can
be 0 for no merging lane, similar to a yield situation and it is default to 0.
The Intersection Data Editor only takes values with 2 decimal places. If
provided with more than 2 decimal places, the values will be rounded up with 2
decimal places. If this value is equal to or greater than the Free Turn Exit
Lane Max Length value in the Intersection File Settings screen (See Data file
settings), then it is assumed that no merging is needed or no impact on the
free turn capacity.

FREETURNFOLLOWUP

Free turn followup time in seconds. It only becomes
effective when calculating the statistics for free right-turn movements. It
will default to the Intersection File Setting. If not specified in file
setting, default to 2.5 seconds. The Intersection Data Editor only takes values
with 2 decimal places. If provided with more than 2 decimal places, the values
will be rounded up with 2 decimal places.

FREETURNGAP

This keyword defines free turn critical gap in seconds. It
only becomes effective when calculating the statistics for free right-turn
movements. It will default to the Intersection File Setting (See Data file
settings). If not specified in file setting, default to 4 seconds. The
Intersection Data Editor only takes values with 2 decimal places. If provided
with more than 2 decimal places, the values will be rounded up with 2 decimal
places.

GRADE

The real-valued keyword
GRADE describes the grade, expressed as a
percentage, of an approach to a geometrically modeled signals or a two-way
stop-controlled intersection. It is a signed value; negative values indicate
that the approach is downhill and positive values indicate that the approach is
uphill.

By default the approach is assumed to be flat
(GRADE = 0).

The models have been calibrated for grades the range -6% to
+11%, but more extreme grades do occur. For example the maximum grade in San
Francisco is about 31%.

NODEFACTOUNOPPOSE

Option to stop the de-facto exclusive turn lane check on
the unopposed turning movement (right turn on right drive and left turn on left
drive). This is a boolean keyword. Setting this option to True will disable the
check for exclusive turn lane modeling when volumes exceed threshold. This
setting is used to control the lane grouping for turn movements.

NODEFACTOOPPOSE

Option to stop the de-facto exclusive turn lane check on
the opposed turning movement (left turn on right drive and right turn on left
drive). This is a boolean keyword. Setting this option to True will disable the
check for exclusive turn lane modeling when volumes exceed threshold. This
setting is used to control the lane grouping for turn movements.

PARKINGMANEUVERS

The real values supplied to this keyword are number of
maneuvers per hour. The first element refers to the normal curb side of the
road; the second refers to the other side of the road (that is, if there is
parking in a central reservation or on the offside of a one way street). Only
parking within 80 meters of the stop line should be included

By default, parking is not allowed. Coding
`PARKINGMANUEVERS=0` means that parking is allowed, but it
is extremely rare.

This keyword is only applicable at geometrically modeled
signals.

PEDESTRIANFLOW

The number of pedestrians crossing the approach per hour.
Note that this is a two-way flow.

PEDESTRIANPHASE

The keyword
PEDESTRIANPHASE is integer-valued but,
conceptually, it consist of either one phase number (that is, digit) or of two
phase numbers (that is, two digits). In this respect, it is like the keyword
PHASES. The phases mentioned are the phases when
pedestrians crossing the approach are given permission to use the crosswalk.
The symbols displayed to the pedestrians vary by country, for example in the
U.S. the word WALK or an icon of a man walking is displayed in white whereas in
the U.K. an icon of a man walking is displayed in green.

If using a two-digit number, the two phases must be
adjacent.

PHASES

The keyword
PHASES is integer-valued but, conceptually, it
consist of either one phase number (that is, one digit) or of two phase numbers
(that is, two digits). The vehicles making the movement see a green signal
aspect when the specified phase(s) is/are running and red otherwise.

Note that the (node-level) keyword
PHASE is used to define phases and the
(movement-level) keyword
PHASES associates movements with the defined
phases.

At geometrically specified signals, any two-digit phase
specifications must specify contiguous phases. No such restriction is required
when coding saturation flows.

UNITEXTENSION

The minimum gap, in seconds, between successive vehicles
moving on a traffic-actuated approach to a signalized intersection that will
cause the signal controller to terminate the green display.

VEHICLELENGTH

This keyword defines queued vehicle spacing on the adjacent
through lane in meter or feet depending on the unit setting of the file. It
only becomes effective when calculating the statistics for free right-turn
movements. It will default to the Intersection File Setting (See Data file
settings). If not specified in file setting, default to 6 meters. The
Intersection Data Editor only takes values with 2 decimal places. If provided
with more than 2 decimal places, the values will be rounded up with 2 decimal
places.

Geometric signals
example

CUBE Voyager does not contain a model for right turn on red.
The right filter phase coded below might be used as a proxy for RTOR when the
right turns are heavy.

```
Junction,
   Node = 276,
   laneadjust=t,
   Type = FixedTimeSignal,
   Approach1 = 291,
   CycleTime = 90,
   Phase = 1,
     ActualGreen = 59,
   Phase = 2,
     ActualGreen = 5,
   Phase = 3,
     ActualGreen = 11,
   Approach = 291,
     AverageLaneWidth = 3.6,
     minimumcapacity=50,
     Movement = Left,
       ExclusiveLanes = 1,
       EstimatedDelay = 0.1,
       Phases = 1,
     Movement = Through,
       EstimatedDelay = 0.1,
       ExclusiveLanes = 1,
       Phases = 1,
     Movement = Right,
       ExclusiveLanes = 1,
       EstimatedDelay = 0.1,
       Phases = 12,
   Approach = 264,
     AverageLaneWidth = 3.6,
     minimumcapacity=50,
     Movement = Left,
       EstimatedDelay = 0.3,
       ExclusiveLanes = 1,
       Phases = 3,
     Movement = Through,
       EstimatedDelay = 0.3,
       Phases = 3,
       ExclusiveLanes = 1,
     Movement = Right,
       EstimatedDelay = 0.3,
       ExclusiveLanes = 1,
       Phases = 32,
   Approach = 267,
     AverageLaneWidth = 3.6,
     minimumcapacity=50,
     Movement = Left,
       ExclusiveLanes = 1,
       EstimatedDelay = 0.1,
       Phases = 1,
     Movement = Through,
       EstimatedDelay = 0.1,
       ExclusiveLanes = 1,
       Phases = 1,
     Movement = Right,
       ExclusiveLanes = 1,
       EstimatedDelay
       Phases = 12,
   Approach = 306,
     AverageLaneWidth = 3.6
     Movement = Left,
       EstimatedDelay = 0.2,
       ExclusiveLanes = 1,
       Phases = 3,
     Movement = Through,
       EstimatedDelay = 0.2,
       Phases = 3,
       ExclusiveLanes = 1,
     Movement = Right,
       EstimatedDelay = 0.2,
       ExclusiveLanes = 1,
       Phases = 32
Saturation flow signals e
```

Saturation flow
signals example

This example illustrates the coding of fixed-time signals:

```
Junction,
  Node = 276,
  Type = FixedTimeSignal,
  Approach1 = 291,
  CycleTime = 90,
  Phase = 1,
    ActualGreen = 59,
  Phase = 2,
    ActualGreen = 5,
  Phase = 3,
    ActualGreen = 11,
  Approach = 291,
    Movement = Left,
      CanShareRight=y,
      EstimatedDelay = 0.1,
      Phases = 1,
    Movement = Through,
      CanShareLeft=y,
      EstimatedDelay = 0.1,
      ExclusiveLanes = 1,
      Phases = 1,
    Movement = Right,
      ExclusiveLanes = 1,
      EstimatedDelay = 0.1,
      Phases = 2,
  Approach = 264,
    Movement = Left,
      EstimatedDelay = 0.3,
      CanShareRight=y,
      Phases = 3,
    Movement = Through,
      EstimatedDelay = 0.3,
      CanShareLeft=y,
      Phases = 3,
      ExclusiveLanes = 1,
    Movement = Right,
      EstimatedDelay = 0.3,
      ExclusiveLanes = 1,
      Phases = 23,
  Approach = 267,
    Movement = Left,
      CanShareRight=y,
      EstimatedDelay = 0.1,
      Phases = 1,
    Movement = Through,
      CanShareLeft=y,
      EstimatedDelay = 0.1,
      ExclusiveLanes = 1,
      Phases = 1,
    Movement = Right,
      ExclusiveLanes = 1,
      EstimatedDelay = 0.2,
      Phases = 2,
  Approach = 306,
    Movement = Left,
      EstimatedDelay = 0.2,
      CanShareRight=y,
      Phases = 3,
    Movement = Through,
      EstimatedDelay = 0.2,
      CanShareLeft=y,
      Phases = 3,
      ExclusiveLanes = 1,
    Movement = Right,
      EstimatedDelay = 0.2,
      ExclusiveLanes = 1,
      Phases = 23
```

**Parent topic:** [Intersection Modeling](GUID-B225FDCD-0F36-45AB-A3DB-32DC75608255.html)

|
|  |
|
|  |
