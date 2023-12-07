#!/usr/bin/python3
"""use .tgz file"""

from fabric.api import *
from datetime import datetime
import os

@task
def do_pack():
    """web_static"""
    try:
        time = datetime.now().strftime('%Y%m%d%H%M%S')
        name = 'web_static_{}.tgz web_static'.format(time)
        local("mkdir -p versions")
        local("tar -cvzf versions/{}".format(name))
        return "versions/"
    except Exception:
        return None


@task
def do_deploy(archive_path):
    """deploy"""
    env.hosts = ['100.25.215.68', '100.25.147.204']
    env.user = "ubuntu"
    if not os.path.exists(archive_path):
        print("false")
        return (False)
    else:
        print("true")
        return True
