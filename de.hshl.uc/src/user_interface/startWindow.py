import requests
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QStackedLayout
from pyqtgraph.Qt import QtGui
from datetime import datetime
import pytz
import json
from requests import request


from user_interface.Tools.Cursor import Cursor
from user_interface import global_specs


class startWindow(QWidget):
    DEFAULT_WIDTH = 250
    DEFAULT_HEIGTH = 150
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
        self.fontA = QFont("Josefin Sans Medium", 14)
        self.fontB = QFont("Josefin Sans Medium", 40)
        self.fontC = QFont("Josefin Sans Medium", 20)
        # Adds an image lable to the background
        self.imageLabel = QLabel()
        self.imageLabel.setAutoFillBackground(True)
        self.setMaximumSize(width, height)
        self.setMaximumSize(width, height)
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setBackgroundRole(QPalette.Base)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imageLabel.setScaledContents(True)
        # Adds the cursor
        self.cursor = Cursor()
        # Info Label
        self.info_Label_Container = QLabel()
        self.info_Label_Container.setStyleSheet(
            "border-radius: 25px; background: #8BC1E9; color: black;")
        # self.info_Label_Container.setMaximumHeight(400)
        self.info_Label_Container.setFont(self.fontA)
        # self.info_Label_Container.setMaximumSize(100, 400)
        self.info_Label_Container.setAutoFillBackground(True)
        # self.info_Label_Container.setStyleSheet("""background: #ebef00;""")
        # date and temperature vBox
        self.clock_temp_vbox = QLabel()
        self.clock_temp_vbox.layout = QVBoxLayout(self.clock_temp_vbox)

        # get Date and Time
        timezone = pytz.timezone('Europe/Berlin')
        now = datetime.now(timezone)
        now.astimezone()
        time = now.strftime("%H:%M")
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

        # Date Label
        self.date_label = QLabel()
        self.date_label.setText(str(get_date))
        self.date_label.setFont(self.fontA)
        # Clock
        self.clock_label = QLabel()
        self.clock_label.setText(str(time))
        self.clock_label.setAlignment(QtCore.Qt.AlignCenter)
        #self.clock_label.setMinimumWidth(400)
        self.clock_label.setFont(self.fontB)
        self.clock_label.setStyleSheet("margin-bottom: 0px; color: white")

        api_key = "34b02d4ce2b0b1319d917fa7d34a2f92"
        base_url = "https://api.openweathermap.org/data/2.5/weather?q="
        city_name = "lippstadt"

        self.complete_url = base_url + city_name + "&appid=" + api_key
        response = requests.get(self.complete_url)
        data = response.json()

        # -273.15 weil Kelvin zu Celsius
        print("hier muss es hin: " + str(int(data["main"]["temp"] - (273.15))))

        # temperature
        self.temp_label = QLabel()
        self.temp_label.setText(str(int(data["main"]["temp"] - (273.15))) + "°C")
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

        # HBox
        self.mid_label_container = QLabel()
        self.mid_label_container.layout = QHBoxLayout(self.mid_label_container)
        self.mid_label_container.setMaximumHeight(100)
        # inner vbox
        self.inner_vbox_label_container = QLabel()
        self.inner_vbox_label_container.setMaximumSize(200, 200)
        self.inner_vbox_label_container.layout = QVBoxLayout(self.inner_vbox_label_container)
        self.inner_vbox_label_container.setAlignment(QtCore.Qt.AlignCenter)
        # Add Buttons to the inner box
        self.button_Opinion = QPushButton('Meinungsumfrage', self.inner_vbox_label_container)
        self.button_Opinion.setStyleSheet(
            "margin-left: 20px 40px; background-color: #B28BBC; border-style: thin; border-color: black; border-width: 5px; border-radius: 24px;")
        self.button_Opinion.setMinimumSize(200, 200)
        self.button_Opinion.setMaximumSize(200, 200)
        self.button_Opinion.setFont(self.fontA)
        # turned QPushButton button_Play to a QLabel
        #self.button_Play = QPushButton('Spielesammlung', self.inner_vbox_label_container)
        self.buttonWidgetContainer = QLabel()
        self.buttonWidgetContainer.layout = QStackedLayout(self.buttonWidgetContainer)
        self.buttonWidgetContainer.setMinimumSize(250,150)
        self.buttonWidgetContainer.setMinimumSize(250,150)
        #self.buttonWidgetContainer.setStyleSheet( "margin-left: 20px -40px; background: #4B6E74; border: 1px solid black; border-radius: 24px;")
        self.button_Play = QLabel()
        self.button_Play.layout = QStackedLayout(self.button_Play)
        self.button_Play.setStyleSheet(
            "background: #4B6E74; border: 1px solid black; border-radius: 24px;")
        #self.button_Play.setStyleSheet(
        #    "margin-left: 20px -40px; background: #4B6E74;")
        #self.button_Play.setStyleSheet(
        #    "background: #4B6E74")
        self.button_Play.setMinimumSize(250, 150)
        self.button_Play.setMaximumSize(250, 150)
        self.DEFAULT_WIDTH = self.button_Play.width()
        self.DEFAULT_HEIGTH = self.button_Play.height()
        self.button_Play.setFont(self.fontA)
        self.button_Play.setText("Start Pong Game")
        #self.button_Play.layout = QVBoxLayout()

        self.loading_label = QLabel()
        #self.loading_label.width = 150
        #self.loading_label.height = 250
        self.loading_label.setVisible(False)
        self.loading_label.setMaximumSize(50, 150)
        self.loading_label.setMinimumSize(50, 150)

        self.loading_label.setStyleSheet(
            "margin-left: -2px; background: Yellow; border: 1px solid black; border-radius: 24px;")
        #self.buttonWidgetContainer.layout.addWidget(self.loading_label)
        #self.buttonWidgetContainer.layout.addWidget(self.button_Play)
        self.button_Play.layout.addWidget(self.loading_label)
        # Add the two "buttons"
        self.inner_vbox_label_container.layout.addWidget(self.button_Opinion)
        self.inner_vbox_label_container.setStyleSheet('background-color: blue')

        #self.inner_vbox_label_container.layout.addWidget(self.buttonWidgetContainer)

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
            "Lorem ipsum dolor sit amet, \nconsetetur sadipscing elitr, \nsed diam nonumy eirmod tempor invidunt \nut "
            "labore et dolore magna aliquyam \nerat, sed diam voluptua.")
        self.inner_chat_label.setStyleSheet(
            "background: #EBEFF0;")
        self.inner_chat_label.setMinimumWidth(800)

        # setup the QScrollArea
        self.scrollArea = QtGui.QScrollArea()
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 100, 100))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidget(self.inner_chat_label)

        # add the chat and the scroll area
        self.outer_chat_v_label.setMaximumSize(300,400)
        self.inner_vbox_label_container.setMaximumSize(300,600)
        #self.mid_label_container.setStyleSheet("background: #EBEFF0;")
        self.mid_label_container.setMaximumHeight(400)



        self.inner_chat_label.setFont(self.fontA)
        # Adds the inner box to the outer box
        self.outer_chat_v_label.layout.addWidget(self.scrollArea)
        # Adds the chat to the midd label container
        self.mid_label_container.layout.addWidget(self.outer_chat_v_label)

    def load(self, i):
        self.loading_label.setMaximumSize(int(self.DEFAULT_WIDTH / 100 * i), self.DEFAULT_HEIGTH)
        self.loading_label.setVisible(True)

    def reset_load(self):
        self.loading_label.setMaximumSize(0, 0)
        self.loading_label.setVisible(False)
