from PyQt5.QtWidgets import QApplication

from model.camera import Camera
from user_interface.mainWindow import StartWindow
from recognition.hand_detector import hand_detector

# Setup the camera
video = 'hands.mp4'
camera = Camera(video)
camera.initialize()
# Qt Start Code
app = QApplication([])
start_window = StartWindow(camera)
start_window.show()
app.exit(app.exec_())
