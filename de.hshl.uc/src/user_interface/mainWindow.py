import threading
import time
from datetime import datetime

import cv2
import numpy as np
import pytz
import qimage2ndarray as qimage2ndarray
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, QRect
from PyQt5.QtGui import QPixmap, QFont, QMovie
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication, QLabel, QGridLayout
from PyQt5.QtWidgets import QMessageBox, QStackedLayout, \
    QHBoxLayout
from stopwatch import Stopwatch

from Socket.online.ChatServer.Online_Chat_Client_V01 import chat_client
from Socket.online.PongServer.Online_Client import local_client
from model.camera import Camera
from recognition.body_detector import body_detector
from user_interface.Tools import FunFacts
from user_interface.pongScreen import pongScreen
from user_interface.startWindow import startWindow

# This class purpose is to color the print statements (it is ment for debugging)
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

# This class purpose is to handle most of the threads used in the program
class VideoThread(QThread):
    change_ab_signal = pyqtSignal(int)
    change_pixmap_signal = pyqtSignal(np.ndarray)
    update_label_signal = pyqtSignal(int)
    update_ball_signal = pyqtSignal(int, int)
    update_player_2 = pyqtSignal(int)
    start_receive_loop = pyqtSignal(local_client)
    update_tor = pyqtSignal()
    counter = int(1)
    client = local_client()

    def __init__(self, camera, hand_detector):
        super(VideoThread, self).__init__()
        self.camera = camera
        self.hand_detector = hand_detector

    def start_receive(self):
        self.client.receive()

    def videoLoop(self, Player):
        lmList = []
        self.hand_detector.handList = lmList
        self.camera = Camera(0)
        self.camera.initialize()
        while True:
            success, img = self.camera.cap.read()
            if not self.client.ballcoords.__getitem__(0) == 1011100 and not self.client.ballcoords.__getitem__(
                    0) == 1011101:
                self.update_ball_signal.emit(self.client.ballcoords.__getitem__(0),
                                             self.client.ballcoords.__getitem__(1))
            if success:
                self.change_ab_signal.emit(1)
                img = cv2.resize(img, (1280, 750), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
                img_proc = self.hand_detector.find_hands_on_image(self.hand_detector, img)
                lmList = self.hand_detector.handList
                self.change_pixmap_signal.emit(img_proc)

                # Game Loop
                if lmList:
                    # Send Tupel
                    self.client.sendcoordinate(Player, lmList[0].__getitem__(2))
                    if self.client.TempTupel.__getitem__(0) == 'Left':
                        self.update_label_signal.emit(self.client.TempTupel.__getitem__(1))
                    else:
                        self.update_player_2.emit(self.client.TempTupel.__getitem__(1))

    # Camera Loop
    def run(self):
        Player = 'Left'
        self.client.player = Player
        rThread = threading.Thread(target=self.start_receive, args=())
        self.client.sendReady('Left')
        while True:
            if self.client.canStart == True:
                self.videoLoop(Player)

# This class purpose is to handle everything connected to the start screen
class StartWindow(QMainWindow):
    windowTitle = "Projekt: Ubi"

    def __init__(self, camera=None, hand_detector=None, local_cL=None):
        super().__init__()
        # screen dimensions
        self.width = 1280
        self.height = 750
        # goal vars
        self.threadOpen = False
        self.scoreLeft = False
        self.scoreRight = False
        self.scoreLeftCounter = 0
        self.scoreRightCounter = 0
        self.goalCounter = 0
        self.goalGlobalCounter = 0
        self.goalSetBool = True
        # fun facts
        self.funFactsClass = FunFacts
        self.funFacts = self.funFactsClass.FunFacts.funFacts
        self.lenOfFunFacts = len(self.funFactsClass.FunFacts.funFacts)
        self.window_title = 'start'
        self.fontA = QFont("Josefin Sans Medium", 24)
        self.fontB = QFont("Josefin Sans Medium", 100)
        self.fontC = QFont("Josefin Sans Medium", 40)
        # ball position
        self.bX = 0
        self.bY = 0
        # ball moving direction
        self.positive = True
        # count the frames the cursor is on a btn
        self.counter = 0
        self.camera = camera
        self.hand_detector = hand_detector
        self.local_cL = local_cL

        self.display_width = self.width
        self.display_height = self.height
        self.setWindowTitle(self.windowTitle)
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
        self.thread.change_lc.connect(self.start_thread_receive)
        # Start Thread
        self.thread.update_infolabel.connect(self.update_infolabel)
        self.thread.start()
        # ChatServer
        self.globalChat = []
        self.stopwatch = Stopwatch(2)

        self.isPause = False
        self.pauseThread = PauseThread()

        # Central Widget
        self.central_widget = QWidget()
        self.layout_for_wids = QStackedLayout()

        self.startWindow = startWindow()
        self.pongWindow = pongScreen()

        # Layout Container for Widgets and Buttons
        self.layout_for_wids.addWidget(self.startWindow)
        self.layout_for_wids.addWidget(self.pongWindow)

        # Debug

        # Adds the elements to the main viewport
        grid_layout = QGridLayout()
        self.mid_label = QLabel()
        self.mid_label.setText("TRUE")
        self.startWindow.layout = QVBoxLayout(self.startWindow)
        self.startWindow.layout.addWidget(self.startWindow.imageLabel)

        self.startWindow.imageLabel.setLayout(grid_layout)

        self.startWindow.info_Label_Container.layout = QHBoxLayout(self.startWindow.info_Label_Container)
        self.startWindow.info_Label_Container.layout.addWidget(self.startWindow.date_label)
        self.startWindow.info_Label_Container.layout.addWidget(self.startWindow.clock_temp_vbox)
        self.startWindow.info_Label_Container.layout.addWidget(self.startWindow.fact_label)
        grid_layout.addWidget(self.startWindow.info_Label_Container, 0, 0, 1, 3)
        grid_layout.addWidget(self.startWindow.button_Play, 1, 0, -1, 1)
        grid_layout.addWidget(self.startWindow.outer_chat_v_label, 1, 2, -1, 1)
        grid_layout.addWidget(self.startWindow.cursor, 1, 0)
        self.startWindow.loading_label.setVisible(False)
        self.pongWindow.layout = QVBoxLayout(self.pongWindow)
        self.pongWindow.layout.addWidget(self.pongWindow.imageLabel)
        self.pongWindow.layout.addWidget(self.pongWindow.button_movie)
        self.central_widget.setLayout(self.layout_for_wids)
        self.setCentralWidget(self.central_widget)
        # Connects the button actions
        self.pongWindow.button_movie.clicked.connect(self.start_movie)

    def start_Game(self):
        self.camera.close_camera()
        if self.window_title == 'start':
            self.window_title = 'game'
            self.startWindow.hide()
            self.pongWindow.show()
            self.pongWindow.button_movie.click()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.local_cL.close_client()
            event.accept()
        else:
            event.ignore()

    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.pongWindow.imageLabel.setPixmap(QPixmap.fromImage(qt_img))
        self.startWindow.imageLabel.setPixmap(QPixmap.fromImage(qt_img))

    def update_cursor(self, x, y):
        self.startWindow.cursor.move(x, y)
        if self.startWindow.cursor.geometry().intersected(self.startWindow.button_Play.geometry()):
            self.counter += 5
            self.startWindow.load(self.counter)
            if self.counter > 100:
                self.start_Game()
                self.counter = 0
        else:
            self.startWindow.reset_load()
            self.counter = 0

    def updatePosition(self, c):
        self.pongWindow.imageLabel1.setGeometry(QRect(100, c - 100, 10, 200))

    def updatePositionPlayer2(self, y):
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
        self.pongWindow.imageLabel3.setGeometry(x, y, 80, 80)
        self.detect_collision()

    def ballMovementpositive(self):
        self.bX += 10
        self.bY += 1
        self.pongWindow.imageLabel3.setGeometry(self.bX, self.bY, 80, 80)

    def ballMovementnegative(self):
        self.bX -= 10
        self.pongWindow.imageLabel3.setGeometry(self.bX, self.bY, 80, 80)

    def detect_collision(self):
        if self.positive:
            # Collision Paddle Right!
            if self.pongWindow.imageLabel3.geometry().intersected(self.pongWindow.imageLabel2.geometry()):
                self.local_cL.sendCollision("paddleR")
                return True
            # Collision Paddle Left
            elif self.pongWindow.imageLabel3.geometry().intersected(self.pongWindow.imageLabel1.geometry()):
                self.local_cL.sendCollision("paddleL")
                return True
            # Collision top
            elif self.pongWindow.imageLabel3.geometry().intersected(self.pongWindow.bandeOben.geometry()):
                self.local_cL.sendCollision("bandeO")
                return True
            # Collision bottom
            elif self.pongWindow.imageLabel3.geometry().intersected(self.pongWindow.bandeUnten.geometry()):
                self.local_cL.sendCollision("bandeU")
                return True
                # Collision left
            elif self.pongWindow.imageLabel3.geometry().intersected(self.pongWindow.torLeft.geometry()):
                self.local_cL.sendCollision("torL")
                self.scoreRight = True
                self.updateTor()
                return True
            # Collision right
            elif self.pongWindow.imageLabel3.geometry().intersected(self.pongWindow.torRight.geometry()):
                self.local_cL.sendCollision("torR")
                self.scoreLeft = True
                self.updateTor()
                return True
            else:
                return False

    def updateTor(self):
        if self.scoreLeft:
            self.scoreLeft = False
            self.scoreRight = False
            self.scoreLeftCounter += 1
            self.pongWindow.scoreLeft.setText(str(self.scoreLeftCounter))
        elif self.scoreRight:
            self.scoreLeft = False
            self.scoreRight = False
            self.scoreRightCounter += 1
            self.pongWindow.scoreRight.setText(str(self.scoreRightCounter))

        if self.goalGlobalCounter <= 20:
            self.goalGlobalCounter += 1
        if self.goalGlobalCounter == 20:
            if self.scoreLeft:
                self.goalGlobalCounter = 0
            if self.scoreRight:
                self.goalGlobalCounter = 0

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

        # wait for the thread to finish

        self.startWindow.clock_label.setText(str(timea))
        self.startWindow.date_label.setText(str(get_date))

        if self.arGlobalCounter <= 50:
            self.arGlobalCounter += 1
        if self.arGlobalCounter == 50:
            self.arCounter += 1
            self.arGlobalCounter = 0

        self.startWindow.fact_label.setText(self.funFacts.__getitem__(self.arCounter))
        if self.arCounter == self.lenOfFunFacts - 1:
            self.arCounter = 0

    def updateCounter(self):
        self.arCounter += 1
        time.sleep(2)

    # convert from an OpenCV image to a QPixmap
    def convert_cv_qt(self, cv_img):
        cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        cv_img = qimage2ndarray.array2qimage(cv_img)
        return cv_img

    def start_thread_receive(self, local_cla):
        self.local_cL = local_cla

    def upchatlabel(self):
        self.startWindow.inner_chat_label.move(400)

    def update_chat_debug(self, ab):
        # uses dict
        self.vbar = self.startWindow.scrollArea.verticalScrollBar()
        self.vbar.setValue(self.vbar.maximum())
        atuple = ('Left', 0)
        ac = []
        ac = ab
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
                self.startWindow.inner_chat_label.setText(str(self.globalChat))
                self.startWindow.inner_chat_label.setText(str("\n".join(self.globalChat)))

    def start_movie(self):
        self.pongWindow.button_movie.setVisible(False)
        # create the video capture thread
        self.thread = VideoThread(self.camera, self.hand_detector)
        self.local_cL = self.thread.client
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.update_label_signal.connect(self.updatePosition)
        self.thread.update_ball_signal.connect(self.updateBall)
        self.thread.update_tor.connect(self.updateTor)
        self.thread.update_player_2.connect(self.updatePositionPlayer2)
        # start the thread
        self.thread.start()


class msg(object):
    def __init__(self, message):
        self.message = message


class BackgroundFeed(QThread):
    a = "a"
    change_ab_signal = pyqtSignal(object)
    change_pixmap_signal = pyqtSignal(np.ndarray)
    change_cursor_position = pyqtSignal(int, int)
    update_infolabel = pyqtSignal()
    change_lc = pyqtSignal(chat_client)
    counter = int(1)
    client = chat_client()

    def start_receive(self):
        self.client.receive()

    def __init__(self, camera, hand_detector):
        super().__init__()
        self.camera = camera
        self.hand_detector = hand_detector

    # Camera Loop
    def run(self):
        lmList = []
        # capture from web cam
        Player = 'Left'
        bodyDetector = body_detector()
        self.client.player = Player
        self.client.startClientThread()  # Client Thread for receiving messages from the Chat Server
        rThread = threading.Thread(target=self.start_receive, args=())
        while True:
            success, img = self.camera.cap.read()
            if success:
                self.update_infolabel.emit()
                self.change_ab_signal.emit(self.client.TempChatList)
                img = cv2.resize(img, (1280, 750), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
                img_proc = self.hand_detector.find_hands_on_image(self.hand_detector, img)
                lmList = self.hand_detector.handList
                if len(lmList) != 0:
                    x = int(lmList[0].__getitem__(1))
                    y = int(lmList[0].__getitem__(2))
                    # Updates Cursor Coordinate from the lmList hands points
                    # Tracks always the middle point
                    self.change_cursor_position.emit(x, y)
                body_image_black = bodyDetector.findPose(img_proc)
                body_image_black = cv2.resize(body_image_black, (1280, 750), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
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
