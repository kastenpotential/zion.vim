import vim
import logging
import weakref
import inspect


log = logging.getLogger()
FocusGained = "FocusGained"


class GlobalEvent(object):
    """GlobalEvents Decorator"""
    _event_dict = dict()

    def __init__(self, event, pattern="*"):
        """Init Global Events """
        self._event = event
        self._pattern = pattern

    def __call__(self, func):
        # called once as part of decoration process
        log.debug("event=%s pattern=%s func=%s", self._event, self._pattern, func.__qualname__)
        # self.addEvent(self._event, func)
        func._event_name = self._event
        func._event_pattern = self._pattern
        return func

    def addEvent(self, name, func):
        if name not in GlobalEvent._event_dict:
            GlobalEvent._event_dict[name] = list()
        ref = weakref.WeakMethod(func)
        GlobalEvent._event_dict[name].append(ref)

    @classmethod
    def register(cls, obj):
        for _, func in inspect.getmembers(obj, predicate=inspect.ismethod):
            # print(func)
            if hasattr(func, "_event_name"):
                name = getattr(func, "_event_name")
                log.debug("register event listener method=%s event=%s", func.__qualname__, name)
                if name not in cls._event_dict:
                    log.debug("new event")
                    cls._event_dict[name] = list()
                ref = weakref.WeakMethod(func)
                cls._event_dict[name].append(ref)
                vim.command("autocmd FocusGained * nested py3 pv.sendEvent('FocusGained')")

