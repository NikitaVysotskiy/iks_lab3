import time

from version_generator import get_version

version = None


def main():
    global version
    version = get_version()
    time.sleep(5)
    do_something_with_version(version)


def do_something_with_version(v):
    print(v)


if __name__ == '__main__':
    main()
