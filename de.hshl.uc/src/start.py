from PyQt5.QtWidgets import QApplication

from model.camera import Camera
from recognition.hand_detector import hand_detector
from user_interface.mainWindow import StartWindow

# Setup the camera
video = 'hands.mp4'
handDetector = hand_detector()
camera = Camera(0)
camera.initialize()

# Qt Start Code
app = QApplication([])
start_window = StartWindow(camera, hand_detector)
start_window.show()
app.exit(app.exec_())
