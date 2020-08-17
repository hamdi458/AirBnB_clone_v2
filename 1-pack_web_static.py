#!/usr/bin/python3
"""Fabric script"""

from fabric.api import local
from datetime import datetime
import time


def do_pack():
    tiime = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(tiime)
    if local('mkdir -p versions').failed is True or local(
            "tar -cvzf {} web_static".format(archive_path)).failed is True:
        return None
    return archive_path
