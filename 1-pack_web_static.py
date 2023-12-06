#!/usr/bin/python3
"""store data(archives) in specfic folder"""
from fabric import task
from datetime import datetime
import os


@task
def do_pack(c):
    """do_pack funcation"""
    source_folder = 'web_static'
    target_folder = 'versions'
    c.run(f'mkdir -p {target_folder}')
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = f'web_static_{timestamp}.tgz'
    archive_path = os.path.join(target_folder, archive_name)
    result = c.run(f'tar -cvzf {archive_path} {source_folder}')
    if result.ok:
        return archive_path
    else:
        return None
