**Only download the Setup .exe to install TurtleBox Designer on Windows.**

### [Download TurtleBox-Designer-Setup-{{VERSION}}.exe](https://github.com/ravenridgelights-turtle/TurtleBox-Designer/releases/download/v{{VERSION}}/TurtleBox-Designer-Setup-{{VERSION}}.exe)

Run the installer to install or update the same app in place. If TurtleBox is already installed, use **Updates** beside the turtle, read the changes, then choose **Save project & install update**.

![TurtleBox Designer feature flyer](https://raw.githubusercontent.com/ravenridgelights-turtle/TurtleBox-Designer/v{{VERSION}}/docs/releases/v{{VERSION}}/feature-flyer.jpg)

## What's new in v{{VERSION}}

<!-- turtlebox:changes:start -->
- **Controller views fixed:** restored the verified Uno/Quad SVG models, corrected the separate K16 A-B, and added the official Dig-Octa Power-5 mounting profile. Screens, brains, terminals and sockets now share positions between the detailed 2D and 3D controller views.
- **Gland patterns stay editable:** opening Gland pattern edits the existing pattern. Board-port labels, wire links and fitting IDs stay attached. Drag a box around fittings to move, replace or remove them together.
- **Problems point to the right place:** pattern previews mark affected openings. Placement selects the exact warning, fitting and position controls, with a button to highlight its assigned board port in 3D.
- **More complete wiring and networking:** male/female pixel pigtails run through their selected glands; Ethernet leads follow the actual socket direction. Add folding USB Wi-Fi or an Ethernet/USB hub, direct insertion or extension placement, and cable-tie slots.
- **Box mounting is easier to find:** the Box mounts view shows factory attachment spots and screw information. Plates start on the selected box mounts; optional extra height and assembled-board height are visible controls.
- **Better printed plates and PSU stacks:** zoom the print preview, emboss names/outlines/hole sizes, and split 3mm/4mm plates with adjustable dovetails. Original PSU stack frames have adjustable airflow gaps, locating slots, whole uprights and separate STL/laser files.
- **A fuller parts list:** hardware, glands, pigtails, Ethernet cables, wire gauges and cut lengths with slack in inches and millimetres, material estimates and product/vendor links.
<!-- turtlebox:changes:end -->

## See the features

Click a screenshot to view it at full size. These are captures of the working v{{VERSION}} app.

| Design a plate | Inspect the 3D assembly |
|---|---|
| [![Box-fitted mounting plate](https://raw.githubusercontent.com/ravenridgelights-turtle/TurtleBox-Designer/v{{VERSION}}/docs/releases/v{{VERSION}}/plate-design.jpg)](https://raw.githubusercontent.com/ravenridgelights-turtle/TurtleBox-Designer/v{{VERSION}}/docs/releases/v{{VERSION}}/plate-design.jpg) | [![Double-deck 3D assembly](https://raw.githubusercontent.com/ravenridgelights-turtle/TurtleBox-Designer/v{{VERSION}}/docs/releases/v{{VERSION}}/assembly-3d.jpg)](https://raw.githubusercontent.com/ravenridgelights-turtle/TurtleBox-Designer/v{{VERSION}}/docs/releases/v{{VERSION}}/assembly-3d.jpg) |
| **Make PDF / STL drilling templates** | **3D print plates with dovetails** |
| [![Drilling template tools](https://raw.githubusercontent.com/ravenridgelights-turtle/TurtleBox-Designer/v{{VERSION}}/docs/releases/v{{VERSION}}/drilling-templates.jpg)](https://raw.githubusercontent.com/ravenridgelights-turtle/TurtleBox-Designer/v{{VERSION}}/docs/releases/v{{VERSION}}/drilling-templates.jpg) | [![Printed plate preview](https://raw.githubusercontent.com/ravenridgelights-turtle/TurtleBox-Designer/v{{VERSION}}/docs/releases/v{{VERSION}}/printed-plates.jpg)](https://raw.githubusercontent.com/ravenridgelights-turtle/TurtleBox-Designer/v{{VERSION}}/docs/releases/v{{VERSION}}/printed-plates.jpg) |
| **Drag and drop controllers** | **Get your build's parts list** |
| [![Drag-and-drop component placement](https://raw.githubusercontent.com/ravenridgelights-turtle/TurtleBox-Designer/v{{VERSION}}/docs/releases/v{{VERSION}}/drag-and-drop.jpg)](https://raw.githubusercontent.com/ravenridgelights-turtle/TurtleBox-Designer/v{{VERSION}}/docs/releases/v{{VERSION}}/drag-and-drop.jpg) | [![Hardware and wire cut list](https://raw.githubusercontent.com/ravenridgelights-turtle/TurtleBox-Designer/v{{VERSION}}/docs/releases/v{{VERSION}}/parts-list.jpg)](https://raw.githubusercontent.com/ravenridgelights-turtle/TurtleBox-Designer/v{{VERSION}}/docs/releases/v{{VERSION}}/parts-list.jpg) |

<details>
<summary>Detailed change notes</summary>

{{CHANGELOG}}

</details>

Built and checked with 684 regression checks, real browser interaction/rendering checks, and automated Windows upgrade, reinstall and uninstall checks.
