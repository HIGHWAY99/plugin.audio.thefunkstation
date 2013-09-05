#
#      Copyright (C) 2013
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with XBMC; see the file COPYING.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#
#  The code was originally supplied as part of the XBMC Last.FM - SlideShow
#  by divingmule (script.image.lastfm.slideshow), and modified under the 
#  GNU General Public License to work better with the audio streams from
#  Ram FM Eighties Hit Radio (http://www.ramfm.org)

import urllib
import urllib2
import os
import xbmcaddon
from BeautifulSoup import BeautifulStoneSoup
try:
    import json
except:
    import simplejson as json

#__settings__ = xbmcaddon.Addon(id='script.image.lastfm.slideshow')
__settings__ = xbmcaddon.Addon(id='plugin.audio.ramfm')
__language__ = __settings__.getLocalizedString
home = __settings__.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ) )


def slideshow():
        if xbmc.Player().isPlayingAudio():
            p_name = get_name()
            start_slideshow(p_name)
            while True:
                p_name == get_name()
                xbmc.sleep(2000)
                if not p_name == get_name():
                    break
            slideshow()
        else:
            xbmc.executebuiltin("XBMC.Notification("+__language__(30000)+","+__language__(30001)+",5000,"+icon+")")
            clear_slideshow()
            return


def get_name():
        try:
            name = xbmc.Player().getMusicInfoTag().getArtist()
        except:
            xbmc.sleep(1000)
            try:
                name = xbmc.Player().getMusicInfoTag().getArtist()
            except:
                return
        if len(name) < 1:
            name = xbmc.Player().getMusicInfoTag().getTitle().split(' - ')[0]
        return name


def clear_slideshow():
        get_players = json.loads(xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "Player.GetActivePlayers", "id": 1}'))
        for i in get_players['result']:
            if i['type'] == 'picture':
                stop_slideshow = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "Player.Stop", "params": {"playerid":%i}, "id": 1}' % i['playerid'])
            else: continue
        clear_playlist = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "Playlist.Clear", "params": {"playlistid":2}, "id": 1}')

        return []


def add_playlist(images):
        items =[]
        for image in images:
            if __settings__.getSetting('limit_size')=="true":
                if int(image.size['height']) >= int(__settings__.getSetting('min_height')):
                    item = '{ "jsonrpc": "2.0", "method": "Playlist.Add", "params": { "playlistid": 2 , "item": {"file": "%s"} }, "id": 1 }' %image.size.string
                    add_item = items.append(item.encode('ascii'))
                else:
                    print '--- image skipped, not minimum height %s  --- ' %image.size['height']
            else:
                item = '{ "jsonrpc": "2.0", "method": "Playlist.Add", "params": { "playlistid": 2 , "item": {"file": "%s"} }, "id": 1 }' %image.size.string
                add_item = items.append(item.encode('ascii'))
        print 'Adding - %s images' %str(len(items))
        if len(items) > 0:
            add_playlist = xbmc.executeJSONRPC(str(items).replace("'",""))


def get_images(name, u_name, notify):
    if notify:
        xbmc.executebuiltin("XBMC.Notification("+__language__(30000)+","+__language__(30004)+name.replace(',', '')+",5000,"+icon+")")
    url    = 'http://ws.audioscrobbler.com/2.0/?method=artist.getimages&artist='+u_name+'&autocorrect=1&api_key=1dda8497b435d2597823613e480fc860'
    print 'URL requested: %s' % url
    try:
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        link = response.read()
        response.close()
    except urllib2.URLError, e:
        print 'We failed to open "%s".' % url
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
        if hasattr(e, 'code'):
            print 'We failed with error code - %s.' % e.code
        xbmc.executebuiltin("XBMC.Notification("+__language__(30000)+","+__language__(30003)+",10000,"+icon+")")
        return clear_slideshow()
    soup = BeautifulStoneSoup(link)
    images = soup('image')
    print 'Images = '+ str(len(images))
    return images


def start_slideshow(name):
        print "Starting Slideshow - %s" % name

        u_name = name.upper().replace(' & ',' ').replace(',','').replace('(','').replace(' ) ','').replace(' ','+')

        if u_name != "THE+THE" and u_name != "THE":
            u_name = u_name.replace('THE', '')

        images  = []
        images += get_images(name, u_name, True)        

        split = u_name.split('+')
        if len(split) > 1:
            images += get_images(name, split[1] + '+' + split[0], False)
            
        if len(images) > 0:
            clear_slideshow()
            if len(images) > 5:
                add_playlist(images[:5])
            else:
                add_playlist(images)
            get_playlist = json.loads(xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "Playlist.GetItems", "params": {"playlistid":2}, "id": 1}'))
            if get_playlist['result']['limits']['total'] > 1:
                play = xbmc.executeJSONRPC('{ "jsonrpc": "2.0", "method": "Player.Open","params":{"item":{"playlistid":2}} }')
            if len(images) > 5:
                add_playlist(images[5:])
            get_playlist = json.loads(xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "Playlist.GetItems", "params": {"playlistid":2}, "id": 1}'))
            if get_playlist['result']['limits']['total'] > 0:
                get_players = json.loads(xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "Player.GetActivePlayers", "id": 1}'))
                pic_player = False
                for i in get_players['result']:
                    if i['type'] == 'picture':
                        pic_player = True
                    else: continue
                if not pic_player:
                    play = xbmc.executeJSONRPC('{ "jsonrpc": "2.0", "method": "Player.Open","params":{"item":{"playlistid":2}} }')
        else:
            xbmc.executebuiltin("XBMC.Notification("+__language__(30000)+","+__language__(30002)+name+",5000,"+icon+")")
            clear_slideshow()

slideshow()