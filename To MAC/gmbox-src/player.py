#!/usr/bin/env python
# -*- coding: utf-8 -*-

# gmbox, Google music box.
# Copyright (C) 2009, gmbox team
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gtk

class playbox(gtk.HBox):
    '''embedded to play list tab for audition songs'''
    
    def __init__(self):
        gtk.HBox.__init__(self)

        # need more work: change interface label to china
        self.but_prev = gtk.Button(label="前一首",
                                   stock=gtk.STOCK_MEDIA_PREVIOUS)
        self.but_next = gtk.Button(label="后一首",
                                   stock=gtk.STOCK_MEDIA_NEXT)
        self.but_play = gtk.Button(label="播放",
                                   stock=gtk.STOCK_MEDIA_PLAY)
        self.but_pause = gtk.Button(label="暂停",
                                    stock=gtk.STOCK_MEDIA_PAUSE)

        self.pack_start(self.but_prev, False)
        self.pack_start(self.but_play, False)
        self.pack_start(self.but_pause, False)
        self.pack_start(self.but_next, False)
        
    def play(self,start):
        '''试听,播放'''
        if os.name=='posix':
            self.notification = pynotify.Notification("试听", self.current_list.get_title(start), "dialog-warning")
            self.notification.set_timeout(1)
            self.notification.show()
        self.playbar.set_text("now playing " + self.current_list.get_title(start))
        print "now playing ",self.current_list.get_title(start)
        self.current_list.play(start)
        #self.current_list.autoplay(start)

    def listen_init(self, widget):
        self.current_list=self.playlist
        self.current_path=self.path[0]
        self.listen(widget)

    def focus_next(self,widget):
        self.current_path= self.current_path + 1
        widget.set_cursor(self.current_path)
        if DEBUG:
            print "now focus",self.current_path
    def focus_prev(self,widget):
        self.current_path= self.current_path - 1
        widget.set_cursor(self.current_path)
        if DEBUG:
            print "now focus",self.current_path

    def play_next(self,widget):
        #widget.focus_next(widget)
        self.focus_next(widget)
        self.listen(widget)
        if DEBUG:
            print "now playing",self.current_path
    def play_prev(self,widget):
        #widget.focus_prev(widget)
        self.focus_prev(widget)
        self.listen(widget)
        if DEBUG:
            print "now playing",self.current_path
