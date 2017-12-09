import os


def get_version():
    return os.popen('git describe --tags').read().strip()
