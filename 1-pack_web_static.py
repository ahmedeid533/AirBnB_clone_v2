#!/usr/bin/python3
"""genrate.tgz file"""

from fabric.api import local, task
from datetime import datetime


def do_pack():
    """archive web_static"""
    try:
        time_now = datetime.now().strftime('%Y%m%d%H%M%S')
        nameOfFile = 'web_static_{}.tgz'.format(time_now)
        local("mkdir -p versions")
        local("tar -cvzf versions/{} web_static".format(nameOfFile))
        return "versions/{}".format(nameOfFile)
    except Exception:
        return None
