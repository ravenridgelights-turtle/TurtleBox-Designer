**Only download the Setup .exe to install TurtleBox Designer on Windows.**

### [Download TurtleBox-Designer-Setup-{{VERSION}}.exe](https://github.com/ravenridgelights-turtle/TurtleBox-Designer/releases/download/v{{VERSION}}/TurtleBox-Designer-Setup-{{VERSION}}.exe)

Run Setup to update the same installation, or use **Updates** beside the turtle and choose **Save project & install update**.

![LRS-350 power LED correction](https://raw.githubusercontent.com/ravenridgelights-turtle/TurtleBox-Designer/v{{VERSION}}/docs/releases/v{{VERSION}}/feature-flyer.jpg)

## What's new

<!-- turtlebox:changes:start -->
- **LRS-350 power LED position:** move the green indicator to the open corner at the +V end of the terminal strip, beside the voltage-adjust area shown in the supplied photo and Mean Well drawing.
- The indicator follows the supply's rotation, flip and upright mounting, dims when power is off, and stays hidden when another supply or the housing blocks it.
<!-- turtlebox:changes:end -->

This is a focused correction to the LRS-350 power indicator.

Checked in the real browser with powered, unpowered, rotated, flipped, upright and stacked views. The existing power-path and fan regression checks pass; all 781 regression checks and Windows upgrade/reinstall/uninstall checks gate publication.
