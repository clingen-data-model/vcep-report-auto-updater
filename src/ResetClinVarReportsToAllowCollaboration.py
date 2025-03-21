import gspread
from oauth2client.service_account import ServiceAccountCredentials
from AllowCollaboration import allowCollaboration

# Google Sheets API setup
SHEET_ID = "1bADskBcobHTmmXungY09beWPDEa1nqM-PP__86yGVj0"
RANGE_NAME = "A2:K"

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Authenticate and initialize gspread
creds = ServiceAccountCredentials.from_json_keyfile_name("resources/clingen-dev-d4160bc486ae.json", scope)
client = gspread.authorize(creds)

# print("Successfully authenticated")

# Open the Google Sheet by ID
sheet = client.open_by_key(SHEET_ID)

# Select the first worksheet (Sheet1)
worksheet = sheet.worksheet("Reports")

# Get the values from the specified range
reports = worksheet.get(RANGE_NAME)

# Pass the 7th element (google sheet id) of the first row to the allowCollaboration function
# for report in reports[:4]:
for report in reports:
  if len(report) > 8 and report[8] == "To Do":
    allowCollaboration(report[6])
    worksheet.update_cell(reports.index(report) + 2, 9, "Done")
