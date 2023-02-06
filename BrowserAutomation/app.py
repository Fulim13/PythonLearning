from selenium import webdriver
from selenium.webdriver.common.by import By
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(PATH)

browser.get("https://github.com")
browser.maximize_window()
time.sleep(2)
sign_in_link = browser.find_element(By.PARTIAL_LINK_TEXT, "Sign in")
sign_in_link.click()
time.sleep(2)
username_box = browser.find_element(By.ID, "login_field")
username_box.send_keys("fulim1130@gmail.com")
password_box = browser.find_element(By.ID, "password")
password_box.send_keys("Wong.0230")
password_box.submit()
time.sleep(2)
assert "Fulim13" in browser.page_source
profile_box = browser.find_element(By.CLASS_NAME, "avatar-small")
profile_box.click()
time.sleep(2)
profile_link = browser.find_element(By.CLASS_NAME, "user-profile-link")
link_label = profile_link.get_attribute("innerHTML")

assert "Fulim13" in link_label

time.sleep(10)
browser.close()

# DOCUMENTATION
# https://selenium-python.readthedocs.io/getting-started.html
