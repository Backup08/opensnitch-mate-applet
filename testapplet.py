#!/usr/bin/env python
 
# this code is based on example appet by Vincent Untz for GNOME Panel 3
# http://git.gnome.org/browse/gnome-panel/commit/?id=5ad4d9e
 
# ensure we are using Gtk 2, not Gtk3
# this will print a warning but everything should work
import gi
gi.require_version("Gtk", "2.0")
 
from gi.repository import Gtk
from gi.repository import MatePanelApplet
 
def applet_fill(applet):
 
    # you can use this path with gio/gsettings
    settings_path = applet.get_preferences_path()
 
    label = Gtk.Label("My MATE applet in Python")
    applet.add(label)
    applet.show_all()
 
def applet_factory(applet, iid, data):
    if iid != "TestApplet":
       return False
 
    applet_fill(applet)
 
    return True
 
MatePanelApplet.Applet.factory_main("TestAppletFactory", True,
                                    MatePanelApplet.Applet.__gtype__,
                                    applet_factory, None)

