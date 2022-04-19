import numpy as np

from PyQt5.QtCore import Qt, QThread, QTimer
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout, QApplication, QSlider, QLabel, QSizePolicy
from PyQt5.uic.properties import QtGui
from pyqtgraph import ImageView
from PyQt5.QtGui import QImage, QPalette, QPixmap


class StartWindow(QMainWindow):
    def __init__(self, camera = None):
        super().__init__()
        self.camera = camera

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

        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_movie)

    def update_movie(self):

        image = np.array(self.camera).reshape(1920, 1080).astype(np.int32)
        #image = np.transpose(image, (1, 0, 2)).copy()
        qimage = QtGui.QImage(image, image.shape[0], image.shape[1], QtGui.QImage.Format_RGB32)
        self.imageLabel.setPicture(QImage(qimage))



    def start_movie(self):
        self.movie_thread = MovieThread(self.camera)
        self.movie_thread.start()
        self.update_timer.start(30)


class MovieThread(QThread):
    def __init__(self, camera):
        super().__init__()
        self.camera = camera

    def run(self):
        self.camera.acquire_movie(200)

if __name__ == '__main__':
    app = QApplication([])
    window = StartWindow()
    window.show()
    app.exit(app.exec_())
