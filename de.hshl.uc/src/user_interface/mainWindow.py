import numpy as np

from PyQt5.QtCore import Qt, QThread, QTimer, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout, QApplication, QSlider, QLabel, QSizePolicy
from PyQt5 import QtGui
from pyqtgraph import ImageView
from PyQt5.QtGui import QImage, QPalette, QPixmap
import cv2


class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self, camera):
        super().__init__()
        self.camera = camera

    def run(self):
        # capture from web cam
        while True:
            ret, cv_img = self.camera.cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)


class StartWindow(QMainWindow):

    def __init__(self, camera = None):
        super().__init__()
        self.camera = camera
        self.disply_width = 640
        self.display_height = 480

        self.imageLabel = QLabel()
        self.imageLabel.setBackgroundRole(QPalette.Base)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)

        self.central_widget = QWidget()
        self.button_movie = QPushButton('Start Movie', self.central_widget)
        #self.image_view = ImageView()

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addWidget(self.imageLabel)
        self.setCentralWidget(self.central_widget)

        self.button_movie.clicked.connect(self.start_movie)

       # self.update_timer = QTimer()
       # self.update_timer.timeout.connect(self.update_movie)

    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.imageLabel.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

    def start_movie(self):
        # create the video capture thread
        self.thread = VideoThread(self.camera)
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        # start the thread
        self.thread.start()
        #self.update_timer.start(30)


if __name__ == '__main__':
    app = QApplication([])
    window = StartWindow()
    window.show()
    app.exit(app.exec_())
