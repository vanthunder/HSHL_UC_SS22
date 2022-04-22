import io

import keyboard
import qimage2ndarray as qimage2ndarray
from PyQt5.QtWidgets import QGraphicsRectItem, QGraphicsView, QGraphicsProxyWidget
from PyQt5 import QtGui, QtCore

import numpy as np
from PIL import Image

from PyQt5.QtCore import Qt, QThread, QTimer, pyqtSignal, pyqtSlot, QRectF, QRect
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout, QApplication, QSlider, QLabel, QSizePolicy
from PyQt5 import QtGui
from pyqtgraph import ImageView
from PyQt5.QtGui import QImage, QPalette, QPixmap
import cv2
from pyqtgraph.Qt import QtCore

from recognition.hand_detector import hand_detector
from recognition.gesture_detector import gesture_detector
#from Socket.local.localClient import local_client
from Socket.online.onlineClient import local_client


class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    update_label_signal = pyqtSignal(int)
    counter = int(1)


    def __init__(self, camera, hand_detector):
        super().__init__()
        self.camera = camera
        self.hand_detector = hand_detector
        hd = self.hand_detector
        gd = gesture_detector()


    # Camera Loop
    def run(self):
        hd = hand_detector()
        gd = gesture_detector()
        lmList = []
        client = local_client()
        # capture from web cam
        while True:
            success, img = self.camera.cap.read()
            #img.flags.writeable = False
            if success:
                # init Hand detector
                # hd.findHands(img)
                img = self.hand_detector.hand_detector_run(hand_detector, img)
                lmList = self.hand_detector.handlist
                # print(lmList)
                gd.writeLmList(lmList)
                gd.print()
                # cv2.imshow('Test', img)
                self.change_pixmap_signal.emit(img)
                #To Do send to server:
                client.sendcoordinate(lmList[0].__getitem__(2))
                #print(client.y)
                #To Do receive Coordinate
                self.update_label_signal.emit(client.Y)
                # Updates the label



class StartWindow(QMainWindow):

    def __init__(self, camera=None, hand_detector=None):
        super().__init__()
        self.camera = camera
        self.hand_detector = hand_detector
        self.disply_width = 1728
        self.display_height = 972
        self.setWindowTitle('Projekt: Ubi')
        self.setMinimumSize(1920, 1080)


        self.imageLabel = QLabel()
        self.imageLabel.setMaximumSize(1728, 972)
        self.imageLabel.setAutoFillBackground(True)
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setBackgroundRole(QPalette.Base)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        # self.imageLabel.setScaledContents(True)

        self.central_widget = QWidget()
        self.pad = QLabel
       # self.central_widget.a
        self.layout = QVBoxLayout(self.imageLabel)
        self.imageLabel1 = QLabel()
        self.imageLabel1.setMaximumSize(100, 400)
        self.imageLabel1.setAutoFillBackground(True)
        self.imageLabel.layout().addWidget(self.imageLabel1)
       # self.imageLabel.setParent(self.pad)


        #self.setScene(self.scene)
        self.button_movie = QPushButton('Start Movie', self.central_widget)
        #self.pd = QGraphicsRectItem(1, 1, 20, 20, self.central_widget)
        # self.image_view = ImageView()

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

    def updatePosition(self, c):
        self.imageLabel1.setGeometry(QRect(400,c-200,100,400))
        print("Klick")

    def convert_cv_qt(self, cv_img):

        cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        image = qimage2ndarray.array2qimage(cv_img)
        #img = QImage(cv_img, cv_img.shape[1], cv_img.shape[0], QImage.Format_RGB888)
        #pix = QPixmap.fromImage(cv_img)
        #pix = pix.scaled(self.lblVid.width(), self.lblVid.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        #self.lblVid.setPixmap(pix)
        return QPixmap.fromImage(image)
    """Convert from an opencv image to QPixmap"""
       # rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
       # h, w, ch = rgb_image.shape
       # bytes_per_line = ch * w
       # convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
       # p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)


    def start_movie(self):
        # create the video capture thread
        self.thread = VideoThread(self.camera, self.hand_detector)
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.update_label_signal.connect(self.updatePosition)
        # start the thread
        self.thread.start()
        # self.update_timer.start(30)


if __name__ == '__main__':
    app = QApplication([])
    window = StartWindow()
    window.setWindowTitle('Project: UBI')
    window.setBaseSize(1920, 1080)
    window.show()
    app.exit(app.exec_())
