'''
main

Copyright (C) 2020 Yuto Watanabe
'''
import os
from datetime import date

try:
    # from operation import surveillance
    from database import write, read_all, create_table
    from create import graph
except ImportError:
    # from .operation import surveillance
    from .database import write, read_all, create_table
    from .create import graph


def main():
    '''
    main function.
    '''

    database = 'data.db'
    if not os.path.isfile(database):
        create_table(database)
    write(database, 23, 40, 150, True)

    graph(database)


if __name__ == "__main__":
    main()
