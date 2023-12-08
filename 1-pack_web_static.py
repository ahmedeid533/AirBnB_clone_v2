#!/usr/bin/python3
"""genrate.tgz file"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """archive web_static"""
    time = datetime.now().strftime('%Y%m%d%H%M%S')
    name_we = 'web_static_{}.tgz'.format(time)
    local("mkdir -p versions")
    create = local("tar -cvzf versions/{} web_static".format(name_we))
    if create is not None:
        return name_we
    else:
        return None
