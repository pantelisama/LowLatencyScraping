from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "(//div[@class='products'])/div")
counter = len(results)

assert counter > 0
for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "(//img[@alt='Cart'])[1]").click()
driver.find_element(By.XPATH, "(//button[normalize-space()='PROCEED TO CHECKOUT'])[1]").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

promoinfo = driver.find_element(By.CLASS_NAME, "promoInfo").text


assert promoinfo == "Code applied ..!"



