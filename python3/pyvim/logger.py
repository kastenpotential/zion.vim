# -*- coding: utf-8 -*-
"""
Log module for Zion / PyVim.
"""
import logging
from datetime import datetime


def init():
    """ Initialize the logging system. """
    logging.basicConfig(filename="/tmp/pyvim.log",
                        format='%(asctime)s %(levelname)s %(name)s %(funcName)s - %(message)s',
                        level=logging.DEBUG)
    log = logging.getLogger("pyvim")
    log.setLevel(logging.DEBUG)
    log.info("log started at %s", datetime.now())
    return log
