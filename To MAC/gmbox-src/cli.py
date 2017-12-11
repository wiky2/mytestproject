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

'''gmbox的命令行界面'''
import sys,copy,cmd
from optparse import OptionParser
from lib.core import *
 
reload(sys)
sys.setdefaultencoding('utf8')

#既然只有国内可以使用google music,就不考虑国际化了,提示都用中文.
class CLI(cmd.Cmd):
    '''解析命令行参数'''
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.currentlist=u'华语新歌'
        self.currentalbumlist=u'影视新碟'
        self.prompt = "gmbox> "

    def default(self,line):
        print line,u' 不支持的命令!'

    def help_lists(self):
        print u'用法: lists\n查看支持的榜单名.'
    def do_lists(self,arg=None):
        print u'目前gmbox支持以下列表: '+u'、'.join(['"%s"'%key for key in songlists])
    def help_albums(self):
        print u'用法: albums\n查看支持的专辑列表名.'
    def do_albums(self,arg=None):
        print u'目前gmbox支持以下专辑列表: '+u'、'.join(['"%s"'%key for key in albums_lists])
    def help_list(self):
        print u'用法: list  <榜单名>\n列出榜单名的所有歌曲,默认列出上次list的榜单或华语新歌.'
    def do_list(self,arg):
        arg=deal_input(arg)
        if arg != '':
            if arg in songlists:
                self.currentlist=arg
            else:
                print u'未知列表:"'+arg+u'"'
                return
        gmbox.get_list(self.currentlist)
        gmbox.listall()
        print self.currentlist,u'包含以上',len(gmbox.songlist),u'首歌.'
    def help_albumlist(self):
        print u'用法: albumlist  <专辑列表名>\n列出专辑列表的所有专辑,默认列出上次albumlist的专辑或影视新碟.'
    def do_albumlist(self,arg):
        arg=deal_input(arg)
        if arg != '':
            if arg in albums_lists:
                self.currentalbumlist=arg
            else:
                print u'未知列表:"'+arg+u'"'
                return
        gmbox.get_album_IDs(self.currentalbumlist)
        gmbox.listallalbum()
        print self.currentalbumlist,u'包含以上',len(gmbox.albumlist),u'个专辑.'
    def help_search(self):
        print u'用法: search  关键字\n搜索关键字'
    def do_search(self,arg):
        arg=deal_input(arg)
        if arg != '':
            gmbox.search(arg)
            gmbox.listall()
        else:
            self.help_search()
    def help_albumsearch(self):
        print u'用法: albumsearch  关键字\n以关键字搜索专辑'
    def do_albumsearch(self,arg):
        arg=deal_input(arg)
        if arg != '':
            gmbox.searchalbum(arg)
            gmbox.listallalbum()
        else:
            self.help_albumsearch()

    def help_down(self):
        print u'用法: down num1 [num2 [num3 ...]]\n下载上次list或search的所有歌曲中的一部分,从1开始计数'
    def do_down(self,arg):
        if self._candown():
            k=[]
            try:
                [k.append(int(t)-1) for t in arg.split()]
            except ValueError:
                print u'down 后面要加数字序号.'
                return
            k=list(set(k))
            if len(k) > 0:
                gmbox.down_listed(k)
            else:
                print u'down 后面要加数字序号.'
    def help_albumdown(self):
        print u'用法: albumdown num1 [num2 [num3 ...]]\n下载上次albumlist或albumsearch的所有专辑中的一部分,从1开始计数'
    def do_albumdown(self,arg):
        if self._candownalbum():
            k=[]
            try:
                [k.append(int(t)-1) for t in arg.split()]
            except ValueError:
                print u'downalbum 后面要加数字序号.'
                return
            k=list(set(k))
            if len(k) > 0:
                gmbox.downalbums(k)
            else:
                print u'downalbum 后面要加数字序号.'
            
    def help_downall(self):
        print u'用法: downall\n下载上次list或search的所有歌曲'
    def do_downall(self,arg=None):
        if self._candown():
            gmbox.downall()
    def help_albumdownall(self):
        print u'用法: albumdownall\n下载上次albumlist或albumsearch的所有专辑'
    def do_albumdownall(self,arg=None):
        if self._candownalbum():
            gmbox.downallalbum()

    def help_albumsongs(self):
        print u'用法:albumsongs num\n列出专辑内容'

    def do_albumsongs(self,arg=None):
        if self._candownalbum():
            gmbox.get_albumlist(int(arg)-1)
            gmbox.listall()
            print gmbox.albuminfo['title']+'-'+gmbox.albuminfo['artist'], \
                u'包含以上',len(gmbox.songlist),u'首歌.'

    def help_config(self):
        print u'''用法: config 选项名 参数:
config savedir       目录        设置歌曲保存路径
config id3utf8       True|False  设置是否转换ID3信息到UTF-8编码
config makeartistdir True|False  设置下载时是否建立歌手目录
config makealbumdir  True|False  设置下载专辑时是否下载到专辑目录
config addalbumnum   True|False  设置下载专辑时是否在专辑下载时前置专辑序号
'''
    def do_config(self,arg):
        if arg == '':
            print config.item
            print u'歌曲下载路径：',gmbox.setup_file_info(u'歌名',u'歌手',False,u'专辑名',u'专辑歌手',1)[0]
            print u'专辑下载路径：',gmbox.setup_file_info(u'歌名',u'歌手',True,u'专辑名',u'专辑歌手',1)[0]
        else:
            if len(arg.split()) != 2:
                self.help_config()
            else:
                if arg.split()[0]=='savedir':
                    config.savedir_changed(arg.split()[1])
                elif arg.split()[0]=='id3utf8':
                    config.id3utf8_changed(arg.split()[1])
                elif arg.split()[0]=='makealbumdir':
                    config.makealbumdir_changed(arg.split()[1])
                elif arg.split()[0]=='makeartistdir':
                    config.makeartistdir_changed(arg.split()[1])
                elif arg.split()[0]=='addalbumnum':
                    config.addalbumnum_changed(arg.split()[1])
                else:
                    self.help_config()
        
    def help_exit(self):
        print u'用法: exit\n退出gmbox.'
    def do_exit(self,arg):
        sys.exit(0)
    def help_version(self):
        print u'用法: version\n显示版本号.'
    def do_version(self,arg):
        print 'gmbox V'+VERSION
    def do_EOF(self,arg):
        print
        sys.exit(0)

    def _candown(self):
        if not gmbox.songlist:
            print u'执行down或downall命令前,需先执行list或search命令'
            return False
        else:
            return True
    def _candownalbum(self):
        if not gmbox.albumlist:
            print u'执行downalbum或downalbumall命令前,需先执行albumslist或searchalbum命令'
            return False
        else:
            return True

    #shortcuts
    do_l = do_list
    do_s = do_search
    do_d = do_down
    do_da = do_downall
    do_al = do_albumlist
    do_as = do_albumsearch
    do_ad = do_albumdown
    do_ada = do_albumdownall
    do_ass = do_albumsongs

def BatchMode():
    parser = OptionParser(version='%prog '+VERSION, prog='gmbox', 
        description=u'不加参数运行可以进入交互模式.否则进入批处理模式,执行参数指定的相应动作后退出.')
    parser.add_option('-b', '--lists', action="store_true", 
        dest='lists', help=u'列出所有支持的榜单名,并退出')
    parser.add_option('-l', '--list', 
        dest='list', metavar=u'榜单名', help=u'列出榜单歌曲')
    parser.add_option('-s', '--search', 
        dest='search', metavar=u'关键词', help=u'搜索包含关键词的歌曲')
    parser.add_option('-a', '--downall', action="store_true", 
        dest='downall', help=u'search(-s)或list(-l)后下载全部歌曲.')
    parser.add_option('-d', '--down', action="store", 
        dest='down', metavar=u'"1 3 6"', help=u'search(-s)或list(-l)后下载部分歌曲.后面跟歌曲序号(注意需要引号)')
    
    parser.add_option('-B', '--albumlists', action="store_true", 
        dest='albumlists', help=u'列出所有支持的专辑榜单名,并退出')
    parser.add_option('-L', '--albumlist', 
        dest='albumlist', metavar=u'专辑列表名', help=u'列出专辑列表的歌曲')
    parser.add_option('-S', '--albumsearch', 
        dest='albumsearch', metavar=u'关键词', help=u'搜索包含关键词的专辑')
    parser.add_option('-A', '--albumdownall', action="store_true", 
        dest='albumdownall', help=u'albumsearch或albumlist后下载全部歌曲.')
    parser.add_option('-D', '--albumdown', action="store", 
        dest='albumdown', metavar=u'"1 3 6"', help=u'albumsearch(-S)或albumlist(-L)后下载部分专辑.后面跟专辑序号(注意需要引号)')
    (options, args) = parser.parse_args()
    
    cli=CLI()
    
    if options.lists:
        cli.do_lists()
    else:
        if options.search:
            cli.do_search(options.search)
        elif options.list:
            cli.do_list(options.list)
        if not(options.search or options.list) and (options.downall or options.down):
            print u'downall(-a)或down(-d)需要配合search(-s)或list(-l)使用.'
            return
        if options.downall:
            cli.do_downall()
        elif options.down:
            cli.do_down(options.down)
    
    if options.albumlists:
        cli.do_albums()
    else:
        if options.albumsearch:
            cli.do_albumsearch(options.albumsearch)
        elif options.albumlist:
            cli.do_albumlist(options.albumlist)
        if not(options.albumsearch or options.albumlist) and (options.albumdownall or options.albumdown):
            print u'albumdownall(-A)或albumdown(-D)需要配合albumsearch(-S)或albumlist(-L)使用.'
            return
        if options.albumdownall:
            cli.do_albumdownall()
        elif options.albumdown:
            cli.do_albumdown(options.albumdown)
            

if __name__ == '__main__':
    if len(sys.argv)==1:
        '''交互模式'''
        cli=CLI()
        welcominfo=u"欢迎使用 gmbox!\n更多信息请访问 http://code.google.com/p/gmbox/\n可以输入 'help' 查看支持的命令"
        print welcominfo
        cli.cmdloop()
        #TODO: cli.cmdloop(welcominfo)  #本来应该是这样的,但是无奈在windows下会乱码...谁知道怎么搞定?
    else:
        BatchMode()
