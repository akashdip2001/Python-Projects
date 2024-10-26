import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time # for time duration to take SS

# Display screen resolution, get it from your OS settings
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dim = (width, height) #or you can use your screen resolution diractly, like (1920, 1080).

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID') #create a variable to store the codec
# save the output video in the same directory
out = cv2.VideoWriter('Python-Projects/10 Screen Recorder/outputVideo.mp4', fourcc, 30.0, dim) #create a video writer object, with the codec, frame rate and screen resolution.

# time duration to take SS
start_time = time.time() # get the current time
duration = 10 + 4 # 10 seconds, +4 seconds for the loop to take SS
end_time = start_time + duration

# loop to take SS
while True:
    img = pyautogui.screenshot() #take a screenshot
    frame = np.array(img) #convert the screenshot to a numpy array
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #convert the BGR image to RGB
    out.write(frame) #write the frame to the video

    # check if the time is up
    if time.time() > end_time:
        break #break the while loop

# Release everything if job is finished
out.release() #release the video writer
print('Done') #print done
