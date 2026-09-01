from selenium import webdriver

driver = webdriver.Chrome()

print("Browser:", driver.capabilities["browserName"])
print("Browser Version:", driver.capabilities["browserVersion"])
print("ChromeDriver Version:",
      driver.capabilities["chrome"]["chromedriverVersion"])

try:
    driver.get("https://example.com")

    print("Page Title:", driver.title)
    print("Current URL:", driver.current_url)

finally:
    driver.quit()