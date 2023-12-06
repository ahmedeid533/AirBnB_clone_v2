#!/usr/bin/python3
"""genrate.tgz file"""
from fabric import Connection
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
    """do_deploy function"""
    env = {
        "hosts": ['54.89.57.165', '18.207.142.135'],
        "user": "your_username",
    }
    if not os.path.exists(archive_path):
        print(f"Archive '{archive_path}' does not exist.")
        return False

    try:
        for host in env["hosts"]:
            with Connection(host=host, user=env["user"]) as conn:
                filename = os.path.basename(archive_path)
                folder = os.path.splitext(filename)[0]

                remote_tmp_path = f'/tmp/{filename}'
                remote_release = f'/data/web_static/releases/{folder}/'
                current_link = '/data/web_static/current'

                conn.put(archive_path, remote_tmp_path)
                conn.run(f'mkdir -p {remote_release}')
                conn.run(f'tar -xzf {remote_tmp_path} -C {remote_release}')
                conn.run(f'rm {remote_tmp_path}')

                conn.sudo(f'rm -rf {current_link}')
                conn.sudo(f'ln -s {remote_release} {current_link}')

                print('New version deployed!')

        return True
    except Exception as e:
        return False
