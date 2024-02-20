from sense_hat import SenseHat
import time
import datetime

import numpy as np
import time
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import CircularOutput
from libcamera import controls
import cv2

sense=SenseHat()
blue = (0,0,255)
yellow = (255,255,0)
red = (255,0,0)

initial_temperature=round(sense.get_temperature(),1)
initial_humidity=sense.get_humidity()

while True:
    current_temperature = round(sense.get_temperature(), 1)
    current_humidity = round(sense.get_humidity(),1)
    if abs(current_temperature-initial_temperature) >=1 or abs(current_humidity-initial_humidity) >= 1:

        picam2=Picamera2()  ## Create a camera object

        dispW=1280
        dispH=720
        ## Next, we configure the preview window size that determines how big should the image be from the camera, the bigger the image the more the details you capture but the slower it runs
        ## the smaller the size, the faster it can run and get more frames per second but the resolution will be lower. We keep 
        picam2.preview_configuration.main.size= (dispW,dispH)  ## 1280 cols, 720 rows. Can also try smaller size of frame as (640,360) and the largest (1920,1080)
        ## with size (1280,720) you can get 30 frames per second

        ## since OpenCV requires RGB configuration we set the same format for picam2. The 888 implies # of bits on Red, Green and Blue
        picam2.preview_configuration.main.format= "RGB888"
        picam2.preview_configuration.align() ## aligns the size to the closest standard format
        picam2.preview_configuration.controls.FrameRate=30 ## set the number of frames per second, this is set as a request, the actual time it takes for processing each frame and rendering a frame can be different

        picam2.configure("preview")
        ## 3 types of configurations are possible: preview is for grabbing frames from picamera and showing them, video is for grabbing frames and recording and images for capturing still images.


        picam2.start()

        faceCascade=cv2.CascadeClassifier("/home/pi/Downloads/haarcascade_frontalface_default.xml")


        while True:
            #tstart=time.time()
            frame=picam2.capture_array() ## frame is a large 2D array of rows and cols and at intersection of each point there is an array of three numbers for RGB i.e. [R,G,B] where RGB value ranges from 0 to 255
            frameGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces=faceCascade.detectMultiScale(frameGray,1.3,5)
            count = 0
            #print(faces)
            for face in faces:
                x,y,w,h=face
                cv2.rectangle(frame, (x,y), (x+w, y+h),(255,0,0),3)
                if face is not None:
                    count += 1
            print(count)

            
            ## frame[rows,columns] --> is the pixel of each frame
            
            ## the above command will only grab the frame
            
            cv2.imshow("piCamera2", frame) ## show the frame
            time.sleep(0.1)
            key=cv2.waitKey(1) & 0xFF
            
            if key ==ord(" "):
                cv2.imwrite("frame-" + str(time.strftime("%H:%M:%S", time.localtime())) + ".jpg", frame)
            if key == ord("q"): ## stops for 1 ms to check if key Q is pressed
                break
        
        
cv2.destroyAllWindows()
