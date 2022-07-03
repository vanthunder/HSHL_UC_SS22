import pickle
import socket
import threading


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Server:
    xC = 500
    yC = 500
    canStart = False
    startCounter = 0
    xPositive = True
    yPositive = True
    ballStartCoords = (625, 375)
    playerLeft = False
    playerRight = False

    def __init__(self):

        self.host = '34.159.99.140'
        self.port = 1667
        # Only for debugging
        self.testList = []
        self.testtupel = (1, 1)

        # Bools for Player
        # Asks is the player is ready

        # Starting Server
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.server.bind((socket.gethostname(), self.port))
        self.server.listen(120)  # Defines the number of clients which can conect to the server
        print('Server started!')
        print('Booted: ', self.server.getsockname())
        self.clients = []
        self.Is_closed = 'False'
        self.msgTuple = ("", 1)
        self.receive()
        # Ball start Coordinates
        self.ballStartCoords = (625, 375)
        self.positive = True
        self.canStart = False

    def updateBall(self, collisionObject):

        if collisionObject == 'paddleR':
            self.xPositive = False
        elif collisionObject == 'paddleL':
            self.xPositive = True
        elif collisionObject == 'bandeO':
            self.yPositive = True
        elif collisionObject == 'bandeU':
            self.yPositive = False

        if self.xPositive == True:
            self.ballMovementpositivex()
        elif self.xPositive == False:
            self.ballMovementnegativex()

        if self.yPositive:
            self.ballMovementpositivey()
        elif self.yPositive == False:
            self.ballMovementnegativey()

        if collisionObject == 'torL':
            self.xC = self.ballStartCoords.__getitem__(0)
            self.yC = self.ballStartCoords.__getitem__(1)
        elif collisionObject == 'torR':
            self.xC = self.ballStartCoords.__getitem__(0)
            self.yC = self.ballStartCoords.__getitem__(1)

    def ballMovementpositivex(self):
        self.xC += 2

    def ballMovementpositivey(self):
        self.yC += 2

    def ballMovementnegativex(self):
        self.xC -= 2

    def ballMovementnegativey(self):
        self.yC -= 2

    # Sending Messages To All Connected Clients
    def broadcast(self, message):
        for client in self.clients:
            client.send(message)
            print("Server send: ", message, " to Client")

    # Handling Messages From Clients
    def handle(self, client):
        while True:
            try:
                # Broadcasting Messages
                print(self.clients)
                print(bcolors.WARNING, "Oben", "Player L: ", self.playerLeft, " Player R: ", self.playerRight,
                      bcolors.ENDC,
                      self.startCounter)
                if self.startCounter == 0:
                    message = client.recv(102048)
                    print(message)
                    message = pickle.loads(message)
                self.msgTuple = message
                # Checks if one player is ready
                # If the number is 101100 the player is ready
                # If the number is 101101 the player is not ready
                if message.__getitem__(0) == 'Left':
                    if message.__getitem__(1) == 101100:
                        self.playerLeft = True
                    elif message.__getitem__(1) == 101101:
                        self.playerLeft = False
                elif message.__getitem__(0) == 'Right':
                    if message.__getitem__(1) == 101100:
                        self.playerRight = True
                    elif message.__getitem__(1) == 101101:
                        self.playerRight = False
                received_tupel = pickle.dumps(message)
                print(bcolors.HEADER, "Player L: ", self.playerLeft, " Player R: ", self.playerRight, bcolors.ENDC,
                      self.startCounter)
                if self.playerLeft == self.playerRight:
                    if self.startCounter == 1:
                        # time.sleep(0.5)
                        msg = pickle.dumps(self.playerLeft)
                        self.broadcast(msg)
                        # One of them must be different because of bool bug in the client!
                        self.playerLeft = True
                        self.playerRight = False
                        self.canStart = True
                        self.startCounter = 0
                    else:
                        self.startCounter += 1

                ## Ball code
                if self.canStart == True:
                    print('Can Start', self.xC, self.yC, message.__getitem__(1))
                    self.updateBall(message.__getitem__(1))
                    if message.__getitem__(1) == 'torL':
                        # msg 1011101 for torL
                        # msg 1011100 for torR
                        msgT = (1011101, 0)
                        msgT = pickle.dumps(msgT)
                        self.broadcast(msgT)
                    elif message.__getitem__(1) == 'torR':
                        msgT = (1011100, 0)
                        msgT = pickle.dumps(msgT)
                        self.broadcast(msgT)
                    msg = (self.xC, self.yC)
                    msg = pickle.dumps(msg)
                    self.broadcast(msg)
                if not self.msgTuple.__getitem__(1) == 101100 and not self.msgTuple.__getitem__(
                        1) == 101101 and not self.msgTuple.__getitem__(0) == 'ball':
                    self.broadcast(received_tupel)

            except:
                print('close Client')
                self.reset()
                # Removing And Closing Clients
                index = self.clients.index(client)
                self.clients.remove(client)
                self.clients.clear()
                client.close()
                self.reset()

            print(bcolors.BOLD, "Unten", "Player L: ", self.playerLeft, " Player R: ", self.playerRight, bcolors.ENDC,
                  self.startCounter)

    def reset(self):
        self.xC = 500
        self.yC = 500
        self.canStart = False
        self.startCounter = 0
        self.xPositive = True
        self.yPositive = True
        self.ballStartCoords = (625, 375)
        self.playerLeft = False
        self.playerRight = False
        print(bcolors.WARNING, "Sever Reset wurde durchgeführt!", bcolors.ENDC)

    # Receiving / Listening Function
    def receive(self):
        while True:
            # Accept Connection
            client, address = self.server.accept()
            print("Connected with {}".format(str(address)))
            self.clients.append(client)
            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()

    def main(self):

        server_inst = Server()
        receive_thread = threading.Thread(target=server_inst.receive, args=())
        receive_thread.start()


if __name__ == "__main__":
    c = Server
    c.main(self=Server)
