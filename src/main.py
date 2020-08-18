'''
main

Copyright (C) 2020 Yuto Watanabe
'''
try:
    from operation import surveillance
except ImportError:
    from .operation import surveillance


def main():
    '''
    main function.
    '''
    print(surveillance(True, 3, 0))


if __name__ == "__main__":
    main()
