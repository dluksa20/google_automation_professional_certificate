#! /usr/bin/env python3

import os
import requests

files = os.listdir('/data/feedback')
id = 1
url = 'http://34.73.2.235/feedback/'

for txt in files:
    dict = {}
    dict['id'] = is
    with open(f'/data/feedback/{txt}', 'r') as f:
        lines = f.readlines()
        dict['title'] = lines[0].strip()
        dict['name'] = lines[1].strip()
        dict['date'] = lines[2].strip()
        dict['feedback'] = lines[3].strip()
    response = requests.post(url, data=dict)
    print(response)
    id+=1

