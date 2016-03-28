# -*- coding: utf-8 -*-
"""
Python3 support for Vim.
"""
from pyvim import logger
# from pyvim.events import GlobalEvents
from pyvim import config
import importlib
import vim


events = None  # global vim events
plugins = {}
log = None


def init():
    """ Initializes the Python Vim extension. """
    global log
    conf = config.Config()
    log = logger.init()
    global events
    events = GlobalEvents()
    for plugin_name in conf.plugins:
        try:
            print(plugin_name)
            module_name, class_name = plugin_name.rsplit(".", 1)
            PluginClass = getattr(importlib.import_module(module_name), class_name)
            plugin_instance = PluginClass()
            plugins[plugin_name] = plugin_instance
        except Exception as ex:
            log.error("unable to initialize %s", plugin_name)
            log.exception(ex)


def on(event, callback):
    cmd = "autocmd {0} * nested py3 {1}()".format(event.name, callback)
    log.debug("cmd=%s", cmd)
    # vim.command(cmd)

init()
