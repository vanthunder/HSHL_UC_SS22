from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QStackedLayout
from PyQt5.QtWidgets import QLabel, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets


class Cursor():
    def __init__(self):
        super().__init__()
        self.s1 = "Das größte Gebiet, das zu keinem Staat der Erde gehört, ist das Marie-Byrd-Land mit einer Fläche von \n" \
                  "etwa 1,6 Millionen Quadratkilometern. Es befindet sich in der Antarktis und beherbergt einige aktive \n" \
                  "Vulkane und ist auch sonst ziemlich unwirtlich."
        self.s2 = "Die tiefste jemals gemessene Temperatur auf der Erde wurde 2004 auf einer Hochebene in der Antarktis \n" \
                  "gemessen. Sage und schreibe -98,6 Grad Celsius wurden dort gemessen. Der heißeste Ort der Erde ist \n" \
                  "dagegen in der iranischen Wüste Dascht-e Lut. Dort wurden über 70 Grad Celsius gemessen."
        self.s3 = "Entgegen der landläufigen Meinung, das Nordkapp sei der nördlichste Punkt des europäischen Festlands,\n" \
                  " ist die Felsspitze Kinnarodden der nördlichste Punkt. Nur über eine 24 Kilometer lange Wanderung \n" \
                  "kann man den schroffen Fels erreichen. Der südlichste Punkt Europas ist die Punta de Tarifa im \n" \
                  "spanischen Andalusien. Fact am Rande: Die Entfernung in Luftlinie zwischen den beiden Punkten beträgt \n" \
                  "rund 4.400 Kilometer."
        self.s4 = "Der größte See von Europa ist der Ladogasee in Russland. Mit einer Fläche von etwa 17.700 \n" \
                  "Quadratkilometern ist er etwa 33 mal so groß wie der Bodensee. Damit ist der Ladogasee auf Platz 14 \n" \
                  "der größten Seen der Welt."
        self.s5 = "Das Gewässer mit dem klarsten Wasser auf der ganzen Welt ist der Blue Lake in Neuseeland. \n" \
                  "Sein Wasser ist so klar, dass du darin mehr als 70 Meter weit sehen kannst. Weiter geht es nur in \n" \
                  "destilliertem Wasser. Darin kannst du 80 Meter weit sehen."
        self.s6 = "Es gibt einen kochenden Fluss. Der Shanay-timpishka in Peru ist durchschnittlich 86 Grad \n" \
                  "Celsius heiß und ein Mysterium der Wissenschaft."
        self.s7 = "Über die Höhe des Mount Everest besteht erst seit kurzem Einigkeit. Denn bis zum Jahre 2020 waren \n" \
                  "sich Nepal und China nicht einig darüber. Nun ist die offizielle Höhe des höchsten Berges der \n" \
                  "Welt 8.848 Meter und 86 Zentimeter."
        self.s8 = "Der abgelegenste bewohnte Ort der Welt ist die Inselgruppe Tristan da Cunha im südlichen Atlantik. \n" \
                  "Auf der gleichnamigen Hauptinsel liegt der Ort Edinburgh of the Seven Seas, der etwa 300 Einwohner \n" \
                  "hat. Fast 3.000 Kilometer sind es von dort aus nach Südafrika. Der von allen Küsten und Inseln der \n" \
                  "Erde am weitesten abgelegene Ort dagegen liegt im südlichen Pazifik. Es handelt sich dabei um Point \n" \
                  "Nemo, auch als Pol der Unzugänglichkeit bezeichnet. Dort befindet sich übrigens ein Raumschifffriedhof."
        self.s9 = "Der größte Containerhafen der Welt ist der Hafen von Shanghai. Der größte europäische Containerhafen \n" \
                  "ist der Hafen von Rotterdam. Er liegt immerhin auf Platz 11 der größten Containerhafen der Welt und \n" \
                  "hat etwa ein Drittel des Containerumschlags von Shanghai."
        self.s10 = "Spätestens seit dem Videospiel Silent Hill oder dem gleichnamigen Film erlangte die US-Stadt \n" \
                   "Centralia weltweite Bekanntheit. Denn ein unheimlicher Kohlebrand unter der Erde verwandelte die \n" \
                   "Stadt in eine Geisterstadt. Aber Centralia ist nicht das einzige Gebiet auf der Welt, wo es einen \n" \
                   "solchen Kohlebrand gibt. Auch in Deutschland gibt es so etwas: der Brennende Berg im Saarland."
        self.s11 = "Der Nevado Ojos del Salado ist nicht nur der höchste aktive Vulkan der Welt, sondern auch der \n" \
                   "höchste Berg in Chile. Er ist 6.893 Meter hoch. Sein letzter Ausbruch ist schon ein paar \n" \
                   "Jahrhunderte her. Fun Fact am Rande: Der Nevado Ojos del Salado ist recht einfach zu besteigen. \n" \
                   "Man kann sogar mit dem Auto auf den Gipfel fahren."
        self.s12 = "Der längste Straßentunnel der Welt ist der Lærdalstunnel. Er liegt in der norwegischen Region \n" \
                   "Sogn och Fjordane und ist 24,51 Kilometer lang. \n" \
                   "Der längste Eisenbahntunnel der Welt liegt übrigens in der Schweiz. Es ist der \n" \
                   "57 Kilometer lange Gotthard-Basistunnel."
        self.s13 = "Die höchste Brücke der Welt ist seit 2016 und mit einer Höhe von 565 Metern die \n" \
                   "Beipanjiang-Brücke in China. Die höchste Brücke von Europa ist das 270 Meter hohe Viaduc de Millau \n" \
                   "in Frankreich."
        self.s14 = "Der Musikantenknochen ist kein Knochen, sondern ein Nerv mit der Bezeichnung Nervus ulnaris."
        self.s15 = "Hausstaub besteht meist bis zu 80% aus abgestorbenen Hautzellen. Der Körper verliert am Tag bis \n" \
                   "zu 14 Gramm abgestorbene Hautzellen. Das können dann im Jahr etwa 3-5 Kilogramm sein. "
        self.s16 = "Bis zum Jahre 1937 hatten Haiti und Liechtenstein die selbe Flagge. Und das ist niemandem \n" \
                   "aufgefallen bis zu den olympischen Spielen 1936. Daraufhin wurde der Flagge Liechtensteins \n" \
                   "eine Krone hinzugefügt."
        self.s17 = "Im Jahre 1859 gab es ein extrem seltenes Ereignis. Wegen starker Sonnenstürme konnten Nordlichter \n" \
                   "über Rom bewundert werden."
        self.s18 = "Im Jahre 1961 bestellte der US-Präsident Kennedy noch schnell 1.000 kubanische Zigarren, \n" \
                   "bevor er das Embargo gegen das bewundernswerte kleine Land unterzeichnete."
        self.s19 = "Da die Mammuts erst etwa 2.000 vor Christus endgültig ausgestorben sind, überschneidet sich ihre \n" \
                   "Lebenszeit noch mit dem Bau der ersten ägyptischen Pyramiden."
        self.s20 = "Es gibt nach derzeitigem Stand 39 Menschen, die alle 14 Berge der Erde, die über 8.000 Meter \n" \
                   "hoch sind, bestiegen haben. Der erste davon war Reinhold Messner."
        self.s21 = "Die USA haben bis heute 11 Atombomben verloren. Ihr Aufenthaltsort ist nicht bekannt. \n" \
                   "Insgesamt gingen weltweit bisher etwa 50 Atombomben verloren."
        self.s22 = "Auf der Venus dauert ein Tag länger als ein Jahr. Ein Venus-Tag entspricht nämlich \n" \
                   "ungefähr 243 Tagen auf der Erde und ein Venus-Jahr nur etwa 225 Tagen auf der Erde."
        self.funFacts = [self.s1, self.s2, self.s3, self.s4, self.s5, self.s6, self.s7, self.s8, self.s9, self.s10]