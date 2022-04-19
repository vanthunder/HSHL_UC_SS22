import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from recognition import hand_detector

class ui():
    def create_frame(self):
        app = QApplication(sys.argv)
        hdt = hand_detector()
        hdt.hand_detector.main(self=hdt)



        window = QWidget()
        window.setWindowTitle('PyQt5 APP')
        window.setGeometry(100, 100, 280, 80)
        window.move(60, 15)
        helloMsg = QLabel('<h1>Hello World!<h1>', parent=window)
        helloMsg.move(60, 15)

        window.show()
        sys.exit(app.exec_())


if __name__ == "create_frame":
    window = ui
    window.create_frame(self=window)
