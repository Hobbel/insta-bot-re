from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.instagram.com")

# Wait for the page to load
time.sleep(3)

# Log in (replace with your credentials)
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
username.send_keys("YOUR_USERNAME")
password.send_keys("YOUR_PASSWORD")
password.send_keys(Keys.RETURN)

# Wait for the login to complete
time.sleep(5)

# Navigate to the target account
target_account = "TARGET_ACCOUNT_NAME"
driver.get(f"https://www.instagram.com/{target_account}/")

# Wait for the account page to load
time.sleep(3)

# Click the three dots
options = driver.find_element(By.XPATH, "//button[contains(text(), '...')]")
options.click()

# Select "Report"
report_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Report')]")
report_button.click()

# Follow the steps to report the account
time.sleep(2)
report_reason = driver.find_element(By.XPATH, "//button[contains(text(), 'It's inappropriate')]")
report_reason.click()

time.sleep(2)
confirm_report = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit report')]")
confirm_report.click()

# Close the browser
driver.quit()
