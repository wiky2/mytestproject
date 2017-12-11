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

import pygtk,sys
if not sys.platform == 'win32':
    pygtk.require('2.0')
import gtk
import os
from optparse import OptionParser
import logging
import gobject

from lib.utils import find_image_or_data,module_path #从lib目录下utils文件中导入所有函数，类
from tabview import * #从文件中导入所有函数，类
from statusbar import *#从文件中导入所有函数，类

if os.name == 'posix':
    import pynotify

log = logging.getLogger('gmbox')

class Mainwin(gtk.Window):#继承
    def __init__(self):
        
        gtk.Window.__init__(self, gtk.WINDOW_TOPLEVEL)

        log = logging.getLogger('gmbox.mainwin')
        
        self.set_title("GMBox")
        self.set_default_size(800, 600)
        # need work
        ui_logo=gtk.gdk.pixbuf_new_from_file(find_image_or_data('gmbox.png',module_path()))
        self.set_icon(ui_logo)

        log.debug('Setup up system tray icon')
        self.setupSystray()


        self.connect('destroy', gtk.main_quit)
        #self.window.connect('key_press_event', self.key_checker)
        
        self.but_index=0
        vb = gtk.VBox(False, 0)
        log.debug('Begin to setup notebook')
        self.gm_notebook = Tabview()
        self.status = statusbar
        self.but_box = self.setup_but_box()
        vb.pack_start(self.but_box, False, False, 5)
        vb.pack_start(self.gm_notebook, True, True)
        vb.pack_start(self.status, False, False)

        self.add(vb)
        log.debug('End to setup notebook')
        self.show_all()

        
    def setupSystray(self):
        
        self.systray = gtk.StatusIcon()
        # need write a find picture method
        self.systray.set_from_file(find_image_or_data('gmbox.png',module_path()))
        self.systray.connect("activate", self.systrayCb)
        self.systray.connect('popup-menu', self.systrayPopup)
        self.systray.set_tooltip("Click to toggle window visibility")
        self.systray.set_visible(True)

        if os.name == 'posix':
            pynotify.init("Some Application or Title")
            self.notification = pynotify.Notification("Title", "body", "dialog-warning")
            self.notification.set_urgency(pynotify.URGENCY_NORMAL)
            self.notification.set_timeout(1)
        return

    def systrayCb(self, widget):
        """Check out window's status"""
        
        if self.get_property('visible'):
            self.hide()
        else:
            self.show()
            #self.deiconify()
            #self.present()

    def systrayPopup(self, statusicon, button, activate_time):
        """Create and show popup menu"""
        
        popup_menu = gtk.Menu()
        restore_item = gtk.MenuItem("Restore")
        restore_item.connect("activate", self.systrayCb)
        popup_menu.append(restore_item)

        #prev_item = gtk.MenuItem("Previous")
        #prev_item.connect("activate", self.tray_play_prev)
        #popup_menu.append(prev_item)

        #next_item = gtk.MenuItem("Next")
        #next_item.connect("activate", self.tray_play_next)
        #popup_menu.append(next_item)

        quit_item = gtk.ImageMenuItem(gtk.STOCK_QUIT)
        quit_item.connect("activate", gtk.main_quit)
        popup_menu.append(quit_item)

        popup_menu.show_all()
        time = gtk.get_current_event_time()
        popup_menu.popup(None, None, None, 0, time)

    def setup_but_box_one(self,but_box,but_name):
        but_x = gtk.Button(but_name)
        but_x.connect('clicked',lambda o,x:self.gm_notebook.set_current_page(x),self.but_index)
        self.but_index+=1
        but_box.pack_start(but_x)
        
    def setup_but_box(self):
        but_box = gtk.HButtonBox()
        tabs=[u'榜单下载',u'音乐搜索',u'专辑榜单',u'专辑搜索',u'下载管理',u'播放列表',u'设置',u'关于']
        [self.setup_but_box_one(but_box,i) for i in tabs]
        return but_box

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-d', '--debug',  action='store_true', dest='debug')

    (options, args) = parser.parse_args()

    if options.debug:
        logging.basicConfig(level=logging.DEBUG)

    gobject.threads_init()
    Mainwin()
    gtk.main()
    
