from pyvim import pv, events
from pyvim.plugin import Plugin
import vim
import logging
import re
import weakref
import inspect


log = logging.getLogger(__name__)



def str_remove(string, start, end):
    return string[:start] + string[end:]


def str_insert(string, pos, text):
    return string[:pos] + text + string[pos:]


def toggle_line_comment(chars="#", whitespace=1):
    """Toggle line comments.
    """
    line = vim.current.line
    regex = re.compile(r"^\s*(" + re.escape(chars) + r"\s{0," + str(whitespace) + r"})")
    # log.debug(regex)
    m = regex.match(line)
    if m:
        # vim.current.line = line[:m.start(1)] + line[m.end(1):]
        vim.current.line = str_remove(vim.current.line, m.start(1), m.end(1))
    else:
        m = re.match(r"\s*", line)
        vim.current.line = str_insert(vim.current.line, m.end(), chars + " "*whitespace)


class TextManipulation(Plugin):
    """Class that handles basic text manipulations."""

    def __init__(self):
        """ctor"""
        pass

    # @KeyMap("f5", "noral")
    def moveLineUp():
        """move the current line up"""
        win = pv.get_window(0)
        vim.command("echom 'movelineup'")
        log.debug("inmoveup")
        return "helllo move up"

    @events.KeyEvent("<leader>c")
    def toggleLineComment(self):
        toggle_line_comment()

