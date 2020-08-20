'''
database operation.

Copyright (C) 2020 Yuto Watanabe
'''
import sqlite3
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Union


def read_today(database: str) -> List[Dict[str, Union[str, bool]]]:
    '''
    read element of today from database.

    Args:
        database (str): database file path

    Returns:
        List[Dict[str, Union[str, bool]]]: [description]
    '''
    conn = sqlite3.connect(database)
    table = conn.cursor()
    data = []

    jst = timezone(timedelta(hours=+9), 'JST')
    now = datetime.now(jst)

    for row in table.execute(f'SELECT * from datas WHERE day={str(now.strftime(r"%Y%m%d"))}'):
        data.append({
            'date': row[0],
            'temp': row[2],
            'hu': row[3],
            'light': row[4],
            'people': bool(row[5])
        })

    conn.close()

    return data


def read_all(database: str) -> List[Dict[str, Union[str, bool]]]:
    '''
    read all element from database.

    Args:
        database (str): database file path.

    Returns:
        List[Dict[str, Union[str, bool]]]: element.
    '''
    conn = sqlite3.connect(database)
    table = conn.cursor()
    data = []

    for row in table.execute('SELECT * from datas'):
        data.append({
            'date': row[0],
            'temp': row[2],
            'hu': row[3],
            'light': row[4],
            'people': bool(row[5])
        })

    conn.close()

    return data


def write(database: str, temp: int, hu: int, light: int, people: bool) -> None:
    '''
    write element in database.

    Args:
        database (str): database file path.
        temp (int): Temperature
        hu (int): Humidity
        light (int): Illuminance sensor.
        people (bool): Human Sensor.
    '''
    conn = sqlite3.connect(database)
    table = conn.cursor()

    jst = timezone(timedelta(hours=+9), 'JST')
    now = datetime.now(jst)

    data = (str(now.strftime(r'%Y%m%d%H%M%S')), str(now.strftime(r'%Y%m%d')), temp, hu, light, str(people),)

    table.execute('INSERT INTO datas VALUES(?, ?, ?, ?, ?, ?)', data)

    conn.commit()
    conn.close()


def create_table(database: str) -> None:
    '''
    create database.

    Args:
        database (str): database file path.
    '''
    conn = sqlite3.connect(database)
    table = conn.cursor()

    table.execute('CREATE TABLE datas (date TEXT, day TEXT, temp INTEGER, hu INTEGER, light INTEGER, people TEXT)')

    conn.commit()
    conn.close()
