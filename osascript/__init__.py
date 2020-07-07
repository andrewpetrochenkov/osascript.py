__all__ = ['run', 'osascript']


import os
from tempfile import mkstemp
import runcmd


def tempfile():
    """create temp file and return path"""
    f, path = mkstemp()
    os.close(f)
    return path


def run(applescript, background=False):
    """run applescript file/code"""
    if os.path.exists(applescript):
        path = applescript
    else:
        path = tempfile()
        open(path, "w").write(applescript)
    cmd = ["osascript", path]
    r = runcmd.run(cmd, background=background)
    return r.code, r.out, r.err


def osascript(applescript, background=False):
    """run applescript file/code. deprecated"""
    return run(applescript, background=False)
