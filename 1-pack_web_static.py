#!/usr/bin/env python3
'''Fabric script to generate .tgz archive'''

from fabric.api import local
from datetime import datetime

from fabric.decorators import runs_once


@runs_once
def generate_archive():
    '''Generates a .tgz archive from the contents of the web_static folder'''
    local("mkdir -p versions")
    archive_path = ("versions/web_static_{}.tgz"
            .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    result = local("tar -cvzf {} web_static"
                   .format(archive_path))

    if result.failed:
        return None
    return archive_path

