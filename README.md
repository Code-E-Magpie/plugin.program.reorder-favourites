# Kodi plugin program Reorder Favourites

![icon](https://github.com/Code-E-Magpie/plugin.program.reorder-favourites/blob/main/resources/media/icon.png)

Easy to use reordering of favourites for Kodi in a small package.


# Instructions
Open the addon to access the menu.

![icon](https://github.com/Code-E-Magpie/plugin.program.reorder-favourites/blob/main/.screenshots/menu.png)

Click on "R e o r d e r&nbsp;&nbsp;&nbsp;F a v o u r i t e s" to open the user interface.

![icon](https://github.com/Code-E-Magpie/plugin.program.reorder-favourites/blob/main/.screenshots/interface.png)

Click on the favourite to be moved which will change colour.

Then click on the favourite where it needs to go and it will move.

Multiple changes can be made to different favourites or an individual favourite. ("Start Again" can be used to cancel changes made in error without exiting the user interface and addon. Favourites reload in the original order).

Click on the "Close" button to return to the menu.

Choose from one of the three menu options:

Exit Only - no changes saved and exits the addon. Favourites remain in the original order.

Save + Exit - changes saved and exits the addon. Exit and restart Kodi for the changes to take effect. Do not make further changes until Kodi is restarted.

Save + Reload - changes saved and exits the addon. Kodi profile reloads (and changes to favourites). Do not make further changes until the profile reloads.'


# Notes
Default X image displayed where thumbnail is unavailable.

Up to two lines of fixed text displayed below an image (from start of favourite text).

Up to three lines of scrolling text displayed when the cursor is on an image (from start to end of favourite text).

"Save + Reload" may crash Kodi if there is a large number of favourites (i.e. large favourites.xml file). Profile reload automatically runs Kodi startup.'


# Development
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

Reorder Favourites displays a default X image where a thumbnail is unavailable. Thumbnail availability appears to be dependent on the addon it is sourced from.

Rumble and iPlayer WWW addons work fine but viwX doesn't. The viwX thumbnails display in Kodi favourites but are unavailable to the Reorder Favourites interface.

Please contact me if you can help in resolving this or explain why (Kodi logs may help).


# IMPORTANT
Distribution of this add-on is NOT permitted.
This add-on is exclusively distributed via the Magpie Repository and / or Code-E-Magpie on GitHub.

The code and files of this add-on are free for use, subject to crediting Code-E-Magpie.


# Alternatives to Reorder Favourites
Several other Kodi addons relating to favourites exist (including):

Order Favourites by doko-desuka:<br/>https://github.com/doko-desuka/plugin.program.orderfavourites

Insert-Swap-Kodi-Favourites by M-Borsch:<br/>https://github.com/M-Borsch/Insert-Swap-Kodi-Favourites

Manage-Kodi-Favourites by M-Borsch:<br/>https://github.com/M-Borsch/Manage-Kodi-Favourites/tree/main

Super Favourites by jmooremcc:<br/>https://github.com/jmooremcc/plugin.program.super.favourites

Super Favourites on kodi.wiki:<br/>https://kodi.wiki/view/Add-on:Super_Favourites