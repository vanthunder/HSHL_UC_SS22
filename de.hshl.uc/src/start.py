import cv2
import sys

import pandas as pd
from PyQt5.QtWidgets import QApplication


from model.camera import Camera
from user_interface.mainWindow import StartWindow
from recognition.hand_detector import hand_detector
#from Socket import New_Client

# Setup the camera
video = 'hands.mp4'
handDetector = hand_detector()

camera = Camera(0)
#width = camera.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
#height = camera.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
#camera.cap.set(3, 1920)
#camera.cap.set(4, 1080)
#width = camera.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
#
#print(width, height)


# camera.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# camera.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 240)

camera.initialize()
#client = New_Client
# Qt Start Code
app = QApplication([])
start_window = StartWindow(camera, hand_detector)
start_window.show()
app.exit(app.exec_())
