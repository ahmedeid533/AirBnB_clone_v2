#!/usr/bin/python3
"depoly by fabric"
from MySQLdb import Connection
from fabric.api import *
from fabric import task
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
    """Deploy web_static to servers"""
    env = {
        "hosts": ['35.153.79.242', '52.201.164.137'],
        "user": "your_username"  # Replace with your actual username
    }
    if not os.path.exists(archive_path):
        return False

    try:
        for host in env["hosts"]:
            with Connection(host=host, user=env["user"]) as conn:
                filename = os.path.basename(archive_path).split('.')[0]
                remote_tmp = f'/tmp/{filename}.tgz'
                remote_release = f'/data/web_static/releases/{filename}/'

                conn.put(archive_path, remote_tmp)
                conn.run(f'mkdir -p {remote_release}')
                conn.run(f'tar -xzf {remote_tmp} -C {remote_release}')
                conn.run(f'rm {remote_tmp}')
                conn.run(f'mv {remote_release}web_static/* {
                    remote_release}')
                conn.run(f'rm -rf {remote_release}web_static')
                conn.run(f'rm -rf /data/web_static/current')
                conn.run(f'ln -s {remote_release} /data/web_static/current')
                print(f'New version deployed to {host}!')

        return True
    except Exception:
        return False
