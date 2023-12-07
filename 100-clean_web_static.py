#!/usr/bin/python3
"""use .tgz file"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = ["100.25.215.68", "100.25.147.204"]
env.user = "ubuntu"


def do_pack():
    """web_static"""
    try:
        time = datetime.now().strftime('%Y%m%d%H%M%S')
        name_we = 'web_static_{}.tgz'.format(time)
        local("mkdir -p versions")
        local("tar -cvzf versions/{} web_static".format(name_we))
        return "versions/{}".format(name_we)
    except Exception:
        return None


def do_deploy(archive_path):
    """deploy"""

    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True


def deploy():
    """Create and distribute"""
    file_pa = do_pack()
    if file_pa is None:
        return False
    return do_deploy(file_pa)


def do_clean(number):
    """clean unwanted versions"""
    result = local("ls versions/", hide=True)
    output_lines = result.stdout.splitlines()
    file_names = [line.strip() for line in output_lines]
    file_names.sort()
    if number < 1:
        number = 1
    rm_files = file_names[0:-number]
    for file in rm_files:
        f_n = file.split(".")[0]
        if run("rm -rf /data/web_static/releases/{}/".
               format(f_n)).failed is True:
            return False
        local("rm -rf versions/{}".format(file))
