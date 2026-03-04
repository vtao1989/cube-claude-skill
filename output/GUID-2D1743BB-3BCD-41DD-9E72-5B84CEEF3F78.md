# Priority junctions

This section describes priority junctions (two-way
yield-controlled intersections). Topics include:

- [Overview of priority junctions](GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78.html#GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78__OVERVIEW_unique_3)
- [Keywords](GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78.html#GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78__KEYWORDS_unique_2)
- [Geometric priority junctions: Keywords](GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78.html#GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78__GEOMETRICPRIORITYKW)
- [Geometric priority junctions: Example](GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78.html#GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78__GEOMETRICPRIORITYEX)
- [Saturation-flow priority junctions: Keywords](GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78.html#GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78__SATURATIONFLOWKW)
- [Saturation-flow priority junctions: Example](GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78.html#GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78__SATURATIONFLOWEX)

Overview of priority
junctions

A priority-junction control is an unsignalized intersection
between a major road and a minor road. It has different names in the U.K.
(where "priority junctions" are common) and the U.S. (where "two- way
yield-controlled intersections" are rare). In the U.S., the minor road approach
(at a "T"), or approaches (at a crossroads) have "yield" signs. In the U.K.,
the yield signs are optional. Traffic on the minor need not stop before
entering the intersection, but must give way to any major road traffic.

CUBE Voyager offers two model variants, both of which are
calibrated to U.K. traffic conditions: a full empirical model based on junction
geometry and a simplified models in which the user provides saturation flows
which have been estimated or measured externally to CUBE Voyager.

The geometric model is developed based on the TRRL report
941, and the saturation model is developed based on a similar model utilized in
the signal saturation flow model. Both models can be used to analyze the
capacity, delay, queue and LOS of roundabout intersections. The low flow delays
are the inverse of the capacity for both priority intersections.

When a single-lane major road is being modeled, very large
capacities may be reported. This occurs when a movement, which is
unconstrained, shares a lane. The capacity is chosen to give the correct ratio
of volume to capacity (as calculated for the constrained movement).

References

- Kimber, R. M., Mcdonald, M., Hounsell, N. B. (1986).
  The prediction of saturation flows for single
  road junctions controlled by traffic signals. Transport and Road
  Research Laboratory Report RR 67.
- Semmens M. C. (1980).
  PICADY: a computer program to model capacities,
  queues and delays at major/minor junctions. Transport and Road
  Research Laboratory Report RL 941.

Keywords

This section describes keywords for priority junctions:

- [GEOMETRIC](GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78.html#GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78__GEOMETRIC)
- [SINGLELANE](GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78.html#GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78__SINGLELANE_unique_2)

Note: Keywords are case insensitive. For example, capitalizing
as SingleLane might improve readability.

GEOMETRIC

The keyword "Geometric=y", invokes
modeling of layout geometry at a priority junction.

The default, "GapAcceptance=n", at a
priority junction is for the user to supply saturation flows directly.

The logical-valued keyword is used to indicate that an
approach consists of a single lane. It is applicable to many junction types:

SINGLELANE

- Signals

  Geometric Data -
  SINGLELANE may be coded. Saturation Flows -
  SINGLELANE may be coded.
- All-way stop-controlled intersection

  SINGLELANE
  may not be coded. code
  NUMBEROFLANES = 1.
- Two-way stop-controlled intersection

  SINGLELANE may be coded for minor
  road. Use
  FOURLANEMAJOR to describe major road.
- Priority intersection (two-way yield-controlled
  intersection)

  Geometric Data -
  SINGLELANE may be coded.
- Roundabout

  Saturation Flows -
  SINGLELANE may be coded.

  Empirical -
  SINGLELANE may not be coded.

  Gap Acceptance -
  SINGLELANE may not be coded.

Coding
SINGLELANE = Y for an approach precludes the use
of
EXCLUSIVELANES, CANSHARERIGHT, or
CANSHARELEFT on that approach.

At two-way stop-controlled intersections and priority
junctions, a minor arm, which does not have
`SINGLELANE=Y` explicitly coded, has two lanes.

Geometric priority
junctions: Keywords

This section describes the keywords for geometric priority
junctions:

- [CENTRALRESERVATIONWIDTH](GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78.html#GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78__CENTRALRESERVATIONWIDTH)
- [CROSSING2ENTRY](GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78.html#GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78__CROSSING2ENTRY_unique_1)
- [CROSSING2EXIT](GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78.html#GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78__CROSSING2EXIT_unique_1)
- [CROSSINGLENGTH](GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78.html#GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78__CROSSINGLENGTH_unique_1)
- [FREEFLOWCAP](GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78.html#GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78__FREEFLOWCAP_unique_1)
- [MAJORROADWIDTH](GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78.html#GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78__MAJORROADWIDTH)
- [VISIBILITY](GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78.html#GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78__VISIBILITY)
- [WIDTH](GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78.html#GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78__WIDTH)

Note: Keywords are case insensitive. For example, capitalizing
as SingleLane might improve readability.

CENTRALRESERVATIONWIDTH

CENTRALRESERVATIONWIDTH is a
real-valued keyword (only) applicable to geometrically modeled priority
junctions. Its value is the width, in meters or feet, of the curbed central
reservation in the major road. If there is no central reservation, or the
central reservation is composed of ghost islands (that is, road markings), then
CENTRALRESERVATIONWIDTH
should be zero (the default). Otherwise its value should be
in the range from 2.2 to 5.

In the diagram below, the
CENTRALRESERVATIONWIDTH is given by 1â2(W5 + W6).

![](GUID-135E2D81-2711-47B3-A051-7505BA39DA6B-low.png)

CROSSING2ENTRY

This keyword specifies the position of a zebra crossing on
an approach to a roundabout or a minor approach priority junction. Its value is
the number of vehicles that may queue at the junction without impeding
pedestrians who wish to cross. At roundabouts and single lane minor approaches
to priority junctions, a single integer value should be supplied. However, on
two-lane minor approaches to priority junctions, separate values should be
supplied for each of the two lanes.

CROSSING2EXIT

This integer-valued keyword specifies the position of a
zebra crossing on an exit from a roundabout or priority junction. Its value is
the number of vehicles that may queue at the crossing without impeding vehicles
using other exits from the junction.

CROSSINGLENGTH

This real-valued keyword allows the specification of the
length of a zebra crossing that crosses an approach to a roundabout or priority
junction. If it is absent then no crossing will be modeled.

FREEFLOWCAP

By default, the unmodelled movements from the major
approaches of a priority junction have infinite capacity. However, this may
result in too large a capacity for the approach as a whole when it must share a
lane with a modelled turn. You can supply a capacity for these movements by
coding FreeFlowCap=value and SingleLane=t.

MAJORROADWIDTH

MAJORROADWIDTH is only applicable to
geometrically modeled priority junctions, where it is required. The presence or
absence of this keyword allows the two methodologies for priority junction
modeling to be distinguished.

MAJORROADWIDTH is a real valued
keyword whose value is the width, in meters or feet, of the major road lane
(excluding any central reservation or ghost islands) near the intersection. It
is illustrated in the four diagrams below. In each case the major road width is
given by the expression 1â2(W1 + W2 + W3 + W4).

![](GUID-644A13EA-057B-4140-84F0-F2CF7AFEEED1-low.png)

VISIBILITY

This real-valued keyword allows the visibilities, in meters
or feet, at a geometrically coded priority junction (two-way yield-controlled
intersection) to be entered.

Visibilities may be coded for the minor road left and right
movements and for the opposed movement from the major road. Minor road
visibilities should be measured from a point ten meters before the give-way
line and 1.05 meters above the road surface. The major road visibility is
measured from the mid-point of the turning lane (again at height 1.05m), along
the major road, towards the road center line.

WIDTH

This real-valued keyword is used to specify the lane widths
(in meters or feet) for a minor road at a priority junction (two-way
yield-controlled intersection).

Code widths for left and right movements on minor roads and
for the opposed movement from the major road. The width for the major roadâs
opposed movement is the width of the lane from which vehicles on the major road
turn. Coding techniques for minor roads vary with the number of lanes.

To describe a two-lane minor road:

- Do not code
  `SINGLELANE=T`.
- Code the width of the left lane in the left movement.
- Code the width of the right lane in the right movement.

To describe a one-lane minor road:

- Code
  `SINGLELANE=T`.
- Code the width of the single lane in the left movement,
  or the right movement, but not both.

The coded widths should be the laneâs average width during
the final 25 meters of the approach before the give-way line.

Geometric priority
junctions: Example

This example illustrates the coding of a three-arm priority
junction, with input geometric data.

```
Junction,
   Node = 250,
   Type = Priority,
   Approach1 = 455,
   MajorRoadWidth = 10.9,
   CentralReservation = 1.2,
   Approach = 455,
      Movement = Right,
         Width = 2.5,
         Visibility = 170.0,
   Approach = 249,
      Movement = Left,
         Width = 2.05,
         Visibility = 130.0,
      Movement = Right,
         Width = 2.05,
         Visibility = 125.0,
   Approach = 251,
      Movement = Right,
         Width = 2.9,
         Visibility = 150.0,
   Approach = 255,
      SingleLane = y,
      Movement = Left,
         Visibility = 100.0,
      Movement = Right,
         Width = 3.1,
         Visibility = 127.0
```

Saturation-flow priority
junctions: Keywords

This section describes the keywords for saturation-flow
priority junctions:

- [CANSHARELEFT](GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78.html#GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78__CANSHARELEFT_unique_1)
- [CANSHARERIGHT](GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78.html#GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78__CANSHARERIGHT_unique_1)
- [EXCLUSIVELANES](GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78.html#GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78__EXCLUSIVELANES_unique_1)
- [SATFLOWPERLANE](GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78.html#GUID-2D1743BB-3BCD-41DD-9E72-5B84CEEF3F78__SATFLOWPERLANE_unique_1)

Note: Keywords are case insensitive. For example, capitalizing
as SingleLane might improve readability.

CANSHARELEFT

This keyword specifies that there is a shared lane to the
left of the exclusive lanes for this movement (that is, the movement can share
with the movement to its left). Note that this keyword does not mean "can share
with left turners" unless either the movement is THROUGH or the movement is on
the minor leg of a three-arm junction.

If a movement has
`CANSHARELEFT=T` coded then there must be a movement to
this movementâs left and the movement to this movementâs left must have
`CANSHARERIGHT=T` coded.

If
`SINGLELANE=T` then
CANSHARELEFT should not be coded.

CANSHARERIGHT

This keyword specifies that there is a shared lane to the
right of the exclusive lanes for this movement (that is, the movement can share
with the movement to its right). Note that this keyword does not mean "can
share with right turners" unless either the movement is THROUGH or the movement
is on the minor leg of a three arm junction.

If a movement has
`CANSHARERIGHT=T` coded, then there must be a movement to
this movementâs right, and the movement to this movementâs right must have
`CANSHARELEFT=T` coded.

If
`SINGLELANE=T` then
CANSHARERIGHT should not be coded.

EXCLUSIVELANES

This integer-valued keyword gives the number of lanes, on
the specified approach, which are reserved for the exclusive use of vehicles
making the specified movement.

If
`SingleLane=t` then
ExclusiveLanes should not be coded.

SATFLOWPERLANE

This real-valued keyword allows the specification of
saturation flows in pcu (vehicles) per hour per lane.

Saturation flows at signals are the flows that would be
observed if the movement had a continuous green all other movements had no flow
and no green.

Saturation flow at a priority junction (two-way
yield-controlled intersection) is defined similarly, except that no signal
aspects are involved.

Saturation-flow priority
junctions: Example

The example describes a priority junction using with a
three-lane major and two-lane minor using default saturation flows per lane.

```
Junction,
   Node = 229,
   Approach1 = 396,
   Type = Priority,
   Approach = 228,
     Movement = Left,
       ExclusiveLanes = 1,
       CanShareRight = y,
     Movement = Through
       ExclusiveLanes = 1,
       CanShareLeft = y,
       CanShareRight = y,
     Movement = Right,
       ExclusiveLanes = 1,
       CanShareLeft = y,
   Approach = 396,
     Movement = Left,
       ExclusiveLanes = 1,
       CanShareRight = y,
     Movement = Through,
       ExclusiveLanes = 1,
       CanShareLeft = y,
       CanShareRight = y,
     Movement = Right,
       ExclusiveLanes = 1,
       CanShareLeft = y,
   Approach = 315,
     Movement = Left,
       ExclusiveLanes = 1,
       CanShareRight = y,
     Movement = Through,
       CanShareLeft = y,
       CanShareRight = y,
     Movement = Right,
       ExclusiveLanes = 1,
       CanShareLeft = y,
   Approach = 409,
     Movement = Left,
       ExclusiveLanes = 1,
       CanShareRight = y,
     Movement = Through,
       CanShareLeft = y,
       CanShareRight = y,
     Movement = Right,
       ExclusiveLanes = 1,
       CanShareLeft = y
```

**Parent topic:** [Intersection Modeling](GUID-B225FDCD-0F36-45AB-A3DB-32DC75608255.html)

|
|  |
|
|  |
