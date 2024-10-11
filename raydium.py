from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(2) ################################################################################################### implicit delay


driver.get("https://web.telegram.org/a/#-1002145187012")