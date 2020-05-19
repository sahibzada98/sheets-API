from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
RANGE_NAME = 'B3:B15'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API

    """

    # to reuse this, change the sample name and range at the top of the sheet
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[4]))

    """
    sheet = service.spreadsheets()

    """
    
    #used this code to create a new spreadsheet and print its ID; going to read, write from it

    spreadsheet = {
            'properties': {
                'title': "first Sheet"
            }
    }
    spreadsheet = sheet.create(body=spreadsheet,
                                            fields='spreadsheetId').execute()
    print('Spreadsheet ID: {0}'.format(spreadsheet.get('spreadsheetId')))

    """

    """

    # this code was used to access a range in the HEALTH SHEET and Print it
    
    result = sheet.values().get(spreadsheetId='17y4Evak7BfeGwVpiZ0AUL8gf0IXWuxvxBHRw5kYkhBg',
                                range=SAMPLE_RANGE_NAME).execute()
    rows = result.get('values', [])
    print('{0} rows retrieved.'.format(len(rows)))

    for x in range(len(rows)): 
        print (rows[x])

    """


if __name__ == '__main__':
    main()