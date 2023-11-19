import logging
import sys

from database import get_collections, insert_document, get_documents
import util

# get a new logging utility for current module
_logger = logging.getLogger(__name__)

# main index logic
# this function will be executed when user type "$ carrers" without any arguments


def run():
    print("principal functionality")

# executed when the given action does not exist


def not_found(options):
    print("La acción ingresada no existe. Por favor revisa la ayuda (-h --help) para ver las acciones disponibles.")

# View Information
# this function will list documents depending of the option value
# e.g. Input: $ consultor view courses
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

    colleges = get_colleges()

    display_colleges(colleges)

    _logger.debug(".view_colleges.end")

# view courses
def view_courses(options):
    _logger.debug(".view_colleges.start")

    courses = get_courses()

    _logger.debug("courses:\n {}".format(courses))

    display_courses(courses)

    _logger.debug(".view_colleges.end")

# view careers
def view_careers(options):
    _logger.debug(".view_consultor.start")

    careers = get_careers()

    display_careers(careers)

    _logger.debug(".view_consultor.end")

def get_careers(filters = None):
    return get_documents("ctr_careers", filters)

def get_colleges(filters = None):
    _logger.debug(".search.colleges filters: {}".format(filters))
    return get_documents("ctr_colleges", filters)

def get_courses(filters = None):
    return get_documents("ctr_courses", filters)

# display careers in the shell
def display_careers(careers):
    # configuring table
    table_headers = ["ID", "Nombre", "Descripción"]
    table_rows = list(
        map(lambda course: [course["id_career"],
                            course["name"], course["description"]], careers)
    )

    # show info
    util.show_title("Resultado de Carreras")
    util.show_table(table_rows, table_headers)

# display courses in the shell
def display_courses(courses):
    # configuring table
    table_headers = ["ID", "Nombre", "Descripción"]
    table_rows = list(
        map(lambda course: [course["id_course"],
                            course["name"], course["description"]], courses)
    )

    # show info
    util.show_title("Resultado de Cursos")
    util.show_table(table_rows, table_headers)

# display colleges in the shell
def display_colleges(colleges):
    # configure table
    table_headers = ["ID", "Nombre", "Descripción"]
    table_rows = list(
        map(lambda college: [college["id_college"], college["name"], college["description"]], colleges))

    # show info
    util.show_title("Resultado de Universidades")
    util.show_table(table_rows, table_headers)

# search in all collections
def search(options):
    _logger.debug(".search.start")

    # reference to local actions (functions)
    local_actions = sys.modules[__name__]

    _logger.debug("local_actions: {}".format(local_actions))

    if options.option is None:
        # execute view default function
        print('Por favor ingresa una opción para realizar la busqueda. ejemplo: $ consultor buscar "matematica"')
        return

    _logger.debug(".search.filter: {}".format(options.option))

    filters = {
        "$or": [
            {
                "name": {
                    "$regex": options.option,
                    "$options": "i"
                },
            },
            {
                "description": {
                    "$regex": options.option,
                    "$options": "i"
                }
            }
        ]
    }

    colleges = get_colleges(filters)
    _logger.debug('.search.colleges')

    courses = get_courses(filters)
    _logger.debug('.search.courses')

    careers = get_careers(filters)
    _logger.debug('.search.careers')


    # display results
    display_colleges(colleges)
    display_careers(careers)
    display_courses(courses)
