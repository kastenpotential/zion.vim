from pyvim.plugin import Plugin
import logging
from pyvim.core import pv
from pyvim import const, events


log = logging.getLogger()


class EventLogger(Plugin):

    """Test plugin just logging some events."""

    def __init__(self):
        """Initializes the plugin. """
        log.info("EventLogger initialized.")

    def __del__(self):
        log.info("EventLogger deleted.")

    @events.GlobalEvent(events.FocusGained)
    def onFocusGained(self):
        log.debug("onFocusGained called.")
