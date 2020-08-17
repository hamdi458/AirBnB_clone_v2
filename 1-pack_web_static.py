#!/usr/bin/python3
"""Module"""
from fabric.api import *
from datetime import datetime
import time


def do_pack():
    """generates a .tgz archive"""
    time_file = time.strftime('%Y%m%d%H%M%S')
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{:s}.tgz web_static/".format(time_file))
        return ("versions/web_static_{}.tgz".format(time_file))
    except path:
        return None
