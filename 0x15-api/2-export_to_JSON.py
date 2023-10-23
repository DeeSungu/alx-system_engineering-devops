#!/usr/bin/python3
"""Ascript that fetches data about an employee using an api
and exports it in csv format
"""
import json
import requests
import sys


base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    user_id = sys.argv[1]

    # get user info e.g https://jsonplaceholder.typicode.com/users/1/
    user_url = '{}/users?id={}'.format(base_url, user_id)
    # print("user url is: {}".format(user_url))

    response = requests.get(user_url)

    data = response.text

    data = json.loads(data)

    user_name = data[0].get('username')

    tasks_url = '{}/todos?userId={}'.format(base_url, user_id)

    response = requests.get(tasks_url)

    tasks = response.text

    tasks = json.loads(tasks)

    # build the csv
    builder = ""
    for task in tasks:
        builder += '"{}","{}","{}","{}"\n'.format(
            user_id,
            user_name,
            task['completed'],
            task['title']
        )
    with open('{}.csv'.format(user_id), 'w', encoding='UTF8') as myFile:
        myFile.write(builder)
