'''
Lighting operation

Copyright (C) 2020 Yuto Watanabe
'''
import datetime
import os

try:
    from json_operation import json_read, json_write
except ImportError:
    from .json_operation import json_read, json_write


def surveillance(people: bool, light: int, status: int) -> int:
    '''
    If the room is dark when are people and you are not sleeping, light on.
    Also, if no people are left for 10 hours, light off.

    Args:
        people (bool): Human sensor value.
        light (int): Illuminance.
        status (int): Current light state.
                      | 0: do nothing.
                      | 1: light on.
                      | 2: light off.

    Returns:
        int: Light operation.
              | 0: do nothing.
              | 1: light on.
              | 2: light off.
    '''

    file_path = 'latest_people.json'
    light_level = 50
    light_status = 0

    if people:
        if is_midnight():
            if light < light_level:
                # light on
                light_status = 1
            else:
                # light off
                light_status = 2
    else:
        if elapsed_time(file_path):
            # light off
            light_status = 2

    if light_status == status:
        return 0
    return light_status


def elapsed_time(file_path: str) -> bool:
    '''
    Refers to the date and time acquired in the past and returns True if 10 hours have passed.

    Args:
        file_path (str): Cache file path.

    Returns:
        bool: True if 10 hours have passed, else False.
    '''
    elapsed_time_hour = 10
    now = datetime.datetime.now()

    if os.path.isfile(file_path):
        latest_element = json_read(file_path)
    else:
        # new create cache file
        json_write(file_path, {'date': now.strftime(r'%Y%m%d%H%M%S')})
        return False

    if 'date' in latest_element:
        latest_date = datetime.datetime.strptime(str(latest_element['date']), r'%Y%m%d%H%M%S')
    else:
        # if `date` element is not found
        latest_date = now
        json_write(file_path, {'date': now.strftime(r'%Y%m%d%H%M%S')})

    elapsed = now - latest_date

    if elapsed.seconds > (elapsed_time_hour * 3600):
        json_write(file_path, {'date': now.strftime(r'%Y%m%d%H%M%S')})
        return True

    return False


def is_midnight() -> bool:
    '''
    PM7:00 to AM10:00 is set as midnight, and False is executed if it is executed at that time, and True otherwise.

    Returns:
        bool: PM7:00 to AM10:00 -> False, and True otherwise.
    '''
    now = datetime.datetime.now()

    if 10 < now.hour < 19:
        return True

    return False
