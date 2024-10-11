import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


driver = webdriver.Firefox()
driver.get("http://192.1.0.131/Web/Index.htm")
time.sleep(4)




pan = driver.find_element(By.ID, "PosP").text
  #pan_encoder = driver.find_element(By.ID, "StegPosP").text
  #pan_high_limit = driver.find_element(By.ID, "HiLimP").text
  #pan_low_limit = driver.find_element(By.ID, "LoLimP").text

clean = pan.replace("Pan", "")
  #cleanT = pan_encoder.replace("Pan", "")
  #cleanTfixed = cleanT.rstrip("NaN")
  #cleanTT = pan_high_limit.replace("Pan", "")
  #cleanTTT = pan_low_limit.replace("Pan", "")


pan_position = os.linesep.join([s for s in clean.splitlines() if s])   ######################## PAN POSITION
 # pan_encoder = os.linesep.join([s for s in cleanTfixed.splitlines() if s])   ######################## PAN ENCODER
 # pan_high = os.linesep.join([s for s in cleanTT.splitlines() if s])     ######################## PAN HIGH LIMIT
 # pan_low = os.linesep.join([s for s in cleanTTT.splitlines() if s])     ######################## PAN LOW LIMIT


print(dt.datetime.now().strftime('%H:%M:%S') + "," + pan_position + "\n")


f = open("pantilt.txt", "a")
f.write(dt.datetime.now().strftime('%H:%M:%S') + "," + pan_position + "\n")
f.write("")
f.close()




