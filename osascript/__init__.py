#!/usr/bin/env python
import os
import public
import runcmd
import temp


@public.add
def run(applescript, background=False):
    """run applescript file/code"""
    if os.path.exists(applescript):
        path = applescript
    else:
        path = temp.tempfile()
        open(path, "w").write(applescript)
    cmd = ["osascript", path]
    r = runcmd.run(cmd, background=background)
    return r.code, r.out, r.err


@public.add
def osascript(applescript, background=False):
    """run applescript file/code. deprecated"""
    return run(applescript, background=False)
