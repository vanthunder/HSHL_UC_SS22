# Connection Data
import pickle
import socket
import sys
import threading
import time
from typing import Tuple

from pymongo import MongoClient, collection
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
    ballstartcoords = (625,375)

    def __init__(self):

        self.host = '34.159.99.140'
        self.port = int(1666)
        # Only for debugging
        self.testList = []
        self.testtupel = (1, 1)

        # Bools for Player
        # Asks is the player is ready
        self.playerLeft = False
        self.playerRight = False

        # Starting Server
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.server.bind((socket.gethostname(), 1667))
        self.server.listen(120)
        print('Server started!')
        print('Booted: ', self.server.getsockname())
        self.chat_Tag = "chat"
        self.chatContainer = []
        self.y = []
        self.chat_Text = ("", "")

        # Lists For Clients and Their Nicknames
        self.clients = []
        self.nicknames = ['Server']
        self.Is_closed = 'False'
        self.msgTuple = ("",1)
        self.receive()
        # Ball start Coordinates
        self.ballStartCoords = (625, 375)
        self.positive = True
        self.canStart = False


    def updateBall(self, collisionObject):
        #print('Die positive Variable: ', self.positive)

        # elif self.detect_collision()==False and not self.positive:
        #    self.positive = True
        #if self.detect_collision():
        #    if self.positive:
        #        self.positive = False

        #    elif self.positive == False:
        #        self.positive = True

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
            self.xC = self.ballStartCoords.__getitem__(1)
            self.yC = self.ballStartCoords.__getitem__(2)
        elif collisionObject == 'torR':
            self.xC = self.ballStartCoords.__getitem__(1)
            self.yC = self.ballStartCoords.__getitem__(2)

        #elif self.positive == False:
        #    self.ballStartCoords = self.ballMovementnegative()



    def ballMovementpositivex(self):
        self.xC += 2
        #self.pongWindow.imageLabel3.setGeometry(self.bX, self.bY, 80, 80)
    def ballMovementpositivey(self):
        self.yC += 2
        #self.pongWindow.imageLabel3.setGeometry(self.bX, self.bY, 80, 80)

    def ballMovementnegativex(self):
        self.xC -= 2
        #self.pongWindow.imageLabel3.setGeometry(self.bX, self.bY, 80, 80)
    def ballMovementnegativey(self):
        self.yC -= 2
        # self.pongWindow.imageLabel3.setGeometry(self.bX, self.bY, 80, 80)



    def update_Chat(self):
        print("Update_Chat")
        for x in collection.find():
            # print(x)
            document = x
            if not (self.y.__contains__(document)):
                print(document)
                chat = (document, self.chat_Tag)
                chat_Text = chat
                self.chatContainer.append(chat)
                # chatContainer.append(chat, chat_Tag)
                # Adds Container here!
                self.y.append(document)





    # Sending Messages To All Connected Clients
    def broadcast(self,message):
        for client in self.clients:
            # print(message)
            client.send(message)
            print("Server send: ", message, " to Client")


    # Handling Messages From Clients
    def handle(self, client):
        self.packets = []
        #playerLeft = False
        #playerRight = False
        while True:

            # Broadcasting Messages
            print(self.clients)
            print(bcolors.WARNING, "Oben", "Player L: ", self.playerLeft, " Player R: ", self.playerRight,
                  bcolors.ENDC,
                  self.startCounter)
            if self.startCounter == 0:
                message = client.recv(102048)
                print(message)
                message = pickle.loads(message)

           # print("Update_Chat")
           # update_Chat()
           # print("Update_Chat")

            print(message)
            #message = pickle.loads(message)
            self.msgTuple = message
           # print("Update_Chat!")
           # Checks if one player is ready
           # If the number is 101100 the player is ready
           # If the number is 101101 the player is not ready
           # if message == tuple:
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



            if self.playerRight:
                print('TRUE!!!!!!!!!!!!!!!!!!!')
           # print("Message: ", received_tupel)
            received_tupel = pickle.dumps(message)
           # chatTuple = pickle.dumps(chatContainer)
            ## Client start code
            print(bcolors.HEADER, "Player L: ", self.playerLeft, " Player R: ", self.playerRight, bcolors.ENDC, self.startCounter)
            if self.playerLeft == self.playerRight:
                if self.startCounter == 1:
                    #time.sleep(0.5)
                    print('Das ist ein OK!!!!!!!!!!!!!')
                    msg = pickle.dumps(self.playerLeft)
                    self.broadcast(msg)
                    # One of them must be different because of bool bug in the client!
                    self.playerLeft = True
                    self.playerRight = False
                    self.canStart = True
                    self.startCounter = 0
                else:
                    print("Counter wird gesetzt!")
                    self.startCounter += 1


            ## Ball code
            if self.canStart == True:
                print('Can Start', self.xC, self.yC, message.__getitem__(1))
                self.updateBall(message.__getitem__(1))
                #self.ballMovementpositive()
                #self.x += 10
                msg = (self.xC, self.yC)
                msg = pickle.dumps(msg)
                self.broadcast(msg)
               # broadcast(playerLeft)
           # broadcast(chatTuple)
            print(self.msgTuple, " DER TUPLE!!!!!")
            if not self.msgTuple.__getitem__(1) == 101100 and not self.msgTuple.__getitem__(1) == 101101 and not self.msgTuple.__getitem__(0) == 'ball':
                self.broadcast(received_tupel)
           # if playerLeft == True:
            # print('TEST')
            # allReady = True
            # print("Alle Clients sind TRUE")
            # msg = pickle.dumps(allReady)
            # broadcast(msg)
           # If statemnt if all players are ready sent start command to clients

            # broadcast(msg)

            # packets.append(received_tupel)
            # Player 1 Packet

            # if(len(packets) == 2):
            #    serialPackets = pickle.dumps(packets)
            #    print(packets)
            #    broadcast(serialPackets)
            #    packets.clear()

            # print('TUPLE: ', received_tupel)
            # Proof if message is a coordinate
            # if (type(received_tupel) == tuple):
            #    print("Tuple detectet")
            #    writeList(received_tupel)
            # else:
            #    broadcast(message)
            print(bcolors.BOLD, "Unten","Player L: ", self.playerLeft, " Player R: ", self.playerRight, bcolors.ENDC,
                self.startCounter)


            #print('close Client')
            # Removing And Closing Clients
            #self.index = self.clients.index(client)
            #self.clients.remove(client)
            #self.clients.clear()
            #client.close()

            # To Do Close Thread

            # nickname = nicknames[index]
            # broadcast('{} left!'.format(nickname).encode('ascii'))
            # nicknames.remove(nickname)


    # Receiving / Listening Function
    def receive(self):
        while True:
            # Accept Connection
            client, address = self.server.accept()
            print("Connected with {}".format(str(address)))

            # Request And Store Nickname
            # client.send('NICK'.encode('utf8'))
            #        nickname = client.recv(1024).decode('ascii')
            #       nicknames.append(nickname)
            self.clients.append(client)

            # Print And Broadcast Nickname
            #      print("Nickname is {}".format(nickname))
            #     broadcast("{} joined!".format(nickname).encode('ascii'))
            # client.send('Connected to server!'.encode('ascii'))

            # Start Handling Thread For Client
            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()
            # thread.join()



    def main(self):

        server_inst = Server()
        receive_thread = threading.Thread(target=server_inst.receive, args=())
        print('TEST')
        receive_thread.start()




if __name__ == "__main__":
    c = Server
    c.main(self=Server)
