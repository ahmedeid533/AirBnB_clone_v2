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
    try:
        for host in env.hosts:
            env.host_string = host
            filename = archive_path.split('/')[-1]
            up_filename = filename.split('.')[0]
            put(archive_path, '/tmp/')
            run(f'mkdir -p /data/web_static/releases/{up_filename}/')
            run(f'tar -xzf /tmp/{up_filename}.tgz -C \
                /data/web_static/releases/{up_filename}/')
            run(f'rm /tmp/{up_filename}.tgz')
            run(f'mv /data/web_static/releases/{up_filename}/web_static/* \
                /data/web_static/releases/{up_filename}/')
            run(
                f'rm -rf /data/web_static/releases/{up_filename}/web_static')
            run(f'rm -rf /data/web_static/current')
            run(f'ln -s /data/web_static/releases/{up_filename}/ \
                /data/web_static/current')
            print('New version deployed!')

        return True
    except Exception as err:
        return False
