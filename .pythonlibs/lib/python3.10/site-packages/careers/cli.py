#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following line in the
entry_points section in setup.py:

    [console_scripts]
    fibonacci = careers.skeleton:run

Then run `python setup.py install` which will install the command `fibonacci`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.

Note: This skeleton file can be safely removed if not needed!
"""
from __future__ import division, print_function, absolute_import

import argparse
import sys
import logging
import actions

from careers import __version__

__author__ = "Kevin Eduardo"
__copyright__ = "Kevin Eduardo"
__license__ = "mit"

_logger = logging.getLogger(__name__)

def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="An explorer for careers and courses using a command line interface.")

    parser.add_argument(
        "--version",
        action="version",
        version="careers {ver}".format(ver=__version__))

    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO)

    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG)

    parser.add_argument(
        dest="action",
        help="Can be: search [careers, courses, colleges], show [careers, courses, colleges], insert [career, course, college]",
        type=str,
        metavar="Action",
        choices=["view"],
        nargs="?",
        default="run"
        )

    parser.add_argument(
        dest="option",
        help="Every ACTION has an option parameter, this is optional.",
        metavar="Option",
        nargs="?",
        default=None
    )

    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")

def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("Starting to setting up the action")

    if args.action:
        # get the given action from actions module
        _logger.debug("actions:\n {}".format(dir(actions)))
        action = getattr(actions, args.action, actions.not_found)

        # execute the action
        action(args)

    # end of script
    _logger.info("action = {}".format(args.action))
    _logger.info("Script ends here")

def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
