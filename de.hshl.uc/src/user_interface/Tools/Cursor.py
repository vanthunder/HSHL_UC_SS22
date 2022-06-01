from PyQt5.QtWidgets import QLabel


class Cursor(QLabel):
    def __init__(self):
        super().__init__()
        self.width = 40
        self.height = 40
        self.setMinimumSize(self.width, self.height)
        self.setMaximumSize(self.width, self.height)
        self.setStyleSheet("background: yellow")
        self.geometry().intersects(self.rect())

    def setPosition(self, x, y):
        self.setGeometry(self.width, self.height, x, y)
