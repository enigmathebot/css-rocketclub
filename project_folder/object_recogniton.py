# Created by Shelby Palmer
# Haar-cascade Detection

from __future__ import print_function
import cv2 as cv # OpenCV library
import argparse #helps you write CLI code

def detectAndDisplay(frame):
    frame_gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY) #converts color to grayscale
    frame_gray=cv.equalizeHist(frame_gray) #equalizes histogram values (for grayscale pixels)

    # - Detect Faces -

    faces = face_cascade.detectMultiScale(frame_gray) # detect multiple sizes of faces
    for (x,y,w,h) in faces:
        # // means division with no remainder
        # center's x coordinate: x + half of image width (x axis)
        # center's y coordinate: y + half of the image's height (y axis)
        center = (x + w//2, y + h//2)
        #ellipse arguments: cv2.ellipse(image, center_coordinates, axesLength, angle, start angle, end angle, color, thickness)
        frame = cv.ellipse(frame, center, (w//2), (h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = frame_gray[y:y+h, x:x+w]

        # - In each face, detect eyes - 
        # detectMultiScale is used to detect faces it returns a rectangle with 
        # coordinates (x,y,w,h) around the detected face it takes 3 common arguments
        # input image, scaleFactor and minNeighbors
        # scaleFactor how much the image size is reduced with each scale
        # minNeighbors paraneter specifying how many neighbors can candidate rectangle should have retain it
        # minSize minimum possible object size, objects smaller than that are ignored
        eyes = eyes_cascade.detectMultiscale(faceROI)
        for (x2, y2, w2, h2) in eyes:
            eyes_center = (x+x2 + w2//2, y+y2+h2//2)
            radius = int(round((w2+h2)*0.25))
            frame = cv.circle(frame, eye_center, radius (255,0,0), 4)

        cv.imshow('Capture - Face Detection', frame)
    
    # argparse helps create a program in a command-line environment and generates error messages
    parser = argparse.ArgumentParser(description= 'Code for Cascade Classifier tutorial.')
    parser.add_argument('--face_cascade', help='Path to face cascade.', default = 'add')
    parser.add_argument('--eye_cascade', help='Path to eyes cascade.', default='data')
    parser.add_argument('--camera', help='Camera divide number.', type=int, default=0)
    args=parser.parse_args()

    face_cascade_name=args.face_cascade
    eyes_cascade_name=args.eyes_cascade

    face_cascade=cv.CascadeClassifier()
    eyes_cascade=cv.CascadeClassifier()

    #-- 1. Load the cascades
    if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
        print('--(!)Error loading face cascade')
        exit(0)
    if not eyes_cascade.load(cv.samples.findFile(eyes_cascade_name)):
        print('--(!)Error loading eyes cascade')
        exit(0)

    camera_device=args.camera
    #-- 2. Read the video stream
    # cap is a video capture object (it's argument can be either the device index or the name of a video file)
    # a device index is just the number to specify which camera
    # don't forget to release the capture at the end
    cap = cv.VideoCapture(camera_device)
    if not cap.isOpened:
        print('--(!)Error opening video capture')
        exit(0)
    
    while True:
        # cap.read returns a bool, if frame is read correctly True
        # if frame is read ret is true
        ret,frame = cap.read()
        if frame is None:
            print('--(!) No captured frame -- Break!')
            break

        detectAndDisplay(frame)
        # display the image for 27 ms before it automatically closes
        if cv.waitKey(10) == 27:
            break
