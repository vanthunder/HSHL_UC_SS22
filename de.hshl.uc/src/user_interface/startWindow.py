from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy
from pyqtgraph.Qt import QtGui

from user_interface.Tools.Cursor import Cursor


class startWindow(QWidget):
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
        self.fontA = QFont("Josefin Sans Medium", 24)
        self.fontB = QFont("Josefin Sans Medium", 100)
        self.fontC = QFont("Josefin Sans Medium", 40)
        # Adds an image lable to the background
        self.imageLabel = QLabel()
        self.imageLabel.setAutoFillBackground(True)
        self.setMinimumSize(width, height)
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setBackgroundRole(QPalette.Base)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)
        # Adds the cursor
        self.cursor = Cursor()
        # Info Label
        self.info_Label_Container = QLabel()
        self.info_Label_Container.setStyleSheet(
            "margin: 20px 40px; border-radius: 25px; background: #8BC1E9; color: black;")
        # self.info_Label_Container.setMaximumHeight(400)
        self.info_Label_Container.setFont(self.fontA)
        # self.info_Label_Container.setMaximumSize(100, 400)
        self.info_Label_Container.setAutoFillBackground(True)
        # self.info_Label_Container.setStyleSheet("""background: #ebef00;""")
        # date and temp vBox
        self.clock_temp_vbox = QLabel()
        self.clock_temp_vbox.layout = QVBoxLayout(self.clock_temp_vbox)

        # Date Label
        self.date_label = QLabel()
        self.date_label.setText("Montag")
        self.date_label.setFont(self.fontA)
        # Clock
        self.clock_label = QLabel()
        self.clock_label.setText("20:00")
        self.clock_label.setAlignment(QtCore.Qt.AlignCenter)
        # self.clock_label.setMinimumWidth(400)
        self.clock_label.setFont(self.fontB)
        self.clock_label.setStyleSheet("margin-bottom: 0px; color: white")
        # Temp
        self.temp_label = QLabel()
        self.temp_label.setText("24°C")
        self.temp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_label.setFont(self.fontC)
        self.temp_label.setStyleSheet("margin-top: 0px; color: white")
        # Fact Label
        self.fact_label = QLabel()
        self.fact_label.setText(
            "Lorem ipsum dolor sit amet, \nconsetetur sadipscing elitr, \nsed diam nonumy eirmod tempor invidunt \nut labore et dolore magna aliquyam \nerat, sed diam voluptua.")
        self.fact_label.setFont(self.fontA)
        # Adds Clock and Temp to the vbox
        self.clock_temp_vbox.layout.addWidget(self.clock_label)
        self.clock_temp_vbox.layout.addWidget(self.clock_label)
        self.clock_temp_vbox.layout.addWidget(self.temp_label)
        self.clock_temp_vbox.setMinimumWidth(800)
        # self.clock_temp_vbox.setStyleSheet("overflow: hidden;border-radius: 25px; background: #F7AF9D; color: black;")

        # Hbox
        self.mid_label_container = QLabel()
        self.mid_label_container.layout = QHBoxLayout(self.mid_label_container)
        # inner vbox
        self.inner_vbox_label_container = QLabel()
        self.inner_vbox_label_container.layout = QVBoxLayout(self.inner_vbox_label_container)
        self.inner_vbox_label_container.setAlignment(QtCore.Qt.AlignCenter)
        # Adds Buttons to the inner box
        self.button_Opinion = QPushButton('Meinungsumfrage', self.inner_vbox_label_container)
        self.button_Opinion.setStyleSheet(
            "margin-left: 20px 40px; background-color: #B28BBC; border-style: thin; border-color: black; border-width: 5px; border-radius: 24px;")
        self.button_Opinion.setMinimumSize(100, 250)
        self.button_Opinion.setMaximumSize(400, 250)
        self.button_Opinion.setFont(self.fontA)
        self.button_Play = QPushButton('Spielesammlung', self.inner_vbox_label_container)
        self.button_Play.setStyleSheet(
            "margin-left: 20px -40px; background-color: #4B6E74; border-style: thin; border-color: black; border-width: 5px; border-radius: 24px;")
        self.button_Play.setMinimumSize(100, 250)
        self.button_Play.setMaximumSize(400, 250)
        self.button_Play.setFont(self.fontA)
        self.inner_vbox_label_container.layout.addWidget(self.button_Opinion)
        self.inner_vbox_label_container.layout.addWidget(self.button_Play)
        # Adds the inner box to the outer box
        self.mid_label_container.layout.addWidget(self.inner_vbox_label_container)
        # Chat Container
        # outer box
        self.outer_chat_v_label = QLabel()
        self.outer_chat_v_label.layout = QVBoxLayout(self.outer_chat_v_label)
        self.outer_chat_v_label.setStyleSheet(
            "overflow: hidden;border-radius: 25px; background: #F7AF9D; color: black;")
        # inner box
        self.inner_chat_label = QLabel()
        self.inner_chat_label.setText(
            "Lorem ipsum dolor sit amet, \nconsetetur sadipscing elitr, \nsed diam nonumy eirmod tempor invidunt \nut labore et dolore magna aliquyam \nerat, sed diam voluptua.")
        self.inner_chat_label.setStyleSheet(
            "float: left; left: 20px; padding-right: opx; border-radius: 25px; background: #EBEFF0; color: black;")
        self.inner_chat_label.setMinimumWidth(800)

        self.scrollArea = QtGui.QScrollArea()
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 201, 121))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.inner_chat_label)
        self.outer_chat_v_label.setMaximumSize(400,500)
        self.inner_vbox_label_container.setMaximumSize(600,600)
        #self.mid_label_container.setStyleSheet("background: #EBEFF0;")
        self.mid_label_container.setMaximumHeight(560)



        self.inner_chat_label.setFont(self.fontA)
        # Adds the inner box to the outer box
        self.outer_chat_v_label.layout.addWidget(self.scrollArea)
        # Adds the chat to the midd label container
        self.mid_label_container.layout.addWidget(self.outer_chat_v_label)
