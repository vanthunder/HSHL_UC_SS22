import numpy as np

from PyQt5.QtCore import Qt, QThread, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout, QApplication, QSlider, QLabel
from PyQt5.uic.properties import QtGui
from pyqtgraph import ImageView


class StartWindow(QMainWindow):
    def __init__(self, camera = None):
        super().__init__()
        self.camera = camera

        self.central_widget = QWidget()
        self.button_frame = QPushButton('Acquire Frame', self.central_widget)
        self.button_movie = QPushButton('Start Movie', self.central_widget)
        self.image_view = ImageView()
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,10)

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addWidget(self.button_frame)
        self.layout.addWidget(self.button_movie)
        self.layout.addWidget(self.image_view)
        self.layout.addWidget(self.slider)
        self.setCentralWidget(self.central_widget)

        self.button_frame.clicked.connect(self.update_image)
        self.button_movie.clicked.connect(self.start_movie)
        self.slider.valueChanged.connect(self.update_brightness)

        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_movie)

    def update_image(self):
        frame = self.camera.get_frame()
        self.image_view.setImage(frame.T)

    def update_movie(self):
        #self.image_view.setImage(self.camera.last_frame.T)
        image = np.array(self.camera.last_frame.T).reshape(2048, 2048).astype(np.int32)
        qimage = QtGui.QImage(image, image.shape[0], image.shape[1], QtGui.QImage.Format_RGB32)
        img = PrintImage(QPixmap(qimage))
        #image = self.camera.last_frame.T
       # h, w = image.shape

        label = QLabel(self)
        pixmap = QPixmap(self.camera.last_frame.T)
        label.setPixmap(pixmap)
        self.image_view=label

        # Optional, resize window to image size
        #self.resize(pixmap.width(), pixmap.height())
        #image = np.transpose(image, (1, 0, 2)).copy()
        #self.image_view.setImage(image)

    def update_brightness(self, value):
        value /= 10
        self.camera.set_brightness(value)

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
