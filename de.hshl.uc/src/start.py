import cv2
from PyQt5.QtWidgets import QApplication

from model.camera import Camera
from user_interface.mainWindow import StartWindow
from recognition.hand_detector import hand_detector
#from Socket import New_Client

# Setup the camera
video = 'hands.mp4'
handDetector = hand_detector()
camera = Camera(video)
# camera.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# camera.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 240)
camera.initialize()
#client = New_Client
# Qt Start Code
app = QApplication([])
start_window = StartWindow(camera, hand_detector)
start_window.show()
app.exit(app.exec_())
