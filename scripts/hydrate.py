#!/usr/bin/env python

import json
import requests
from os import walk, path

user_id = 'guestuser@gmail.com'
url = 'http://localhost:8081'

def get_(obj: str):
    response = requests.get(f"{url}/api/{obj}?user_id=guestuser@gmail.com")
    data = response.json()
    print(json.dumps(data, indent=2))

def post(obj: str, data: any):
    json_payload = { 'user_id': user_id, **data }
    response = requests.post(f"{url}/api/{obj}", json=json_payload)
    print(response)

def hydrate(obj: str):
    """walks folder {obj} and posts respective json files"""
    print(f"hydrating {obj}..")
    for folder, _, files in walk(f'./{obj}'):
        for filepath in map(lambda f: path.join(folder, f), files):
            do_hydrate(obj, filepath)

    print(f"done hydrating {obj}!")
    print("")

def do_hydrate(obj:str, filepath: str):
    print(f"processing {filepath} ..")
    with open(filepath, 'r') as fp:
        data = json.load(fp)

    post(obj, data)

hydrate('skills')
hydrate('models')
hydrate('agents')
