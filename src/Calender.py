# coding: utf-8
import datetime
import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from dotenv import load_dotenv
load_dotenv()


class Calender:
    def __init__(self):
        self.scopes = ['https://www.googleapis.com/auth/calendar']
        self.calId = os.environ['CALENDAR_ID']
        self.year = int(os.environ['YEAR'])

        creds = None
        # The file token.pickle stores the user's access and refresh tokens,
        # and is created automatically when the authorization flow completes
        # for the first time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.scopes)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        self.service = build('calendar', 'v3', credentials=creds)

    def datetime_formatter(self, date, period):
        year = self.year
        date = list(map(int, date.split('/')))
        time = self.period2time(int(period))
        if date[0] <= 3:
            year += 1
        start_date = datetime.datetime(year, *date, *time[0]).isoformat()
        end_date = datetime.datetime(year, *date, *time[1]).isoformat()
        return [start_date, end_date]

    def period2time(self, period):
        if period == 1:
            return [[9, 20], [10, 50]]
        elif period == 2:
            return [[11, 00], [12, 30]]
        elif period == 3:
            return [[13, 30], [15, 00]]
        elif period == 4:
            return [[15, 10], [16, 40]]
        elif period == 5:
            return [[16, 50], [18, 20]]
        elif period == 6:
            return [[18, 30], [20, 00]]

    def add_schedules(self, title, url, schedules, colorId):
        schedules = [schedules[i:i + 5] for i in range(0, len(schedules), 5)]
        for i, date, period, location, note in schedules:
            date_time = self.datetime_formatter(date.text, period.text)
            body = {
                'summary': f"{title} [第{int(i.text)}回]",
                'location': location.text,
                'description': f"{note.text}\n{url}",
                'start': {
                    'dateTime': date_time[0],
                    'timeZone': 'Japan',
                },
                'end': {
                    'dateTime': date_time[1],
                    'timeZone': 'Japan',
                },
                'colorId': colorId + 1
            }
            event = self.service.events().insert(
                calendarId=self.calId, body=body).execute()
            print(event)

    def delete_all_events(self):
        page_token = None
        while True:
            events = self.service.events().list(calendarId=self.calId,
                                                pageToken=page_token).execute()
            print(events)
            for item in events['items']:
                self.service.events().delete(calendarId=self.calId,
                                             eventId=item['id']).execute()
            page_token = events.get('nextPageToken')
            if not page_token:
                break
