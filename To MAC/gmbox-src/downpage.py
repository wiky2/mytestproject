#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gtk
import gtk.glade
import gmbox
import os
import thread
if os.name=='posix':
    import pynotify

(COL_STATUS,COL_NUM, COL_TITLE, COL_ARTIST,COL_DOWN) = range(5)
(COL_STATUS,COL_NUM, COL_TITLE, COL_ARTIST,COL_ALBUM) = range(5)

class DownTreeView(gmbox.DownloadLists):
    def __init__(self,xml):
        gmbox.DownloadLists.__init__(self)
        #依次存入：歌曲编号，歌曲名，歌手，下载状态，下载进度
        self.model=gtk.ListStore(bool,str,str,str,str)
        self.treeview = xml.get_widget("download_treeview")
        self.treeview.set_model(self.model)
        self.treeview.set_enable_search(0)
        self.treeview.get_selection().set_mode(gtk.SELECTION_SINGLE)

        checkbutton = gtk.CheckButton()
        renderer = gtk.CellRendererToggle()
        renderer.connect('toggled', self.fixed_toggled)
        #column = gtk.TreeViewColumn("选中", renderer,active=COL_STATUS)
        #column = gtk.TreeViewColumn("选中", renderer,text=COL_STATUS)
        column = gtk.TreeViewColumn("选中", renderer)
        column.set_resizable(True)
        self.treeview.append_column(column)
        
        renderer = gtk.CellRendererText()
        renderer.set_data("column", COL_NUM)
        column = gtk.TreeViewColumn("编号", renderer, text=COL_NUM)
        column.set_resizable(True)
        self.treeview.append_column(column)
        
        renderer = gtk.CellRendererText()
        renderer.set_data("column", COL_TITLE)
        column = gtk.TreeViewColumn("歌曲", renderer, text=COL_TITLE)
        column.set_resizable(True)
        self.treeview.append_column(column)

        renderer = gtk.CellRendererText()
        renderer.set_data("column", COL_ARTIST)
        column = gtk.TreeViewColumn("歌手", renderer, text=COL_ARTIST)
        column.set_resizable(True)
        self.treeview.append_column(column)

        renderer = gtk.CellRendererText()
        renderer.set_data("column", COL_DOWN)
        column = gtk.TreeViewColumn("状态", renderer, text=COL_DOWN)
        column.set_resizable(True)
        self.treeview.append_column(column)
        self.treeview.set_rules_hint(True)

    def add(self,title,artist,id):
        thread.start_new_thread(gmbox.DownloadLists.add, (self,title,artist,id,))
        num = len(self.songlist)
        self.model.append([False,num,title,artist,"start"])

        if os.name=='posix':
            self.notification = pynotify.Notification("下载", title, "dialog-warning")
        self.notification.set_timeout(1)
        self.notification.show()
        print 'being to download'

    def fixed_toggled(self, cell, path):
        # get toggled iter
        iter = self.model.get_iter((int(path),))
        fixed = self.model.get_value(iter, COL_STATUS)
        print "fixed is ",fixed

        # do something with the value
        fixed = not fixed

        print "now fixed is ",fixed

        if not fixed:
            print 'Select[row]:',path
        else:
            print 'Invert Select[row]:',path

        # set new value
        self.model.set(iter, COL_STATUS, fixed)        
