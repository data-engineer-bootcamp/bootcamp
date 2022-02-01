import requests

r = requests.get('http://google.com').text  # html

# текстовые форматы данных (csv, json)
# csv
# id, name, value
# 1, Jim, 42
# 2, Stacey, 52

# json
# [
#     {
#         "id": 1,
#         "name": "Jim",
#         "value": 42
#     },
#     {
#         "id": 1,
#         "name": "Stacey",
#         "value": 52
#     }
# ]
# json -> dict

import psycopg2
connection = psycopg2.connect(
    host="localhost",
    database="data",
    user="data_engineer",
    password="data_engineer",
)

with connection.cursor() as cursor:
    # логика взаимодействия с БД
    pass
