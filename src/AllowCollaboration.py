from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from oauth2client.service_account import ServiceAccountCredentials
import gspread

def allowCollaboration(sheet_id):
  # an array of sheet names "priorities by release", "alerts by release", and "gene list"
  SHEET_NAMES = ["priorities by release", "alerts by release", "gene list"]

  # Construct the full Google Sheets URL
  SHEET_URL = f"https://docs.google.com/spreadsheets/d/{sheet_id}/edit"

  # # Use credentials and a Google service account to authenticate

  # # Define the scope
  # scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

  # # Add credentials to the account
  # creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/credentials.json', scope)

  # # Authorize the client
  # client = gspread.authorize(creds)

  # Attach to the already open Chrome session
  options = webdriver.ChromeOptions()
  options.debugger_address = "localhost:9222"

  driver = webdriver.Chrome(options=options)

  # Open the Google Sheet
  driver.get(SHEET_URL)

  # Wait for page to load
  time.sleep(5)

  # Loop through the sheet names and use each sheet name as the dataConnectorTab name value and then execute all the following commands
  for sheetName in SHEET_NAMES:
    
    # Attempt to open up the hidden dataconnector sheets
    docSheetsButton = driver.find_element(By.XPATH, "//div[contains(@class, 'docs-sheet-menu-button')]")
    docSheetsButton.click()
    time.sleep(1) 

    # Show sheetName tab
    showSheetMenuItem = driver.find_element(By.XPATH, f"//div[(@role='menuitem' or @role='menuitemcheckbox') and .//div[text()='{sheetName}']]")
    showSheetMenuItem.click()
    time.sleep(1)    

    # Click on the first visible cell (adjust selector as needed)
    dataConnectorTab = driver.find_element(By.XPATH, f"//div[@role='button' and contains(@class, 'docs-sheet-tab') and .//span[@class='docs-sheet-tab-name' and text()='{sheetName}']]") 
    dataConnectorTab.click()
    time.sleep(1)

    # Now click on the button "Connect settings"
    connSettingsButton = driver.find_element(By.XPATH, "//div[contains(@class, 'docs-material-button') and .//span[text()='Connection settings']]")
    connSettingsButton.click()
    if sheetName == SHEET_NAMES[0]:
      time.sleep(15)
    else:
      time.sleep(5)

    # Now select the Allow RB
    allowRadioButton = driver.find_element(By.XPATH, "//div[@role='radio' and @data-value='allow']")
    allowRadioButton.click()
    time.sleep(2)

    # Now click the Done button to save the change
    doneButton = driver.find_element(By.XPATH, "//div[@role='button' and (.//span[text()='Done'] or .//span[text()='Connect'])]")
    doneButton.click()
    time.sleep(5)

    # DataConnectorTab popup Menu
    dcTabPopupMenu = driver.find_element(By.XPATH, "//div[contains(@class, 'docs-sheet-active-tab')]//div[contains(@class, 'docs-sheet-tab-dropdown')]")
    dcTabPopupMenu.click()
    time.sleep(1) 

    # Hide sheet menu item
    hideSheetMenuItem = driver.find_element(By.XPATH, "//div[@role='menuitem' and .//div[text()='Hide sheet']]")
    hideSheetMenuItem.click()
    time.sleep(1)

  # Wait and close
  time.sleep(2)
  driver.quit()

def main():
  # Replace with your actual Google Sheet ID
  SHEET_ID = "1lOtofHK1Fb6cy2ATLN6JWXuerGEyWPoceFS1HGrgkH4"
  allowCollaboration(SHEET_ID)

if __name__ == "__main__":
  main()

  # def read_google_sheet(sheet_id, sheet_name):
  #   # Define the scope
  #   scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

  #   # Add credentials to the account
  #   creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/credentials.json', scope)

  #   # Authorize the clientsheet 
  #   client = gspread.authorize(creds)

  #   # Get the instance of the Spreadsheet
  #   sheet = client.open_by_key(sheet_id)

  #   # Get the first sheet of the Spreadsheet
  #   worksheet = sheet.worksheet(sheet_name)

  #   # Get all the records of the data
  #   records = worksheet.get_all_records()

  #   return records

  # def main():
  #   SHEET_ID = "1TwXb_n1ESYatu5XHAqOTu3sGP6jhWb3AHV52ypbpXi8"
  #   SHEET_NAME = "Sheet1"
  #   # allow_collaboration(SHEET_ID)
  #   records = read_google_sheet(SHEET_ID, SHEET_NAME)
  #   print(records)

  # if __name__ == "__main__":
  #   main()