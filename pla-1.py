from sense_hat import SenseHat
import time
from time import sleep

sense=SenseHat()
blue = (0,0,255)
# yellow = (255,255,0)
# red = (255,0,0)
x = 3
y = 5
sense.clear()
sense.set_pixel(x,y, blue)
time.sleep(0.5)
    
while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action)
        if event.action =="pressed" and event.direction=="right":
            if x <= 6:
                x += 1
            sense.clear()
            sense.set_pixel(x,y, blue)
            time.sleep(0.5)
        elif event.action =="pressed" and event.direction=="left":
            if x >= 1:
                x -= 1
            sense.clear()
            sense.set_pixel(x,y, blue)
            time.sleep(0.5)
        elif event.action =="pressed" and event.direction=="down":
            if y <= 6:
                y += 1
            sense.clear()
            sense.set_pixel(x,y, blue)
            time.sleep(0.5)
        elif event.action =="pressed" and event.direction=="up":
            if y >= 1:
                y -= 1
            sense.clear()
            sen
            se.set_pixel(x,y, blue)
            time.sleep(0.5)
        elif event.action =="pressed" and event.direction=="middle":
            sense.clear()
            exit()
            