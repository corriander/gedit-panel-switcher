README
======

Description
-----------

Switch panels with a keyboard shortcut in gedit3

Allows switching focus to and from the bottom panel (embedded terminal
etc) with CTRL+Tab. 

Install
-------

Move `panelswitcher.py` and `panelswitcher.plugin` into 

`~/.local/share/gedit/plugins` (for single-user usage)

or

`/usr/lib/gedit/plugins` (for multi-user usage)

TODO
----

The following are possible improvements I might eventually get round to:

  - Extend switching functionality to side panel
  - Inherit sloppy mouse focus behaviour if set in desktop config
  - Allow switching between bottom panel items (tabs)
  - Facilitate hotkey configuration to avoid clashes with other plugins

Credits
-------

  - Flynsarmy for the GEdit3TabSwitch base
  - Inspiration from Christian Dannie Storgaard for the (deprecated)
    gedit2 FocusBottomPane plugin.
