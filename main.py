#!/usr/bin/env python

from __future__ import print_function
import httplib2
import os

from apiclient import discovery


KEY_FOR_GOOGLE_SERVICE = os.environ.get('GOOGLE_KEY')  # This key is found in google console
ID_OF_GOOGLE_SHEET = 'GOOGLE_SHEET_ID' # This id can be found in the google sheet's url
# https://docs.google.com/spreadsheets/d/1wZKactDqiDfTPxdZys7klAksJMTLtu1RIj4ztALCtmA/edit#gid=0
# For the above example url of a dummy spreadsheet, the google sheet id is given below which is between /d/ and /edit
# 1wZKactDqiDfTPxdZys7klAksJMTLtu1RIj4ztALCtmA


def get_sheet(service, sheetName):
    rangeName = sheetName + '!A1:Z100'
    result = service.spreadsheets().values().get(
                spreadsheetId=ID_OF_GOOGLE_SHEET,
                range=rangeName
            ).execute()
    values = result.get('values', [])
    return values

def main():
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?version=v4')
    service = discovery.build('sheets', 'v4', http=httplib2.Http(), discoveryServiceUrl=discoveryUrl, developerKey=KEY_FOR_GOOGLE_SERVICE)

    all_sheets = service.spreadsheets().get(spreadsheetId=ID_OF_GOOGLE_SHEET).execute()
    for sheet in all_sheets.get('sheets'):
        sheet_name = sheet.get('properties').get('title')
        values = get_sheet(service, sheet_name)
        print(values)


if __name__ == '__main__':
    main()
