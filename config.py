### ############################################################################################################
###	#	
### # Project: 			#		Config.py - by The Highway 2013.
### # Author: 			#		The Highway
### # Version:			#		(ever changing)
### # Description: 	#		My Project Config File
###	#	
### ############################################################################################################
### ############################################################################################################
### Imports ###
import xbmc,xbmcplugin,xbmcgui,xbmcaddon,xbmcvfs
import re,os,sys,string,StringIO,logging,random,array,time,datetime
from t0mm0.common.addon import Addon

### ############################################################################################################
### ############################################################################################################
### ############################################################################################################
### Plugin Settings ###
def ps(x):
	return {
		'__plugin__': 					"TheFunkStation.com"
		,'__authors__': 				"[COLOR white]The[COLOR tan]Highway[/COLOR][/COLOR]"
		,'__credits__': 				"TheHighway of plugin.video.theanimehighway for teh_tools.py, anilkuj of plugin.video.soloremovie (solarmovie.eu) for much initial work.  Mikey1234 of SimplyMovies.  Bstrdsmkr of 1 Channel.  Those that worked on UrlResolver.  Those of #XBMCHUB on irc.freenode.net.  And of course,  XBMCHub.com itself."
		,'_addon_id': 					"plugin.audio.thefunkstation"
		,'_plugin_id': 					"plugin.audio.thefunkstation"
		,'_domain_url': 				"http://listento.thefunkstation.com:8000/"
		,'_image_url': 					"%s"
		,'_button_url':					"http://listento.thefunkstation.com/funkradio/templates/funkstation2/images/header.jpg"
		,'_button2_url':				"http://listento.thefunkstation.com/funkradio/templates/funkstation2/images/Bottom_texture.jpg"
		,'_fanart_url': 				"http://listento.thefunkstation.com/funkradio/templates/funkstation2/images/header.jpg"
		,'_settings_url': 			"http://listento.thefunkstation.com/funkradio/templates/funkstation2/images/Bottom_texture.jpg"
		,'_play_url': 					"%s"
		,'_category_url':				'%s'
		,'_database_name': 			"thefunkstation"
		,'_addon_path_art': 		"art"
		,'art_sun':							'http://ramfm.org/images/Computer-icon.png'
		,'art_dead':						'http://ramfm.org/images/Computer-icon.png'
		,'art_youtube':					''
		,'special.home.addons': 'special:'+os.sep+os.sep+'home'+os.sep+'addons'+os.sep
		,'special.home': 				'special:'+os.sep+os.sep+'home'
		,'GENRES': 							['','','']
		,'YEARS': 							['','','']
		,'YEARSo': 							['','','']
		,'GENRESo': 						['','','']
		,'COUNTRIES': 					['','','']
		,'RATINGS':							['','','']
		,'SCORES':							['','','']
		,'default_art_ext': 		'.png'
		,'default_cFL_color': 	'lime'
		,'cFL_color': 					'lime'
		,'cFL_color2': 					'blue'
		,'cFL_color3': 					'red'
		,'cFL_color4': 					'grey'
		,'cFL_color5': 					'white'
		,'cFL_color6': 					'blanchedalmond'
		,'default_section': 		'movies'
		,'section.wallpaper':		'wallpapers'
		,'section.movie': 			'movies'
		,'section.trailers':		'trailers'
		,'section.users':				'users'
		,'section.tv': 					'tv'
		,'domain.search.movie': ''
		,'domain.search.tv': 		''
		,'domain.url.tv': 			'/tv'
		,'domain.url.movie': 		''
		,'LatestThreads.url':		''
		,'changelog.local': 		'changelog.txt'
		,'changelog.url': 			''
		,'news.url': 						''
		,'domain.thumbnail.default': 			''
		,'rating.max': 										'10'
		,'cMI.favorites.tv.add.url': 			'XBMC.RunPlugin(%s?mode=%s&section=%s&title=%s&year=%s&img=%s&fanart=%s&country=%s&plot=%s&genre=%s&url=%s&dbid=%s&subfav=%s)'
		,'cMI.favorites.tv.add.name': 		'Add Favorite'
		,'cMI.favorites.tv.add.mode': 		'FavoritesAdd'
		,'cMI.favorites.movie.add.url': 	'XBMC.RunPlugin(%s?mode=%s&section=%s&title=%s&year=%s&img=%s&fanart=%s&country=%s&plot=%s&genre=%s&url=%s&subfav=%s)'
		,'cMI.favorites.tv.remove.url': 	'XBMC.RunPlugin(%s?mode=%s&section=%s&title=%s&year=%s&img=%s&fanart=%s&country=%s&plot=%s&genre=%s&url=%s&dbid=%s&subfav=%s)'
		,'cMI.favorites.tv.remove.name': 	'Remove Favorite'
		,'cMI.favorites.tv.remove.mode': 	'FavoritesRemove'
		,'cMI.favorites.movie.remove.url': 'XBMC.RunPlugin(%s?mode=%s&section=%s&title=%s&year=%s&img=%s&fanart=%s&country=%s&plot=%s&genre=%s&url=%s&subfav=%s)'
		,'cMI.airdates.find.name': 				'Find AirDates'
		,'cMI.airdates.find.url': 				'XBMC.RunPlugin(%s?mode=%s&title=%s)'
		,'cMI.airdates.find.mode': 				'SearchForAirDates'
		,'cMI.showinfo.name': 						'Show Information'
		,'cMI.showinfo.url': 							'XBMC.Action(Info)'
		,'cMI.jDownloader.addlink.url':		'XBMC.RunPlugin(plugin://plugin.program.jdownloader/?action=addlink&url=%s)'
		,'LI.nextpage.name': 							''
		,'LI.nextpage.match': 						''
		,'LI.nextpage.check': 						''
		,'LI.page.param': 								''
		,'LI.page.find': 									''
		,'Hosters.icon.url': 							'http://www.google.com/s2/favicons?domain='
		,'LLinks.compile.hosters': 				''
		,'LLinks.compile.hosters2': 			''
		,'AdvSearch.menu.0': 		'0.) Do Search >>'
		,'AdvSearch.menu.1': 		'1.) Title       '
		,'AdvSearch.menu.2': 		'2.) Description '
		,'AdvSearch.menu.3': 		'3.) Actor       '
		,'AdvSearch.menu.4': 		'4.) Country[N/A]'
		,'AdvSearch.menu.5': 		'5.) Year (From) '
		,'AdvSearch.menu.6': 		'6.) Year (To)   '
		,'AdvSearch.menu.7': 		'7.) Genre  [N/A]'
		,'AdvSearch.menu.8': 		'8.) Cancel      '
		,'AdvSearch.url.tv': 		''
		,'AdvSearch.url.movie': ''
		,'AdvSearch.tags.0': 		'is_series'
		,'AdvSearch.tags.1': 		'title'
		,'AdvSearch.tags.2': 		'actor'
		,'AdvSearch.tags.3': 		'description'
		,'AdvSearch.tags.4': 		'country'
		,'AdvSearch.tags.5': 		'year_from'
		,'AdvSearch.tags.6': 		'year_to'
		,'AdvSearch.tags.7': 		'genre'
		,'AdvSearch.tags.8': 		''
##		,'LLinks.compile.': 							
#		,'': 		''
#		,'': 
#		,'': 
	}[x]
_art_DefaultExt  ='.png'
_cFL_DefaultColor='goldenrod'


### ############################################################################################################
### ############################################################################################################
### ############################################################################################################
### For Multiple Methods ###

### ############################################################################################################
### ############################################################################################################
### ############################################################################################################
### Other Settings ###
GENRES = ['','','']
COUNTRIES = ['','','']

### ############################################################################################################
### ############################################################################################################
### ############################################################################################################
### Configurable Functions ###

### ############################################################################################################
