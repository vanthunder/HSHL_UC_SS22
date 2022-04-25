import pickle
import socket
import threading




# Only for debug


# Listening to Server and Sending Nickname


class local_client:
    Y = [11]
    Player = 'Left'
    tempTupel = ("", 0)
    def __init__(self) :
        # Choosing Nickname
        self.nickname = 'Client: '  # input("Choose your nickname: ")

        # Connecting To Server
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('127.0.0.2', 1666))
        #print(self.client)
        self.tuple = (1, 2)
        counter = 0
        self.serial = pickle.dumps(self.tuple)
        #self.y = [2]

    def receive(self):
        while True:
            #print('message')
            try:
                Y = 10
                print(Y)
                #print(self.client)
                # Receive Message From Server
                # If 'NICK' Send Nickname
                message = self.client.recv(1024)
                message = pickle.loads(message)
                self.y = message
                self.tempTupel = message
                #message = self.client.recv(1024).decode('ascii')
                print('Server: ', message)
                if message == 'NICK':
                    print()
                    self.client.send(self.nickname.encode('ascii'))
                else:
                    print(message)

            except:
                # Close Connection When Error
                print("An error occured!")
                # client.close()
                # break
    def upadteA(self):
        self.y.clear()
        print(self.y)

    def updateCoordinate(self, update):
        self.y = update
        print('Update!!!!: ',update)

    # Sending Messages To Server
    def write(self):
        while True:
            message = '{}: {}'.format(self.nickname, input(''))
            #self.sendcoordinate(10)
            print(message)
            #self.client.send(self.serial)

    # message = '{}: {}'.format(nickname, input(''))
    # print(message)
    # client.send(serial)

    def sendcoordinate(self,Player ,yCoordiante):
        print('Send: ', Player ,yCoordiante)
        self.Y = yCoordiante
        #print(self.Y)
        playerCoordinates = (Player, yCoordiante)
        serialPC = pickle.dumps(playerCoordinates)
        #serialY = pickle.dumps(yCoordiante)
        self.client.send(serialPC)
        # Starting Threads For Listening And Writing

    def main(self):

        lclient = local_client()
        receive_thread = threading.Thread(target=lclient.receive, args=())
        print('TEST')
        receive_thread.start()

        write_thread = threading.Thread(target=lclient.write(), args=())
        write_thread.start()



if __name__ == "__main__":
    c = local_client
    c.main(self=local_client)
