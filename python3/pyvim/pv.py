# -*- coding: utf-8 -*-
"""
Python3 support for Vim.
"""
from pyvim import events
import vim


__core__ = None  # the python core
__win__ = None  # the window manager


def send_global_event(name):
    events.GlobalEvent.notify(name)


def send_key_event(name):
    events.KeyEvent.notify(name)


def get_window(nr):
    """Returns the window with the given number."""
    __win__.get_window(nr)


def window():
    return __win__.current()


def buffer():
    return __win__.current().buffer

