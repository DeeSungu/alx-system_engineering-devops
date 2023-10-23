#!/usr/bin/python3
"""Ascript that fetches info on all employees using an api
and exports it in json format
"""
import json
import requests


base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    # get users info e.g https://jsonplaceholder.typicode.com/users
    users_url = '{}/users'.format(base_url)

    response = requests.get(users_url)

    data = response.text

    data = json.loads(data)


    builder = {}
    for user in data:
        user_id = user.get('id')


        user_name = user.get('username')


        dict_key = str(user_id)

        builder[dict_key] = []
        # get user info about todo tasks
        # e.g https://jsonplaceholder.typicode.com/users/1/todos
        tasks_url = '{}/todos?userId={}'.format(base_url, user_id)
        # print("tasks url is: {}".format(tasks_url))

        # get info from api
        response = requests.get(tasks_url)
        # pulls data from api
        tasks = response.text
        # parses data into JSON format
        tasks = json.loads(tasks)
        # print("JSOON LOADS IS: {}".format(tasks))

        for task in tasks:
            json_data = {
                "task": task['title'],
                "completed": task['completed'],
                "username": user_name
            }

            builder[dict_key].append(json_data)
    # writes the data to the file
    json_encoded_data = json.dumps(builder)
    with open('todo_all_employees.json', 'w', encoding='UTF8') as myFile:
        myFile.write(json_encoded_data)
