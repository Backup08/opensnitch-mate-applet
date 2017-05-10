#!/bin/sh

cp org.mate.panel.OpensnitchApplet.mate-panel-applet /usr/share/mate-panel/applets/
cp org.mate.panel.applet.OpensnitchAppletFactory.service /usr/share/dbus-1/services/

chmod 755 snitch.py
cp snitch.py /usr/local/bin

mkdir /usr/share/icons/snitch

cp images/online.png /usr/share/icons/snitch
cp images/offline.png /usr/share/icons/snitch


