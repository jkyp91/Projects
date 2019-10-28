from datetime import datetime

import requests
from requests import Session

from constants import (
    HOME_URL,
    REFORMER_ID,
    ISLINGTON_CLUB_ID,
    INSTRUCTORS,
    CLASSES,
)


def request_login(username: str, password: str, session: Session):
    return session.post(
        url=f"{HOME_URL}/login?sf_cntrl_id=ctl00%24Body%24C00",
        data={
            "UserName": username,
            "Password": password,
        }
    )


def request_club_timetable(club_id: str, session: Session):
    return session.get(
        url=f"{HOME_URL}/api/club/getclubtimetable",
        params={"id": club_id}
    )


def request_book_class(class_id: int, club_id: str, session: Session):
    return session.post(
        url=f"{HOME_URL}/api/Class/BookClass",
        json={
            "clubId": club_id,
            "classId": class_id,
        }
    )


def request_cancel_class(class_id: int, club_id: str, session: Session):
    return session.post(
        url=f"{HOME_URL}/api/Class/CancelClass",
        json={
            "clubId": club_id,
            "classId": class_id,
        }
    )


def request_my_bookings(session: Session):
    """
    Dictionary of bookings by class_id
    """

    response = session.get(
        url=f"{HOME_URL}/api/class/getBookedClasses"
    ).json()

    bookings = {}
    for booking in response['data']:
        bookings[booking['classId']] = (
            booking['className'],
            booking['state'],
        )
    return bookings


def book_classes(class_times: list, my_bookings: dict, session: Session):
    """
    Go through each class in the timetable and make a booking if:
    Meets the following criteria
    1. Weekday @ 7 and reformer pilates
    2. Weekend @ 9
    3. Not already booked
    """
    for _class in class_times:
        start_time = datetime.strptime(
            _class['startTime'], "%Y-%m-%dT%H:%M:%SZ"
        )
        slot_id = _class['id']
        class_id = _class["classId"]
        status = _class["status"]
        instructor_id = _class["instructorId"]

        if is_valid_class(start_time, class_id, status) and (
            slot_id not in my_bookings
        ):
            try:
                r_booking = request_book_class(
                    slot_id, ISLINGTON_CLUB_ID, session
                )
                r_booking.raise_for_status()

                confirmation = (
                    f"Booked: {CLASSES[str(class_id)]} "
                    f"at {start_time.strftime('%H:%M on the %d/%m/%Y')} "
                    f"with {INSTRUCTORS[str(instructor_id)]}. "
                )

                if status == "Waitlist":
                    confirmation += (
                        f"On waitlist in position"
                        f" {_class['waitlistCount'] + 1}"
                        f"/{_class['waitlistCapacity']}."
                    )

                print(confirmation)

            except requests.HTTPError as e:
                print(f"There was an error {e}. Continuing search.")
                continue


def is_valid_class(start_time: datetime, class_id: int, status: str):
    if start_time.day <= datetime.now().day:
        return False

    if status == "Full":
        return False

    return (
        (
            is_weekday(start_time)
            and (is_time(start_time, "06:45") or is_time(start_time, "07:00"))
            and class_id == REFORMER_ID
        )
        or (
            not is_weekday(start_time) and (is_time(start_time, "09:00"))
        )
    )


def is_weekday(time: datetime):
    return time.weekday() < 5


def is_time(time: datetime, desired_time: str):
    return time.strftime("%H:%M") == desired_time
