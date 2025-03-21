from selenium import webdriver

# For Chrome
driver = webdriver.Chrome()

# For Firefox
# driver = webdriver.Firefox()

driver.get("http://www.google.com")
print(driver.title)
driver.quit()