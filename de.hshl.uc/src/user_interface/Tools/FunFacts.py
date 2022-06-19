from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QStackedLayout
from PyQt5.QtWidgets import QLabel, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets


class Cursor():
    def __init__(self):
        super().__init__()
        self.s1 = "Das größte Gebiet, das zu keinem Staat der Erde gehört, ist das Marie-Byrd-Land mit einer Fläche von " \
                  "etwa 1,6 Millionen Quadratkilometern. Es befindet sich in der Antarktis und beherbergt einige aktive " \
                  "Vulkane und ist auch sonst ziemlich unwirtlich."
        self.s2 = "Die tiefste jemals gemessene Temperatur auf der Erde wurde 2004 auf einer Hochebene in der Antarktis " \
                  "gemessen. Sage und schreibe -98,6 Grad Celsius wurden dort gemessen. Der heißeste Ort der Erde ist " \
                  "dagegen in der iranischen Wüste Dascht-e Lut. Dort wurden über 70 Grad Celsius gemessen."
        self.s3 = "Entgegen der landläufigen Meinung, das Nordkapp sei der nördlichste Punkt des europäischen Festlands," \
                  " ist die Felsspitze Kinnarodden der nördlichste Punkt. Nur über eine 24 Kilometer lange Wanderung " \
                  "kann man den schroffen Fels erreichen. Der südlichste Punkt Europas ist die Punta de Tarifa im " \
                  "spanischen Andalusien. Fact am Rande: Die Entfernung in Luftlinie zwischen den beiden Punkten beträgt " \
                  "rund 4.400 Kilometer."
        self.s4 = "Der größte See von Europa ist der Ladogasee in Russland. Mit einer Fläche von etwa 17.700 " \
                  "Quadratkilometern ist er etwa 33 mal so groß wie der Bodensee. Damit ist der Ladogasee auf Platz 14 " \
                  "der größten Seen der Welt."
        self.s5 = "Das Gewässer mit dem klarsten Wasser auf der ganzen Welt ist der Blue Lake in Neuseeland. " \
                  "Sein Wasser ist so klar, dass du darin mehr als 70 Meter weit sehen kannst. Weiter geht es nur in " \
                  "destilliertem Wasser. Darin kannst du 80 Meter weit sehen."
        self.s6 = "Es gibt einen kochenden Fluss. Der Shanay-timpishka in Peru ist durchschnittlich 86 Grad " \
                  "Celsius heiß und ein Mysterium der Wissenschaft."
        self.s7 = "Über die Höhe des Mount Everest besteht erst seit kurzem Einigkeit. Denn bis zum Jahre 2020 waren " \
                  "sich Nepal und China nicht einig darüber. Nun ist die offizielle Höhe des höchsten Berges der " \
                  "Welt 8.848 Meter und 86 Zentimeter."
        self.s8 = "Der abgelegenste bewohnte Ort der Welt ist die Inselgruppe Tristan da Cunha im südlichen Atlantik. " \
                  "Auf der gleichnamigen Hauptinsel liegt der Ort Edinburgh of the Seven Seas, der etwa 300 Einwohner " \
                  "hat. Fast 3.000 Kilometer sind es von dort aus nach Südafrika. Der von allen Küsten und Inseln der " \
                  "Erde am weitesten abgelegene Ort dagegen liegt im südlichen Pazifik. Es handelt sich dabei um Point " \
                  "Nemo, auch als Pol der Unzugänglichkeit bezeichnet. Dort befindet sich übrigens ein Raumschifffriedhof."
        self.s9 = "Der größte Containerhafen der Welt ist der Hafen von Shanghai. Der größte europäische Containerhafen " \
                  "ist der Hafen von Rotterdam. Er liegt immerhin auf Platz 11 der größten Containerhafen der Welt und " \
                  "hat etwa ein Drittel des Containerumschlags von Shanghai."
        self.s10 = "Spätestens seit dem Videospiel Silent Hill oder dem gleichnamigen Film erlangte die US-Stadt " \
                   "Centralia weltweite Bekanntheit. Denn ein unheimlicher Kohlebrand unter der Erde verwandelte die " \
                   "Stadt in eine Geisterstadt. Aber Centralia ist nicht das einzige Gebiet auf der Welt, wo es einen " \
                   "solchen Kohlebrand gibt. Auch in Deutschland gibt es so etwas: der Brennende Berg im Saarland."
        self.funFacts = [self.s1, self.s2, self.s3, self.s4, self.s5, self.s6, self.s7, self.s8, self.s9, self.s10]
