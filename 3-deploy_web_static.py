#!/usr/bin/python3
"""genrate.tgz file"""

from fabric.api import *
from datetime import datetime
import os


@task
def do_pack():
    """archive web_static"""
    try:
        time_now = datetime.now().strftime('%Y%m%d%H%M%S')
        nameOfFile = 'web_static_{}.tgz web_static'.format(time_now)
        local("mkdir -p versions")
        local("tar -cvzf versions/{}".format(nameOfFile))
        return "versions/"
    except Exception:
        return None


@task
def do_deploy(archive_path):
    """deploy function"""
    env.hosts = ['54.89.57.165', '18.207.142.135']
    if not os.path.exists(archive_path):
        return False
    else:
        return True


@task
def deploy():
    """deploy function"""
    try:
        path = do_pack()
        if path is None:
            return False
        return do_deploy(path)
    except Exception as e:
        return False
