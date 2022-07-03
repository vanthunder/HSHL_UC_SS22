from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QSizePolicy, QPushButton, QHBoxLayout


class pongScreen(QWidget):
    def __init__(self):
        super().__init__()
        # Variablen für Größe und Breite des Fensters werden festgelegt
        width = 1280
        height = 750
        # Fenstergröße einstellen und Bild wird gesetzt
        self.imageLabel = QLabel()
        self.setMinimumSize(width, height)
        self.setMaximumSize(width, height)
        self.imageLabel.setAutoFillBackground(True)
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setBackgroundRole(QPalette.Base)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)
        # Pong paddle
        self.pad_01 = QLabel
        # Player 2
        self.pad02 = QLabel

        # Alle Elemente werden erstellt mit dem Bild (Kamera) als Hintergrund
        self.layout = QHBoxLayout(self.imageLabel)
        # Player 1 - Imagelabel 1 = paddle1
        self.imageLabel1 = QLabel()
        self.imageLabel1.setMinimumSize(10, 200)
        self.imageLabel1.setMaximumSize(10, 200)
        self.imageLabel1.setStyleSheet("background-color: #00b000;")
        self.imageLabel1.setAutoFillBackground(True)
        # Player 2 - Imagelabel 2 = paddle2
        self.imageLabel2 = QLabel()
        self.imageLabel2.setMinimumSize(10, 200)
        self.imageLabel2.setMaximumSize(10, 200)
        self.imageLabel2.setStyleSheet("background-color: red;")
        self.imageLabel2.setAutoFillBackground(True)
        # Ball - Imagelabel 3 = Ball
        self.imageLabel3 = QLabel()
        self.imageLabel3.move(100, 100)
        self.imageLabel3.resize(30, 30)
        self.imageLabel3.setMaximumSize(30, 30)
        self.imageLabel3.setAutoFillBackground(True)
        self.imageLabel3.setStyleSheet("border: 3px solid #4447e3; border-radius: 15px; background-color: #3032b3;")

        # Scorelabel left
        self.scoreLeft = QLabel('0')
        self.scoreLeft.setMinimumSize(30, 50)
        self.scoreLeft.setMaximumSize(30, 50)
        self.scoreLeft.setStyleSheet("background-color: white; color: black; font-size: 30px; padding: 1px;")
        # Scorelabel right
        self.scoreRight = QLabel('0')
        self.scoreRight.setMinimumSize(30, 50)
        self.scoreRight.setMaximumSize(30, 50)
        self.scoreRight.setStyleSheet("background-color: white; color: black; font-size: 30px; padding: 1px;")

        # Grenzen werden festgelegt
        # Bande oben
        self.bandeOben = QLabel()
        self.bandeOben.setMinimumSize(width, 10)
        self.bandeOben.setMaximumSize(width, 10)
        self.bandeOben.setAutoFillBackground(True)
        self.bandeOben.setVisible(False)
        # Bande unten
        self.bandeUnten = QLabel()
        self.bandeUnten.setMinimumSize(width, 10)
        self.bandeUnten.setMaximumSize(width, 10)
        self.bandeUnten.setAutoFillBackground(True)
        self.bandeUnten.setVisible(False)
        # Tor links
        self.torLeft = QLabel()
        self.torLeft.setMinimumSize(10, height)
        self.torLeft.setMaximumSize(10, height)
        self.torLeft.setAutoFillBackground(True)
        # Tor rechts
        self.torRight = QLabel()
        self.torRight.setMinimumSize(10, height)
        self.torRight.setMaximumSize(10, height)
        self.torRight.setAutoFillBackground(True)

        self.imageLabelRect = QtCore.QRectF(100, 100, 20, 20)
        # ball wird erstellt mit größe und breite
        self.pixmap = QPixmap(100, 100)
        self.pixmap.fill(Qt.transparent)

        # Adds paddles to the main image label
        self.button_movie = QPushButton('Start Movie')
        self.imageLabel.layout().addWidget(self.imageLabel1)
        self.imageLabel.layout().addWidget(self.imageLabel3)
        self.imageLabel.layout().addWidget(self.imageLabel2)
        self.imageLabel.layout().addWidget(self.bandeOben)
        self.imageLabel.layout().addWidget(self.bandeUnten)
        self.imageLabel.layout().addWidget(self.torLeft)
        self.imageLabel.layout().addWidget(self.torRight)
        self.imageLabel.layout().addWidget(self.scoreLeft)
        self.imageLabel.layout().addWidget(self.scoreRight)
