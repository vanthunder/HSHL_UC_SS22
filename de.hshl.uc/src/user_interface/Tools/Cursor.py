from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QLabel, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets


class Cursor(QLabel):
    def __init__(self):
        super().__init__()
        self.width = 40
        self.height = 40
        self.setMinimumSize(self.width, self.height)
        self.setMaximumSize(self.width, self.height)
        self.setStyleSheet("background: yellow")



    def setPosition(self, x, y):
        self.setGeometry(self.width, self.height, x, y)

    def start_giph(self):
        self.movie = QMovie("loading-circle.gif")
        #self.setMovie(self.movie)
        #self.movie.start()

