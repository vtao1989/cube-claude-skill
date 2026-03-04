# Scenario Manager

A scenario defines a value for each key in the project.
Scenarios are used to test the effects of variations in input data.

You begin with a standard situation represented by a "Base"
scenario. You then introduce new scenarios to test variations on this base
situation. A corresponding scenario folder is created in the 'Scenarios' folder
in the project folder by default. Starting CUBE 7, all scenarios
(parents/child/siblings) will be stored in the same {Project\_Dir}\Scenarios
folder and there will be no hierarchical structure for the scenario folders.
All scenario folders in CUBE 7 will be appended with the respective scenario
code separated by a hyphen '-'. E.g., if Base scenario exists with Scenario
Code of 0001, a folder Base-0001 will be created automatically under the
{Project\_Dir}\Scenarios folder.

Note: Scenario names need
to be unique within a certain level. While scenario names can be same, the
scenario codes must be different. If they are not, CUBE will automatically
change the code to avoid any duplicate folders. The naming convention of the
scenario itself is flexible, the scenario names can start with a number which
was previously not allowed in earlier versions of CUBE. However, they can only
contain alphanumeric characters, spaces, underscores "\_", dashes "-", or the
pound sign "#".

All scenarios are listed under the
Project tab in Project Explorer, which is
known as Scenario Manager.
  
![](GUID-8656B611-9077-4DFA-ABC2-709C41A0DDD5-low.png)  
Scenarios are
hierarchical in nature. From the Base scenario, you can create scenarios that
will appear as children of the Base. A child may be considered as a variation
on its parent. A child scenario will inherit key values from its parent. For
example, a project may have some keys, one of which is named "Year". This may
be set to 2020 in the Base scenario. If a new scenario "New Road" is created as
a child of the Base, then the new scenario will also initially have a value of
2020 for the Year key. You may then edit the "New Road" scenario, updating the
value of Year to 2025. You may choose to update some of the other keys of the
scenario, or you can leave them the same as in the Base. Running the "New Road"
scenario will substitute the value of 2025 into the application for the Year
key, giving new results and providing a comparison with the base situation.

As example below, Base has 2 Childs: Y2025 and Y2035 and
they each have 2 childs, Plan A and Plan B. All these scenarios will be stored
under the same Scenarios folder.

![](GUID-B083A13D-FEF0-4D1B-859B-7D90EB398754-low.jpg)

For more information on arranging your Scenarios go to
[Manage Scenarios](GUID-34E09F90-114D-4955-B32F-1EFE3E572E66.html)

**Parent topic:** [Project Explorer](GUID-F6C1BA07-3C3C-4F25-8BDD-629A92C446B8.html)

|
|  |
|
|  |
