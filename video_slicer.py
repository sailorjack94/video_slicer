import cv2
import os
import sys


# cwd stores the current path to the script (and also the video file)
cwd = os.getcwd()


# update the vid variable with the name of the video file you wish to slice
vid = cv2.VideoCapture('test1.mov')

# specify the number of frames to be taken from the video per second below
FPS = 1
vid.set(cv2.CAP_PROP_FPS, FPS)

# creates output photo folder
try: 
    if os.path.exists('frames'):
        print('Output directory already exists, please empty it, or try a new directory name...')
        exit()
    else: 
        os.makedirs('frames')
        print('Output directory successfully created...')
except OSError:
    print('File error, please try again and re-check variables.')

# sets up holding values, counter 'i' and a bool return and frame data for each slice
i = 0
ret, frame = vid.read()

# initialise loop to continue processing while a 'next frame' exists
while (ret):
    vid.set(cv2.CAP_PROP_POS_MSEC, i*1000)
    fileName = './frames/frame' + str(i)+'.jpeg'
    print('Processing: ' + fileName)
    resized = cv2.resize(frame, (400,400))
    cv2.imwrite(fileName, resized)

    ret, frame = vid.read()
    i += 1

vid.release()
