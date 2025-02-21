import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import math
import logging

logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)
logging.basicConfig(filename='spreadsheet_update.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

SCOPE = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = "1hoY87CzLOdPwfl31fR1gFkP7SJvvwz0Mm9_W5ht9OF8"
CLEAR_RANGE = "engenharia_de_software!G4:H27"
DATA_RANGE = "engenharia_de_software!A4:H27"


def check_situation(tests_average, class_frequency):
    if class_frequency > 0.25:
        return "AbsentFailed for Absence"
    elif tests_average < 50:
        return "Failed by Grade"
    elif tests_average <= 50 or tests_average < 70:
        return "Final Test"
    else:
        return "Approved"


def clear_fields(sheet):
    try:
        clear_values = [["" for _ in range(2)] for _ in range(24)]
        body = {'values': clear_values}
        sheet.values().update(spreadsheetId=SPREADSHEET_ID, range=CLEAR_RANGE,
                              valueInputOption='USER_ENTERED', body=body).execute()
        logging.info("Fields G4:H27 cleared successfully.")
        print("Fields G4:H27 cleared successfully!")
    except HttpError as err:
        logging.exception(f"An HTTP error occurred while clearing fields: {err}")
        print(err)


def calculate_grades(creds):
    try:
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()
        clear_fields(sheet)
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=DATA_RANGE).execute()
        values = result.get("values", [])
        logging.info("Spreadsheet data retrieved.")
        if not values:
            logging.warning("No data found in spreadsheet.")
            print("No data found.")
            return

        for i, row in enumerate(values[0:]):
            try:
                class_frequency = float(row[2]) / 60
                tests_average = (float(row[3]) + float(row[4]) + float(row[5])) / 3
                course_situation = check_situation(tests_average, class_frequency)
                row.append(course_situation)
                if course_situation == "Final Test":
                    row.append(math.ceil(10 - tests_average / 10))
                else:
                    row.append(0)
                logging.info(
                    f"Row {i + 4}: Average={tests_average}, Absence={class_frequency}, Status={course_situation}")
            except (ValueError, IndexError) as e:
                logging.error(f"Error processing row {i + 4}: {e}")
                print(f"Error to process row {i + 4}. Check the data.")

        body = {'values': values}
        sheet.values().update(spreadsheetId=SPREADSHEET_ID, range=DATA_RANGE,
                              valueInputOption='USER_ENTERED', body=body).execute()
        logging.info("Spreadsheet updated successfully.")
        print("Spreadsheet updated successfully!")
    except HttpError as err:
        logging.exception(f"An HTTP error occurred: {err}")
        print(err)
    except Exception as e:
        logging.exception(f"A general error occurred: {e}")
        print(f"A general error occurred: {e}")


def main():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPE)
        logging.info("Credentials loaded from token.json")
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            logging.info("Credentials refreshed.")
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPE
            )
            creds = flow.run_local_server(port=0)
            logging.info("New credentials obtained.")
        with open("token.json", "w") as token:
            token.write(creds.to_json())
            logging.info("Credentials saved to token.json")
    calculate_grades(creds)


if __name__ == "__main__":
    main()
