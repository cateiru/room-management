import json
from src.response import get_device, get_environment, post_light_operation


def test_get_device():
    data_path = 'test/device.json'
    user = 'user.json'

    with open(user, mode='r') as contents:
        body = json.load(contents)

    get_device(body['token'], data_path)


def test_get_environment():
    user = 'user.json'
    json_file_path = 'environment.json'

    with open(user, mode='r') as contents:
        body = json.load(contents)

    data = get_environment(body['token'])

    with open(json_file_path, mode='w') as contents:
        json.dump(data, contents, indent=4, ensure_ascii=False)


def test_light_operation():
    user = 'user.json'
    with open(user, mode='r') as contents:
        body = json.load(contents)

    post_light_operation(body['token'], body['light_id'])
