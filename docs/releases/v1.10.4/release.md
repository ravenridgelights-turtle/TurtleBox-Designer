**Only download the Setup .exe to install TurtleBox Designer on Windows.**

### [Download TurtleBox-Designer-Setup-{{VERSION}}.exe](https://github.com/ravenridgelights-turtle/TurtleBox-Designer/releases/download/v{{VERSION}}/TurtleBox-Designer-Setup-{{VERSION}}.exe)

Run Setup to update the same installation, or use **Updates** beside the turtle and choose **Save project & install update**.

![Wire routing and room to design](https://raw.githubusercontent.com/ravenridgelights-turtle/TurtleBox-Designer/v{{VERSION}}/docs/releases/v{{VERSION}}/feature-flyer.jpg)

## What's new

<!-- turtlebox:changes:start -->
- **No smoke without power:** switching ON an unwired box no longer reports blue smoke. Unpowered wiring mistakes stay in **Review wiring**; only a fault with a live source and connected supply/return path produces the simulation effect. Crossing drawn insulated wires does not create an electrical connection.
- **Easy AC lead selection:** the black, white and green cores fan apart. Separate **L Hot**, **N Neutral** and **PE Ground** labels give each lead a clear click target. Click a label to start its wire directly. Review wiring highlights an incorrect connection.
- **Click bends in 3D:** start at a terminal, click a path around the PSU or controller, then click the destination. A dashed preview shows the route and length. **Bend height mm** sets the height for new points.
- **Fix an existing straight wire:** select it and choose **Redraw route in 3D**. Click the new bends, then **Finish route**. Endpoints, wire size, color and the wire ID are retained. Cancel leaves the original wire intact. Drag numbered bend handles to adjust a saved route.
- **Move the AC plug reliably:** separate amber handles let you move the plug and outlet even while the Wire tool is active. Pull an inserted plug out and drop it back onto the outlet to snap in. Move an outlet with its plugged-in cord attached. Selected plugs and outlets also have X, Y and height fields.
- **More workspace:** Parts and Details each have a hide/show button on the edge of the canvas. **Panels** or **F9** toggles both. The canvas expands into the free space and remembers your choice. Power options can collapse while keeping the on/off switch available.
- **Keep the measured route:** clicked and moved bends feed the saved project, live parts list and wire cut list. Direct 3D connections save without an extra form; the advanced endpoint editor remains available.
<!-- turtlebox:changes:end -->

## How to route around a supply

1. Open **Wiring** and choose **Wire** once.
2. Click the AC pigtail lead or source terminal.
3. Click each bend beside the supply. Change **Bend height mm** when you need a different height. Right-drag turns the view; the wheel zooms.
4. Click the destination terminal. The wire is saved, with the route length plus your chosen slack.

Use **Undo bend** while drawing, **Escape** to cancel, or double-click the Wire tool to keep drawing additional connections.

| Click a route around the PSU | Hide the menus for more room |
| --- | --- |
| ![Clicking 3D wire bends](https://raw.githubusercontent.com/ravenridgelights-turtle/TurtleBox-Designer/v{{VERSION}}/docs/releases/v{{VERSION}}/wire-bends.png) | ![Expanded workspace and movable AC outlet](https://raw.githubusercontent.com/ravenridgelights-turtle/TurtleBox-Designer/v{{VERSION}}/docs/releases/v{{VERSION}}/full-workspace.png) |

Validated with 769 regression checks and 25 real-browser workflows, including the earlier USB, stacked PSU, mounting, power preview and integral printed-plate workflows. Windows installer upgrade, reinstall and uninstall checks gate publication.
