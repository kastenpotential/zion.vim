from pyvim.plugin import Plugin
import logging
from pyvim import events


log = logging.getLogger(__name__)


class EventLogger(Plugin):

    """Test plugin just logging some events."""

    def __init__(self):
        """Initializes the plugin. """
        log.info("EventLogger initialized.")

    def __del__(self):
        log.info("EventLogger deleted.")

    @events.GlobalEvent(events.FocusGained)
    def onFocusGained(self):
        """Log the event FocusGained."""
        log.debug("onFocusGained called.")

    @events.GlobalEvent(events.FocusLost)
    def onFocusLost(self):
        """Log the event FocusLost."""
        log.debug("onFocusLost called.")

    @events.GlobalEvent(events.TabEnter)
    def onTabEnter(self):
        """Log the event TabEnter."""
        log.debug("onTabEnter called.")

    @events.GlobalEvent(events.TabLeave)
    def onTabLeave(self):
        """Log the event TabLeave."""
        log.debug("onTabLeave called.")
