import logging
import vim


log = logging.getLogger(__name__)


class WindowManager(object):

    """Docstring for WindowManager. """

    def __init__(self):
        """Initializes the global window manager."""
        self.windows = dict()

    def add(self, win):
        """Add a new vim window to manager.

        :win: TODO
        :returns: TODO

        """
        self.windows[win] = Window(win)

    # def get(self, nr):
        # return self.windows.get(vim.windows[nr])

    def current(self):
        win = self.windows.get(vim.current.window)
        if win is None:
            win = Window(vim.current.window)
            self.windows[vim.current.window] = win
        return win


class Window(object):
    """Docstring for Window. """

    def __init__(self, win):
        """TODO: to be defined1. """
        self.win = win
        self.buffer = win.buffer

    def getCursorPos(self):
        row, col = self.win.cursor
        return row-1, col

    def setCursorPos(self, row, col):
        self.win.cursor = row+1, col

    def setCursorRow(self, row):
        _, col = self.win.cursor
        self.win.cursor = row+1, col

    def moveCursor(self, row, col):
        r, c = self.win.cursor
        self.win.cursor = row+r, col+c


