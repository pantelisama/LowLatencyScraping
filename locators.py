from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.get("http://rahulshettyacademy.com/angularpractice/")




############################ ID, Xpath, CSSSelector , Classname , name, linkText


# CSS Selector   tagname[attribute='value']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Pantelos")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

# name
driver.find_element(By.NAME, "email").send_keys("rocktelis@gmail.com")

# id
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Shotoku1@")

# static dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Male")
dropdown.select_by_index(0)
# dropdown.select_by_value()


#Xpath
driver.find_element(By.XPATH, "//input[@type='submit']").click()


# classname
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

# Xpath
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("hello")



