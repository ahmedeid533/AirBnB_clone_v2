#!/usr/bin/python3
"depoly by fabric"
from fabric.api import *
from fabric import task
from datetime import datetime
import os


env.hosts = ['54.89.57.165', '18.207.142.135']
env.user = "ubuntu"


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
    """fuck fabric depoly by command"""
    if not os.path.exists(archive_path):
        return (False)
    try:
        li = archive_path.split('/')
        file_name = li[-1]
        path_of_releases = "/data/web_static/releases/{}/".format(
            file_name[:-4])
        path_of_tmp = "/tmp/{}".format(file_name)
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path_of_releases))
        run("tar -xzf {} -C {}".format(path_of_tmp, path_of_releases))
        run("rm {}".format(path_of_tmp))
        run("mv {}web_static/* {}".format(path_of_releases, path_of_releases))
        run("rm -rf {}web_static".format(path_of_releases))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(path_of_releases))
        print("New version deployed!")
        return (True)
    except Exception:
        return (False)
