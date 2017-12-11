# coding: utf-8
import os, sys, copy, time
import types, webbrowser, subprocess
import wx
import threading
import panels, dialogs, config, storage, export, recycle, task, sync
from wx.lib.wordwrap import wordwrap
import event
from loader import load_bitmap
import sqlite3, datetime, shutil
from category import Category
import pprint, traceback, logfile, version
from storage import catetypes, payways, cycles

class MainFrame (wx.Frame):
    def __init__(self, parent, id, title, cf):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(900,600),
                name=u'YouMoney', style=wx.DEFAULT_FRAME_STYLE)
        config.cf = cf
        self.rundir = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.bmpdir = os.path.join(self.rundir, 'images')
        icon = wx.EmptyIcon()
        iconpath = os.path.join(self.bmpdir, 'small.png')
        icon.CopyFromBitmap(wx.BitmapFromImage(wx.Image(iconpath, wx.BITMAP_TYPE_PNG)))
        self.SetIcon(icon)
        self.CenterOnScreen()

        if config.cf:
            self.conf = config.cf
        else:
            raise ValueError, 'config.cf is None'
        
        self.lang2id = {}
        self.id2lang = {}

        self.make_menu()
        self.make_toolbar()
        self.make_statusbar()

        self.initdb()
        self.load()
        self.book = panels.ContentTab(self)
        self.book.load_category(self.category)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.book, 1, wx.EXPAND|wx.ALL)
        self.SetSizer(sizer)
        self.SetAutoLayout(True)

        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.check_password()

        self.Bind(event.EVT_UPDATE_NOTIFY, self.OnUpdateNotify) 
        self.Bind(event.EVT_MYALERT, self.OnMyAlert) 
        wx.CallLater(100, self.notify)

        self.initcate()
        
        # start server
        th = threading.Thread(target=task.start_server, args=(self,))
        th.start()
        # start check update
        task.taskq.put({'id':1, 'type':'update', 'frame':self})

        
    def initcate(self):
        sql = "select count(*) from category"
        count = self.db.query_one(sql)
        #print 'count:', count, 'iscreate:', config.cf.iscreate, 'lang:', config.cf['lang']
        if count == 0 and config.cf.iscreate and config.cf['lang'] == 'zh_CN':
            path = os.path.join(self.rundir, 'data', 'category.csv')
            if not os.path.isfile(path):
                return
            exp = export.DataImport(self.db, 'gbk')
            try:
                exp.category(path)
            except:
                logfile.info(traceback.format_exc())
            self.reload()

    def notify(self):
        lastdb = self.conf['lastdb']
        if sys.platform.startswith('win32') and lastdb.startswith(os.environ['SystemDrive']) and self.conf.lastdb_is_default():
            wx.MessageBox(_('You db file is in default path, strongly advise save it to other path. Choose menu File->Change Account Path to change path.'), _('Note:'), wx.OK|wx.ICON_INFORMATION)
        

    def check_password(self):
        sql = "select * from user" 
        ret = self.db.query(sql)
        if ret:
            row = ret[0]
            if row['password']:
                dlg = dialogs.UserCheckDialog(self)
                dlg.CenterOnScreen()
                while True:
                    chi = dlg.ShowModal()
                    if chi != wx.ID_OK:
                        sys.exit()

                    passwd = dlg.values()['password'] 
                    if passwd != row['password']:
                        dlg.set_warn(_('Password error.'))
                        continue
                    break
                dlg.Destroy()

    def initdb(self, path=None):
        if not path:
            path = self.conf['lastdb']
        try:
            self.db = storage.DBStorage(path)
        except:
            wx.MessageBox(_('Account file is not exist! You may create one or open exist.'), _('Error'), wx.OK|wx.ICON_INFORMATION) 
            path = self.conf.default_db_path()
            self.conf['lastdb'] = path
            self.db = storage.DBStorage(path)

        self.SetStatusText(_('Database file: ') + path, 0)

        dbver  = int(self.db.version.replace('.', '')) 
        prgver = int(version.VERSION.replace('.', ''))
        
        if dbver > prgver:
            wx.MessageBox(_('Database version is newer than program.'), _('Error'), wx.OK|wx.ICON_INFORMATION)
            sys.exit()
        
        self.conf.setid(storage.name)

        # sync
        #if self.conf['sync_way'] == 'user':
        #    sync.synchronization(self, alert=False)

        # check record cycle
        rc = recycle.RecordCycle(self.db)
        rc.cycle()
        rc = None

        
    def load(self):
        tday = datetime.date.today()
        sql = "select * from category order by parent"
        cates = self.db.query(sql)
        sql = "select * from capital where year=%d and month=%d" % (tday.year, tday.month)
        recs  = self.db.query(sql)
   
        self.category = Category(cates, recs)
        self.SetStatusText(_('Database file: ') + self.conf['lastdb'], 0)

    
    def reload(self):
        self.load()
        self.book.load_category(self.category)
        self.book.load_list()
        self.book.load_cycle()
    
    def make_menu(self):
        self.ID_FILE_NEW  = wx.NewId()
        self.ID_FILE_OPEN = wx.NewId()
        self.ID_FILE_SAVEAS = wx.NewId()
        self.ID_FILE_CHANGE = wx.NewId()
        self.ID_FILE_PASSWORD = wx.NewId()
        self.ID_FILE_IMPORT = wx.NewId()
        self.ID_FILE_IMPORT_CATE = wx.NewId()
        self.ID_FILE_IMPORT_DATA = wx.NewId()
        self.ID_FILE_EXPORT = wx.NewId()
        self.ID_FILE_EXPORT_CATE = wx.NewId()
        self.ID_FILE_EXPORT_DATA = wx.NewId()
        self.ID_FILE_EXIT = wx.NewId()

        self.ID_EDIT_ADDCATE = wx.NewId()
        self.ID_EDIT_ADDINCOME = wx.NewId()
        self.ID_EDIT_ADDPAY = wx.NewId()
        self.ID_EDIT_ADDCYCLE = wx.NewId()
        self.ID_EDIT_SYNC = wx.NewId()
        self.ID_EDIT_CATE = wx.NewId()
        self.ID_EDIT_INCOME = wx.NewId()
        self.ID_EDIT_PAY = wx.NewId()
        self.ID_EDIT_CYCLE = wx.NewId()
        self.ID_EDIT_STAT = wx.NewId()

        self.ID_VIEW_LANG = wx.NewId()
        self.ID_VIEW_LANG_EN = wx.NewId()
        self.ID_VIEW_LANG_CN = wx.NewId()
        self.ID_VIEW_LANG_TW = wx.NewId()
        self.ID_VIEW_LANG_JP = wx.NewId()
        
        self.ID_ABOUT_UPDATE  = wx.NewId()
        self.ID_ABOUT_WEBSITE = wx.NewId()
            
        self.lang2id['zh_CN'] = self.ID_VIEW_LANG_CN
        self.lang2id['zh_TW'] = self.ID_VIEW_LANG_TW
        self.lang2id['en_US'] = self.ID_VIEW_LANG_EN
        self.lang2id['ja_JP'] = self.ID_VIEW_LANG_JP
        
        self.id2lang[self.ID_VIEW_LANG_CN] = 'zh_CN'
        self.id2lang[self.ID_VIEW_LANG_TW] = 'zh_TW'
        self.id2lang[self.ID_VIEW_LANG_EN] = 'en_US'
        self.id2lang[self.ID_VIEW_LANG_JP] = 'ja_JP'
        
        menubar = wx.MenuBar()
        
        self.importmenu = wx.Menu()
        self.importmenu.Append(self.ID_FILE_IMPORT_CATE, _('Import Category'))
        self.importmenu.Append(self.ID_FILE_IMPORT_DATA, _('Import Data'))
        
        self.exportmenu = wx.Menu()
        self.exportmenu.Append(self.ID_FILE_EXPORT_CATE, _('Export Category'))
        self.exportmenu.Append(self.ID_FILE_EXPORT_DATA, _('Export Data'))

        self.filemenu = wx.Menu()
        self.filemenu.Append(self.ID_FILE_NEW, _('New Account')+"\tAlt+N")
        self.filemenu.Append(self.ID_FILE_OPEN, _('Open Account')+"\tAlt+O")
        self.filemenu.Append(self.ID_FILE_SAVEAS, _('Account Backup')+"\tAlt+B")
        self.filemenu.Append(self.ID_FILE_CHANGE, _('Change Account Path')+"\tAlt+G")
        self.filemenu.AppendSeparator()
        self.filemenu.Append(self.ID_FILE_PASSWORD, _('Set Password')+"\tAlt+S")
        self.filemenu.AppendSeparator()
        self.filemenu.AppendMenu(self.ID_FILE_IMPORT, _('Import'), self.importmenu)
        self.filemenu.AppendMenu(self.ID_FILE_EXPORT, _('Export'), self.exportmenu)
        self.filemenu.AppendSeparator()
        self.filemenu.Append(self.ID_FILE_EXIT, _('Exit')+"\tAlt+X")
        menubar.Append(self.filemenu, _('File'))

        self.editmenu = wx.Menu()
        self.editmenu.Append(self.ID_EDIT_ADDCATE, _('Add Category')+"\tAlt+T")
        self.editmenu.Append(self.ID_EDIT_ADDINCOME, _('Add Income')+"\tAlt+I")
        self.editmenu.Append(self.ID_EDIT_ADDPAY, _('Add Payout')+"\tAlt+P")
        self.editmenu.Append(self.ID_EDIT_ADDCYCLE, _('Add Record Cycle')+"\tAlt+C")
        #self.editmenu.Append(self.ID_EDIT_SYNC, _('Sync User Data')+"\tAlt+Y")
        self.editmenu.AppendSeparator()
        self.editmenu.Append(self.ID_EDIT_CATE, _('Category')+"\tAlt+1")
        self.editmenu.Append(self.ID_EDIT_INCOME, _('Income List')+"\tAlt+2")
        self.editmenu.Append(self.ID_EDIT_PAY, _('Payout List')+"\tAlt+3")
        self.editmenu.Append(self.ID_EDIT_CYCLE, _('Record Cycle')+"\tAlt+4")
        self.editmenu.Append(self.ID_EDIT_STAT, _('Statistic')+"\tAlt+5")
        menubar.Append(self.editmenu, _('Edit'))         
       
        self.langmenu = wx.Menu()
        self.langmenu.AppendRadioItem(self.ID_VIEW_LANG_CN, _('Simple Chinese'))
        self.langmenu.AppendRadioItem(self.ID_VIEW_LANG_TW, _('Traditional Chinese'))
        self.langmenu.AppendRadioItem(self.ID_VIEW_LANG_EN, _('English'))
        self.langmenu.AppendRadioItem(self.ID_VIEW_LANG_JP, _('Japanese'))
        
        self.viewmenu = wx.Menu()
        self.viewmenu.AppendMenu(self.ID_VIEW_LANG, _('Language'), self.langmenu)
        menubar.Append(self.viewmenu, _('View'))
        
        self.aboutmenu = wx.Menu()
        self.aboutmenu.Append(self.ID_ABOUT_UPDATE, _('Update YouMoney'))
        self.aboutmenu.Append(self.ID_ABOUT_WEBSITE, _('About Information'))
        menubar.Append(self.aboutmenu, _('About'))

        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnFileNew, id=self.ID_FILE_NEW)
        self.Bind(wx.EVT_MENU, self.OnFileOpen, id=self.ID_FILE_OPEN)
        self.Bind(wx.EVT_MENU, self.OnFileSaveAs, id=self.ID_FILE_SAVEAS)
        self.Bind(wx.EVT_MENU, self.OnFileChange, id=self.ID_FILE_CHANGE)
        self.Bind(wx.EVT_MENU, self.OnFilePassword, id=self.ID_FILE_PASSWORD)
        self.Bind(wx.EVT_MENU, self.OnFileImportCate, id=self.ID_FILE_IMPORT_CATE)
        self.Bind(wx.EVT_MENU, self.OnFileImportData, id=self.ID_FILE_IMPORT_DATA)
        self.Bind(wx.EVT_MENU, self.OnFileExportCate, id=self.ID_FILE_EXPORT_CATE)
        self.Bind(wx.EVT_MENU, self.OnFileExportData, id=self.ID_FILE_EXPORT_DATA)
        self.Bind(wx.EVT_MENU, self.OnCloseWindow, id=self.ID_FILE_EXIT)
        
        self.Bind(wx.EVT_MENU, self.OnCateEdit, id=self.ID_EDIT_ADDCATE)
        self.Bind(wx.EVT_MENU, self.OnIncome, id=self.ID_EDIT_ADDINCOME)
        self.Bind(wx.EVT_MENU, self.OnPayout, id=self.ID_EDIT_ADDPAY)
        self.Bind(wx.EVT_MENU, self.OnCycle, id=self.ID_EDIT_ADDCYCLE)
        #self.Bind(wx.EVT_MENU, self.OnSync, id=self.ID_EDIT_SYNC)

        self.Bind(wx.EVT_MENU, self.OnEditTabCate, id=self.ID_EDIT_CATE)
        self.Bind(wx.EVT_MENU, self.OnEditTabIncome, id=self.ID_EDIT_INCOME)
        self.Bind(wx.EVT_MENU, self.OnEditTabPayout, id=self.ID_EDIT_PAY)
        self.Bind(wx.EVT_MENU, self.OnEditTabCycle, id=self.ID_EDIT_CYCLE)
        self.Bind(wx.EVT_MENU, self.OnEditTabStat, id=self.ID_EDIT_STAT)

        self.Bind(wx.EVT_MENU, self.OnLanguage, id=self.ID_VIEW_LANG_CN)
        self.Bind(wx.EVT_MENU, self.OnLanguage, id=self.ID_VIEW_LANG_TW)
        self.Bind(wx.EVT_MENU, self.OnLanguage, id=self.ID_VIEW_LANG_EN)
        self.Bind(wx.EVT_MENU, self.OnLanguage, id=self.ID_VIEW_LANG_JP)

        self.Bind(wx.EVT_MENU, self.OnAboutUpdate, id=self.ID_ABOUT_UPDATE)
        self.Bind(wx.EVT_MENU, self.OnAboutInfo, id=self.ID_ABOUT_WEBSITE)
        
        lang = self.conf['lang']
        if lang:
            mid = self.lang2id[lang]
        else:
            mid = self.ID_VIEW_LANG_EN
        self.langmenu.Check(mid, True)

    def make_toolbar(self):
        self.ID_TB_CATEEDIT = wx.NewId()
        self.ID_TB_INCOME   = wx.NewId()
        self.ID_TB_PAYOUT   = wx.NewId()
        self.ID_TB_CYCLE    = wx.NewId()
        self.ID_TB_SYNC     = wx.NewId()
        
        self.toolbar = wx.ToolBar(self, -1, wx.DefaultPosition, wx.Size(48,48), wx.TB_HORIZONTAL|wx.TB_FLAT|wx.TB_TEXT)
        self.toolbar.SetToolBitmapSize(wx.Size (48, 48))
        #self.toolbar.AddLabelTool(self.ID_TB_CATEEDIT, _('Add Category')+'(&T)', load_bitmap(os.path.join(self.bmpdir, 'categories.png')), shortHelp=_('Add Category'), longHelp=_('Add Category')) 
        self.toolbar.AddLabelTool(self.ID_TB_CATEEDIT, _('Add Category')+'(&T)', load_bitmap(os.path.join(self.bmpdir, 'categories.png')), shortHelp=_('Add Category')) 
        self.toolbar.AddLabelTool(self.ID_TB_INCOME, _('Add Income')+'(&I)', load_bitmap(os.path.join(self.bmpdir, 'cashin.png')), shortHelp=_('Add Income'), longHelp=_('Add Income')) 
        self.toolbar.AddLabelTool(self.ID_TB_PAYOUT, _("Add Payout")+'(&P)', load_bitmap(os.path.join(self.bmpdir, 'cashout.png')), shortHelp=_("Add Payout"), longHelp=_("Add Payout")) 
        self.toolbar.AddLabelTool(self.ID_TB_CYCLE, _("Add Record Cycle")+'(&C)', load_bitmap(os.path.join(self.bmpdir, 'cycle.png')), shortHelp=_("Record Cycle"), longHelp=_("Record Cycle")) 
        #self.toolbar.AddLabelTool(self.ID_TB_SYNC, _("Sync")+'(&Y)', load_bitmap(os.path.join(self.bmpdir, 'sync.png')), shortHelp=_("Sync user data"), longHelp=_("Sync user data")) 

        self.toolbar.Realize ()
        self.SetToolBar(self.toolbar)

        self.Bind(wx.EVT_TOOL, self.OnCateEdit, id=self.ID_TB_CATEEDIT)
        self.Bind(wx.EVT_TOOL, self.OnIncome, id=self.ID_TB_INCOME)
        self.Bind(wx.EVT_TOOL, self.OnPayout, id=self.ID_TB_PAYOUT)
        self.Bind(wx.EVT_TOOL, self.OnCycle, id=self.ID_TB_CYCLE)
        #self.Bind(wx.EVT_TOOL, self.OnSync, id=self.ID_TB_SYNC)

    def make_statusbar(self):
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(1)
        self.SetStatusWidths([-1])

    def OnCloseWindow(self, event):
        #if self.conf['sync_way'] == 'user':
        #    sync.synchronization(self)
        task.taskq.put(None)
        logfile.info('task thread end')
        vi = sys.version_info
        if vi[0] == 2 and vi[1] >= 6:
            task.server.shutdown()
        else:
            task.server.server_close()
        logfile.info('server thread end')

        self.Destroy()
        sys.exit() 

    def OnFileOpen(self, event):
        dlg = wx.FileDialog(
            self, message=_("Choose account file:"),
            defaultDir=os.getcwd(), 
            defaultFile="",
            wildcard=_("YouMoney Database (*.db)|*.db"),
            style=wx.OPEN | wx.CHANGE_DIR
            )

        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            logfile.info("open file:", path) 

            self.db.close()
            self.initdb(path)
            #self.db = storage.DBStorage(path)
            self.reload()
            self.conf['lastdb'] = path
            self.conf.dump()
            
            self.SetStatusText(_('Database file: ') + self.conf['lastdb'], 0)
            
        dlg.Destroy()

    def OnFileNew(self, event):
        dlg = wx.FileDialog(
            self, message=_("New account file save..."), defaultDir=os.getcwd(), 
            defaultFile="", wildcard=_("YouMoney Database (*.db)|*.db"), style=wx.SAVE)
        dlg.SetFilterIndex(2)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            logfile.info("save file:", path) 
            if not path.endswith('.db'):
                path += ".db"
 
            if os.path.isfile(path):
                wx.MessageBox(_('File exist'), _('Can not save account file'), wx.OK|wx.ICON_INFORMATION) 
                return
 
            self.db.close()
            self.initdb(path)
            self.reload()
            self.conf['lastdb'] = path
            self.conf.dump()

            self.conf.iscreate = True
            self.initcate()
 
            self.SetStatusText(_('Database file: ') + self.conf['lastdb'], 0)
 
        dlg.Destroy()


    def OnFileSaveAs(self, event):
        dlg = wx.FileDialog(
            self, message=_("Account save as..."), defaultDir=os.getcwd(), 
            defaultFile="", wildcard=_("YouMoney Database (*.db)|*.db"), style=wx.SAVE)
        dlg.SetFilterIndex(2)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            logfile.info("save file:", path) 
            if not path.endswith('.db'):
                path += ".db"
            
            if os.path.isfile(path):
                wx.MessageBox(_('File exist'), _('Can not save account file'), wx.OK|wx.ICON_INFORMATION) 
                return
            try:
                shutil.copyfile(self.conf['lastdb'], path)
            except Exception, e:
                wx.MessageBox(_('Save account failture:') + str(e), _('Can not save account file'), wx.OK|wx.ICON_INFORMATION)
                return
        
        dlg.Destroy()

    def OnFileChange(self, event):
        dlg = wx.FileDialog(
            self, message=_("Change account path..."), defaultDir=os.getcwd(), 
            defaultFile="", wildcard=_("YouMoney Database (*.db)|*.db"), style=wx.SAVE)
        dlg.SetFilterIndex(2)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            logfile.info("save file:", path) 
            if not path.endswith('.db'):
                path += ".db"
            
            self.conf.dump()
            oldfile = self.conf['lastdb']
            if os.path.isfile(path):
                wx.MessageBox(_('File exist'), _('Can not save account file'), wx.OK|wx.ICON_INFORMATION) 
                return
            try:
                shutil.copyfile(self.conf['lastdb'], path)
            except Exception, e:
                wx.MessageBox(_('Change account path failture:') + str(e), _('Can not save account file'), wx.OK|wx.ICON_INFORMATION)
                return
            self.db.close()
            if os.path.isfile(oldfile):
                os.remove(oldfile)
            self.initdb(path)
            #self.db = storage.DBStorage(path)
            self.reload()
            self.conf['lastdb'] = path
            self.conf.dump()
            
            self.SetStatusText(_('Database file: ') + self.conf['lastdb'], 0)
        
        dlg.Destroy()


    def OnCateEdit(self, event):
        ready = {'cates':[], 'cate':'', 'upcate':_('No Higher Category'), 'catetype':_('Payout'), 'mode':'insert'}
        self.cateedit_dialog(ready)


    def cateedit_dialog(self, ready):
        cates = copy.deepcopy(self.category.catelist_parent())
        cates[_('Income')].insert(0, _('No Higher Category'))
        cates[_('Payout')].insert(0, _('No Higher Category'))

        ready['cates'] = cates
        if not ready['upcate']:
            ready['upcate'] = _('No Higher Category')

        dlg = dialogs.CategoryDialog(self, ready)
        dlg.CenterOnScreen()
        if dlg.ShowModal() == wx.ID_OK:
            item = dlg.values()
            logfile.info('cateedit:', item)
            type = catetypes[item['catetype']]
            parent = 0
            if item['catetype'] == _('Income'):
                if item['upcate'] != _('No Higher Category'):
                    parent = self.category.income_catemap[item['upcate']]
            elif item['catetype'] == _('Payout'):
                if item['upcate'] != _('No Higher Category'):
                    parent = self.category.payout_catemap[item['upcate']]
            
            if item['mode'] == 'insert':
                #sql = "insert into category (name,parent,type) values ('%s',%d,%d)" % (item['cate'], parent, type)
                sql = "insert into category (name,parent,type) values (?,?,?)"
                logfile.info('insert category:', sql)
                try:
                    #self.db.execute(sql, (item['cate'], parent, type, ))
                    self.db.execute_param(sql, (item['cate'], parent, type, ))
                except Exception, e:
                    wx.MessageBox(_('Add category failture:') + str(e), _('Add category information'), wx.OK|wx.ICON_INFORMATION)
                else:
                    self.reload()
            elif item['mode'] == 'update':
                #sql = "update category set name='%s',parent=%d,type=%d where id=%d" % (item['cate'], parent, type, item['id'])
                sql = "update category set name=?,parent=?,type=? where id=?"
                logfile.info('update category:', sql)
                try:
                    self.db.execute_param(sql, (item['cate'],parent,type,item['id'],))
                except Exception, e:
                    wx.MessageBox(_('Change category failture:') + str(e), _('Change category information'), wx.OK|wx.ICON_INFORMATION)
                else:
                    self.reload()
 

    def OnIncome(self, event):
        tday = datetime.date.today()
        catelist = self.category.income_catelist
        if len(catelist) == 0:
            wx.MessageBox(_('Add category first!'), _('Can not add income item'), wx.OK|wx.ICON_INFORMATION)
            return
        ready = {'cates':catelist, 'cate':catelist[0], 
                 'year':tday.year, 'month':tday.month, 'day':tday.day,
                 'num':'', 'explain':'', 'mode':'insert'}

        self.income_dialog(ready)

    def income_dialog(self, ready):
        dlg = dialogs.IncomeDialog(self, ready)
        dlg.CenterOnScreen()
        while dlg.ShowModal() == wx.ID_OK:
            data = dlg.values()
            logfile.info('income dialog:', data)
            #sql = "insert into capital (category,num,ctime,year,month,day,payway,explain,type) values (%d,%f,%d,%d,%d,%d,%d,'%s',1)"
            sql = "insert into capital (category,num,ctime,year,month,day,payway,explain,type) values (?,?,?,?,?,?,?,?,1)"
            cate = data['cate'].split('->')[-1]

            if data['mode'] == 'insert':
                try:
                    #cateid = self.category.income_catemap[cate]
                    cateid = self.category.income_catemap[data['cate']]
                    tnow   = int(time.time())
                    num    = float(data['num'])
                    #payway = payways[data['pay']]
                    payway = 0
                    year   = data['date'].GetYear()
                    month  = data['date'].GetMonth() + 1
                    day    = data['date'].GetDay()

                    #sql = sql % (cateid, num, tnow, year, month, day, payway, data['explain'])
                    logfile.info('insert capital:', sql)
                    self.db.execute_param(sql, (cateid, num, tnow, year, month, day, payway, data['explain'],))
                except Exception, e:
                    wx.MessageBox(_('Add income failture:') + str(e), _('Add income information'), wx.OK|wx.ICON_INFORMATION)
                    logfile.info('insert income error:', traceback.format_exc())
                else:
                    self.reload()
                    dlg.ClearForReinput()

            elif data['mode'] == 'update':
                #sql = "update capital set category=%d,num=%d,year=%d,month=%d,day=%d,explain='%s' where id=%d"
                sql = "update capital set category=?,num=?,year=?,month=?,day=?,explain=? where id=?"
                try:
                    #cateid = self.category.income_catemap[cate]
                    cateid = self.category.income_catemap[data['cate']]
                    num    = float(data['num'])
                    year   = data['date'].GetYear()
                    month  = data['date'].GetMonth() + 1
                    day    = data['date'].GetDay()

                    #sql = sql % (cateid, num, year, month, day, data['explain'], data['id'])
                    logfile.info('update capital:', sql)
                    self.db.execute_param(sql, (cateid, num, year, month, day, data['explain'], data['id'],))
                except Exception, e:
                    wx.MessageBox(_('Change income failture:') + str(e), _('Change income information'), wx.OK|wx.ICON_INFORMATION)
                    logfile.info('update error:', traceback.format_exc())
                else:
                    self.reload()

            if not data['reuse']:
                break




    def OnPayout(self, event):
        tday = datetime.date.today()
        catelist = self.category.payout_catelist
        if len(catelist) == 0:
            wx.MessageBox(_('Add category first!'), _('Can not add payout item'), wx.OK|wx.ICON_INFORMATION)
            return
 
        ready = {'cates':catelist, 'cate':catelist[0], 'num':'', 
                 'explain':'', 'year':tday.year, 'month':tday.month, 'day':tday.day,
                 'pay':_('Cash'), 'mode':'insert'}
        #print 'payout insert:', ready 
        self.payout_dialog(ready)

    def payout_dialog(self, ready):
        dlg = dialogs.PayoutDialog(self, ready)
        dlg.CenterOnScreen()
        while dlg.ShowModal() == wx.ID_OK:
            data = dlg.values()
            logfile.info('payout dialog:', data)
            
            cate = data['cate'].split('->')[-1]
            if data['mode'] == 'insert':
                #sql = "insert into capital (category,num,ctime,year,month,day,payway,explain,type) values (%d,%f,%d,%d,%d,%d,%d,'%s',0)"
                sql = "insert into capital (category,num,ctime,year,month,day,payway,explain,type) values (?,?,?,?,?,?,?,?,0)"
                try:
                    #cateid = self.category.payout_catemap[cate]
                    cateid = self.category.payout_catemap[data['cate']]
                    tnow   = int(time.time())
                    num    = float(data['num'])
                    payway = payways[data['pay']]
                    year   = data['date'].GetYear()
                    month  = data['date'].GetMonth() + 1
                    day    = data['date'].GetDay()

                    #sql = sql % (cateid, num, tnow, year, month, day, payway, data['explain'])
                    logfile.info('insert capital payout:', sql)
                    self.db.execute_param(sql, (cateid, num, tnow, year, month, day, payway, data['explain'],))
                except Exception, e:
                    wx.MessageBox(_('Add payout failture:') + str(e), _('Add payout information'), wx.OK|wx.ICON_INFORMATION)
                    logfile.info('insert payout error:', traceback.format_exc())
                else:
                    self.reload()
                    dlg.ClearForReinput()

            elif data['mode'] == 'update':
                #sql = "update capital set category=%d,num=%d,year=%d,month=%d,day=%d,payway=%d,explain='%s' where id=%d"
                sql = "update capital set category=?,num=?,year=?,month=?,day=?,payway=?,explain=? where id=?"
                try:
                    #cateid = self.category.payout_catemap[cate]
                    cateid = self.category.payout_catemap[data['cate']]
                    num    = float(data['num'])
                    payway = payways[data['pay']]
                    year   = data['date'].GetYear()
                    month  = data['date'].GetMonth() + 1
                    day    = data['date'].GetDay()

                    #sql = sql % (cateid, num, year, month, day, payway, data['explain'], data['id'])
                    logfile.info('update capital:', sql)
                    self.db.execute_param(sql, (cateid, num, year, month, day, payway, data['explain'], data['id'],))
                except Exception, e:
                    wx.MessageBox(_('Change payout failture:') + str(e), _('Change payout information'), wx.OK|wx.ICON_INFORMATION)
                    logfile.info('update error:', traceback.format_exc())
                else:
                    self.reload()
            if not data['reuse']:
                break

    def OnCycle(self, event):
        payout_catelist = self.category.payout_catelist
        income_catelist = self.category.income_catelist

        if len(payout_catelist) == 0 and len(income_catelist) == 0:
            wx.MessageBox(_('Add category first!'), _('Can not add cycle item'), wx.OK|wx.ICON_INFORMATION)
            return
        
        cyclelist = []
        for k in storage.cycles:
            if type(k) != types.IntType:
                cyclelist.append(k)
        cyclelist.reverse()

        ready = {'payout_cates':payout_catelist, 'payout_cate':payout_catelist[0], 
                 'income_cates':income_catelist, 'income_cate':income_catelist[0],
                 'num':'', 'types':[_('Payout'), _('Income')], 'type':_('Payout'),
                 'cycles':cyclelist, 'cycle':cycles[1],
                 'explain':'',
                 'pay':_('Cash'), 'mode':'insert'}
        #print 'payout insert:', ready 
        self.cycle_dialog(ready)

    def cycle_dialog(self, ready):
        dlg = dialogs.CycleDialog(self, ready)
        #dlg.CenterOnParent()
        while dlg.ShowModal() == wx.ID_OK:
            data = dlg.values()
            logfile.info('cycle dialog:', data)
            
            cate = data['cate'].split('->')[-1]
            if data['mode'] == 'insert':
                sql = "insert into recycle (category,num,ctime,payway,type,addtime,explain) values (?,?,?,?,?,?,?)"
                try:
                    typeid = catetypes[data['type']]
                    if data['type'] == _('Payout'):
                        #cateid = self.category.payout_catemap[cate]
                        cateid = self.category.payout_catemap[data['cate']]
                    else:
                        #cateid = self.category.income_catemap[cate]
                        cateid = self.category.income_catemap[data['cate']]
                    tnow   = int(time.time())
                    num    = float(data['num'])
                    payway = payways[data['pay']]
                    addtime = cycles[data['addtime']]

                    logfile.info('insert cycle:', sql)
                    self.db.execute_param(sql, (cateid, num, tnow, payway, typeid, addtime, data['explain'],))
                except Exception, e:
                    wx.MessageBox(_('Add cycle failture:') + str(e), _('Add cycle information'), wx.OK|wx.ICON_INFORMATION)
                    logfile.info('insert cycle error:', traceback.format_exc())
                else:
                    cid = self.db.last_insert_id() 
                    rc = recycle.RecordCycle(self.db)
                    rc.cycle(cid)
                    rc = None

                    self.reload()
                    dlg.ClearForReinput()

            elif data['mode'] == 'update':
                sql = "update recycle set category=?,num=?,payway=?,type=?,addtime=?,explain=? where id=?"
                try:
                    typeid = catetypes[data['type']]
                    if data['type'] == _('Payout'):
                        #cateid = self.category.payout_catemap[cate]
                        cateid = self.category.payout_catemap[data['cate']]
                    else:
                        #cateid = self.category.income_catemap[cate]
                        cateid = self.category.income_catemap[data['cate']]
 
                    num    = float(data['num'])
                    payway = payways[data['pay']]
                    addtime = cycles[data['addtime']]

                    logfile.info('update cycle:', sql)
                    self.db.execute_param(sql, (cateid, num, payway, typeid, addtime, data['explain'], data['id'],))
                except Exception, e:
                    wx.MessageBox(_('Change cycle failture:') + str(e), _('Change cycle information'), wx.OK|wx.ICON_INFORMATION)
                    logfile.info('update error:', traceback.format_exc())
                else:
                    self.reload()
            if not data['reuse']:
                break


    def OnLanguage(self, event):
        mid = event.GetId()  
        clang = self.conf['lang']
        ischange = False
        
        lang = self.id2lang[mid]
        if lang != clang:
            ischange = True
            self.conf['lang'] = lang 
            self.conf.dump()

        if ischange:
            wx.MessageBox(_('Language changed! You must restart youmoney !'), _('Note:'), wx.OK|wx.ICON_INFORMATION)

    def OnAboutInfo(self, event):
        info = wx.AboutDialogInfo()
        info.Name = u"YouMoney"
        info.Version = version.VERSION
        info.Copyright = "(C) 2010 zhaoweikid"
        info.Description = wordwrap(_("YouMoney is a opensource personal finance software write by Python language.") + '\n',
            350, wx.ClientDC(self))
        info.WebSite = ("http://code.google.com/p/youmoney", _("YouMoney home page"))
        info.Developers = ["zhaoweikid"]

        info.License = wordwrap("GPL", 500, wx.ClientDC(self))
        wx.AboutBox(info)


    def OnAboutUpdate(self, event):
        self.updater()

    def updater(self):
        cmd = ''
        if sys.platform == 'win32':
            exe = os.path.join(self.rundir, 'updater.exe')
            if os.path.isfile(exe):
                cmd = exe
            else:
                cmd = os.path.join(self.rundir, 'updater.pyw')
            cmd = '"' + cmd + '"'
        elif sys.platform == 'darwin':
            if self.rundir.startswith(os.environ['HOME']):
                cmd = '/usr/bin/python "%s"' % (os.path.join(self.rundir, 'updater.py'))
        elif sys.platform.startswith('linux'):
            if not self.rundir.startswith('/usr/share'):
                cmd = '/usr/bin/python "%s"' % (os.path.join(self.rundir, 'updater.py'))
        if cmd:
            p = subprocess.Popen(cmd, shell=True)
        else:
            wx.MessageBox(_('This version is not support automatic update. Only windows and run with source support.'), _('Note:'), wx.OK|wx.ICON_INFORMATION)


    def OnUpdateNotify(self, event):
        dlg = dialogs.UpdateDialog(self, event.version)
        dlg.CenterOnScreen()
        if dlg.ShowModal() == wx.ID_OK:
            webbrowser.open('http://code.google.com/p/youmoney/')
            self.updater()
        dlg.Destroy()

    def OnMyAlert(self, event):
        dlg = wx.MessageDialog(self, event.message, _('Note:'), wx.OK|wx.ICON_INFORMATION)
        ret = dlg.ShowModal()
        dlg.Destroy()

        if event.name == 'update' and ret == wx.ID_OK:
            sys.exit()

    def OnFilePassword(self, event):
        dlg = dialogs.PasswordDialog(self)
        dlg.CenterOnScreen()
        while dlg.ShowModal() == wx.ID_OK:
            data = dlg.values()
            pass1 = data['password1']
            pass2 = data['password2']
           
            if not pass1 and not pass2:
                dlg.set_warn(_('Delete password'))
                dlg2 = wx.MessageDialog(self, _('Delete password'), _('Note:'), wx.OK|wx.ICON_INFORMATION)
                ret = dlg2.ShowModal()
                dlg2.Destroy()
            else:
                if not pass1 or not pass2:
                    dlg.set_warn(_('Password must not null.'))
                    continue

            if pass1 != pass2:
                dlg.set_warn(_('Different password.'))
                continue
            
            sql = "update user set password=?,mtime=?"
            self.db.execute_param(sql, (pass1, int(time.time()),))

            break

        dlg.Destroy()

            
    def OnEditTabCate(self, event):
        self.book.ChangeSelection(0)
    
    def OnEditTabIncome(self, event):
        self.book.ChangeSelection(1)
        
    def OnEditTabPayout(self, event):
        self.book.ChangeSelection(2)
 
    def OnEditTabCycle(self, event):
        self.book.ChangeSelection(3)
        
    def OnEditTabStat(self, event):
        self.book.ChangeSelection(4)

    def OnFileImportCate(self, event):
        dlg = dialogs.ImportCateDialog(self)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            if not path:
                dlg.Destroy()
                return
            exp = export.DataImport(self.db, 'gbk')
            try:
                exp.category(path)
            except Exception, e:
                logfile.info(traceback.format_exc())
                wx.MessageBox(str(e), _('Import Error:'), wx.OK|wx.ICON_INFORMATION)
            else:
                wx.MessageBox(_('Import complete!'), _('Information'), wx.OK|wx.ICON_INFORMATION)
            self.reload()
        dlg.Destroy()

    def OnFileImportData(self, event):
        dlg = dialogs.ImportDataDialog(self)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            if not path:
                dlg.Destroy()
                return
 
            exp = export.DataImport(self.db, 'gbk')
            try:
                idlg = wx.ProgressDialog(_('Importing...'), _('Waiting for importing.'), 
                                        maximum=100, parent=self,
                                        style=wx.PD_APP_MODAL|wx.PD_ELAPSED_TIME|wx.PD_REMAINING_TIME)
                exp.itemdata(path, idlg)
                idlg.Destroy()
            except Exception, e:
                logfile.info(traceback.format_exc())
                wx.MessageBox(str(e), _('Import Error:'), wx.OK|wx.ICON_INFORMATION)
            else:
                wx.MessageBox(_('Import complete!'), _('Information'), wx.OK|wx.ICON_INFORMATION)
            self.reload()
 
        dlg.Destroy()

    def OnFileExportCate(self, event):
        dlg = wx.FileDialog(
            self, message=_("Export Category"), defaultDir=os.getcwd(), 
            defaultFile="", wildcard=_("csv file (*.csv)|*.csv"), style=wx.SAVE)
        dlg.SetFilterIndex(2)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            exp = export.DataExport(self.db, 'gbk')
            try:
                exp.category(path)
            except Exception, e:
                logfile.info(traceback.format_exc())
                wx.MessageBox(str(e), _('Export Error:'), wx.OK|wx.ICON_INFORMATION)
        dlg.Destroy()

    def OnFileExportData(self, event):
        dlg = wx.FileDialog(
            self, message=_("Export Data"), defaultDir=os.getcwd(), 
            defaultFile="", wildcard=_("csv file (*.csv)|*.csv"), style=wx.SAVE)
        dlg.SetFilterIndex(2)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            exp = export.DataExport(self.db, 'gbk')
            try:
                exp.itemdata(path)
            except Exception, e:
                logfile.info(traceback.format_exc())
                wx.MessageBox(str(e), _('Export Error:'), wx.OK|wx.ICON_INFORMATION)
 
        dlg.Destroy()


    def OnSync(self, event):
        dlg = dialogs.SyncDialog(self, self.conf)
        dlg.CenterOnParent()

        if dlg.ShowModal() == wx.ID_OK:
            ret = dlg.value()
            #self.conf['sync_auto'] = str(ret)
            if ret != self.conf['sync_way']:
                self.conf['sync_way'] = ret
                self.conf.dump()
            
            if ret:
                sync.synchronization(self)
                self.reload()

        dlg.Destroy()
 

