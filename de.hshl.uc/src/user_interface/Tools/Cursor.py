from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QStackedLayout
from PyQt5.QtWidgets import QLabel, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets


class Cursor(QLabel):
    DEFAULT_WIDTH = 40
    DEFAULT_HEIGTH = 40
    def __init__(self):
        super().__init__()
        self.width = self.DEFAULT_WIDTH
        self.height = self.DEFAULT_HEIGTH
        self.setMinimumSize(self.width, self.height)
        self.setMaximumSize(self.width, self.height)
        self.setStyleSheet('background: yellow')
        self.loading_label = QLabel()
        self.loading_label.width = 0
        self.loading_label.height = 40
        self.loading_label.setStyleSheet('background: orange')

        # make
        self.layout = QStackedLayout(self)

        self.layout.addWidget(self.loading_label)
        self.loading_label.setMaximumSize(0, 0)



    def setPosition(self, x, y):
        self.setGeometry(self.width, self.height, x, y)

    def start_giph(self):
        self.movie = QMovie("loading-circle.gif")
        #self.setMovie(self.movie)
        #self.movie.start()



    def load(self, i):
        self.loading_label.setMaximumSize(int(self.DEFAULT_WIDTH/100 * i), self.DEFAULT_HEIGTH)

    def reset_load(self):
        self.loading_label.setMaximumSize(0, 0)