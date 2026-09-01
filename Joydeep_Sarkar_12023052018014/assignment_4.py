from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get("https://the-internet.herokuapp.com/login")



login_btn = driver.find_element(By.CSS_SELECTOR, "form#login > button[type='submit']")


user_field = driver.find_element(By.CSS_SELECTOR, "form#login div > input#username")
pass_field = driver.find_element(By.CSS_SELECTOR, "form#login div > input#password")

user_field.send_keys("tomsmith")
pass_field.send_keys("SuperSecretPassword!")
login_btn.click()