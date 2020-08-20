'''
Communicate with the API.

Copyright (C) 2020 Yuto Watanabe
'''
try:
    from response import get_device
except ImportError:
    from .response import get_device

if __name__ == "__main__":
    TOKEN = ''

    get_device('output.json', TOKEN)
