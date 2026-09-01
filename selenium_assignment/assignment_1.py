
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://practicetestautomation.com/practice-test-login/")



username = driver.find_element(By.ID, "username")
username.send_keys("student")


password = driver.find_element(By.NAME, "password")
password.send_keys("Password123")


submit_btn = driver.find_element(By.CLASS_NAME, "btn")
print("Button Text:", submit_btn.text)


heading = driver.find_element(By.TAG_NAME, "h2")
print("Heading Found:", heading.text)


home_link = driver.find_element(By.LINK_TEXT, "Home")
print("Link URL:", home_link.get_attribute("href"))