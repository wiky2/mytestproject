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
import logging
import webbrowser

from player import playbox
from treeview import ListView,SearchView,AlbumListView,AlbumSearchView
from lib.const import *
from lib.config import *
from lib.core import gmbox

log = logging.getLogger('gmbox.tabview')

class Tabview(gtk.Notebook):
    def __init__(self):
        gtk.Notebook.__init__(self)
        
        self.set_show_tabs(False)

        self.setup_lists_tab()
        self.setup_search_tab()
        self.setup_album_lists_tab()
        self.setup_album_search_tab()
        self.setup_down_tab()
        self.setup_playlist_tab()
        self.setup_config_tab()
        self.setup_about_tab()
        self.show_all()
        self.connect('switch-page',self.page_changed)
        self.re_fun={} #用于缓存tab切换的时候的函数
# =========================================
# methods setup these tabs
        
    def setup_lists_tab(self):
        
        self.list_view = ListView()
        hb = gtk.HBox(False, 0)
        
        self.combox = gtk.combo_box_new_text()
        self.combox.append_text("--请选择--")
        [self.combox.append_text(slist) for slist in songlists]
        self.combox.set_active(0)
        self.combox.connect("changed", self.do_getlist)
        
        self.but_down_select = gtk.Button('下载选中的音乐')
        self.but_down_select.connect('clicked',lambda w:self.list_view.down_select())
        self.but_adition_select = gtk.Button('试听选中的音乐')
        self.but_adition_select.set_sensitive(False)
        o_select_all = gtk.CheckButton(u'全选')
        o_select_all.connect('toggled', self.do_select_all, self.list_view)
        hb.pack_start(gtk.Label(u'榜单下载: '), False, False)
        hb.pack_start(self.combox, False, False)
        hb.pack_start(self.but_down_select, False, False)
        hb.pack_start(self.but_adition_select, False, False)
        hb.pack_end(o_select_all, False)

        scroll = gtk.ScrolledWindow()
        scroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        scroll.add(self.list_view)

        vb = gtk.VBox(False, 0)
        vb.pack_start(hb, False, False)
        vb.pack_start(scroll, True, True)

        self.append_page(vb)

    def setup_search_tab(self):
        
        self.search_view = SearchView()
        hb = gtk.HBox(False, 0)
        self.search_entry = gtk.Entry()
        self.search_entry.connect('activate',lambda w:self.do_search(self.search_ok))
        self.search_ok = gtk.Button("搜索")
        self.search_ok.connect('clicked', self.do_search)
        self.but_down_select = gtk.Button('下载所选')
        self.but_down_select.connect('clicked',lambda w:self.search_view.down_select())
        o_select_all = gtk.CheckButton(u'全选')
        o_select_all.connect('toggled', self.do_select_all, self.search_view)
        hb.pack_start(gtk.Label(u'音乐搜索: '), False, False)
        hb.pack_start(self.search_entry)
        hb.pack_start(self.search_ok, False)
        hb.pack_start(self.but_down_select, False)
        hb.pack_end(o_select_all, False)

        scroll = gtk.ScrolledWindow()
        scroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        scroll.add(self.search_view)
        
        vb = gtk.VBox(False, 0)
        vb.pack_start(hb, False, False)
        vb.pack_start(scroll, True, True)

        self.append_page(vb)
        #page 2: search page
        
        #self.search_entry = self.xml.get_widget('search_entry')
        #self.search_entry.connect('key_press_event', self.entry_key_checker)
        #self.search_button = self.xml.get_widget('search_button')

        #self.search_list_view= SearchListView(self.xml)
        #self.search_list_view.treeview.connect('button-press-event', self.click_checker)
        #self.search_list_view.treeview.connect('key_press_event', self.tree_view_key_checker)

    def setup_album_lists_tab(self):
        
        self.album_list_view = AlbumListView()
        hb = gtk.HBox(False, 0)
        
        self.album_combox = gtk.combo_box_new_text()
        self.album_combox.append_text("--请选择--")
        [self.album_combox.append_text(slist) for slist in albums_lists]
        self.album_combox.set_active(0)
        self.album_combox.connect("changed", self.do_getalbumlist)
        
        self.but_down_select = gtk.Button('下载选中的音乐')
        self.but_down_select.connect('clicked',lambda w:self.album_list_view.down_select())
        self.but_adition_select = gtk.Button('试听选中的音乐')
        self.but_adition_select.set_sensitive(False)
        o_select_all = gtk.CheckButton(u'全选')
        o_select_all.connect('toggled', self.do_select_all, self.album_list_view)
        hb.pack_start(gtk.Label(u'专辑榜单: '), False, False)
        hb.pack_start(self.album_combox, False, False)
        hb.pack_start(self.but_down_select, False, False)
        hb.pack_start(self.but_adition_select, False, False)
        hb.pack_end(o_select_all, False)

        scroll = gtk.ScrolledWindow()
        scroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        scroll.add(self.album_list_view)

        vb = gtk.VBox(False, 0)
        vb.pack_start(hb, False, False)
        vb.pack_start(scroll, True, True)

        self.append_page(vb)

    def setup_album_search_tab(self):
        
        self.album_search_view = AlbumSearchView()
        hb = gtk.HBox(False, 0)
        self.album_search_entry = gtk.Entry()
        self.album_search_entry.connect('activate',lambda w:self.do_album_search(self.album_search_ok))
        self.album_search_ok = gtk.Button("搜索")
        self.album_search_ok.connect('clicked', self.do_album_search)
        self.but_down_select = gtk.Button('下载所选')
        self.but_down_select.connect('clicked',lambda w:self.album_search_view.down_select())
        o_select_all = gtk.CheckButton(u'全选')
        o_select_all.connect('toggled', self.do_select_all, self.album_search_view)
        hb.pack_start(gtk.Label(u'专辑搜索: '), False, False)
        hb.pack_start(self.album_search_entry)
        hb.pack_start(self.album_search_ok, False)
        hb.pack_start(self.but_down_select, False)
        hb.pack_end(o_select_all, False)

        scroll = gtk.ScrolledWindow()
        scroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        scroll.add(self.album_search_view)
        
        vb = gtk.VBox(False, 0)
        vb.pack_start(hb, False, False)
        vb.pack_start(scroll, True, True)

        self.append_page(vb)

    def setup_down_tab(self):

        scroll = gtk.ScrolledWindow()
        scroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        tmp_label=gtk.Label('coming soon ...')
        tmp_label.set_use_markup(True)

        vb = gtk.VBox(False, 0)
        vb.pack_start(tmp_label, True, True)

        self.append_page(vb)

        #page 3:  downlist page
        #self.down_tree = downpage.DownTreeView(self.xml)
        #self.down_tree = DownTreeView(self.xml)
        #self.file_list_view = FileListView(self.xml,gmbox.musicdir)
        #button = self.xml.get_widget('filelist_button')
        #button.connect('clicked',self.dolistLocalFile,)

        
    def setup_playlist_tab(self):

        self.player = playbox()

        scroll = gtk.ScrolledWindow()
        scroll.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        tmp_label=gtk.Label('coming soon ...')

        vb = gtk.VBox(False, 0)
        vb.pack_start(tmp_label, True, True)
        vb.pack_start(self.player, False)

        self.append_page(vb)

        #page 4: playlist page
        #self.playlist_view= PlayListView(self.xml)
        #self.playlist_view.treeview.connect('button-press-event',self.playlist_click_checker)
        #self.playlist_view.treeview.connect('key_press_event',self.tree_view_key_checker)

    def setup_config_tab(self):
        t=gtk.Table(8,2)
        #tmp_label=gtk.Label(u'\n注: 以下内容还未生效 ...\n')
        tmp_label=gtk.Label('\n设置\n')
        tmp_label.set_use_markup(True)
        t.attach(tmp_label,0,2,0,1,gtk.SHRINK,gtk.SHRINK)
    
        hb_savedir = gtk.HBox(False, 0)
        options_savedir = gtk.Entry()
        options_savedir.set_text(config.item['savedir'])
        options_savedir.set_sensitive(False)
        bt_savedir = gtk.Button('浏览...')
        bt_savedir.connect('clicked',self.config_savedir,options_savedir)

        hb_savedir.pack_start(options_savedir, True, True)
        hb_savedir.pack_start(bt_savedir, False, False)
        
        t.attach(gtk.Label(u'    歌曲下载目录:  '),0,1,1,2,gtk.SHRINK,gtk.SHRINK)
        t.attach(hb_savedir,1,2,1,2,yoptions=gtk.SHRINK)

        options_id3utf8 = gtk.CheckButton(u'将ID3信息转换为UTF8,(windows用户无效)')
        options_id3utf8.set_active(config.item['id3utf8'])
        options_id3utf8.connect('toggled', self.config_id3utf8)
        t.attach(gtk.Label(u''),0,1,2,3,gtk.SHRINK,gtk.SHRINK)
        t.attach(options_id3utf8,1,2,2,3,yoptions=gtk.SHRINK)

        options_makeartistdir = gtk.CheckButton(u'下载时建立歌手目录')
        options_makeartistdir.set_active(config.item['makeartistdir'])
        options_makeartistdir.connect('toggled', self.config_makeartistdir)
        t.attach(gtk.Label(u''),0,1,3,4,gtk.SHRINK,gtk.SHRINK)
        t.attach(options_makeartistdir,1,2,3,4,yoptions=gtk.SHRINK)

        options_makealbumdir = gtk.CheckButton(u'下载专辑时下载到各自的目录')
        options_makealbumdir.set_active(config.item['makealbumdir'])
        options_makealbumdir.connect('toggled', self.config_makealbumdir)
        t.attach(gtk.Label(u''),0,1,4,5,gtk.SHRINK,gtk.SHRINK)
        t.attach(options_makealbumdir,1,2,4,5,yoptions=gtk.SHRINK)

        options_addalbumnum = gtk.CheckButton(u'在歌名前放置目录序号')
        options_addalbumnum.set_active(config.item['addalbumnum'])
        options_addalbumnum.connect('toggled', self.config_addalbumnum)
        t.attach(gtk.Label(u''),0,1,5,6,gtk.SHRINK,gtk.SHRINK)
        t.attach(options_addalbumnum,1,2,5,6,yoptions=gtk.SHRINK)

        options_localdir = gtk.Entry()
        options_localdir.set_text('此功能尚未实现.')
        options_localdir.set_sensitive(False)
        t.attach(gtk.Label(u'本地歌曲目录:'),0,1,6,7,gtk.SHRINK,gtk.SHRINK)
        t.attach(options_localdir,1,2,6,7,yoptions=gtk.SHRINK)

        self.previewLabel = gtk.Label()
        t.attach(gtk.Label(u'文件名预览:'),0,1,7,8,gtk.SHRINK,gtk.SHRINK)
        t.attach(self.previewLabel,1,2,7,8,yoptions=gtk.SHRINK)
        self.refresh_pre()

        self.append_page(t)
        
    def setup_about_tab(self):
        vb = gtk.VBox()
        about_label=gtk.Label('<span size="xx-large" weight="ultrabold">'
            +'gmbox V'+VERSION+'</span>')
        about_label.set_use_markup(True)
        bt_home = gtk.Button(u'项目主页')
        bt_home.connect('clicked',lambda w: webbrowser.open('http://code.google.com/p/gmbox/'))
        bt_blog = gtk.Button(u' 博客 ')
        bt_blog.connect('clicked',lambda w: webbrowser.open('http://li2z.cn/category/gmbox/?from=gmbox'))
        hb = gtk.HBox()
        hb.pack_start(bt_home)
        hb.pack_start(bt_blog)
        vb.pack_start(about_label)
        vb.pack_start(hb,False,False)
        self.append_page(vb)
        
# signal methods =======================

    def config_savedir(self,widget,entry):
        dialog = gtk.FileChooserDialog("Open..",
               None,
               gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER,
               (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK) 
        response = dialog.run()
        if response == gtk.RESPONSE_OK:
            config.savedir_changed(dialog.get_filename())
            entry.set_text(dialog.get_filename())
        elif response == gtk.RESPONSE_CANCEL:
            print '取消'
        dialog.destroy()
        
    def config_id3utf8(self,widget):
        config.id3utf8_changed(widget.get_active())

    def refresh_pre(self):
        v=u'歌曲下载路径：'+gmbox.setup_file_info(u'歌名',u'歌手',False,u'专辑名',u'专辑歌手',1)[0] \
            +'\n'+u'专辑下载路径：'+gmbox.setup_file_info(u'歌名',u'歌手',True,u'专辑名',u'专辑歌手',1)[0]
        self.previewLabel.set_text(v)
    
    def config_makealbumdir(self,widget):
        config.makealbumdir_changed(widget.get_active())
        self.refresh_pre()

    def config_makeartistdir(self,widget):
        config.makeartistdir_changed(widget.get_active())
        self.refresh_pre()

    def config_addalbumnum(self,widget):
        config.addalbumnum_changed(widget.get_active())
        self.refresh_pre()

    def do_select_all(self,widget,view):
        view.select_all(widget.get_active())

    def do_getlist(self, widget):
        '''Begin song(album) list download thread'''
        
        text=widget.get_active_text().decode('utf8')
        if text != "--请选择--":
            # get_list thread will set_sensitive true if download done
            widget.set_sensitive(False)
            self.list_view.get_list(text, widget)
        #保存一个恢复用的函数,在切到其他tab再切回来的时候调用
        self.re_fun[0]=lambda:self.list_view.get_list(text, widget)
    def do_getalbumlist(self, widget):
        '''Begin song(album) list download thread'''
        
        text=widget.get_active_text().decode('utf8')
        if text != "--请选择--":
            # get_list thread will set_sensitive true if download done
            widget.set_sensitive(False)
            self.album_list_view.get_albumlist(text, widget)
        self.re_fun[2]=lambda:self.album_list_view.get_albumlist(text, widget)
    def do_search(self, widget):
        text=self.search_entry.get_text()
        widget.set_sensitive(False)
        self.search_view.search(text, widget)
        self.re_fun[1]=lambda:self.search_view.search(text, widget)
    def do_album_search(self, widget):
        text=self.album_search_entry.get_text()
        widget.set_sensitive(False)
        self.album_search_view.search(text, widget)
        self.re_fun[3]=lambda:self.album_search_view.search(text, widget)
    def page_changed(self, notebook, page, page_num):
        log.debug('tab changed to: '+str(page_num))
        #切换tab的时候,再调用一次,相当于和gmbox类的当前列表同步
        if page_num in self.re_fun:
            self.re_fun[page_num]()
    """def doSearchMusic(self,widget):
        '''music search button clicked callback'''
        
        key = self.search_entry.get_text().decode('utf8')
        print key
        self.search_button.set_sensitive(False)
        thread.start_new_thread(self.SearchMusic,(key,))

    def dolistLocalFile(self,widget):
        '''callback for download manage tab'''
        
        print "while start thread"
        thread.start_new_thread(self.listLocalFile,(widget,))
        print "OK"
    
    def SetupPopup2(self):
        '''popup menu for playlist tab'''
        
        time = gtk.get_current_event_time()

        popupmenu = gtk.Menu()

        menuitem = gtk.MenuItem('试听')
        menuitem.connect('activate', self.listen_init)
        popupmenu.append(menuitem)
        
        menuitem = gtk.MenuItem('从列表删除')
        menuitem.connect('activate', self.DelFromPlaylist)
        popupmenu.append(menuitem)
        
        popupmenu.show_all()
        popupmenu.popup(None, None, None, 0, time)


    def playlist_click_checker(self, view, event):
        self.get_current_location(view,event)

        if event.type == gtk.gdk._2BUTTON_PRESS:
            self.listen(view)

        if event.type == gtk.gdk.BUTTON_PRESS and event.button == 3:
            #selected,iter = view.get_selection().get_selected()
            #index = selected.get_value(iter, 0)
            #print index

            # Here test whether we have songlist, if have, show popup menu
            try:
                self.SetupPopup2()
            except:
                pass
"""
