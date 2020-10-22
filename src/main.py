# coding: utf-8
import os
import requests
from bs4 import BeautifulSoup
from time import sleep
from src.Calender import Calender
from dotenv import load_dotenv
load_dotenv()


def get_retry(url, retry_times=5):
    for t in range(retry_times + 1):
        r = requests.get(url)
        if t < retry_times:
            try:
                r.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(e)
                sleep(10)
                continue
        return r


def main():
    colorId = 0
    calender = Calender()
    base_url = "https://subjregist.naist.jp/"

    # start session
    session = requests.session()
    data = {
        "_method": "POST",
        "data[User][account]": os.environ['USER_ACCOUNT'],
        "data[User][password]": os.environ['USER_PASSWORD']
    }
    res = session.post(base_url, data=data)
    res.raise_for_status()

    # get registered subjects list
    list_bs = BeautifulSoup(res.content, "html.parser")
    subjects = list_bs.select('.tbl01.mB20 a[target=_blank]')
    print(subjects)

    # delete all events in google calendar
    calender.delete_all_events()

    # run export for each subjects
    for subject in subjects:
        # get schedules
        subject_name = subject.text
        subject_url = subject.get('href')
        print(subject_name, subject_url)
        subject_response = get_retry(subject_url)
        subject_bs = BeautifulSoup(subject_response.content, "html.parser")
        item = 5 if "subjects" in subject_url else 4
        schedules = subject_bs.select('.tbl01.mB20')[item].select('tr td')

        # skip if no schedule is defined
        if len(schedules) == 1:
            continue

        # add schedules to google calendar
        calender.add_schedules(subject_name, subject_url, schedules, colorId)
        sleep(1)

        # change colorId (11 different colors)
        colorId = (colorId + 1) % 11
