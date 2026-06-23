# ============================================================
#################################
# reorder_favourites.py by Code-E-Magpie
#################################
# ============================================================

# ============================================================
# File information
# ============================================================

# sourced from: plugin.program.orderfavourites > default.py (1.2.3a by doko-desuka)
# location: plugin.program.reorder-favourites > reorder_favourites.py
# type: system
# functionality: reorder favourites in favourites.xml

# ============================================================
# Import
# ============================================================

import xbmc, xbmcaddon, xbmcgui, xbmcplugin, xbmcvfs
import os, re, sys

try:

	# Python 2.x
	from HTMLParser import HTMLParser
	PARSER = HTMLParser()
	DECODE_STRING = lambda val: val.decode('utf-8')
except ImportError as e:

	# Python 3.4+ (see https://stackoverflow.com/a/2360639)
	import html
	PARSER = html
	DECODE_STRING = lambda val: val # Pass-through.

# ============================================================
# Variables
# ============================================================

ADDON_ID = xbmcaddon.Addon().getAddonInfo('id') # id in addons.xml
ADDON = xbmcaddon.Addon(ADDON_ID)
ADDON_DEVELOPER = ADDON.getAddonInfo('author') # provider-name in addons.xml (developer)
ADDON_FANART = ADDON.getAddonInfo('fanart')
ADDON_ICON = ADDON.getAddonInfo('icon')
ADDON_NAME = ADDON.getAddonInfo('name') # name in addons.xml
ADDON_TITLE = (' '.join((ADDON_NAME).strip(' '))) # insert spaces between + remove leading & trailing
ADDON_VERSION = ADDON.getAddonInfo('version') # version in addons.xml
FAVOURITES = os.path.join('special://userdata/', 'favourites.xml')
FAVOURITES_RESULT = 'ordfav.result'
PLUGIN_ID = int(sys.argv[1])
PLUGIN_URL = sys.argv[0]
REORDER = os.path.join(ADDON.getAddonInfo('path'), 'resources', 'media', 'reorder.png')
TEXT_ADDON = 'yellow' # default to "name" colour in addon.xml if quote marks are empty i.e. = ''
TEXT_DARK = 'darkgray'
TEXT_DIM = 'dimgray'
TEXT_GENERAL = 'silver'
TEXT_HIGHLIGHT = 'yellow'
TEXT_ITEM = 'blue'
TEXT_VALUE = 'orange'
THUMBNAILS_FORMAT = 'special://thumbnails/{folder}/{file}'

# ============================================================
# Addon_ID_Version / Addon_Title / Dialogue / Favourites / Log_Title
# ============================================================

Addon_ID_Version = ('[COLOR %s]%s [/COLOR][COLOR %s] %s[/COLOR]' % (TEXT_ITEM, ADDON_ID, TEXT_VALUE, ADDON_VERSION))
Addon_Title = ('[COLOR %s]%s[/COLOR]' % (TEXT_ADDON, ADDON_TITLE))
Dialogue = xbmcgui.Dialog()
Favourites = ('[COLOR %s]favourites > [/COLOR]' % TEXT_GENERAL)
Log_Title = ('[COLOR %s]%s [/COLOR]' % (TEXT_ADDON, ADDON_NAME))

# ============================================================
# FUNCTION: Log
# ============================================================

def Log(msg, level = xbmc.LOGDEBUG):
	xbmc.log(msg, level = level)

#####################################################################################

# ============================================================
# ------------------------------------------------------------
# User Information
# ------------------------------------------------------------
# ============================================================

# ============================================================
# FUNCTION: TextBox
# ============================================================

ACTION_BACKSPACE = 110 # Backspace
ACTION_MOUSE_LEFT_CLICK = 100 # Mouse click
ACTION_MOUSE_LONG_CLICK = 108 # Mouse long click
ACTION_MOUSE_WHEEL_DOWN = 105 # Mouse wheel down
ACTION_MOUSE_WHEEL_UP = 104 # Mouse wheel up
ACTION_MOVE_DOWN = 4 # Down arrow key
ACTION_MOVE_LEFT = 1 # Left arrow key
ACTION_MOVE_MOUSE = 107 # Down arrow key
ACTION_MOVE_RIGHT = 2 # Right arrow key
ACTION_MOVE_UP = 3 # Up arrow key
ACTION_NAV_BACK = 92 # Backspace action
ACTION_PREVIOUS_MENU = 10 # ESC action
ACTION_SELECT_ITEM = 7 # Number Pad Enter

def TextBox(title, msg):
	class TextBoxes(xbmcgui.WindowXMLDialog):

		def onAction(self, action):
			if action == ACTION_PREVIOUS_MENU: self.close()
			elif action == ACTION_NAV_BACK: self.close()

		def onClick(self, controlId):
			if (controlId == self.okbutton):
				self.close()
			elif controlId != self.okbutton:
				self.noop = lambda: None

		def onInit(self): # group = 8000, background = 8100, noop = 8181
			self.title = 8200 # header
			self.msg = 8300 # textbox
			self.scrollbar = 8400 # scrollbar
			self.okbutton = 8500 # close button
			self.noop = lambda: None
			self.showDialog()

		def showDialog(self):
			self.getControl(self.title).setLabel(title)
			self.getControl(self.msg).setText(msg)
			self.setFocusId(self.scrollbar)

	textbox = TextBoxes("Textbox.xml", ADDON.getAddonInfo('path'), 'default')
	textbox.doModal()
	del textbox

# ============================================================
# FUNCTION: Development_Information
# ============================================================

MAGPIE_TEXT = 'M A G P I E   R E P O S I T O R Y[CR][CR]The official repository of [COLOR silver]C[COLOR dimgray]o[/COLOR]d[COLOR dimgray]e[/COLOR]-[COLOR dimgray]E[/COLOR]-[COLOR dimgray]M[/COLOR]a[COLOR dimgray]g[/COLOR]p[COLOR dimgray]i[/COLOR]e[/COLOR] add-ons.[CR]Distribution of the Magpie Repository is permitted.[CR][CR][COLOR silver]IMPORTANT:[CR]Distribution of C[COLOR dimgray]o[/COLOR]d[COLOR dimgray]e[/COLOR]-[COLOR dimgray]E[/COLOR]-[COLOR dimgray]M[/COLOR]a[COLOR dimgray]g[/COLOR]p[COLOR dimgray]i[/COLOR]e add-ons are NOT permitted.[CR]C[COLOR dimgray]o[/COLOR]d[COLOR dimgray]e[/COLOR]-[COLOR dimgray]E[/COLOR]-[COLOR dimgray]M[/COLOR]a[COLOR dimgray]g[/COLOR]p[COLOR dimgray]i[/COLOR]e add-ons are exclusively distributed via the Magpie Repository and / or [COLOR silver]C[COLOR dimgray]o[/COLOR]d[COLOR dimgray]e[/COLOR]-[COLOR dimgray]E[/COLOR]-[COLOR dimgray]M[/COLOR]a[COLOR dimgray]g[/COLOR]p[COLOR dimgray]i[/COLOR]e[/COLOR] on GitHub.[CR]The code and files of these add-ons are free for use, subject to crediting C[COLOR dimgray]o[/COLOR]d[COLOR dimgray]e[/COLOR]-[COLOR dimgray]E[/COLOR]-[COLOR dimgray]M[/COLOR]a[COLOR dimgray]g[/COLOR]p[COLOR dimgray]i[/COLOR]e.[/COLOR][CR][CR][COLOR %s]Available on GitHub only.[CR]https://github.com/Code-E-Magpie/repository.magpie[CR][CR]To install Magpie Repository:[CR]Add the Kodi source https://Code-E-Magpie.github.io/repository.magpie/[CR]Use the \'Install from zip file\' method to install the Magpie Repository.[/COLOR]' % TEXT_DARK

DATABASE_TEXT = '[CR][CR][CR]D A T A B A S E   T O O L B O X[CR][CR]Database Toolbox with easy to use database maintenance tools.[CR][CR][COLOR %s]Add-on available from Magpie Repository. Further details on GitHub and within the add-on itself.[CR]https://github.com/Code-E-Magpie/plugin.program.database-toolbox[/COLOR]' % TEXT_DARK

MAINTENANCE_TEXT = '[CR][CR][CR]M A I N T E N A N C E   T O O L B O X[CR][CR]Maintenance Toolbox with easy to read Kodi information (system, add-ons, network and internet).[CR]Clear cache + folders, surplus add-ons, temp folder and thumbnails.[CR]View logs and errors (new and old).[CR]Check repositories, sources and internet speed (Speedtest by Ookla).[CR]Backup and restore favourites, sources, logs, userdata, add-ons, add-on data etc.[CR][CR][COLOR %s]Add-on available from Magpie Repository. Further details on GitHub and within the add-on itself.[CR]https://github.com/Code-E-Magpie/plugin.program.maintenance-toolbox[/COLOR]' % TEXT_DARK

REORDER_TEXT = '[CR][CR][CR]R E O R D E R   F A V O U R I T E S[CR][CR]Easy to use reordering of favourites for Kodi.[CR][CR][COLOR %s]Add-on available from Magpie Repository. Further details on GitHub and within the add-on itself.[CR]https://github.com/Code-E-Magpie/plugin.program.reorder-favourites[/COLOR]' % TEXT_DARK

LOG_TEXT = '[CR][CR][CR]S Y S T E M   L O G   T O O L B O X[CR][CR]System Log Toolbox easy to use system log viewer.[CR][CR][COLOR %s]Add-on available from Magpie Repository. Further details on GitHub and within the add-on itself.[CR]https://github.com/Code-E-Magpie/plugin.program.system-log-toolbox[/COLOR]' % TEXT_DARK

SPECIAL_TEXT = '[CR][CR][CR]F A V O U R I T E S   &   S O U R C E S[CR][CR]Special Favourites: Kodi special paths and customised examples.[CR]Special Sources: Kodi special paths (files & folders) and customised examples.[CR][CR][COLOR %s]Available on GitHub only.[CR]https://github.com/Code-E-Magpie/Code-E-Magpie[/COLOR]' % TEXT_DARK

TEMPLATE_TEXT = '[CR][CR][CR]T E M P L A T E   R E P O S I T O R Y[CR][CR]Created to illustrate a GitHub repository with a simple folder structure linked to a Kodi repository.[CR][CR][COLOR %s]Available on GitHub only.[CR]https://github.com/Code-E-Magpie/repository.template[/COLOR][CR][CR]Alternatively a GitHub repository linked to a Kodi source, without using a Kodi repository.[CR][CR][COLOR %s]Available on GitHub only.[CR]https://github.com/Code-E-Magpie/repository.simple[/COLOR]' % (TEXT_DARK, TEXT_DARK)

Development_Information_Text = '[CR][CR][CR][COLOR %s][B]C o d e - E - M a g p i e   D e v e l o p m e n t[/B][CR][COLOR %s][LIGHT](Magpie Repository / Database Toolbox / Maintenance Toolbox / Reorder Favourites / System Log Toolbox / Favourites & Sources / Template Repository)[/LIGHT][/COLOR][/COLOR][CR][CR][COLOR %s]%s[/COLOR]' % (TEXT_ITEM, TEXT_VALUE, TEXT_GENERAL, (MAGPIE_TEXT + DATABASE_TEXT + MAINTENANCE_TEXT + REORDER_TEXT + LOG_TEXT + SPECIAL_TEXT + TEMPLATE_TEXT))

# ============================================================
# FUNCTION: User_Information
# ============================================================

INSTRUCTIONS_TEXT = 'I N S T R U C T I O N S[CR][CR]Open the add-on to access the menu.[CR]Click on \'R e o r d e r   F a v o u r i t e s    U s e r   I n t e r f a c e  >\' to open the user interface.[CR][CR]Click on the favourite to be moved which will change colour.[CR]Then click on the favourite where it needs to go and it will move.[CR]Multiple changes can be made to different favourites or an individual favourite.[CR]\'Start Again\' can be used to cancel changes made in error without exiting the user interface and add-on. Favourites reload in the original order.[CR]Click on the \'Close\' button to return to the menu.[CR][CR]Choose from one of the three menu options:[CR]Exit Only - no changes saved and exits the add-on. Favourites remain in the original order.[CR]Save + Exit - changes saved and exits the add-on. Exit and restart Kodi for the changes to take effect. Do not make further changes until Kodi is restarted.[CR]Save + Reload - changes saved and exits the add-on. Kodi profile reloads (and changes to favourites). Do not make further changes until the profile reloads.'

NOTES_TEXT = '[CR][CR][CR]N O T E S[CR][CR]Default X image displayed where thumbnail is unavailable.[CR]Up to two lines of fixed text displayed below an image (from start of favourite text).[CR]Up to three lines of scrolling text displayed when the cursor is on an image (from start to end of favourite text).[CR]\'Save + Reload\' may crash Kodi if there is a large number of favourites (i.e. large favourites.xml file). Profile reload automatically runs Kodi startup.'

DEVELOPMENT_TEXT = '[CR][CR][CR]D E V E L O P M E N T[CR][CR]Kodi v21.3 Omega apk (Android app) with Confluence skin as default (including default font).[CR]Tablet (1340 x 800 aspect ratio 5:3) running Android 14 using QuickEdit apk (TryItAndSee / LearnAsYouGo iterative development and testing).[CR]Chromecast HD (1280 x 720 aspect ratio 16:9) running Android TV OS version 14 (user testing).[CR]100% tested and working on Android.[CR]Not tested on other platforms.[CR]Code debugged and reengineered where required using https://aipy.dev/tools'

CHANGELOG_TEXT = '[CR][CR][CR]C H A N G E L O G [LIGHT] (newest at the top)[/LIGHT][CR][CR]Version code x.y.z attributes (1.5.0 onwards)[CR]x = major change / y = number of \'>\' menu items / z = minor change[CR][CR]version 1.5.1 (5 menu items & 2 user interface buttons)[CR]- minor changes to menu text formats to improve consistency with other add-ons[CR][CR]version 1.5.0 (5 menu items & 2 user interface buttons)[CR]- Textbox.xml background image name change[CR]- minor changes to improve consistency with other add-ons[CR][CR]version 1.2.4 (4 menu items for user interface & 2 user interface buttons)[CR]- menu updated with User Information dialogue box (Instructions / Notes / Development / Changelog)[CR]- menu updated with Developer, Name, Version and Addon ID[CR]- user interface ids in xml renumbered[CR]- user interface remote scrolling within borders[CR]- user interface images and layout improved[CR]- variables and functions reworked[CR]- dialogue boxes and logs reworked[CR]- simplified addon.xml content to reduce maintenance[CR][CR]version 1.0.0 (4 menu items for user interface & 2 user interface buttons)[CR]- code from Order Favourites 1.2.3a by doko-desuka (plugin.program.orderfavourites)[CR]- user interface resized to full screen[CR]- improved layout using new images and default image[CR]- visible scrollbar and resized text[CR]- menu and dialogue boxes reworked[CR]- user instructions added to addon.xml[CR]- icon.png changed and fanart.jpg added'

User_Information_Text = '[COLOR %s][B]U S E R   I N F O R M A T I O N[/B][CR][COLOR %s][LIGHT](Instructions / Notes / Development / Changelog)[/LIGHT][/COLOR][/COLOR][CR][CR][COLOR %s]%s[/COLOR]' % (TEXT_ITEM, TEXT_VALUE, TEXT_GENERAL, (INSTRUCTIONS_TEXT + NOTES_TEXT + DEVELOPMENT_TEXT + CHANGELOG_TEXT))

def User_Information():
	TextBox('[B]%s[/B][CR]%s' % (Addon_Title, Addon_ID_Version), User_Information_Text + Development_Information_Text)

####################################################################################

# ============================================================
# ------------------------------------------------------------
# User Interface
# ------------------------------------------------------------
# ============================================================

# ============================================================
# CLASS: ReorderFavourites
# ============================================================

class ReorderFavourites(xbmcgui.WindowXMLDialog):

# ============================================================
# FUNCTION: __init__
# ============================================================

	# Initialise the class, map control IDs and action IDs to custom handler methods.
	def __init__(self, *args, **kwargs):
		xbmcgui.WindowXMLDialog.__init__(self, *args, **kwargs)

		# Map control IDs to custom handler methods. IDs in /resources/skins/default/1080i/ReorderFavourites.xml
		self.idHandlerDict = {
			8320: self.doSelect,
			8500: self.close,
			8501: self.startAgain,
		}

		# Map action IDs to custom handler methods.
		# See https://github.com/xbmc/xbmc/blob/master/xbmc/input/actions/ActionIDs.h
		self.actionHandlerDict = {
			# All click / select actions are already handled by 'idHandlerDict' above.
			# 7: self.doSelect, # ACTION_SELECT_ITEM
			9: self.doUnselectClose, # ACTION_PARENT_DIR
			10: self.doUnselectClose, # ACTION_PREVIOUS_MENU
			92: self.doUnselectClose, # ACTION_NAV_BACK
			# 100: self.doSelect, # ACTION_MOUSE_LEFT_CLICK
			# 108: self.doSelect, # ACTION_MOUSE_LONG_CLICK
			110: self.doUnselectClose, # ACTION_BACKSPACE
			8320: self.doUnselectClose, # ACTION_MOUSE_RIGHT_CLICK
		}
		self.noop = lambda: None

# ============================================================
# FUNCTION: doCustomModal
# ============================================================

	def doCustomModal(self, favouritesGen):
		allItems = [ ]
		artDict = {'thumb': None}
		Log(Log_Title + Favourites + '[COLOR %s][LIGHT]Started[/LIGHT][/COLOR]' % TEXT_DARK, xbmc.LOGINFO)

		for index, data in enumerate(favouritesGen):
			# Every ListItem contains the original favourite (label, thumb and URL).
			# Favourites are written back to the xml file when saving (only the order changes).
			li = xbmcgui.ListItem(data[0], path=data[2])
			artDict['thumb'] = data[1] # Slightly faster than recreating a dict on every item.
			li.setArt(artDict)
			li.setProperty('index', str(index)) # Helps resetting.
			allItems.append(li)

		self.allItems = allItems
		self.indexFrom = None # Integer index of the source item (or None when nothing is selected).
		self.isDirty = False # Bool indicating if there are any changes.

		self.doModal()

		return self.makeResult() if self.isDirty else ''

# ============================================================
# FUNCTION: doSelect
# ============================================================

	def doSelect(self):
		selectedPosition = self.panel.getSelectedPosition()
		if self.indexFrom == None:
			# Select a new item to reorder.
			self.indexFrom = selectedPosition
			self.panel.getSelectedItem().setProperty('selected', '1')

		else:
			# Reorder if item already selected.
			if self.indexFrom != selectedPosition:
				# Reorder uses the .pop() and .insert() methods of the 'self.allItems' list.
				itemFrom = self.allItems.pop(self.indexFrom)
				self.allItems.insert(selectedPosition, itemFrom)
				self.isDirty = True

				# Reset the selection state.
				self.indexFrom = None
				itemFrom.setProperty('selected', '')

				# Update the panel by clearing it and reloading all the items.
				self.panel.reset()
				self.panel.addItems(self.allItems)
				self.panel.selectItem(selectedPosition)

			else: # Unselect item if its reselected.
				self.indexFrom = None
				self.panel.getSelectedItem().setProperty('selected', '')

# ============================================================
# FUNCTION: doUnselectClose
# ============================================================

	def doUnselectClose(self):
		# Unselect item if one is selected, otherwise close it.
		if self.indexFrom != None:
			self.allItems[self.indexFrom].setProperty('selected', '')
			self.indexFrom = None

		else:
			self.close()

# ============================================================
# FUNCTION: makeResult
# ============================================================

	def makeResult(self):
		INDENT_STRING = ' ' * 4
		return '<favourites>\n' + '\n'.join((INDENT_STRING + li.getPath()) for li in self.allItems) + '\n</favourites>\n'

# ============================================================
# FUNCTION: onAction
# ============================================================

	def onAction(self, action):
		self.actionHandlerDict.get(action.getId(), self.noop)()

# ============================================================
# FUNCTION: onClick
# ============================================================

	def onClick(self, controlId):
		self.idHandlerDict.get(controlId, self.noop)()

# ============================================================
# FUNCTION: onInit
# ============================================================

	def onInit(self):
		self.panel = self.getControl(8320)
		self.panel.reset()
		self.panel.addItems(self.allItems)
		self.setFocusId(8310) # Focus on the group containing the panel, not the panel itself.

# ============================================================
# FUNCTION: startAgain
# ============================================================

	def startAgain(self):
		# Reload favourites in the original order.
		if Dialogue.yesno(Addon_Title, '[COLOR %s]Reorder Favourites: [LIGHT](Start Again)[/LIGHT][CR]Start again ?[CR][COLOR %s]Any changes will be lost.[CR]Favourites will be reloaded in the original order.[/COLOR][/COLOR]' % (TEXT_GENERAL, TEXT_DIM), yeslabel = ('[COLOR %s]Start Again[/COLOR]' % TEXT_VALUE), nolabel = ('[COLOR %s]Cancel[/COLOR]' % TEXT_HIGHLIGHT)):

			self.indexFrom = None
			self.allItems = sorted(self.allItems, key=lambda li: int(li.getProperty('index')))
			self.panel.reset()
			self.panel.addItems(self.allItems)

#####################################################################################

# ============================================================
# ------------------------------------------------------------
# Menu
# ------------------------------------------------------------
# ============================================================

# ============================================================
# FUNCTION: clearWindowProperty
# ============================================================

def clearWindowProperty(prop):
	window = xbmcgui.Window(xbmcgui.getCurrentWindowId())
	window.clearProperty(prop)

# ============================================================
# FUNCTION: favouritesDataGen
# ============================================================

def favouritesDataGen():
	file = xbmcvfs.File(FAVOURITES)
	contents = DECODE_STRING(file.read())
	file.close()

	namePattern = re.compile('name="([^"]+)')
	thumbPattern = re.compile('thumb="([^"]+)')

	for entryMatch in re.finditer('(<favourite\s[^<]+</favourite>)', contents):
		entry = entryMatch.group(1)

		match = namePattern.search(entry)
		name = PARSER.unescape(match.group(1)) if match else ''

		match = thumbPattern.search(entry)

		if match:
			thumb = PARSER.unescape(match.group(1))
			cacheFilename = xbmc.getCacheThumbName(thumb)

			if 'ffffffff' not in cacheFilename:
				if '.jpg' in thumb:
					cacheFilename = cacheFilename.replace('.tbn', '.jpg', 1)
				if '.png' in thumb:
					cacheFilename = cacheFilename.replace('.tbn', '.png', 1)
				thumb = THUMBNAILS_FORMAT.format(folder=cacheFilename[0], file=cacheFilename)

		else:
			thumb = ''

		# Yield a 3-tuple of name, thumb-url and the original favourite.
		yield name, thumb, entry

# ============================================================
# FUNCTION: favouritesSave
# ============================================================

def favouritesSave(xmlText):
	if not xmlText:
		return False

	try:
		file = xbmcvfs.File(FAVOURITES, 'w')
		file.write(xmlText)
		file.close()

	except Exception as e:
		Log(Log_Title + 'favouritesSave > %s' % str(e), xbmc.LOGERROR)

	return True

# ============================================================
# FUNCTION: getRawWindowProperty
# ============================================================

def getRawWindowProperty(prop):
	window = xbmcgui.Window(xbmcgui.getCurrentWindowId())

	return window.getProperty(prop)

# ============================================================
# FUNCTION: setRawWindowProperty
# ============================================================

def setRawWindowProperty(prop, data):
	window = xbmcgui.Window(xbmcgui.getCurrentWindowId())
	window.setProperty(prop, data)

# ============================================================
# Menu Entry Point
# ============================================================

if '/User_Interface' in PLUGIN_URL:

	User_Interface = ReorderFavourites('ReorderFavourites.xml', ADDON.getAddonInfo('path'), 'default', '1080i')

	try:
		result = User_Interface.doCustomModal(favouritesDataGen())
		setRawWindowProperty(FAVOURITES_RESULT, result)

	except Exception as e:
		Log(Log_Title + 'User_Interface > %s' % str(e), xbmc.LOGERROR)

		clearWindowProperty(FAVOURITES_RESULT)

	finally:
		del User_Interface


elif '/Exit_Only' in PLUGIN_URL:

	clearWindowProperty(FAVOURITES_RESULT)
	xbmc.executebuiltin('Action(Back)')

	Log(Log_Title + Favourites + '[COLOR %s][LIGHT]Finished (Exit Only)[/LIGHT][/COLOR]' % TEXT_DARK, xbmc.LOGINFO)


elif '/Save_Exit' in PLUGIN_URL:

	try:
		if favouritesSave(getRawWindowProperty(FAVOURITES_RESULT)):
			clearWindowProperty(FAVOURITES_RESULT)
			Dialogue.ok(Addon_Title, '[COLOR %s]Reorder Favourites: [LIGHT](Save + Exit)[/LIGHT][CR]Changes to favourites saved.[CR][COLOR %s]Exit and restart Kodi for the changes to take effect.[CR]Do not make further changes until Kodi is restarted.[/COLOR][/COLOR]' % (TEXT_GENERAL, TEXT_VALUE))
		xbmc.executebuiltin('Action(Back)')

	except Exception as e:
		Log(Log_Title + 'Save_Exit > %s' % str(e), xbmc.LOGERROR)		

	Log(Log_Title + Favourites + '[COLOR %s][LIGHT]Finished (Save + Exit)[/LIGHT][/COLOR]' % TEXT_DARK, xbmc.LOGINFO)


elif '/Save_Reload' in PLUGIN_URL:

	try:
		if not favouritesSave(getRawWindowProperty(FAVOURITES_RESULT)):
			xbmc.executebuiltin('Action(Back)')

		else:
			clearWindowProperty(FAVOURITES_RESULT)
			Dialogue.ok(Addon_Title, '[COLOR %s]Reorder Favourites: [LIGHT](Save + Reload)[/LIGHT][CR]Changes to favourites saved.[CR][COLOR %s]Kodi profile reloads (and changes to favourites).[CR]Do not make further changes until the profile reloads.[/COLOR][/COLOR]' % (TEXT_GENERAL, TEXT_VALUE))
			xbmc.executebuiltin('LoadProfile(%s)' % xbmc.getInfoLabel('System.ProfileName'))

	except Exception as e:
		Log(Log_Title + 'Save_Reload > %s' % str(e), xbmc.LOGERROR)

	Log(Log_Title + Favourites + '[COLOR %s][LIGHT]Finished (Save + Reload)[/LIGHT][/COLOR]' % TEXT_DARK, xbmc.LOGINFO)


elif '/User_Information' in PLUGIN_URL:

	User_Information()

	Log(Log_Title + Favourites + '[COLOR %s][LIGHT]User Information[/LIGHT][/COLOR]' % TEXT_DARK, xbmc.LOGINFO)


else:
	# Create the menu items.
	xbmcplugin.setContent(PLUGIN_ID, 'files')

	Equals = xbmcgui.ListItem('[COLOR %s]==================================================[/COLOR]' % TEXT_DIM)
	Equals.setArt({'fanart': ADDON_FANART, 'thumb': ADDON_FANART})

	User_Interface = xbmcgui.ListItem('[B]%s[/B]    U s e r   I n t e r f a c e  >' % Addon_Title)
	User_Interface.setArt({'fanart': REORDER, 'thumb': ADDON_ICON})

	Exit_Only = xbmcgui.ListItem('[COLOR %s]Exit Only  >  [/COLOR]no changes saved' % TEXT_GENERAL)
	Exit_Only.setArt({'fanart': REORDER, 'thumb': ADDON_ICON})

	Save_Exit = xbmcgui.ListItem('[COLOR %s]Save + Exit  >  [/COLOR]changes saved + exits  [COLOR %s](requires Kodi restart)[/COLOR]' % (TEXT_GENERAL, TEXT_DIM))
	Save_Exit.setArt({'fanart': REORDER, 'thumb': ADDON_ICON})

	Save_Reload = xbmcgui.ListItem('[COLOR %s]Save + Reload  >  [/COLOR]changes saved + reloads  [COLOR %s](may crash Kodi)[/COLOR]' % (TEXT_GENERAL, TEXT_DIM))
	Save_Reload.setArt({'fanart': REORDER, 'thumb': ADDON_ICON})

	User_Information = xbmcgui.ListItem('U s e r   I n f o r m a t i o n  >')
	User_Information.setArt({'fanart': REORDER, 'thumb': ADDON_ICON})

	Addon_Developer = xbmcgui.ListItem('[COLOR %s]Developer: [/COLOR]%s' % (TEXT_DIM, ADDON_DEVELOPER))
	Addon_Developer.setArt({'fanart': ADDON_FANART, 'thumb': ADDON_ICON})

	Addon_Name = xbmcgui.ListItem('[COLOR %s]Name: %s[/COLOR]' % (TEXT_DIM, ADDON_NAME))
	Addon_Name.setArt({'fanart': ADDON_FANART, 'thumb': ADDON_ICON})

	Addon_Version = xbmcgui.ListItem('[COLOR %s]Version: %s[/COLOR]' % (TEXT_DIM, ADDON_VERSION))
	Addon_Version.setArt({'fanart': ADDON_FANART, 'thumb': ADDON_ICON})

	Addon_ID = xbmcgui.ListItem('[COLOR %s]Addon ID: %s[/COLOR]' % (TEXT_DIM, ADDON_ID))
	Addon_ID.setArt({'fanart': ADDON_FANART, 'thumb': ADDON_ICON})

	# Append to PLUGIN_URL as it already ends with a slash.
	xbmcplugin.addDirectoryItems(
		PLUGIN_ID,
		(
			(PLUGIN_URL, Equals, False),
			(PLUGIN_URL + 'User_Interface', User_Interface, False),
			(PLUGIN_URL, Equals, False),
			(PLUGIN_URL + 'Exit_Only', Exit_Only, False),
			(PLUGIN_URL + 'Save_Exit', Save_Exit, False),
			(PLUGIN_URL + 'Save_Reload', Save_Reload, False),
			(PLUGIN_URL, Equals, False),
			(PLUGIN_URL + 'User_Information', User_Information, False),
			(PLUGIN_URL, Equals, False),
			(PLUGIN_URL, Addon_Developer, False),
			(PLUGIN_URL, Addon_Name, False),
			(PLUGIN_URL, Addon_Version, False),
			(PLUGIN_URL, Addon_ID, False)
		)
	)
	xbmcplugin.endOfDirectory(PLUGIN_ID)