import logging
from beautifultable import BeautifulTable

# get a new logging utility for current module
_logger = logging.getLogger(__name__)

def show_table(table_rows, headers=[]):
    table = BeautifulTable()
    _logger.debug("show_table.table_rows: {}".format(len(table_rows)))
    table.column_headers = headers
    if len(table_rows) == 0:
        table.append_row(
            list(map(lambda i: "--", range(0, len(headers))))
        )

        print(table)
        print(" Sin resultados.\n")
    else:
        for table_row in table_rows:
            table.append_row(table_row)
        print(table)
        print("\n")



def show_line(length=100):
    print("-" * length)


def show_title(title=""):
    title_length = len(title)
    print("\n {}".format(title))
    show_line(title_length + 2)

def show_loading():
    print("\nCargando...\n")
