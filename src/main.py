'''
main

Copyright (C) 2020 Yuto Watanabe
'''
import multiprocessing
import os
import time

import schedule

try:
    from operation import surveillance
    from database import write, create_table
    from create import graph
    from json_operation import json_read
    from response import get_environment, post_light_operation, post_line
except ImportError:
    from .operation import surveillance
    from .database import write, create_table
    from .create import graph
    from .json_operation import json_read
    from .response import get_environment, post_light_operation, post_line


def main():
    '''
    main function.
    '''
    user_path = 'user.json'
    user_data = json_read(user_path)
    token = user_data['token']
    line_token = user_data['line_token']
    light_id_on = user_data['light_id_on']
    light_id_off = user_data['light_id_on']

    database = 'data.db'
    if not os.path.isfile(database):
        create_table(database)

    get_process = multiprocessing.Process(target=run, args=(
        token,
        database,
        light_id_on,
        light_id_off
    ))
    image_send_process = multiprocessing.Process(target=run_one_day, args=(
        line_token,
        database
    ))

    get_process.start()
    image_send_process.start()


def run(token: str, database_file_path: str, light_id_on: str, light_id_off: str):
    '''
    Operate Nature Remo by looping every minute.

    token(str): token of nature remo.
    database_file_path(str): path of database.
    light_id_on(str): light on ID.
    light_id_off(str): light off ID.
    '''
    light_status = 0
    while True:  # pylint: disable=C0325
        get_data = get_environment(token)
        if get_data is not None:
            temp = get_data[0]['newest_events']['te']['val']
            hum = get_data[0]['newest_events']['hu']['val']
            light = get_data[0]['newest_events']['il']['val']
            people = bool(get_data[0]['newest_events']['mo']['val'])

            write(database_file_path, temp, hum, light, people)

            status = surveillance(people, light, light_status)
            if status in (1, 2):
                light_status = status
                if status == 1:
                    # on
                    light_id = light_id_on
                else:
                    # off
                    light_id = light_id_off
                post_light_operation(token, light_id)

        time.sleep(60)


def run_one_day(line_token: str, database_file_path: str):
    '''
    Run at 1:00 am every day.

    Args:
        line_token (str): line access token.
        database_file_path (str): path of database.
    '''
    schedule.every().day.at("01:00").do(
        create_graph,
        line_token=line_token,
        database_file_path=database_file_path
    )


def create_graph(line_token: str, database_file_path: str):
    '''
    Create a graph from the database and send it to LINE.

    line_token(str): line access token.
    database_file_path(str): path of database.
    '''
    image_file_path = graph(database_file_path)
    post_line(line_token, image_file_path, '昨日の部屋の温度変化')


if __name__ == "__main__":
    main()
