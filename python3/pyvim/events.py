import vim
import logging
import weakref
import inspect


log = logging.getLogger(__name__)

# when vim got imput focus (only for GUI version)
FocusGained = "FocusGained"
# when vim lost imput focus (only for GUI version, may happen on dialog popup)
FocusLost = "FocusLost"
# just after entering a tab page (WinEnter -> TabEnter -> BufEnter)
TabEnter = "TabEnter"
# just before leaving a tab page (WinLeave -> TabLeave)
TabLeave = "TabLeave"
# after entering a buffer. useful for setting filetype. after BufReadPost
BufEnter = "BufEnter"

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
                cmd = "autocmd {0} * nested py3 pv.sendEvent('{0}')".format(name)
                log.debug("cmd=%s", cmd)
                vim.command(cmd)

    @classmethod
    def notify(cls, event_name):
        event_methods = cls._event_dict.get(event_name)
        if event_methods:
            log.debug("%s events found for %s", len(event_methods), event_name)
            try:
                for ref in event_methods:
                    method = ref()
                    method()
            except Exception as ex:
                log.exception(ex)
        else:
            log.debug("no events found for %s", event_name)

