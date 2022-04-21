from PyQt5.QtWidgets import QGraphicsRectItem


class Paddle(QGraphicsRectItem):
#initialization and setting up MRO with super
    def __init__(self,maxHeight,parent=None):
        super(Paddle,self).__init__(parent)
        self.maxHeight=maxHeight-105
        #maxHeight comes from the boundary of QGraphicsView class. I define to stop the paddle from #moving out of view

# for moving the paddle up
    def moveUp(self):
        if self.y()>0:
            self.setY(self.y()-10)

# for moving the paddle down
    def moveDown(self):
        if self.y()<self.maxHeight:
            self.setY(self.y()+10)


class View(QGraphicsView, QObject):
    def __init__(self, parent=None):
        super(View, self).__init__(parent)
        # self.resize(600,300)
        self.viewport = QGLWidget()
        self.setViewport(self.viewport)
        self.setFixedSize(700, 400)
        self.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWindowTitle('Pong')
        self.setWindowIcon(QIcon('pong.bmp'))
        self.setRenderHint(QPainter.Antialiasing)
        # print self.x(),'x',self.y(),'y',self.width(),'w',self.height(),'h'
        # self.setSceneRect(self.x()-2,self.y()+self.height()/2-2,self.width(),self.height())
        # self.centerOn(0,0)

    Wpress = pyqtSignal()
    Spress = pyqtSignal()
    UPpress = pyqtSignal()
    DownPress = pyqtSignal()

    def keyPressEvent(self, event):
        # print chr(event.key())
        if event.key() == Qt.Key_W:
            self.Wpress.emit()
        elif event.key() == Qt.Key_S:
            self.Spress.emit()
        elif event.key() == Qt.Key_Up:
            self.UPpress.emit()
        elif event.key() == Qt.Key_Down:
            self.DownPress.emit()


class SceneAndView:
    def __init__(self):
        self.scene = QGraphicsScene()
        self.view = View()
        self.view.setScene(self.scene)
        self.scene.setBackgroundBrush(QColor(0, 120, 30))


class Ball(QGraphicsEllipseItem):
    def __init__(self, parent=None):
        super(Ball, self).__init__(parent)
        self.vel = [0, 0]
        self.radius = 16

    def reflectX(self):
        # print self.vel[1]
        self.vel[0] = -self.vel[0]
        if self.vel[0] < 0:
            self.vel[0] -= 00.5
        else:
            self.vel[0] += 0.5
        self.setX(self.x() + self.vel[0])

    def reflectY(self):
        # print self.vel[1]
        self.vel[1] = -self.vel[1]
        self.setY(self.y() + self.vel[1])
        # print self.vel[1]

    def move(self):
        self.setX(self.x() + self.vel[0])
        self.setY(self.y() + self.vel[1])


class Paddle(QGraphicsRectItem):
    def __init__(self, maxHeight, parent=None):
        super(Paddle, self).__init__(parent)
        self.maxHeight = maxHeight - 105

    def moveUp(self):
        # print self.y(),self.maxHeight
        if self.y() > 0:
            self.setY(self.y() - 10)

    def moveDown(self):
        # print self.y(),self.maxHeight
        if self.y() < self.maxHeight:
            self.setY(self.y() + 10)


class PongGame:
    def __init__(self, parent=None):
        self.sceneView = SceneAndView()
        self.pen = QPen(Qt.green, 5, Qt.SolidLine, Qt.FlatCap, Qt.RoundJoin)
        self.ballbrush = QBrush(Qt.red)
        self.paddlebrush = QBrush(Qt.black)

        self.ball = Ball()
        self.ball.setBrush(self.ballbrush)
        # self.ball.setPen(self.pen)
        # print self.sceneView.view.height()/2,self.sceneView.view.height()
        # print self.sceneView.view.geometry()
        self.ball.setRect((self.sceneView.view.size().width() - 15) / 2, self.sceneView.view.height(), self.ball.radius,
                          self.ball.radius)
        self.boundary = [self.sceneView.view.width(), self.sceneView.view.height()]
        # self.ball.
        self.paddleLeft = Paddle(self.sceneView.view.height())
        self.paddleLeft.setRect(0, self.sceneView.view.size().height() / 2, 10, 100)
        self.paddleRight = Paddle(self.sceneView.view.height())
        self.paddleRight.setRect(self.sceneView.view.size().width() - 15, self.sceneView.view.size().height() / 2, 10,
                                 100)
        self.score = [0, 0]
        self.sceneView.scene.addLine(self.boundary[0] / 2, self.boundary[1] / 2, self.boundary[0] / 2,
                                     self.boundary[1] * 2)
        self.paddleLeft.setBrush(self.paddlebrush)
        self.paddleRight.setBrush(self.paddlebrush)
        # self.sceneView.view.setSceneRect(150,150,900,600)

        self.sceneView.scene.addItem(self.ball)
        self.sceneView.scene.addItem(self.paddleLeft)
        self.sceneView.scene.addItem(self.paddleRight)
        self.sceneView.view.Wpress.connect(self.paddleLeft.moveUp)
        self.sceneView.view.Spress.connect(self.paddleLeft.moveDown)
        self.sceneView.view.UPpress.connect(self.paddleRight.moveUp)
        self.sceneView.view.DownPress.connect(self.paddleRight.moveDown)

        self.scoreText = QGraphicsTextItem()

        self.sceneView.scene.addItem(self.scoreText)








if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = PongGame()
    w.sceneView.view.show()
    sys.exit(app.exec_())
