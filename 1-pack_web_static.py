#!/usr/bin/python3
"""
Generates a .tgz archive from the contents
of the web_static folder of the AirBnB Clone repo
"""
from fabric.api import local
from time import strftime
from datetime import datetime


def do_pack():
    """ Function that makes a packs """

    try:
        now = datetime.now()
        date_create = now.strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        do_tgz = "web_static_{}.tgz".format(date_create)
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(do_tgz))

        return do_tgz
    except Exception as e:
        return None
