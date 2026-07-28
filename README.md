# Reorder Favourites for Kodi

![icon](https://github.com/Code-E-Magpie/plugin.program.reorder-favourites/blob/main/resources/media/icon.png)

Easy to use reordering of favourites for Kodi in a small package.


# Instructions
Open the add-on to access the menu.

![icon](https://github.com/Code-E-Magpie/plugin.program.reorder-favourites/blob/main/.screenshots/menu.png)

Click on 'User Interface >' to open the user interface.

![icon](https://github.com/Code-E-Magpie/plugin.program.reorder-favourites/blob/main/.screenshots/interface.png)

Click on the favourite to be moved which will change colour.

Then click on the favourite where it needs to go and it will move.

Multiple changes can be made to different favourites or an individual favourite. ('Start Again' can be used to cancel changes made in error without exiting the user interface and add-on. Favourites reload in the original order).

Click on the 'Close' button to exit the user interface (changes pending). Follow the exit and save option dialogue boxes.<br/><br/>Choose from one of the exit options:<br/><br/>Exit Only - no changes saved and exits. Favourites remain in the original order.<br/><br/>Save Changes - save options dialogue box (changes pending).<br/><br/><br/>Choose from one of the save options:<br/><br/>Save + Exit - changes saved and exits the add-on. Exit and restart Kodi for the changes to take effect. Do not make further changes until Kodi is restarted.<br/><br/>Save + Reload - changes saved and exits the add-on. Kodi profile reloads (and changes to favourites). Do not make further changes until the profile reloads.


# Notes
Default X image displayed where thumbnail is unavailable.

Up to two lines of fixed text displayed below an image (from start of favourite text).

Up to three lines of scrolling text displayed when the cursor is on an image (from start to end of favourite text).

'Save + Reload' may crash Kodi if there is a large number of favourites (i.e. large favourites.xml file). Profile reload automatically runs Kodi startup.


# Reorder Favourites SE for Kodi

![icon](https://github.com/Code-E-Magpie/plugin.program.reorder-favourites/blob/main/.screenshots/icon_se.png)

Reorder Favourites SE (Special Edition) is the legacy version of Reorder Favourites (version 1.6.0) available from the Magpie Repository (GitHub / Kodi).

Reorder Favourites SE uses the same user interface as Reorder Favourites.<br/>Presentation of the exit and save options differ.<br/>Reorder Favourites SE uses the menu instead of dialogue boxes (see User Pathways below).

![icon](https://github.com/Code-E-Magpie/plugin.program.reorder-favourites/blob/main/.screenshots/menu_se.png)

Follow the instructions above up to and including click on the 'Close' button. Then choose an option from the menu.

Choose from one of the three menu options:

Exit Only - no changes saved and exits the add-on. Favourites remain in the original order.

Save + Exit - changes saved and exits the add-on. Exit and restart Kodi for the changes to take effect. Do not make further changes until Kodi is restarted.

Save + Reload - changes saved and exits the add-on. Kodi profile reloads (and changes to favourites). Do not make further changes until the profile reloads.


# User Pathways
Reorder Favourites:<br/>open add-on > menu > user interface > make changes > close > follow dialogue boxes > exit

Reorder Favourites SE:<br/>open add-on > menu > user interface > make changes > close > menu > choose option > exit


# Development environment
Kodi v21.3 Omega apk (Android app) with Confluence skin as default (including default font).

Tablet (1340 x 800 aspect ratio 5:3) running Android 14 using QuickEdit apk (TryItAndSee / LearnAsYouGo iterative development and testing).

Chromecast HD (1280 x 720 aspect ratio 16:9) running Android TV OS version 14 (user testing).

100% tested and working on Android.<br/>Not tested on other platforms.

Code debugged and reengineered where required using https://aipy.dev/tools


# Future development
Reorder Favourites functionality is simple and easy to use and will remain so.

No further development of Reorder Favourites is planned (see the 'Can you help ?' section below).

Reorder Favourites will be maintained for new releases of Kodi and changes to Python where possible.


# Can you help ?
There is a slight niggle with some thumbnails.

Reorder Favourites displays a default X image where a thumbnail is unavailable. Thumbnail availability appears to be dependent on the add-on it is sourced from.

Rumble and iPlayer WWW add-ons work fine but viwX doesn't. The viwX thumbnails display in Kodi favourites but are unavailable to the Reorder Favourites interface.

Please contact me if you can help in resolving this or explain why (Kodi logs may help).


# IMPORTANT
Distribution of this add-on is NOT permitted.
This add-on is exclusively distributed via the Magpie Repository and / or Code-E-Magpie on GitHub.

The code and files of this add-on are free for use, subject to crediting Code-E-Magpie.


# Alternatives to Reorder Favourites
Several other Kodi add-ons relating to favourites exist (including):

Order Favourites by doko-desuka:<br/>https://github.com/doko-desuka/plugin.program.orderfavourites

Insert-Swap-Kodi-Favourites by M-Borsch:<br/>https://github.com/M-Borsch/Insert-Swap-Kodi-Favourites

Manage-Kodi-Favourites by M-Borsch:<br/>https://github.com/M-Borsch/Manage-Kodi-Favourites/tree/main

Super Favourites by jmooremcc:<br/>https://github.com/jmooremcc/plugin.program.super.favourites

Super Favourites on kodi.wiki:<br/>https://kodi.wiki/view/Add-on:Super_Favourites
