#!/<Change me>
# TODO: Change this by typing `which python3` and entering that above
"""
Script to get instructor and class information
"""
import json

import requests

from http_requests import request_club_timetable

with requests.Session() as sess:
    timetable = request_club_timetable("12", sess).json()

    classes = timetable['data']['classes']
    instructors = timetable['data']['instructors']

    instructors_dict = {i['id']: i['name'] for i in instructors}
    classes_dict = {c['id']: c['name'] for c in classes}

    json.dump(instructors_dict, open("./data/instructors.json", 'w'), indent=4)
    json.dump(classes_dict, open("./data/classes.json", 'w'), indent=4)
