from os import path, walk, remove, rmdir
from datetime import datetime
import logging

"""
    Deleting files and directories by given TTL:
    1. PATH - Directory to watch.
    2. FILES_TTL and DIR_TTL time to live before delete in seconds.

"""


PATH = '/Users/matvejkorcev/Documents/watch_dog'
FILES_TTL = 60
DIR_TTL = 120


def get_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    fmt = logging.Formatter('%(asctime)s %(processName)s: %(name)s %(levelname)s: %(message)s', None)
    ch.setFormatter(fmt)
    logger.addHandler(ch)

    return logger


def remove_by_ttl(root, name):
    full_path = path.join(root, name)
    create_date = datetime.fromtimestamp(path.getctime(full_path))
    if path.isdir(full_path):
        if (datetime.now() - create_date).seconds > DIR_TTL:
            rmdir(full_path)
            logger.info(f'Directory {full_path} removed')
    else:
        if (datetime.now() - create_date).seconds > FILES_TTL:
            remove(full_path)
            logger.info(f'File {full_path} removed')


if __name__ == '__main__':
    logger = get_logger()
    logger.info(f'Watching directory {PATH}')
    while True:
        for root, dirs, files in walk(PATH, topdown=False):
            for name in files:
                remove_by_ttl(root, name)
            for name in dirs:
                remove_by_ttl(root, name)