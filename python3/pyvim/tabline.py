from pyvim.plugin import Plugin
import logging
import os
import vim
from pyvim import events


log = logging.getLogger(__name__)

""" %1T%#TabLineSel# 1 tmp.vim + %2T%#TabLine# 2 [bka Name] %#TabLineFill#%#bka# mymymy """


class TabSegment(object):

    def __init__(self, nr, name, current=False):
        self.name = name or "[Empty]"
        self.nr = nr
        self.current = current
        self.style = "TabLineSel" if current else "TabLine"

    def render(self):
        return "%{nr}T%#{style}#{nr} {name}".format(**vars(self))


class TabSegmentFill(object):

    def render(self):
        return "%#TabLineFill#%T"


class TabSegmentRight(object):

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def render(self):
        return "%=%#TabLine#{count} {name}".format(**vars(self))


class TabLine(Plugin):

    """Test plugin just logging some events."""

    def __init__(self):
        """Initializes the plugin. """
        log.info("TabLine initialized.")
        self._segments = []

    def __del__(self):
        log.info("TabLine deleted.")

    def update(self):
        self._segments.clear()
        for tab in vim.tabpages:
            name = os.path.basename(tab.window.buffer.name)
            current = tab == vim.current.tabpage
            log.debug("%s %s %s", tab.number, name, current)
            self._segments.append(TabSegment(tab.number, name, current))
        self._segments.append(TabSegmentFill())
        self._segments.append(TabSegmentRight("tabs", len(vim.tabpages)))

    def render(self):
        tab_str = " ".join([s.render() for s in self._segments])
        log.debug(tab_str)
        vim.options["tabline"] = tab_str

    @events.GlobalEvent(events.TabEnter)
    def onTabEnter(self):
        """Log the event TabEnter."""
        log.debug("onTabEnter called.")
        self.update()
        self.render()

    @events.GlobalEvent(events.TabLeave)
    def onTabLeave(self):
        """Log the event TabLeave."""
        log.debug("onTabLeave called.")
