'''
Communicate with the API.

Copyright (C) 2020 Yuto Watanabe
'''
try:
    from response import get_device
    from json_operation import json_read
except ImportError:
    from .response import get_device
    from .json_operation import json_read

if __name__ == "__main__":
    DATA = json_read('user.json')

    get_device(DATA['token'], 'output.json')
