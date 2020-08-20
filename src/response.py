'''
Communicate with the API.

Copyright (C) 2020 Yuto Watanabe
'''
from typing import Any, Dict, List, Optional

import requests

try:
    from json_operation import json_write
except ImportError:
    from .json_operation import json_write


def get_device(token: str, data_path: str) -> None:
    '''
    get device datas.

    token(str): access token.
    data_path(str): path of save file.
    '''
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {token}',
    }

    response = requests.get('https://api.nature.global/1/appliances', headers=headers)

    data = response.json()

    json_write(data_path, data)


def get_environment(token: str) -> Optional[List[Dict[str, Any]]]:
    '''
    Acquires various data such as temperature and humidity

    Args:
        token (str): access token.

    Returns:
        Optional[List[Dict[str, Any]]]: get data.
    '''
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {token}',
    }

    response = requests.get('https://api.nature.global/1/devices', headers=headers)

    data = response.json()

    return data


def post_light_operation(token: str, light_id: str) -> None:
    '''
    Operate the light.

    Args:
        token (str): access token.
        light_id (str): id of light
    '''
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    requests.post(f'https://api.nature.global/1/signals/{light_id}/send', headers=headers)


def post_line(token: str, imagefile_path: str, text: str) -> None:
    '''
    send message and images to line.

    Args:
        token (str): access token.
        imagefile_path (str): image file path.
        text (str): send message text.
    '''
    line_access_url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + token}
    payload = {'message': text}

    files = {'imageFile': open(imagefile_path, 'rb')}

    try:
        requests.post(line_access_url, headers=headers, params=payload, files=files)
    except requests.exceptions.RequestException as error:
        print(error)
