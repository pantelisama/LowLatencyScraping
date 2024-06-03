import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


driver = webdriver.Firefox()
driver.get("http://192.1.0.132/Web/Index.htm")
time.sleep(4)


# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

#pantelos commit2

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):

    pan = driver.find_element(By.ID, "PosP").text
    tilt = driver.find_element(By.ID, "PosT").text
    clean = pan.replace("Pan", "")
    cleanT = tilt.replace("Tilt", "")

    clean2 = os.linesep.join([s for s in clean.splitlines() if s])
    clean2T = os.linesep.join([s for s in cleanT.splitlines() if s])

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(float(clean2))

    f = open("pantilt.txt", "a")
    f.write(dt.datetime.now().strftime('%H:%M:%S') + "," + clean2 + "," + clean2T + "\n")
    f.close()

    # Limit x and y lists to 20 items
    xs = xs[-100:]
    ys = ys[-100:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Pan')
    plt.ylabel('Pan Over Time')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=100)
plt.show()
