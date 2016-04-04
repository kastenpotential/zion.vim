from pyvim.plugin import Plugin
import logging
import os
import vim
from pyvim import events


log = logging.getLogger(__name__)

""" %1T%#TabLineSel# 1 tmp.vim + %2T%#TabLine# 2 [bka Name] %#TabLineFill#%#bka# mymymy """


class TabSegment(object):
    char1 = ''
    char2 = ''
    template = "%{nr}T%#{style1}#{char1}{fill1}{nr} {name}{fill2}%#{style2}#{char2}"

    def __init__(self, nr, name, current_nr):
        self.name = name or "N.N."
        self.nr = nr
        if nr == current_nr:
            self.style1 = "TabLineSel"
            self.style2 = "TabLineSelInv"
            self.char1 = TabSegment.char1 if nr > 1 else ""
            self.fill1 = " "
            self.char2 = TabSegment.char1
            self.fill2 = " "
        else:
            self.style1 = self.style2 = "TabLine"
            self.char1 = " " if nr == 1 else ""
            self.fill1 = ""
            self.char2 = TabSegment.char2 if nr != current_nr - 1 else ""
            self.fill2 = " " if nr != current_nr - 1 else ""

    def render(self):
        return self.template.format(**vars(self))


class TabSegmentFill(object):

    def render(self):
        return "%#TabLineFill#%T"


class TabSegmentRight(object):
    left1 = ''
    left2 = ''
    right1 = ''
    right2 = ''

    def __init__(self, name, name_plural, count):
        self.name = name if count == 1 else name_plural
        self.count = count
        self.right = self.right1

    def render(self):
        return "%=%#TabLineTypeInv# {right}%#TabLineType#{count} {name} ".format(**vars(self))


class TabLine(Plugin):
    """Test plugin just logging some events."""
    NEVER = 0
    ON_DEMAND = 1
    ALWAYS = 2

    def __init__(self):
        " ""Initializes the plugin. """
        super().__init__()
        log.info("TabLine initialized.")
        self._segments = []
        self.showTabline()
        # self.update()
        # self.render()

    def showTabline(self, mode=ALWAYS):
        vim.options["showtabline"] = mode

    def update(self):
        self._segments.clear()
        for tab in vim.tabpages:
            name = os.path.basename(tab.window.buffer.name)
            current_nr = vim.current.tabpage.number
            log.debug("%s %s %s", tab.number, name, current_nr)
            self._segments.append(TabSegment(tab.number, name, current_nr))
        self._segments.append(TabSegmentFill())
        self._segments.append(TabSegmentRight("tab", "tabs", len(vim.tabpages)))

    def render(self):
        tab_str = " ".join([s.render() for s in self._segments])
        log.debug(tab_str)
        vim.options["tabline"] = tab_str

    @events.GlobalEvent(events.BufEnter)
    def onTabEnter(self):
        """Log the event BufEnter."""
        log.debug("onBufEnter called.")
        self.update()
        self.render()

    @events.GlobalEvent(events.TabLeave)
    def onTabLeave(self):
        """Log the event TabLeave."""
        log.debug("onTabLeave called.")

    @events.KeyEvent("<leader>1")
    def gotoTab1(self):
        self.gotoTab(1)

    @events.KeyEvent("<leader>2")
    def gotoTab2(self):
        self.gotoTab(2)

    @events.KeyEvent("<leader>3")
    def gotoTab3(self):
        self.gotoTab(3)

    @events.KeyEvent("<leader>4")
    def gotoTab4(self):
        self.gotoTab(4)

    @events.KeyEvent("<leader>5")
    def gotoTab5(self):
        self.gotoTab(5)

    @events.KeyEvent("<leader>6")
    def gotoTab6(self):
        self.gotoTab(6)

    @events.KeyEvent("<leader>7")
    def gotoTab7(self):
        self.gotoTab(7)

    @events.KeyEvent("<leader>8")
    def gotoTab8(self):
        self.gotoTab(8)

    @events.KeyEvent("<leader>9")
    def gotoTab9(self):
        self.gotoTab(9)

    @events.KeyEvent("<leader>0")
    def closeCurrentTabpage(self):
        vim.command("tabclose")

    def gotoTab(self, nr):
        if not 0 < nr < len(vim.tabpages):
            log.debug("invalid tabpage: not 0 < %s < %s", nr, len(vim.tabpages))
            return
        src_nr = vim.current.tabpage.number
        if nr == src_nr:
            log.debug("%s is already current tabpage", nr)
            return
        dst = vim.tabpages[nr-1]
        log.debug("nr=%s src=%s dst=%s", nr, src_nr, dst.number)
        vim.current.tabpage = dst
