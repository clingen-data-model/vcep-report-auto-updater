# Automating the Allow Collaboration option on New/Updated VCEP Tracker Reports

This project contains a collection of Selenium scripts used for automated updates to the ClinGen VCEP Tracker reports. After new sheets are generated or updated it can cause the Google BigQuery Data connector sheets to be left in a state that does not allow collaborators to refresh the queries. Since there are multiple connector sheets this can take considerable manual time to unhide, open, modify the setting, close and hide each sheet for each report that is new or updated.

To make this process a bit more automated the following setup can be implemented on a users machine that has the access to perform the updates. Once they've installed the required chrome webdriver they should be able to startup the selenium remote chrome browser and then execute the ResetClinVarReportsToAllowCollaboration python script. All reports marked as "To Do" in the "Update Status" column of the "Reports" sheet in the "ClinVar Report BQ Support Tables" google sheet will be processed.  

If the update process stops part way through (due to machine slowness) you can simply rerun the last step and it will pick up where it left off. 

## Basic Steps

- (one time) Setting Up Local Selenium WebDriver Environment
- (one time) Download this github project and make devready
- Run the remote Chrome browser and login to your google account
- Run the ResetClinVarReportsToAllowCollaboration python script

## Setting Up Local Selenium WebDriver Environment

NOTE: requires python 3.x

To ensure that the `allow_collaboration.py` functions run successfully, you need to set up a local Selenium WebDriver environment. Follow these steps:

1. **Install WebDriver for your browser**:
  - **Chrome**: Download the ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and place it in a directory included in your system's PATH.
  - **Firefox**: Download the GeckoDriver from [here](https://github.com/mozilla/geckodriver/releases) and place it in a directory included in your system's PATH.
  

2. **Install Selenium**:
  Ensure you have Selenium installed in your Python environment. You can install it using pip:
  ```bash
  pip install selenium
  ```

3. **Verify Installation**:
  To verify that Selenium and the WebDriver are correctly installed, you can run a simple script to open a browser window:
  ```python
  from selenium import webdriver

  # For Chrome
  driver = webdriver.Chrome()

  # For Firefox
  # driver = webdriver.Firefox()

  driver.get("http://www.google.com")
  print(driver.title)
  driver.quit()
  ```

By following these steps, you will have a local Selenium WebDriver environment set up, allowing the `allow_collaboration.py` functions to run successfully.

## Download this github project and make devready

1. Clone the repository:
  ```bash
  git clone https://github.com/yourusername/selenium_scripts.git
  ```
2. Install the required dependencies using the Makefile:
  ```bash
  make devready
  ```

## Run the remote Chrome browser and login to your google account

Before running the ResetClinVarReportsToAllowCollaboration python script you must first start a local chrome browser instance that is specifically configured to allow the python script to open and modify the VCEP Variation Tracker Reports tagged with an Update Status of "To Do".

1. Open a New Terminal and run the startup-selenium.sh script from the root folder of this project
  ```bash
  ./startup-selenium.sh
  ```
  If the script does not execute you may need to run `chmod +x startup-selenium.sh` beforehand to make it executable.

2. Once you see the new chrome browser startup you will need to login to your google account. It must be a google account that is authorized to open and modify the VCEP Variation Tracker Reports.

Once the browser is logged into your account you can continue to running the ResetClinVarReportsToAllowCollaboration step

## Run the ResetClinVarReportsToAllowCollaboration python script

Before running the ResetClinVarReportsToAllowCollaboration.py script you should open the ClinVar Report BQ Support Tables google sheet and set one or more of the Report's Update Statuses to "To Do". Only the Reports in the Reports tab with the column titled Update Status having a value of "To Do" will be processed by the script.

1. Open a New Terminal and run the run-reset-allow-collaboration.sh script from the root folder of this project
  ```bash
  ./run-reset-allow-collaboration.sh
  ```

The script is designed to read data from the Reports sheet in the ClinVar Report BQ Support Tables google sheet. Any report with the Update Status column set to "To Do" will be processed from top to bottom. As each report is processed fully the status will be set to "Done".

If the script stops executing prematurely simply restart the script and it will pick up where it left off. If the script gets stuck and will not move past a given report then notify the developer for assistance with the issue.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License.