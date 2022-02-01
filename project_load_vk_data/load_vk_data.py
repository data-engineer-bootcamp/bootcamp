from copy import deepcopy
from datetime import datetime
import requests
from configparser import ConfigParser
import psycopg2
from psycopg2.extras import execute_values

API_URL = 'https://api.vk.com/method/'

parser = ConfigParser()
parser.read('secrete.cfg')
SECRETS = parser['main']


def extract_vk_data(method: str, params: dict[str, str]) -> dict[str]:
    return requests.post(f"{API_URL}{method}", data=params).json()


def transform_vk_person(person: dict) -> dict:
    result = deepcopy(person)
    result['city'] = person['city']['title'] if person.get('city') else None
    bdate = person.get('bdate')
    if bdate:
        try:
            bdate = datetime.strptime(person['bdate'], '%d.%m.%Y')
        except Exception:
            bdate = None
    result['bdate'] = bdate

    allowed_fields = ('id', 'first_name', 'last_name', 'is_closed', 'sex', 'bdate', 'city')
    for key in list(result.keys()):
        if key not in allowed_fields:
            del result[key]

    for key in allowed_fields:
        if key not in list(result.keys()):
            result[key] = None

    return {k: result[k] for k in allowed_fields}


def load_persons(persons: list):
    connection = psycopg2.connect(
        host="localhost",
        database="data",
        user="data_engineer",
        password="data_engineer",
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        query = "INSERT INTO persons VALUES %s"
        values = [[value for value in person.values()] for person in persons]
        execute_values(cursor, query, values)

    connection.close()


if __name__ == '__main__':
    request_params = dict(SECRETS)
    request_params.update({
        'group_id': '54530371',
        'count': 10,
        'fields': 'city,bdate,sex',
        'offset': 100,
        'sort': 'id_asc',
    })

    # Extract
    vk_data = extract_vk_data('groups.getMembers', request_params)
    persons = vk_data['response']['items']

    # Transform
    prepared_persons = []
    for person in persons:
        prepared_persons.append(transform_vk_person(person))

    # Load
    load_persons(prepared_persons)

