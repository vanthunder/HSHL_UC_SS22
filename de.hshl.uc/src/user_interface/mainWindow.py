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
from PyQt5.QtGui import QImage, QPalette, QPixmap, QPainter, QPen
import cv2
from pyqtgraph.Qt import QtCore

from recognition.hand_detector import hand_detector
from recognition.gesture_detector import gesture_detector
#from Socket.local.localClient import local_client
from Socket.online.onlineClient import local_client


class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    update_label_signal = pyqtSignal(int)
    update_ball_signal = pyqtSignal()
    counter = int(1)


    def __init__(self, camera, hand_detector):
        super().__init__()
        self.camera = camera
        self.hand_detector = hand_detector
        hd = self.hand_detector
        gd = gesture_detector()


    # Camera Loop
    def run(self):
        bX = 0
        bY = 0
        speedX = 10
        speedY = 0
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
                img_proc = self.hand_detector.find_hands_on_image(self.hand_detector, img)
                lmList = self.hand_detector.handlist
                fps = self.camera.cap.get(cv2.CAP_PROP_FPS)
                cv2.putText(img_proc, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                # print(lmList)
                gd.writeLmList(lmList)
                #gd.print()
                # cv2.imshow('Test', img)
                self.change_pixmap_signal.emit(img_proc)

                # Game Loop
                bX += 1+speedX
                bY += 1+speedY
                #Bewege ball
                self.update_ball_signal.emit()
                #To Do send to server:
                if not lmList:
                    print()
                else:
                   client.sendcoordinate(lmList[0].__getitem__(2))
                   self.update_label_signal.emit(client.Y)
                   print()
                #print(client.y)
                #To Do receive Coordinate

                # Updates the label



class StartWindow(QMainWindow):

    def __init__(self, camera=None, hand_detector=None):
        super().__init__()
        self.bX = 0
        self.bY = 0
        self.positive = True
        self.camera = camera
        self.hand_detector = hand_detector
        self.disply_width = 1920
        self.display_height = 1080
        self.setWindowTitle('Projekt: Ubi')
        self.setMinimumSize(1920, 1200)
        #self.pixmap_item = QPixmap()


        self.imageLabel = QLabel()
        self.imageLabel.setMaximumSize(1920, 1080)
        self.imageLabel.setAutoFillBackground(True)
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setBackgroundRole(QPalette.Base)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)

        self.central_widget = QWidget()


        # Pong paddle
        self.pad_01 = QLabel
        #Player 2
        self.pad02 = QLabel




       # self.central_widget.a
        self.layout = QVBoxLayout(self.imageLabel)
        #Player 1 - Imagelabel 1 = paddle1
        self.imageLabel1 = QLabel()
        self.imageLabel1.setMaximumSize(100, 400)
        self.imageLabel1.setAutoFillBackground(True)
        # Player 2 - Imagelabel 2 = paddle2
        self.imageLabel2 = QLabel()
        self.imageLabel2.setMaximumSize(100, 400)
        self.imageLabel2.setAutoFillBackground(True)
        # Ball - Imagelabel 3 = Ball
        self.imageLabel3 = QLabel('round label')
        self.imageLabel3.move(100,100)
        self.imageLabel3.resize(80, 80)
        self.imageLabel3.setMaximumSize(80, 80)
        self.imageLabel3.setAutoFillBackground(True)
        self.imageLabel3.setStyleSheet("border: 3px solid blue; border-radius: 40px;")

        self.imageLabelRect = QtCore.QRectF(100,100,20,20)
        #self.paint = QPainter(self.imageLabelRect)




        # ball
        self.pixmap = QPixmap(100, 100)
        self.pixmap.fill(Qt.transparent)

        #self.painter = QPainter(self.pixmap)
        #self.painter.setPen(QPen(Qt.green, 4, Qt.SolidLine))
        #self.painter.drawEllipse(self.pixmap.rect().adjusted(4, 4, -4, -4))
        #self.painter.end()

        #self.imageLabel3.setPixmap(self.pixmap)
        #self.imageLabel3.adjustSize()
       # self.imageLabel3.hide()
        #self.imageLabel3.raise_()
        self.imageLabel4 = QLabel
        #self.imageLabel4.setPixmap(self.imageLabel2)


        # Adds paddles to the main image label
#        self.imageLabel.setPixmap(self.pixmap_item)
        self.imageLabel.layout().addWidget(self.imageLabel1)
        self.imageLabel.layout().addWidget(self.imageLabel2)
        self.imageLabel.layout().addWidget(self.imageLabel3)
        #self.imageLabel.layout().addWidget(self.imageLabelRect)
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
        #self.pixmap_item.fromImage(self.convert_cv_qt(cv_img))
        qt_img = self.convert_cv_qt(cv_img)
        self.imageLabel.setPixmap(QPixmap.fromImage(qt_img))

    def updatePosition(self, c):
        self.imageLabel1.setGeometry(QRect(10,c-200,10,400))
        self.imageLabel2.setGeometry(QRect(1400,c-200,10,400))
        print("Klick")

    def updateBall(self):
        print('Die positive Variable: ', self.positive)

        #elif self.detect_collision()==False and not self.positive:
        #    self.positive = True
        if self.detect_collision():
            if self.positive:
                self.positive = False

            elif self.positive == False:
                print('TEST!!!!!!!!!!!!!!!!!!!!!!1!!!1')
                self.positive = True


        if self.positive == True:
            self.ballMovementpositive()
        elif self.positive == False:
             self.ballMovementnegative()





    def ballMovementpositive(self):
        self.bX += 10
        self.bY += 1
        print("TEST")
        self.imageLabel3.setGeometry(self.bX,self.bY, 80, 80)

    def ballMovementnegative(self):
        self.bX -= 10
        #self.bY -= 1
        self.imageLabel3.setGeometry(self.bX,self.bY, 80, 80)


    def detect_collision(self):
          #if self.imageLabel3.geometry().center()+80 == self.imageLabel2.geometry().intersects()
          if self.positive:
              if self.imageLabel3.geometry().intersected(self.imageLabel2.geometry()):
                  print("INTERSECTION!")
                  return True
              else:
                  return False
          else:
              if self.imageLabel3.geometry().intersected(self.imageLabel1.geometry()):
                  print("INTERSECTION!")
                  return True
              else:
                  return False


    def convert_cv_qt(self, cv_img):

        cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        cv_img = qimage2ndarray.array2qimage(cv_img)
        #img = QImage(cv_img, cv_img.shape[1], cv_img.shape[0], QImage.Format_RGB888)
        #pix = QPixmap.fromImage(cv_img)
        #pix = pix.scaled(self.lblVid.width(), self.lblVid.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        #self.lblVid.setPixmap(pix)
        return cv_img
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
        self.thread.update_ball_signal.connect(self.updateBall)
        # start the thread
        self.thread.start()
        # self.update_timer.start(30)


if __name__ == '__main__':
    app = QApplication([])
    window = StartWindow()
    window.setWindowTitle('Project: UBI')
    window.setBaseSize(2400, 1444)
    window.show()
    app.exit(app.exec_())
