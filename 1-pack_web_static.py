#!/usr/bin/python3
"""Fabric script"""

from fabric.api import local
from datetime import datetime
import time


def do_pack():
    """do_pack"""
    try:
        tiime = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(tiime)
        local('mkdir -p versions')
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except BaseException:
        return None
