#!/<Change me>
# TODO: Change this by typing `which python3` and entering that above

"""
Script to book classes
1. Login
2. Get class timetable
3. Make booking
"""
import requests

from secrets import username, password
from http_requests import (
    request_login, request_club_timetable, request_my_bookings, book_classes
)
from constants import ISLINGTON_CLUB_ID

with requests.Session() as sess:
    r_login = request_login(username, password, sess)
    print("Login request status:", r_login.status_code)

    r_timetable = request_club_timetable(ISLINGTON_CLUB_ID, sess)
    print("Timetable request status:", r_timetable.status_code)
    class_times = r_timetable.json()['data']['classTimes']

    # Get my account bookings
    bookings = request_my_bookings(sess)
    book_classes(class_times, bookings, sess)
