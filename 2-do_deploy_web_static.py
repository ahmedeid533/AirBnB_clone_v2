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
    env.user = "ubuntu"
    if not os.path.exists(archive_path):
        return (False)

    try:
        li = archive_path.split('/')[-1]

        path_of_releases = f"/data/web_static/releases/{li[:-4]}/"
        path_of_tmp = f"/tmp/{li}"

        put(archive_path, "/tmp/")
        run(f"mkdir -p {path_of_releases}")
        run(f"tar -xzf {path_of_tmp} -C {path_of_releases}")
        run(f"rm {path_of_tmp}")
        run(f"mv {path_of_releases}web_static/* {path_of_releases}")
        run(f"rm -rf {path_of_releases}web_static")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s {path_of_releases} /data/web_static/current")
        print("New version deployed!")
        return (True)
    except Exception:
        return (False)
