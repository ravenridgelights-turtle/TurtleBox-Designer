**Only download the Setup .exe to install TurtleBox Designer on Windows.**

### [Download TurtleBox-Designer-Setup-{{VERSION}}.exe](https://github.com/ravenridgelights-turtle/TurtleBox-Designer/releases/download/v{{VERSION}}/TurtleBox-Designer-Setup-{{VERSION}}.exe)

Run Setup to update your existing installation, or use **Updates** beside the turtle and choose **Save project & install update**.

![Black PSU fan blades inside the grille](https://raw.githubusercontent.com/ravenridgelights-turtle/TurtleBox-Designer/v{{VERSION}}/docs/releases/v{{VERSION}}/feature-flyer.jpg)

## What's new

<!-- turtlebox:changes:start -->
- **Fan aligned with its opening:** the LRS-350 rotor now matches the fan port in the supplied STEP housing. The old fan position was mirrored relative to that model.
- **Black blades inside the PSU:** swept black blades replace the silver lines floating over the cover. The actual metal grille stays in front while the blades turn behind it.
- **Follows the housing:** rotation, flip, upright mounting and stacking keep the fan in place. An upper supply hides the lower fan where it blocks the view. The LRS-600 and thick S-360 fans use the same cover-aware rendering.
- **Works in existing projects:** saved measured PSU profiles acquire the matching native fan placement. Mounting holes and plate cut files stay unchanged.
- **Power controls the motion:** a correctly powered supply spins its fan; an unpowered supply shows stationary black blades.
<!-- turtlebox:changes:end -->

![Powered 3D assembly](https://raw.githubusercontent.com/ravenridgelights-turtle/TurtleBox-Designer/v{{VERSION}}/docs/releases/v{{VERSION}}/fan-assembly.png)

Validated with 781 regression checks and a focused browser check of blade motion, grille occlusion, power-off, flat/upright orientations and stacked supplies. Windows installer upgrade, reinstall and uninstall checks gate publication.
