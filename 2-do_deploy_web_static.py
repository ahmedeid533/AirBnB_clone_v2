
"""genrate.tgz file"""

from fabric.api import local, task, env
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
    env.hosts = ['100.25.215.68', '100.25.147.204']
    env.user = "ubuntu"
    if not os.path.exists(archive_path):
        return (False)
    else:
        return True
