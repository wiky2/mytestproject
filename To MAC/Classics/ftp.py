# notice if listLocal got click
        def actionLocal(self, widget, event):
                if event.type == gtk.gdk._2BUTTON_PRESS:
                        data = self.getSelection("local")
                        if data == "..": # parent directory
                                os.chdir("..")
                                self.listLocal() #refresh
                        else:
                                pbackup = os.getcwd() #path backup
                                try:
                                        p = os.getcwd()+"/"+data
                                        os.chdir(p)
                                        self.listLocal() #refresh

                                except NameError:
                                        print "Not directory"
                                        os.chdir(pbackup)

                elif event.type == gtk.gdk.BUTTON_PRESS and event.button == 3:
                        popmenu_items = {"Remove": self.removeLocal, "Refresh": self.refreshLocal} #menuitems (Name, action)
                        self.listPopMenu(popmenu_items, event.button)

        # notice if listFtp got click
        def actionFtp(self, widget, event):
                if event.type == gtk.gdk._2BUTTON_PRESS:
                        data = self.getSelection("ftp")
                        if data == "..": # parent directory
                                p = self.ftp.pwd().rfind("/")
                                if p == 0:
                                        self.ftp.cwd("/")
                                else:
                                        self.ftp.cwd(self.ftp.pwd()[:p])
                                self.listFtp() #refresh

                        else:
                                try:
                                        p = self.ftp.pwd()+"/"+data
                                        self.ftp.cwd(p)
                                        self.listFtp() #refresh

                                except ftplib.error_perm:
                                        print "Not directory"

                elif event.type == gtk.gdk.BUTTON_PRESS and event.button == 3:
                        popmenu_items = {"Remove": self.removeFtp, "New dir": self.newDir, "Refresh": self.refreshFtp} #menuitems (Name, action)
                        self.listPopMenu(popmenu_items, event.button)

        # local funcs
        def putFile(self, event):
                try:
                        data = self.getSelection("local")
                        file = open(os.getcwd()+"/"+data, 'rb')
                        self.ftp.storbinary("STOR "+data, file)
                        file.close()
                        self.listFtp() #refresh

                except IOError:
                        print data+" is directory"

        def removeLocal(self, event):
                selection = self.getSelection("local")
                #file
                try:
                        os.remove(selection)
                        self.listLocal() #refresh

                #dir
                except:
                        os.rmdir(selection)
                        self.listLocal() #refresh

        def refreshLocal(self, event):
                self.listLocal() #refresh

        # ftp funcs
        def getFile(self, event):
                data = self.getSelection("ftp")
                outfile = file(data, 'w+b')
                self.ftp.retrbinary("RETR "+data, outfile.write)
                self.listLocal() #refresh

        def removeFtp(self, event):
                selection = self.getSelection("ftp")
                #file
                try:
                        self.ftp.delete(selection)
                        self.listFtp() #refresh

                #dir
                except:
                        self.ftp.rmd(selection)
                        self.listFtp() #refresh

        # create new directory to FTP server
        # first open dialog window 
        def newDir(self, event, id=None, action="dialog"):
                if action == "dialog":
                        self.ndd = gtk.Dialog("New directory")
                        self.nde = gtk.Entry()
                        self.ndd.add_action_widget(self.nde, 0)
                        self.ndd.add_button("Create", 1)
                        self.ndd.show_all()
                        self.ndd.connect("response", self.newDir, "create")

                elif action == "create":
                        try:
                                dirname = self.nde.get_text()
                                self.ftp.mkd(dirname)
                                self.ndd.destroy()
                                self.listFtp() #refresh
                        except:
                                print "close"

        def refreshFtp(self, event):
                self.listFtp() #refresh

        # Generates gtk.Menu content
        # menu = gtk.Menu() object 
        # menu_items_dic is dictionary where key is menu item name (str) and value is callback function (def)
        def menuItemsAdd(self, menu, menu_items_dic):
                for item in menu_items_dic.keys():
                                menu_item = gtk.MenuItem(item)
                                menu_item.connect("activate", menu_items_dic[item])
                                menu.append(menu_item)
                                menu_item.show()

        # Generates popupmenu content when you click listLocal or listFtp with button 3 (right button)
        # items is dictionary where key is menu item name (str) and value is callback function (def)
        def listPopMenu(self, items, button):
                self.popmenu = gtk.Menu()
                self.menuItemsAdd(self.popmenu, items)
                self.popmenu.popup(None, None, None, button, 0, None)

        #login to the ftp server and creates listFtp and listLocal liststores
        def loginFTP(self, widget):
                try:
                        self.ftp = ftplib.FTP(self.login_host.get_text())
                        print "connected host: %s" % self.login_host.get_text()
                        self.ftp.login(self.login_name.get_text(),self.login_pw.get_text())
                        print "logged user: %s" % self.login_name.get_text()

                        self.window.resize(600, 400)

                        self.vbox_logged = gtk.VBox()
                        self.window.remove(self.vbox_login)
                        self.window.add(self.vbox_logged)
                        
                        self.vbox_login.remove(self.menu_bar)
                        self.menu_bar.prepend(self.root_menu)
                        self.vbox_logged.pack_start(self.menu_bar, False, False, 2)

                        put_img = gtk.image_new_from_stock(gtk.STOCK_GO_FORWARD, gtk.ICON_SIZE_MENU)
                        get_img = gtk.image_new_from_stock(gtk.STOCK_GO_BACK, gtk.ICON_SIZE_MENU)
                        quit_img = gtk.image_new_from_stock(gtk.STOCK_QUIT, gtk.ICON_SIZE_MENU)

                        put_but = gtk.ToolButton(put_img, "Put")
                        put_but.connect("clicked", self.putFile)
                        get_but = gtk.ToolButton(get_img, "Get")
                        get_but.connect("clicked", self.getFile)
                        quit_but = gtk.ToolButton(quit_img, "Quit")
                        quit_but.connect("clicked", self.kill)

                        self.actions = gtk.Toolbar()
                        self.actions.set_orientation(gtk.ORIENTATION_VERTICAL)
                        self.actions.set_style(gtk.TOOLBAR_ICONS)
                        putitem = self.actions.insert(put_but, -1)
                        getitem = self.actions.insert(get_but, -1)
                        quititem = self.actions.insert(quit_but, -1)

                        self.hbox = gtk.HBox()

                        self.listLocal(False) #create list
                        self.hbox.pack_start(self.actions, False, False) # get and put buttons
                        self.listFtp(False) #create list

                        self.vbox_logged.pack_start(self.hbox)
                        
                        self.menu_bar.show_all()
                        self.actions.show_all()
                        self.hbox.show_all()
                        put_img.show()
                        get_img.show()
                        quit_img.show()
                        self.vbox_logged.show_all()

                except ftplib.error_perm:
                        self.error = gtk.Label("Wrong username or password, try again.")
                        self.vbox_login.pack_start(self.error)
                        self.vbox_login.show_all()
                        print "wrong username or password"

        # logout from ftp server and reshow login entrys
        def logoutFTP(self, event):
                self.ftp.close()
                self.window.remove(self.vbox_logged)
                self.window.add(self.vbox_login)
                self.window.resize(200, 100)
                self.vbox_login.show_all()
        
        # kill program and logout if connection is still open
        def kill(self, event):
                if bool(self.ftp) == True:
                        self.ftp.close()
                        gtk.main_quit()
                        print "logout & quit"
                else:
                        gtk.main_quit()
                        print "quit"
   
        def main(self):
                gtk.main()

miniFTP().main()