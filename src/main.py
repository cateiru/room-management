'''
main

Copyright (C) 2020 Yuto Watanabe
'''
from datetime import date


try:
    # from operation import surveillance
    from database import write, read_all, read_today
except ImportError:
    # from .operation import surveillance
    from .database import write, read_all, read_today


def main():
    '''
    main function.
    '''
    database = 'data.db'
    write(database, 23, 60, 150, True)

    print(read_today(database))


if __name__ == "__main__":
    main()
