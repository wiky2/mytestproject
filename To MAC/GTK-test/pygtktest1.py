'''
Created on 2010-3-18

@author: Administrator
'''
import pygtk
import gtk
 
def createWindow():
    window = gtk.Window()
    window.set_default_size(200, 200)
    window.connect('destroy', gtk.main_quit)
 
    label = gtk.Label('Hello World')
    window.add(label)
 
    label.show()
    window.show()
 
createWindow()
gtk.main()
