from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(2) ################################################################################################### implicit delay


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


driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait = WebDriverWait(driver,10)################################################################################################### explicit delay
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo"))) ############################################

info = driver.find_element(By.CLASS_NAME, "promoInfo").text


assert info == "Code applied ..!"

results = driver.find_elements(By.CSS_SELECTOR, ".amount")
counter = len(results)


for result in results:
    result.find_element(By.XPATH, "")



