from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QStackedLayout


class Cursor(QLabel):
    # Variable für die Größe des Cursors initialisieren
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
        self.layout = QStackedLayout(self)
        self.layout.addWidget(self.loading_label)
        self.loading_label.setMaximumSize(0, 0)

    def setPosition(self, x, y):
        # Position des Cursors setzen/Updaten
        self.setGeometry(self.width, self.height, x, y)

    def start_giph(self):
        self.movie = QMovie("loading-circle.gif")

    def load(self, i):
        # Laden des Spiel starten Buttons
        self.loading_label.setMaximumSize(int(self.DEFAULT_WIDTH / 100 * i), self.DEFAULT_HEIGTH)

    def reset_load(self):
        # Spiel starten Button zurücksetzen
        self.loading_label.setMaximumSize(0, 0)
