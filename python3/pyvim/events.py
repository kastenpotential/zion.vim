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


class BaseEvent(object):
    """BaseEvent Decorator and Multiplexer"""
    _event_dict = None
    _event_command = None
    _event_type = None

    def __init__(self, event_name):
        """Init Events """
        self._event_name = event_name
        log.debug("event_type=%s event_name=%s", self._event_type, self._event_name)

    def __call__(self, func):
        # called once as part of decoration process
        log.debug("event_type=%s event_name=%s func=%s", self._event_type, self._event_name, func.__qualname__)
        # self.addEvent(self._event_name, func)
        func._event_type = self._event_type
        func._event_name = self._event_name
        return func

    @classmethod
    def register(cls, obj):
        log.debug("register events for type: %s", cls._event_type)
        for _, func in inspect.getmembers(obj, predicate=inspect.ismethod):
            event_type = getattr(func, "_event_type", None)
            log.debug("event_type=%s cls._event_type=%s", event_type, cls._event_type)
            if event_type == cls._event_type:
                log.debug("event type found")
                event_name = getattr(func, "_event_name")
                log.debug("func=%s event_name=%s", func.__qualname__, event_name)
                if event_name not in cls._event_dict:
                    log.debug("new event")
                    cls._event_dict[event_name] = list()
                ref = weakref.WeakMethod(func)
                cls._event_dict[event_name].append(ref)
                format_dict = {
                    "event_name": event_name,
                    "event_type": cls._event_type
                }
                cmd = cls._event_command.format(**format_dict)
                log.debug("cmd=%s", cmd)
                vim.command(cmd)
        log.debug("done.")

    @classmethod
    def notify(cls, event_name):
        log.debug("notify events for type: %s", cls._event_type)
        event_methods = cls._event_dict.get(event_name)
        if event_methods:
            log.debug("%s events found for %s", len(event_methods), event_name)
            try:
                for ref in event_methods:
                    method = ref()
                    method()
            except Exception as ex:
                log.exception(ex)
                # log.debug("args=%s", list(ex.args))
                vim.command("echom '{}'".format(ex.args[0]))
        else:
            log.debug("no events found for %s", event_name)
        log.debug("done.")


class GlobalEvent(BaseEvent):
    """Docstring for GlobalEvent. """
    _event_dict = dict()
    # _event_command = "echom 'GlobalEvent {event_name}'"
    _event_command = "autocmd {event_name} * nested py3 pv.send_global_event('{event_name}')"
    _event_type = "GlobalEvent"

    def __init__(self, event_name):
        """TODO: to be defined1. """
        BaseEvent.__init__(self, event_name)


class KeyEvent(BaseEvent):
    """Docstring for KeyEvent. """
    _event_dict = dict()
    _event_command = "nnoremap {event_name} :py3 pv.send_key_event('{event_name}')<cr>"
    _event_type = "KeyEvent"

    def __init__(self, event_name):
        """TODO: to be defined1. """
        leader = vim.vars.get("mapleader")
        localleader = vim.vars.get("maplocalleader")
        log.debug("leader=%s localleader=%s", leader, localleader)
        if leader:
            event_name = event_name.replace("<leader>", leader.decode())
        if localleader:
            event_name = event_name.replace("<localleader>", localleader.decode())
        BaseEvent.__init__(self, event_name)





class GlobalEvent_(object):
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
                cmd = "autocmd {0} * nested py3 pv.send_event('{0}')".format(name)
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

