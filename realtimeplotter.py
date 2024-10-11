import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.get("http://192.1.0.131/Web/Index.htm")
driver.implicitly_wait(6)

## Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

#pantelos commit3

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):

    pan = driver.find_element(By.ID, "PosP").text
    tilt = driver.find_element(By.ID, "PosT").text
    height = driver.find_element(By.ID, "PosH").text

    clean = pan.replace("Pan", "")
    cleanT = tilt.replace("Tilt", "")
    cleanH = height.replace("Height", "")


    pan_position = os.linesep.join([s for s in clean.splitlines() if s])
    tilt_position = os.linesep.join([s for s in cleanT.splitlines() if s])
    height_position = os.linesep.join([s for s in cleanH.splitlines() if s])

    print(dt.datetime.now().strftime('%H:%M:%S') + "," + pan_position + "," + tilt_position + "," + height_position + "\n")


     #Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(float(tilt_position))


    f = open("pantilt.txt", "a")
    f.write(dt.datetime.now().strftime('%H:%M:%S') + "," + pan_position + "," + tilt_position + "\n")
    f.close()



    # Limit x and y lists to 20 items
    xs = xs[-100:]
    ys = ys[-100:]

     #Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Tilt over time')
    plt.ylabel('Tilt over time')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=100)
plt.show()
