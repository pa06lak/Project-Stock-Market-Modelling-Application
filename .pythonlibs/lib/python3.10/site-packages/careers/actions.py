import logging
import sys

from database import get_collections, insert_document, get_documents
from util import show_table, show_title

# get a new logging utility for current module
_logger = logging.getLogger(__name__)

# main index logic
# this function will be executed when user type "$ carrers" without any arguments
def run():
    print("principal functionality")

# executed when the given action does not exist
def not_found(options):
    print("The acction does not exists. Please check help (-h --help) to see available actions.")

# View Information
# this function will list documents depending of the option value
# e.g. Input: $ careers view courses
# output: A list of every courses
def view(options):
    _logger.debug(".view.start")

    # reference to local actions (functions)
    local_actions = sys.modules[__name__]

    _logger.debug("local_actions: {}".format(local_actions))

    if options.option is None:
        # execute view default function
        return view_default(options)

    view_action_name = "view_{}".format(options.option)

    _logger.debug("view_action_name = {}".format(view_action_name))

    view_action = getattr(local_actions, view_action_name, view_default)

    _logger.debug("view_action {}".format(view_action))

    # execute View Option Action function
    return view_action(options)

# view default action
def view_default(options):
        print("default view option action")

# view colleges
def view_colleges(options):
    _logger.debug(".view_colleges.start")

    colleges = get_documents("crs_colleges")

    _logger.debug("colleges:\n{}".format(colleges))

    # configure table
    table_headers = ["Nombre", "Descripción"]
    table_rows = list(
        map(lambda college: [college["name"], college["description"]], colleges))
    
    # show info
    show_title("Resultado de Universidades")
    show_table(table_rows, table_headers)

    _logger.debug(".view_colleges.end")

# view courses
def view_courses(options):
    _logger.debug(".view_colleges.start")

    courses = get_documents("crs_courses")

    _logger.debug("courses:\n {}".format(courses))

    # configuring table
    table_headers = ["Nombre", "Descripción"]
    table_rows = list(
        map(lambda course: [course["name"], course["description"]], courses)
    )
    
    # show info
    show_title("Resultado de Cursos")
    show_table(table_rows, table_headers)

    _logger.debug(".view_colleges.end")

# view careers
def view_careers(options):
    _logger.debug(".view_careers.start")

    courses = get_documents("crs_careers")

    _logger.debug("careers:\n {}".format(courses))

    # configuring table
    table_headers = ["Nombre", "Descripción"]
    table_rows = list(
        map(lambda course: [course["name"], course["description"]], courses)
    )
    # show info
    show_title("Resultado de Carreras")
    show_table(table_rows, table_headers)

    _logger.debug(".view_careers.end")

