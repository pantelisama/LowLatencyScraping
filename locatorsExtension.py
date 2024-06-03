from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.get("http://rahulshettyacademy.com/client/")




driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("pantelis@gmail.com")

