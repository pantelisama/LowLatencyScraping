from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
import time


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")


driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))


for country in countries:
    print(country.text)
    if country.text == "India":
        country.click()
        break

finalselection = driver.find_element(By.ID, "autosuggest").get_attribute("value")
print(finalselection)
assert finalselection == "India"