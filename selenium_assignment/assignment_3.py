from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://practicetestautomation.com/practice-test-login/")



user_input = driver.find_element(By.CSS_SELECTOR, "input[id^='user']")
user_input.send_keys("student")


pass_input = driver.find_element(By.CSS_SELECTOR, "input[name$='word']")
pass_input.send_keys("Password123")

submit_btn = driver.find_element(By.CSS_SELECTOR, "button[class*='bt']")
print("Button found with wildcard:", submit_btn.text)
submit_btn.click()