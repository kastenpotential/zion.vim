# -*- coding: utf-8 -*-
"""
Config Module for Zion / PyVim.
"""

conf = None


class Config(object):
    """ Default configurations for Zion / PyVim. """

    plugins = [
        "pyvim.eventlogger.EventLogger",
        "pyvim.tabline.TabLine",
        "pyvim.textmanipulation.TextManipulation"
    ]

    def __init__(self):
        """ Loads the default config. """
        pass


def init():
    global conf
    if not conf:
        conf = Config()
    return conf
