**Only download the Setup .exe to install TurtleBox Designer on Windows.**

### [Download TurtleBox-Designer-Setup-{{VERSION}}.exe](https://github.com/ravenridgelights-turtle/TurtleBox-Designer/releases/download/v{{VERSION}}/TurtleBox-Designer-Setup-{{VERSION}}.exe)

Run Setup to update the same installation, or use **Updates** beside the turtle and choose **Save project & install update**.

![Draw pigtails to the port you choose](https://raw.githubusercontent.com/ravenridgelights-turtle/TurtleBox-Designer/v{{VERSION}}/docs/releases/v{{VERSION}}/feature-flyer.jpg)

## What's new

<!-- turtlebox:changes:start -->
- **Draw pigtails to a port:** choose Pigtail, click a pixel port or PG gland, add bends around the parts, then click the other end. The dashed preview shows your route and measured length, and snaps to the destination under the pointer.
- **Choose the actual output:** clicking a gland starts a route. It no longer immediately creates a cable to its assigned port. Choose another port, or explicitly click **Use assigned P…**.
- **Reconnect and redraw:** start at an existing pigtail's gland to choose another board port, or select the cable and use **Redraw route in 3D**. Its connector, gender, outside length, wire gauge, slack and pin order stay intact. Cancel keeps the saved cable.
- **One or many:** click Pigtail once for one cable; double-click to keep drawing. Choose style, male/female end and outside length in the drawing bar.
- **2D and wall drilling:** start from the selected wall opening and finish on the board in Wiring, or draw both ends in the 2D plate. The 2D preview no longer blocks clicks on the destination terminal.
<!-- turtlebox:changes:end -->

Drawn bends remain attached to the endpoints and count toward the parts list and cut lengths in millimetres and inches, including slack. Existing projects remain compatible.

Checked with real mouse interaction in the browser, all 800 automated regression checks, and Windows install, upgrade, reinstall and uninstall checks before publication.
