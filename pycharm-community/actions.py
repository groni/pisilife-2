#!/usr/bin/python

from pisi.actionsapi import get, pisitools, shelltools

WorkDir = "."
NoStrip = ["/"]

def install():
    #shutil.rmtree("pycharm-community-2016.2.3/jre")
    pisitools.insinto("/opt/pycharm-community", "pycharm-community-2017.2.3/*")
    pisitools.dosym("/opt/pycharm-community/bin/pycharm.sh", "/usr/bin/pycharm-community")
