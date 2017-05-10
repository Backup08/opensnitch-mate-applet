#!/usr/bin/env python
 
# ensure we are using Gtk 2, not Gtk3
# this will print a warning but everything should work
import gi
gi.require_version("Gtk", "3.0")
gi.require_version('MatePanelApplet', '4.0')
 
from gi.repository import Gtk
from gi.repository import MatePanelApplet
from threading import Timer
from gi.repository import GLib
import time
import socket
import os

class TimeLabel(Gtk.Image):
    def __init__(self):
        Gtk.Image.__init__(self)
        GLib.timeout_add_seconds(1, self.updateTime)
        self.updateTime()


    def updateTime(self):
        timeStr = self.getTime()

        status = pname_exists('opensnitch') 
        if status == 1:
            self.set_from_file("/usr/share/icons/snitch/online.png")
        else:
            self.set_from_file("/usr/share/icons/snitch/offline.png")

        return GLib.SOURCE_CONTINUE

    def getTime(self):
       return time.strftime("%c")



def pname_exists(inp):
    os.system('ps -ef > /tmp/psef')
    lines=open('/tmp/psef', 'r').read().split('\n')
    res=[i for i in lines if inp in i]
    return True if res else False


def applet_fill(applet):
    global label  
    # you can use this path with gio/gsettings
    settings_path = applet.get_preferences_path()
 
    label = TimeLabel()
    #label = Gtk.Label("OpenSnitch")
    applet.add(label)
    applet.show_all()
 
def applet_factory(applet, iid, data):
    #if iid != "OpensnitchApplet":
    #   return False
 
    applet_fill(applet)
 
    return True
 
MatePanelApplet.Applet.factory_main("SnitchAppletFactory", True,
                                    MatePanelApplet.Applet.__gtype__,
                                    applet_factory, None)

