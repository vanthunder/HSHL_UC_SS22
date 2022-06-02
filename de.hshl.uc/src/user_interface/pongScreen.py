from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QSizePolicy, QVBoxLayout, QPushButton


class pongScreen(QWidget):
    def __init__(self):
        super().__init__()
        # Change the desired Resolution!
        # Default:
        #         w: 1920
        #         h: 1080
        # Beamer in use:
        #         w: 1280
        #         h: 750
        width = 1280
        height = 750
        self.imageLabel = QLabel()
        self.setMinimumSize(width, height)
        self.setMaximumSize(width, height)
        #self.imageLabel.setMinimumSize(width, height)
        #self.imageLabel.setMaximumSize(width, height)
        self.imageLabel.setAutoFillBackground(True)
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setBackgroundRole(QPalette.Base)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)
        # Pong paddle
        self.pad_01 = QLabel
        # Player 2
        self.pad02 = QLabel

        # self.central_widget.a
        self.layout = QVBoxLayout(self.imageLabel)
        # Player 1 - Imagelabel 1 = paddle1
        self.imageLabel1 = QLabel()
        self.imageLabel1.setMaximumSize(10, 400)
        #self.imageLabel1.setGeometry(QRect(10, 200, 10, 400))
        self.imageLabel1.setAutoFillBackground(True)
        # Player 2 - Imagelabel 2 = paddle2
        self.imageLabel2 = QLabel()
        self.imageLabel2.setMaximumSize(10, 400)
        #self.imageLabel2.setGeometry(QRect(1270, 200, 10, 400))
        self.imageLabel2.setAutoFillBackground(True)
        # Ball - Imagelabel 3 = Ball
        self.imageLabel3 = QLabel('round label')
        self.imageLabel3.move(100, 100)
        self.imageLabel3.resize(80, 80)
        self.imageLabel3.setMaximumSize(80, 80)
        self.imageLabel3.setAutoFillBackground(True)
        self.imageLabel3.setStyleSheet("border: 3px solid blue; border-radius: 40px;")

        self.imageLabelRect = QtCore.QRectF(100, 100, 20, 20)
        # self.paint = QPainter(self.imageLabelRect)
        # ball
        self.pixmap = QPixmap(100, 100)
        self.pixmap.fill(Qt.transparent)

        self.imageLabel4 = QLabel
        # self.imageLabel4.setPixmap(self.imageLabel2)

        # Adds paddles to the main image label
        #        self.imageLabel.setPixmap(self.pixmap_item)
        self.imageLabel.layout().addWidget(self.imageLabel1)
        self.imageLabel.layout().addWidget(self.imageLabel2)
        self.imageLabel.layout().addWidget(self.imageLabel3)
        # self.imageLabel.layout().addWidget(self.imageLabelRect)
        # self.imageLabel.setParent(self.pad)

        # self.setScene(self.scene)
        self.button_movie = QPushButton('Start Movie')
        # self.pd = QGraphicsRectItem(1, 1, 20, 20, self.central_widget)
        # self.image_view = ImageView()
