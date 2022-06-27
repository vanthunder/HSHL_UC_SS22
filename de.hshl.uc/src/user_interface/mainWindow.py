import threading

import cv2
import numpy as np
import pytz
import qimage2ndarray as qimage2ndarray
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, QRect, QMutex
from PyQt5.QtGui import QPixmap, QFont, QMovie
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication, QLabel, QGridLayout
from PyQt5.QtWidgets import QMessageBox, QStackedLayout, \
    QHBoxLayout

# from Socket.local.localClient import local_client
from pyqtgraph import Qt
from stopwatch import Stopwatch

from Socket.online.onlineClient import local_client
from Socket.online.Chat.Chat_Client_V01 import chat_client
from model.camera import Camera
from recognition.gesture_detector import gesture_detector
from recognition.hand_detector import hand_detector
from user_interface.Tools import FunFacts
from user_interface.pongScreen import pongScreen
from user_interface.startWindow import startWindow

from recognition.body_detector import body_detector
from datetime import datetime
import time

import requests


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



class VideoThread(QThread):
    ar = []
    change_ab_signal = pyqtSignal(int)
    change_pixmap_signal = pyqtSignal(np.ndarray)
    update_label_signal = pyqtSignal(int)
    update_ball_signal = pyqtSignal(int, int)
    update_player_2 = pyqtSignal(int)
    starte_receive_loop = pyqtSignal(local_client)
    update_tor = pyqtSignal()
    counter = int(1)
    client = local_client()

    def __init__(self, camera, hand_detector):
        super(VideoThread, self).__init__()
        self.ser = False
        self.state = 0
        self._mutex = QMutex()
        self.serialEnabled = True
        self.camera = camera
        self.hand_detector = hand_detector
        hd = self.hand_detector
        gd = gesture_detector()

    def start_receive(self):
        self.client.receive()
        print("THEADING!!!!!")

    def videoLoop(self, Player):
        bX = 0
        bY = 0
        speedX = 10
        speedY = 0
        hd = hand_detector()
        gd = gesture_detector()
        lmList = []
        self.hand_detector.handlist = lmList
        video = 'hands.mp4'
        self.camera = Camera(0)
        self.camera.initialize()
        # Left or Right
        #Player = 'Left'  # input('Player: ')

        #self.client.player = Player

        # rThread.start()
        # self.starte_receive_loop.emit(self.client)
        # capture from web cam
        # self.update_chat_signal.emit()
        #self.client.sendReady('Left')
        # self.client.sendcoordinate('Left', 111)

        print("SRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
        while True:
            success, img = self.camera.cap.read()
            # img.flags.writeable = False
            print(self.client.canStart, '2222222222222')

            #if self.client.canStart == True:
            if not self.client.ballcoords.__getitem__(0) == 1011100 and not self.client.ballcoords.__getitem__(
                    0) == 1011101:
                self.update_ball_signal.emit(self.client.ballcoords.__getitem__(0),
                                             self.client.ballcoords.__getitem__(1))
            if success:

                # self.client.canStart = False
                self.change_ab_signal.emit(1)

                # init Hand detector
                # hd.findHands(img)
                img = cv2.resize(img, (1280, 750), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
                img_proc = self.hand_detector.find_hands_on_image(self.hand_detector, img)
                lmList = self.hand_detector.handlist

                # fps = self.camera.cap.get(cv2.CAP_PROP_FPS)
                # cv2.putText(img_proc, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                # print(lmList)
                gd.writeLmList(lmList)
                # gd.print()
                # cv2.imshow('Test', img)
                self.change_pixmap_signal.emit(img_proc)

                # Game Loop
                bX += 1 + speedX
                bY += 1 + speedY
                print(bcolors.OKBLUE, self.client.test, " TorLinks", bcolors.ENDC)
                # Bewege ball
                print(bcolors.FAIL, self.client.ballcoords.__getitem__(0), bcolors.ENDC)

                # Tor L


                # self.update_ball_signal.emit(500, 500)

                # To Do send to server:

                if not lmList:
                    print()
                else:
                    print(bcolors.FAIL, self.client.TempChatList,
                          "EMITYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY",
                          bcolors.ENDC)
                    # self.update_chat.emit()
                    if not self.client.TempChatList:
                        print(bcolors.FAIL,
                              "EMITYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY",
                              bcolors.ENDC)

                    # Send Tupel
                    print('Send Coordinates form Main Window')
                    self.client.sendcoordinate(Player, lmList[0].__getitem__(2))
                    print('Send Coordinates form Main Window 2')
                    # print("Player:  ", self.client.TempTupel.__getitem__(0))

                    if self.client.TempTupel.__getitem__(0) == 'Left':
                        self.update_label_signal.emit(self.client.TempTupel.__getitem__(1))
                    else:
                        self.update_player_2.emit(self.client.TempTupel.__getitem__(1))
                    print()
                # print(client.y)
                # To Do receive Coordinate

                # Updates the label


    # Camera Loop
    def run(self):
        Player = 'Right'  # input('Player: ')

        self.client.player = Player
        rThread = threading.Thread(target=self.start_receive, args=())
        #rThread.start()
        #self.client.receive()
        self.client.sendReady('Right')
        while True:
            if self.client.canStart == True:
                print(bcolors.WARNING, "Starte VideoLoop", bcolors.ENDC)
                self.videoLoop(Player)




class StartWindow(QMainWindow):
    window_title = ""

    def __init__(self, camera=None, hand_detector=None, local_cL=None):
        super().__init__()
        self.threadOpen = False
        self.scoreLeft = False
        self.scoreRight = False
        self.scoreLeftCounter = 0
        self.scoreRightCounter = 0
        self.goalSetBool = True
        self.funFactsClass = FunFacts
        self.funFacts = self.funFactsClass.FunFacts.funFacts
        self.sizeOfAr = len(self.funFactsClass.FunFacts.funFacts)
        self.arCounter = 0
        self.arGlobalCounter = 0
        self.goalCounter = 0
        self.goalGlobalCounter = 0
        self.width = 1280
        self.height = 750
        self.window_title = 'start'
        self.fontA = QFont("Josefin Sans Medium", 24)
        self.fontB = QFont("Josefin Sans Medium", 100)
        self.fontC = QFont("Josefin Sans Medium", 40)
        self.bX = 0
        self.bY = 0
        self.positive = True
        self.counter = 0
        self.camera = camera
        self.hand_detector = hand_detector
        self.local_cL = local_cL
        self.display_width = self.width
        self.display_height = self.height
        self.setWindowTitle('Projekt: Ubi')
        self.setMinimumSize(self.width, self.height)
        self.setMaximumSize(self.width, self.height)
        self.loading = QMovie('Tools/loading-circle.gif')
        # Create Video Thread
        self.thread = BackgroundFeed(self.camera, self.hand_detector)
        # Update Label
        self.thread.change_pixmap_signal.connect(self.update_image)
        # Updates the Cursor
        self.thread.change_cursor_position.connect(self.update_cursor)
        # Debug
        self.thread.change_ab_signal.connect(self.update_chat_debug)
        self.chat_client = self.thread.client
        print(self.chat_client)
        self.thread.change_lc.connect(self.start_thread_receive)
        # Start Thread
        self.thread.update_infolabel.connect(self.update_infolabel)
        self.thread.start()
        # Chat
        self.globalChat = []
        self.stopwatch = Stopwatch(2)

        self.isPause = False
        self.pauseThread = PauseThread()

        # self.pixmap_item = QPixmap()

        # Central Widget
        self.central_widget = QWidget()
        self.layout_for_wids = QStackedLayout()

        self.startWindow = startWindow()
        self.pongWindow = pongScreen()

        # Widgets

        # self.wid_start.setStyleSheet("""background: blue;""")

        # Layout Container for Widgets and Buttons
        self.layout_for_wids.addWidget(self.startWindow)
        self.layout_for_wids.addWidget(self.pongWindow)

        # Debug

        # Adds the eleemnets to the main viewport
        grid_layout = QGridLayout()
        self.mid_label = QLabel()
        self.mid_label.setText("TRUE")
        self.startWindow.layout = QVBoxLayout(self.startWindow)
        self.startWindow.layout.addWidget(self.startWindow.imageLabel)

        self.startWindow.imageLabel.setLayout(grid_layout)


        #self.startWindow.imageLabel.layout.addWidget(self.startWindow.info_Label_Container)

        self.startWindow.info_Label_Container.layout = QHBoxLayout(self.startWindow.info_Label_Container)
        self.startWindow.info_Label_Container.layout.addWidget(self.startWindow.date_label)
        self.startWindow.info_Label_Container.layout.addWidget(self.startWindow.clock_temp_vbox)
        self.startWindow.info_Label_Container.layout.addWidget(self.startWindow.fact_label)
        grid_layout.addWidget(self.startWindow.info_Label_Container, 0, 0, 1, 3)

        #self.startWindow.imageLabel.layout.addWidget(self.startWindow.mid_label_container)
        #self.startWindow.imageLabel.layout.addWidget(self.startWindow.button_Play)

        grid_layout.addWidget(self.startWindow.button_Play, 1, 0, -1, 1)
        grid_layout.addWidget(self.startWindow.outer_chat_v_label, 1, 2, -1, 1)
        grid_layout.addWidget(self.startWindow.cursor, 1, 0)
        self.startWindow.loading_label.setVisible(False)

        #self.startWindow.imageLabel.layout.addWidget(self.startWindow.cursor)

        #self.startWindow.imageLabel.layout.addWidget(self.mid_label)

        self.pongWindow.layout = QVBoxLayout(self.pongWindow)
        self.pongWindow.layout.addWidget(self.pongWindow.imageLabel)
        self.pongWindow.layout.addWidget(self.pongWindow.button_movie)
        #self.pongWindow.setMinimumSize(1920, 1080)
        self.central_widget.setLayout(self.layout_for_wids)


        # self.layout = QVBoxLayout(self.central_widget)
        # self.layout.addWidget(self.imageLabel)
        self.setCentralWidget(self.central_widget)
        # Connects the button actions
        self.pongWindow.button_movie.clicked.connect(self.start_movie)
        # self.startWindow.button_Play.clicked.connect(self.start_Game)
        #self.pongWindow.imageLabel1.setGeometry(QRect(10, 200, 10, 400))
        #self.pongWindow.imageLabel2.setFixedWidth(10)
        #self.pongWindow.imageLabel2.move(400, 222)
        #self.pongWindow.imageLabel2.setAlignment(Qt.AlignCenter)
        #self.start_Game()



    def start_Game(self):
        print("Test")
        self.camera.close_camera()
        if self.window_title == 'start':
            print("True")
            self.window_title = 'game'
            self.startWindow.hide()
            self.pongWindow.show()
            #ToDo: Implement direct play start!
            self.pongWindow.button_movie.click()


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
        # self.pixmap_item.fromImage(self.convert_cv_qt(cv_img))
        qt_img = self.convert_cv_qt(cv_img)
        self.pongWindow.imageLabel.setPixmap(QPixmap.fromImage(qt_img))
        self.startWindow.imageLabel.setPixmap(QPixmap.fromImage(qt_img))
        #self.startWindow.imageLabel.pixmap().scaled(1920, 1080)

    def update_cursor(self, x, y):
        print(x, y)

        self.startWindow.cursor.move(x, y)
        #self.startWindow.button_Play.move(x, y)
        if self.startWindow.cursor.geometry().intersected(self.startWindow.button_Play.geometry()):
            self.counter += 5
            #self.startWindow.cursor.setText(str(self.startWindow.cursor.geometry().getCoords()))
            #self.startWindow.button_Play.setText(str(self.startWindow.button_Play.geometry().getCoords()))
            print("counter:", self.counter)
            self.startWindow.load(self.counter)
            #self.startWindow.loading_label.setGeometry(QRect(100, 250, 250, 150))
            if self.counter > 100:
                #If Counter hits 60 -> the view switches to the game (Pong screen)
                self.start_Game()
                self.counter = 0
        else:
            self.startWindow.reset_load()
            self.counter = 0;
            #self.start_Game()
            print()

        #else:
        #    self.startWindow.cursor.setStyleSheet('background-color: yellow')

    def updatePosition(self, c):
        self.pongWindow.imageLabel1.setGeometry(QRect(100, c - 100, 10, 200))
        #self.pongWindow.imageLabel2.setGeometry(QRect(1240, 200, 10, 200))
        # self.imageLabel2.setGeometry(QRect(1400,c-200,10,400))
        print("Klick")

    def updatePositionPlayer2(self, y):
        print(y, " TEST")
        self.pongWindow.imageLabel2.setGeometry(QRect(1140, y - 100, 10, 200))

    def updateBall(self, x, y):
        self.pongWindow.bandeOben.setVisible(True)
        self.pongWindow.bandeUnten.setVisible(True)
        self.pongWindow.bandeOben.setGeometry(0, 0, 80, 80)
        self.pongWindow.bandeUnten.setGeometry(0, 720, 80, 80)
        self.pongWindow.torLeft.setVisible(True)
        self.pongWindow.torRight.setVisible(True)
        self.pongWindow.torLeft.setGeometry(0, 0, 80, 80)
        self.pongWindow.torRight.setGeometry(1250, 0, 80, 80)

        self.pongWindow.scoreLeft.setGeometry(QRect(600, 50, 10, 50))
        self.pongWindow.scoreRight.setGeometry(QRect(700, 50, 10, 50))

        print('Die positive Variable: ', self.positive)

        # elif self.detect_collision()==False and not self.positive:
        #    self.positive = True
        #if self.detect_collision():
        #    if self.positive:
        #        self.positive = False

        #    elif self.positive == False:
        #        self.positive = True

        #if self.positive == True:
        #    self.ballMovementpositive()
        #elif self.positive == False:
        #    self.ballMovementnegative()


        self.pongWindow.imageLabel3.setGeometry(x, y, 80, 80)
        self.detect_collision()
        print(bcolors.FAIL,self.pongWindow.imageLabel3.geometry().x(), " X Coord", bcolors.ENDC)
        #if self.pongWindow.imageLabel3.geometry().x() >= 850 and self.pongWindow.imageLabel3.geometry().x() <= 853:
        #    self.updateTor()


    def ballMovementpositive(self):
        self.bX += 10
        self.bY += 1
        self.pongWindow.imageLabel3.setGeometry(self.bX, self.bY, 80, 80)

    def ballMovementnegative(self):
        self.bX -= 10
        # self.bY -= 1
        self.pongWindow.imageLabel3.setGeometry(self.bX, self.bY, 80, 80)

    def detect_collision(self):
        # if self.imageLabel3.geometry().center()+80 == self.imageLabel2.geometry().intersects()
        if self.positive:
            # Collision Paddle Right!
            if self.pongWindow.imageLabel3.geometry().intersected(self.pongWindow.imageLabel2.geometry()):
                print("INTERSECTION!")
                self.local_cL.sendCollision("paddleR")
                return True
            # Collision Paddle Left
            elif self.pongWindow.imageLabel3.geometry().intersected(self.pongWindow.imageLabel1.geometry()):
                print("INTERSECTION!")
                self.local_cL.sendCollision("paddleL")
                return True
            # Collision Bande Oben
            elif self.pongWindow.imageLabel3.geometry().intersected(self.pongWindow.bandeOben.geometry()):
                print("INTERSECTION!")
                self.local_cL.sendCollision("bandeO")
                return True
            # Collision Bande Unten
            elif self.pongWindow.imageLabel3.geometry().intersected(self.pongWindow.bandeUnten.geometry()):
                print("INTERSECTION!")
                self.local_cL.sendCollision("bandeU")
                return True
                # Collision Bande Oben
            elif self.pongWindow.imageLabel3.geometry().intersected(self.pongWindow.torLeft.geometry()):
                print("INTERSECTION!")
                #self.String("torL")
                self.local_cL.sendCollision("torL")
                #self.scoreRightCounter += 1
                #self.pongWindow.scoreRight.setText(str(20))
                self.scoreRight = True
                self.updateTor()
                #time.sleep(0.5)
                return True
            # Collision Bande Unten
            elif self.pongWindow.imageLabel3.geometry().intersected(self.pongWindow.torRight.geometry()):
                print("INTERSECTION!")
                self.local_cL.sendCollision("torR")
                #self.scoreLeftCounter += 1
                #self.pongWindow.scoreLeft.setText(str(self.scoreLeftCounter))
                self.scoreLeft = True
                self.updateTor()
                #time.sleep(0.5)
                return True
            else:
                return False


    def updateTor(self):
        print("DIE METHODE WIRD AUSGEFÜHRT#####################################################1111####1##")
        if self.goalGlobalCounter <= 20:
            self.goalGlobalCounter += 1
        if self.goalGlobalCounter == 20:
            #TODO: Put Goal Code Here:
            if self.scoreLeft:
                self.scoreLeft = False
                self.scoreRight = False
                self.scoreLeftCounter +=1
                self.pongWindow.scoreLeft.setText(str(self.scoreLeftCounter))
                self.goalGlobalCounter = 0
            if self.scoreRight:
                self.scoreLeft = False
                self.scoreRight = False
                self.scoreRightCounter += 1
                self.pongWindow.scoreRight.setText(str(self.scoreRightCounter))
                self.goalGlobalCounter = 0
            #self.scoreLeft = False
            #self.scoreRight = False

        #self.startWindow.fact_label.setText(self.funFacts.__getitem__(self.arCounter))

        #if self.goalCounter == self.sizeOfAr - 1:
        #    self.goalCounter = 0



        #if self.goalSetBool == True:
        #    self.scoreRightCounter += 1
        #    self.pongWindow.scoreRight.setText(str(self.scoreRightCounter))
        #    print('Tor')
        #    self.goalSetBool == False
        #    self.stopwatch.restart()
        #if self.stopwatch >= 5.00:
        #    self.goalSetBool == True




    def update_infolabel(self):
        # Get Date and Time
        timezone = pytz.timezone('Europe/Berlin')
        now = datetime.now(timezone)
        now.astimezone()
        timea = now.strftime("%H:%M")
        get_date = now.date().strftime("%A")

        match str(get_date):
            case "Monday":
                get_date = "Montag"
            case "Tuesday":
                get_date = "Dienstag"
            case "Wednesday":
                get_date = "Mittwoch"
            case "Thursday":
                get_date = "Donnerstag"
            case "Friday":
                get_date = "Freitag"
            case "Saturday":
                get_date = "Samstag"
            case "Sunday":
                get_date = "Sonntag"

        #if not self.threadOpen:
        #    self.arCounter = 0
        #    thread = threading.Thread(target=self.updateCounter)
        #    thread.start()
        #    self.threadOpen = True
        # run the thread

        # wait for the thread to finish
        print('Waiting for the thread...')

        self.startWindow.clock_label.setText(str(timea))
        self.startWindow.date_label.setText(str(get_date))

        if self.arGlobalCounter <= 50:
            self.arGlobalCounter += 1
        if self.arGlobalCounter == 50:
            self.arCounter += 1
            self.arGlobalCounter = 0

        self.startWindow.fact_label.setText(self.funFacts.__getitem__(self.arCounter))
        #self.updateCounter()
        #if self.arCounter < self.sizeOfAr - 1:
        #    self.arCounter += 1
        #    time.sleep(4)
        if self.arCounter == self.sizeOfAr - 1:
            self.arCounter = 0
        #print(self.funFacts)
        #thread.join()

        #ToDo: Implements Wait
        #if self.goalSetBool == True:

        #    self.goalSetBool == False
        #    #self.stopwatch.restart()
        #if str(self.stopwatch) >= str(1000.00):
        #    self.stopwatch.reset()
        #    self.stopwatch.start()
        #    self.goalSetBool == True




    def updateCounter(self):
        self.arCounter += 1
        print(self.arCounter)
        time.sleep(2)

    def convert_cv_qt(self, cv_img):
        cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        cv_img = qimage2ndarray.array2qimage(cv_img)
        return cv_img

    """Convert from an opencv image to QPixmap"""

    # rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    # h, w, ch = rgb_image.shape
    # bytes_per_line = ch * w
    # convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
    # p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
    def start_thread_receive(self, local_cla):
        self.local_cL = local_cla

    def upchatlabel(self):
        self.startWindow.inner_chat_label.move(400)
        self.startWindow.inner_chat_label.setText("TEST111111111111111111111111!")
        print(bcolors.BOLD,"TEST111111111111111111111111!",bcolors.ENDC)

    # Only for debug!







    def update_chat_debug(self, ab):
        # uses dict
        self.vbar = self.startWindow.scrollArea.verticalScrollBar()
        self.vbar.setValue(self.vbar.maximum())
        #Debug
        atuple = ('Left', 0)
        if ab[0] == atuple:
            print('TRUE!!!!')
            print(bcolors.HEADER, ab, bcolors.ENDC)


        ac = []
        ac = ab
        #print(ac[1].__getitem__(0))


        if not ab == tuple:
            if not ab[0] == atuple:

                abc = {'user': 'ab'}

                dicta = {}
                for x in range(len(list(ac))):


                    dicta = list(ac)[x].__getitem__(0)

                    user = list(iter(dicta))[1]

                    chat = dicta.get(user)

                    if not self.globalChat.__contains__(chat):
                        self.globalChat.append(chat)

                a = {}
                a.values()

                # print(ab.index())
                ele = []
                # for k, v in list(ac)[0].__getitem__(1).items():

                # print(k, v)

                # for x in ac:
                #    ele.append(x[0])
                # res_list = [x[0] for x in ac]
                # x = list(ac)[0].__getitem__(1).count

                print(bcolors.FAIL, self.globalChat, bcolors.ENDC)

                # print(bcolors.FAIL, dicta.values(), bcolors.ENDC)
                # print(bcolors.FAIL, ac[1], bcolors.ENDC)
                self.startWindow.inner_chat_label.setText(str(self.globalChat))
                self.startWindow.inner_chat_label.setText(str("\n".join(self.globalChat)))

        #self.camera.close_camera()
        #self.startWindow.inner_chat_label.setText("TEST!")
        #self.startWindow.show()
        #self.pongWindow.hide()


    def start_movie(self):
        self.pongWindow.button_movie.setVisible(False)
        #self.pongWindow.imageLabel2.setGeometry(QRect(1240, 100, 10, 200))
        # create the video capture thread
        self.thread = VideoThread(self.camera, self.hand_detector)
        # self.thread.client.client.close()
        self.local_cL = self.thread.client
        print(self.local_cL)
        #self.thread.starte_receive_loop.connect(self.start_thread_receive)
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.update_label_signal.connect(self.updatePosition)
        self.thread.update_ball_signal.connect(self.updateBall)
        #self.thread.update_chat_signal.connect(self.upchatlabel)
        self.thread.update_tor.connect(self.updateTor)
        self.thread.update_player_2.connect(self.updatePositionPlayer2)

        #self.update_chat_debug()

        # start the thread
        self.thread.start()
        # self.thread1.start()
        # self.update_timer.start(30)

class msg(object):
    def __init__(self, message):
        self.message = message




class BackgroundFeed(QThread):
    a = "a"
    #change_ab_signal = pyqtSignal(str)
    change_ab_signal = pyqtSignal(object)
    change_pixmap_signal = pyqtSignal(np.ndarray)
    change_cursor_position = pyqtSignal(int, int)
    update_infolabel = pyqtSignal()
    ## LC
    change_lc = pyqtSignal(chat_client)
    counter = int(1)

    client = chat_client()



    def start_receive(self):
        self.client.receive()
        print("THEADING!!!!!")

    def __init__(self, camera, hand_detector):
        super().__init__()
        self.camera = camera
        self.hand_detector = hand_detector
        hd = self.hand_detector
        gd = gesture_detector()

    # Camera Loop
    def run(self):
        print("Video Started")
        hd = hand_detector()
        gd = gesture_detector()
        lmList = []
        # rThread.start()
        # self.starte_receive_loop.emit(self.client)
        # capture from web cam
        Player = 'Left'  # input('Player: ')
        bodyDetector = body_detector()

        self.client.player = Player
        self.client.sendcoordinate(Player, 100)
        rThread = threading.Thread(target=self.start_receive, args=())


        while True:

            self.client.sendcoordinate(Player, 100)
            success, img = self.camera.cap.read()
            # img.flags.writeable = False
            if success:
                self.update_infolabel.emit()
                print(bcolors.OKCYAN,'!!@@',self.client.TempChatList,bcolors.ENDC)
                self.change_ab_signal.emit(self.client.TempChatList)
                # init Hand detector
                # hd.findHands(img)
                img = cv2.resize(img, (1280, 750), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
                img_proc = self.hand_detector.find_hands_on_image(self.hand_detector, img)
                lmList = self.hand_detector.handlist
                # print(lmList)
                gd.writeLmList(lmList)
                if len(lmList) !=0:
                    x = int(lmList[0].__getitem__(1))
                    y = int(lmList[0].__getitem__(2))
                    #print(x, "_", y)
                    # Updates Cursor Coordinate from the lmList hands points
                    # Tracks always the middle point
                    self.change_cursor_position.emit(x, y)
                # gd.print()
                # cv2.imshow('Test', img)
                body_image_black = bodyDetector.findPose(img_proc)
                body_image_black = cv2.resize(body_image_black, (1280, 750), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
                #img_proc = self.hand_detector.find_hands_on_image(self.hand_detector, body_image_black)
                self.change_pixmap_signal.emit(body_image_black)



class PauseThread(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        time.sleep(0.1)
        return False

if __name__ == '__main__':
    app = QApplication([])
    window = StartWindow()
    window.setWindowTitle('Project: UBI')
    window.setBaseSize(2400, 1444)
    window.show()
    app.exit(app.exec_())
