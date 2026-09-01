from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")

language_link = driver.find_element(By.LINK_TEXT, "About")
language_link.click()

time.sleep(3)

driver.quit()