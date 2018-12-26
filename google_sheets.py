# -*- coding: utf-8 -*-
import arrow
from google.oauth2 import service_account
from googleapiclient.discovery import build


class GoogleSheets:

    # https://developers.google.com/sheets/api/guides/authorizing
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    # TODO
    SPREADSHEET_ID = ''

    # TODO
    SERVICE_ACCOUNT_KEY = ''

    # TODO
    TAB_NAME = 'master!'

    # TODO
    RANGE_NAME = '%sA:B' % TAB_NAME

    RAW = 'RAW'

    def __init__(self):
        if self.SERVICE_ACCOUNT_KEY:
            creds = service_account.Credentials.from_service_account_file(
                self.SERVICE_ACCOUNT_KEY, scopes=self.SCOPES
            )
            service = build('sheets', 'v4', credentials=creds)
            self.sheets = service.spreadsheets()

    def _append(self, new_rows):
        return self.sheets.values().append(
            spreadsheetId=self.SPREADSHEET_ID,
            range=self.RANGE_NAME,
            valueInputOption=self.RAW,
            body={'values': new_rows}
        ).execute()

    def append_todays_data(self, price):
        new_rows = [
            [str(arrow.utcnow().date()), price],
        ]
        self._append(new_rows)

    def append_dummy_row(self):
        self.append_todays_data(9999)


if __name__ == '__main__':
    GoogleSheets().append_dummy_row()
