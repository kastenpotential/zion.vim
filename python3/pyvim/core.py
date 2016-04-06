"""
Core library for Zion / PyVim.
"""
import vim
import importlib
from pyvim import logger, config, events


log = None


class PyVimCore(object):
    """docstring for PyVimCor """

    def __init__(self):
        self.conf = config.init()
        global log
        log = logger.init()
        self._plugins = {}
        for plugin in self.conf.plugins:
            self.loadPlugin(plugin)

    def loadPlugin(self, plugin_name):
        try:
            log.debug(plugin_name)
            module_name, class_name = plugin_name.rsplit(".", 1)
            log.debug("module_name=%s class_name=%s", module_name, class_name)
            module = importlib.import_module(module_name)
            PluginClass = getattr(module, class_name)
            plugin_instance = PluginClass()
            self._plugins[plugin_name] = plugin_instance
            events.GlobalEvent.register(plugin_instance)
            events.KeyEvent.register(plugin_instance)
        except Exception as ex:
            log.error("unable to initialize plugin %s", plugin_name)
            log.exception(ex)

    def sendEvent(self, name):
        log.debug("name=%s", name)
        events.GlobalEvent.notify(name)

    def showDebug(self):
        print("hello debug")


def init():
    """Initializes the core library."""
    from pyvim import pv
    pv.__core__ = PyVimCore()
    from pyvim.window import WindowManager
    pv.__win__ = WindowManager()
    return pv
