from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get("https://the-internet.herokuapp.com/")

all_links = driver.find_elements(By.TAG_NAME, "a")

print(f"Total links found on webpage: {len(all_links)}\n")

for index, link in enumerate(all_links[:len(all_links)], start=1):
    href = link.get_attribute("href")
    print(f"{index}. Text: '{text}' | URL: {href}")