import pickle
import socket
import threading




# Only for debug


# Listening to Server and Sending Nickname
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

class local_client:
    Y = [11]
    player = 'Left'
    TempTupel = (player, 0)
    TempChatList = [TempTupel]
    packets = []
    #client = "Client"
    nickname = 'Client'
    pkg = []
    def __init__(self) :
        # Choosing Nickname
        self.nickname = 'Client: '  # input("Choose your nickname: ")

        # Connecting To Server
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.client.connect(('34.159.99.140', 1667))
        #print(self.client)
        self.tuple = (1, 2)
        counter = 0
        self.Player = ""
        self.serial = pickle.dumps(self.tuple)
        #self.tempTupel=(self.Player,2)
        #self.y = [2]

    def receive(self):
        while True:
            try:
                print(bcolors.WARNING, "Server_____: ", bcolors.ENDC)
                Y = 10
                print(Y)
                #print(self.client)
                # Receive Message From Server
                # If 'NICK' Send Nickname
                print('Vor Server Receive')
                message = self.client.recv(102048)
                #message = self.client.recv(1048576)
                print('Vor Message decode')
                message = pickle.loads(message)
                print(message)
                # To-Do: Filter Mongo db message!
                #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print('Vor Message CHAT')
                #if message[2].__getitem__(1) == "chat":
                #    print(bcolors.WARNING, "Chat_____: ", bcolors.ENDC)
                #    self.TempChatList = message
                #    print(bcolors.OKBLUE, "Chat: ", self.TempChatList,bcolors.ENDC)
                #    print(self.TempChatList)
                #else:
                #    print('Vor Message decode1')
                #    #
                self.TempTupel = message

                #packets = message
                print('Vor Message decode2')
                #self.pKg = packets
                #print("SERVERPACKET: ",packets)
                #self.TempTupel = message
                #if len(self.pKg) != 0:
                #    for tuple in packets:
                #        self.TempTupel = tuple
                #self.settimeout(0.050)
                #self.y = message
                #self.tempTupel = message
                #message = self.client.recv(1024).decode('ascii')
                print('Server: ', message)
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

    def close_client(self):
        self.client.close()

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
    def sendReady(self, Player):
        #Special number: 101100 defines Player is ready
        readeyNumber = 101100
        playerCoordinates = (Player, readeyNumber)
        serialPC = pickle.dumps(playerCoordinates)
        self.client.send(serialPC)

    def sendcoordinate(self, Player ,yCoordiante):
        print('Send: ', Player ,yCoordiante)
        self.Y = yCoordiante
        receive_thread = threading.Thread(target=self.receive, args=())
        receive_thread.start()
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
