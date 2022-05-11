import io
import sys
import threading

import keyboard
import qimage2ndarray as qimage2ndarray
from PyQt5.QtWidgets import QGraphicsRectItem, QGraphicsView, QGraphicsProxyWidget, QMessageBox, QStackedLayout, \
    QHBoxLayout
from PyQt5 import QtGui, QtCore

import numpy as np

from PyQt5.QtCore import Qt, QThread, QTimer, pyqtSignal, pyqtSlot, QRectF, QRect
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout, QApplication, QSlider, QLabel, QSizePolicy
from PyQt5 import QtGui

from pyqtgraph import ImageView
from PyQt5.QtGui import QImage, QPalette, QPixmap, QPainter, QPen, QFont
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
    update_player_2 = pyqtSignal(int)
    starte_receive_loop = pyqtSignal(local_client)
    counter = int(1)
    client = local_client()


    def __init__(self, camera, hand_detector):
        super().__init__()
        self.camera = camera
        self.hand_detector = hand_detector
        hd = self.hand_detector
        gd = gesture_detector()

    def start_receive(self):
        self.client.receive()
        print("THEADING!!!!!")


     #Camera Loop
    def run(self):
        bX = 0
        bY = 0
        speedX = 10
        speedY = 0
        hd = hand_detector()
        gd = gesture_detector()
        lmList = []

        # Left or Right
        Player = 'Left'#input('Player: ')

        self.client.player = Player
        rThread = threading.Thread(target=self.start_receive, args=())
        #rThread.start()
        #self.starte_receive_loop.emit(self.client)
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
                    # Send Tupel
                   print('Send Coordinates form Main Window')
                   self.client.sendcoordinate(Player,lmList[0].__getitem__(2))
                   print('Send Coordinates form Main Window 2')
                   print("Player:  ",self.client.TempTupel.__getitem__(0))

                   if self.client.TempTupel.__getitem__(0) == 'Left':
                      self.update_label_signal.emit(self.client.TempTupel.__getitem__(1))
                   else:
                      self.update_player_2.emit(self.client.TempTupel.__getitem__(1))
                   print()
                #print(client.y)
                #To Do receive Coordinate

                # Updates the label



class StartWindow(QMainWindow):
    window_title = ""
    def __init__(self, camera=None, hand_detector=None, local_cL = None):
        super().__init__()
        self.window_title = 'start'
        self.fontA = QFont("Josefin Sans Medium", 24)
        self.bX = 0
        self.bY = 0
        self.positive = True
        self.camera = camera
        self.hand_detector = hand_detector
        self.local_cL = local_cL
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
        # Central Widget
        self.central_widget = QWidget()
        self.layout_for_wids = QStackedLayout()

        # Widgets
        self.wid_start = QWidget()
        self.wid1 = QWidget()
        #self.wid_start.setStyleSheet("""background: blue;""")

        # Layout Container for Widgets and Buttons
        self.layout_for_wids.addWidget(self.wid_start)
        self.layout_for_wids.addWidget(self.wid1)

        # Info Label
        self.info_Label_Container = QLabel()
        self.info_Label_Container.setStyleSheet("margin-left: 10px; border-radius: 25px; background: #8BC1E9; color: black;")
        self.info_Label_Container.setFont(self.fontA)
        #self.info_Label_Container.setMaximumSize(100, 400)
        self.info_Label_Container.setAutoFillBackground(True)
        #self.info_Label_Container.setStyleSheet("""background: #ebef00;""")
        # Date Label
        self.date_label = QLabel()
        self.date_label.setText("Montag")
        self.date_label.setFont(self.fontA)
        # Clock
        self.clock_label = QLabel()
        self.clock_label.setText("20:00")
        self.clock_label.setFont(self.fontA)
        # Temp
        self.temp_label = QLabel()
        self.temp_label.setText("24°C")
        self.temp_label.setFont(self.fontA)
        # Fact Label
        self.fact_label = QLabel()
        self.fact_label.setText("Lorem ipsum dolor sit amet, \nconsetetur sadipscing elitr, \nsed diam nonumy eirmod tempor invidunt \nut labore et dolore magna aliquyam \nerat, sed diam voluptua. \nAt vero eos et accusam et justo duo dolores et ea rebum. \nStet clita kasd gubergren, \nno sea takimata sanctus est Lorem ipsum dolor sit amet.")
        self.fact_label.setFont(self.fontA)

        # Hbox
        self.mid_label_container = QLabel()
        self.mid_label_container.layout = QHBoxLayout(self.mid_label_container)
        # inner vbox
        self.inner_vbox_label_container = QLabel()
        self.inner_vbox_label_container.layout = QVBoxLayout(self.inner_vbox_label_container)
        # Adds Buttons to the inner box
        self.button_Opinion = QPushButton('Meinungsumfrage', self.inner_vbox_label_container)
        self.button_Opinion.setStyleSheet("background-color: #B28BBC; border-style: thin; border-color: black; border-width: 5px; border-radius: 10px;")
        self.button_Opinion.setMinimumSize(200,200)
        self.button_Play = QPushButton('Spielesammlung', self.inner_vbox_label_container)
        self.button_Play.setStyleSheet("background-color: #4B6E74; border-style: thin; border-color: black; border-width: 5px; border-radius: 10px;")
        self.button_Play.setMinimumSize(200, 200)
        self.inner_vbox_label_container.layout.addWidget(self.button_Opinion)
        self.inner_vbox_label_container.layout.addWidget(self.button_Play)
        # Adds the inner box to the outer box
        self.mid_label_container.layout.addWidget(self.inner_vbox_label_container)
        # Chat Container
        # outer box
        self.outer_chat_v_label = QLabel()
        self.outer_chat_v_label.layout = QVBoxLayout(self.outer_chat_v_label)
        self.outer_chat_v_label.setStyleSheet("border-radius: 25px; background: #F7AF9D; color: black;")
        # inner box
        self.inner_chat_label = QLabel()
        self.inner_chat_label.setText("Lorem ipsum dolor sit amet, \nconsetetur sadipscing elitr, \nsed diam nonumy eirmod tempor invidunt \nut labore et dolore magna aliquyam \nerat, sed diam voluptua.")
        self.inner_chat_label.setStyleSheet("border-radius: 25px; background: #EBEFF0; color: black;")
        self.inner_chat_label.setMinimumWidth(800)
        self.inner_chat_label.setFont(self.fontA)
        # Adds the inner box to the outer box
        self.outer_chat_v_label.layout.addWidget(self.inner_chat_label)
        # Adds the chat to the midd label container
        self.mid_label_container.layout.addWidget(self.outer_chat_v_label)









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
        self.button_movie = QPushButton('Start Movie', self.wid1)
        #self.pd = QGraphicsRectItem(1, 1, 20, 20, self.central_widget)
        # self.image_view = ImageView()

        self.wid_start.layout = QVBoxLayout(self.wid_start)
        self.wid_start.layout.addWidget(self.info_Label_Container)
        self.info_Label_Container.layout = QHBoxLayout(self.info_Label_Container)
        self.info_Label_Container.layout.addWidget(self.date_label)
        self.info_Label_Container.layout.addWidget(self.clock_label)
        self.info_Label_Container.layout.addWidget(self.temp_label)
        self.info_Label_Container.layout.addWidget(self.fact_label)
        self.wid_start.layout.addWidget(self.mid_label_container)
        self.wid1.layout = QVBoxLayout(self.wid1)
        self.wid1.layout.addWidget(self.imageLabel)
        self.wid1.layout.addWidget(self.button_movie)
        self.wid1.setMinimumSize(1920, 1080)
        self.central_widget.setLayout(self.layout_for_wids)


        #self.layout = QVBoxLayout(self.central_widget)
        #self.layout.addWidget(self.imageLabel)
        self.setCentralWidget(self.central_widget)

        self.button_movie.clicked.connect(self.start_movie)
        self.button_Play.clicked.connect(self.start_Game)


    def start_Game(self):
        print("Test")
        if self.window_title == 'start':
            print("True")
            self.window_title = 'game'
            self.wid_start.hide()
            self.wid1.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.local_cL.close_client()
            event.accept()

            print('Window closed')
        else:
            event.ignore()

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
        #self.imageLabel2.setGeometry(QRect(1400,c-200,10,400))
        print("Klick")
    def updatePositionPlayer2(self, y):
        print(y," TEST")
        self.imageLabel2.setGeometry(QRect(1400,y-200,10,400))

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
    def start_thread_receive(self, local_cla):
        self.local_cL = local_cla

    def start_movie(self):
        # create the video capture thread
        self.thread = VideoThread(self.camera, self.hand_detector)
        #self.thread.client.client.close()
        self.local_cL = self.thread.client
        print(self.local_cL)
        self.thread.starte_receive_loop.connect(self.start_thread_receive)
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.update_label_signal.connect(self.updatePosition)
        self.thread.update_ball_signal.connect(self.updateBall)
        self.thread.update_player_2.connect(self.updatePositionPlayer2)
        # start the thread
        self.thread.start()
        #self.thread1.start()
        # self.update_timer.start(30)


if __name__ == '__main__':
    app = QApplication([])
    window = StartWindow()
    window.setWindowTitle('Project: UBI')
    window.setBaseSize(2400, 1444)
    window.show()
    app.exit(app.exec_())
