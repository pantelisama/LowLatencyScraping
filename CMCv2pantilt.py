from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time




driver = webdriver.Firefox()
driver.get("http://192.1.0.132/Web/Index.htm")
time.sleep(4)

print("Ready for test...............................................")


while True:

  pan = driver.find_element(By.ID, "PosP").text
  tilt = driver.find_element(By.ID, "PosT").text
  clean = pan.replace("Pan","")
  cleanT = tilt.replace("Tilt","")

  clean2 = os.linesep.join([s for s in clean.splitlines() if s])
  clean2T = os.linesep.join([s for s in cleanT.splitlines() if s])

  print(clean2 + "," + clean2T + "\n")

  #f = open("pantilt.txt", "a")
  #f.write(clean2 + "," + clean2T)
  #f.write("")
  #f.close()


