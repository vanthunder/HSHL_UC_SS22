import threading

import cv2
import numpy as np
import qimage2ndarray as qimage2ndarray
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot, QRect
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication
from PyQt5.QtWidgets import QMessageBox, QStackedLayout, \
    QHBoxLayout

# from Socket.local.localClient import local_client
from Socket.online.onlineClient import local_client
from model.camera import Camera
from recognition.gesture_detector import gesture_detector
from recognition.hand_detector import hand_detector
from user_interface.pongScreen import pongScreen
from user_interface.startWindow import startWindow


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

    # Camera Loop
    def run(self):
        bX = 0
        bY = 0
        speedX = 10
        speedY = 0
        hd = hand_detector()
        gd = gesture_detector()
        lmList = []
        self.hand_detector.handlist = lmList
        video = 'hands.mp4'
        self.camera = Camera(video)
        self.camera.initialize()
        # Left or Right
        Player = 'Left'  # input('Player: ')

        self.client.player = Player
        rThread = threading.Thread(target=self.start_receive, args=())
        # rThread.start()
        # self.starte_receive_loop.emit(self.client)
        # capture from web cam

        while True:
            success, img = self.camera.cap.read()
            # img.flags.writeable = False
            if success:
                # init Hand detector
                # hd.findHands(img)
                img = cv2.resize(img, (1920, 1080), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
                img_proc = self.hand_detector.find_hands_on_image(self.hand_detector, img)
                lmList = self.hand_detector.handlist
                #fps = self.camera.cap.get(cv2.CAP_PROP_FPS)
                #cv2.putText(img_proc, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
                # print(lmList)
                gd.writeLmList(lmList)
                # gd.print()
                # cv2.imshow('Test', img)
                self.change_pixmap_signal.emit(img_proc)

                # Game Loop
                bX += 1 + speedX
                bY += 1 + speedY
                # Bewege ball
                self.update_ball_signal.emit()
                # To Do send to server:
                if not lmList:
                    print()
                else:
                    # Send Tupel
                    print('Send Coordinates form Main Window')
                    self.client.sendcoordinate(Player, lmList[0].__getitem__(2))
                    print('Send Coordinates form Main Window 2')
                    print("Player:  ", self.client.TempTupel.__getitem__(0))

                    if self.client.TempTupel.__getitem__(0) == 'Left':
                        self.update_label_signal.emit(self.client.TempTupel.__getitem__(1))
                    else:
                        self.update_player_2.emit(self.client.TempTupel.__getitem__(1))
                    print()
                # print(client.y)
                # To Do receive Coordinate

                # Updates the label


class StartWindow(QMainWindow):
    window_title = ""

    def __init__(self, camera=None, hand_detector=None, local_cL=None):
        super().__init__()
        self.window_title = 'start'
        self.fontA = QFont("Josefin Sans Medium", 24)
        self.fontB = QFont("Josefin Sans Medium", 100)
        self.fontC = QFont("Josefin Sans Medium", 40)
        self.bX = 0
        self.bY = 0
        self.positive = True
        self.camera = camera
        self.hand_detector = hand_detector
        self.local_cL = local_cL
        self.disply_width = 1920
        self.display_height = 1080
        self.setWindowTitle('Projekt: Ubi')
        self.setMaximumSize(1920, 1080)
        # Create Video Thread
        self.thread = BackgroundFeed(self.camera, self.hand_detector)
        # Update Label
        self.thread.change_pixmap_signal.connect(self.update_image)
        # Updates the Cursor
        self.thread.change_cursor_position.connect(self.update_cursor)
        # Start Thread
        self.thread.start()

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

        # Adds the eleemnets to the main viewport
        self.startWindow.layout = QVBoxLayout(self.startWindow)
        self.startWindow.layout.addWidget(self.startWindow.imageLabel)
        self.startWindow.imageLabel.layout = QVBoxLayout(self.startWindow.imageLabel)
        self.startWindow.imageLabel.layout.addWidget(self.startWindow.info_Label_Container)
        self.startWindow.info_Label_Container.layout = QHBoxLayout(self.startWindow.info_Label_Container)
        self.startWindow.info_Label_Container.layout.addWidget(self.startWindow.date_label)
        self.startWindow.info_Label_Container.layout.addWidget(self.startWindow.clock_temp_vbox)
        self.startWindow.info_Label_Container.layout.addWidget(self.startWindow.fact_label)
        self.startWindow.imageLabel.layout.addWidget(self.startWindow.mid_label_container)
        self.startWindow.imageLabel.layout.addWidget(self.startWindow.cursor)
        self.pongWindow.layout = QVBoxLayout(self.pongWindow)
        self.pongWindow.layout.addWidget(self.pongWindow.imageLabel)
        self.pongWindow.layout.addWidget(self.pongWindow.button_movie)
        self.pongWindow.setMinimumSize(1920, 1080)
        self.central_widget.setLayout(self.layout_for_wids)
        # self.layout = QVBoxLayout(self.central_widget)
        # self.layout.addWidget(self.imageLabel)
        self.setCentralWidget(self.central_widget)
        # Connects the button actions
        self.pongWindow.button_movie.clicked.connect(self.start_movie)
        self.startWindow.button_Play.clicked.connect(self.start_Game)

    def start_Game(self):
        print("Test")
        self.camera.close_camera()
        if self.window_title == 'start':
            print("True")
            self.window_title = 'game'
            self.startWindow.hide()
            self.pongWindow.show()

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

    def updatePosition(self, c):
        self.pongWindow.imageLabel1.setGeometry(QRect(10, c - 200, 10, 400))
        # self.imageLabel2.setGeometry(QRect(1400,c-200,10,400))
        print("Klick")

    def updatePositionPlayer2(self, y):
        print(y, " TEST")
        self.pongWindow.imageLabel2.setGeometry(QRect(1400, y - 200, 10, 400))

    def updateBall(self):
        print('Die positive Variable: ', self.positive)

        # elif self.detect_collision()==False and not self.positive:
        #    self.positive = True
        if self.detect_collision():
            if self.positive:
                self.positive = False

            elif self.positive == False:
                self.positive = True

        if self.positive == True:
            self.ballMovementpositive()
        elif self.positive == False:
            self.ballMovementnegative()

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
            if self.pongWindow.imageLabel3.geometry().intersected(self.pongWindow.imageLabel2.geometry()):
                print("INTERSECTION!")
                return True
            else:
                return False
        else:
            if self.pongWindow.imageLabel3.geometry().intersected(self.pongWindow.imageLabel1.geometry()):
                print("INTERSECTION!")
                return True
            else:
                return False

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

    def start_movie(self):
        # create the video capture thread
        self.thread = VideoThread(self.camera, self.hand_detector)
        # self.thread.client.client.close()
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
        # self.thread1.start()
        # self.update_timer.start(30)





class BackgroundFeed(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    change_cursor_position = pyqtSignal(int, int)
    counter = int(1)

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

        while True:
            success, img = self.camera.cap.read()
            # img.flags.writeable = False
            if success:
                # init Hand detector
                # hd.findHands(img)
                img = cv2.resize(img, (1920, 1080), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
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
                self.change_pixmap_signal.emit(img_proc)


if __name__ == '__main__':
    app = QApplication([])
    window = StartWindow()
    window.setWindowTitle('Project: UBI')
    window.setBaseSize(2400, 1444)
    window.show()
    app.exit(app.exec_())
