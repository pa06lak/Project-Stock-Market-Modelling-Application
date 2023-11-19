#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following line in the
entry_points section in setup.py:

    [console_scripts]
    fibonacci = consultor.skeleton:run

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

from consultor import __version__

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
        description="Un consultor vocacional que te ayudará a ver detalles de cursos, carreras y universidades.")

    parser.add_argument(
        "--version",
        action="version",
        version="consultor {ver}".format(ver=__version__))

    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="Configurar nivel de mensajes de ayuda a INFO",
        action="store_const",
        const=logging.INFO)

    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="Configurar nivel de mensajes de ayuda a DEBUG",
        action="store_const",
        const=logging.DEBUG)

    parser.add_argument(
        dest="action",
        help="Es la acción que deseas ejecutar, puedes elegir entre: mostrar, buscar",
        type=str,
        metavar="Acción",
        choices=["mostrar", "buscar"],
        nargs="?",
        default="run"
        )

    parser.add_argument(
        dest="option",
        help="Puedes enviar una opción a la acción que deseas ejecutar. Ejem: consultor mostrar carreras",
        metavar="Opción",
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

# translate arguments from user input
translated_args = {
    "view": "mostrar",
    "courses": "cursos",
    "colleges": "universidades",
    "careers": "carreras",
    "search": "buscar"
}
# translate arguments function
def translate_args(args):
    __args = args

    # translate action
    for key, value in translated_args.items():
        __args.action = key if __args.action == value else __args.action

    # translate option
    for key, value in translated_args.items():
        __args.option = key if __args.option == value else __args.option

    return __args

def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("Starting to setting up the action")

    _logger.debug("args before translate: \n{}".format(args))

    args = translate_args(args)

    _logger.debug("args after translate: \n{}".format(args))

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
