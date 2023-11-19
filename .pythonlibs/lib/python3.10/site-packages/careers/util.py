from beautifultable import BeautifulTable

def show_table(data, headers=[]):
    table = BeautifulTable()
    table.column_headers = headers
    for d in data:
        table.append_row(d)

    print(table)

def show_line(length=100):
    print("-" * length)

def show_title(title=""):
    title_length = len(title)
    print("\n {}".format(title))
    show_line(title_length + 2)

