#!/usr/bin/python3
"""1. Compress before sending"""
from fabric.api import local
from datetime import datetime
from os import makedirs
from os.path import exists

def do_pack():
    """1. Compress before sending"""
    try:
        if not exists("versions"):
            makedirs("versions")
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        ac_name = "versions/web_static_{}.tgz".format(now)
        local("tar -czvf {} web_static".format(ac_name))
        return ac_name
    except Exception:
        return None
