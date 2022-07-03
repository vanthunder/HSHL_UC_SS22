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


class local_client:
    canStart = False
    player = 'Left'  # 'Left' Only for instancing variable. Client will be defined in mainWindow
    TempTupel = (player, 0)
    ballcoords = (111, 111)

    def __init__(self):

        # Connecting To Server
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.host = '34.159.99.140'
        self.port = 1667
        self.client.connect((self.host, self.port))
        receive_thread = threading.Thread(target=self.receive, args=())
        receive_thread.start()

    def receive(self):
        while True:
            message = self.client.recv(102048)
            if not message == None:
                message = pickle.loads(message)
                print(message)

            if type(message) is not bool:
                if type(message.__getitem__(0)) is str:
                    print(bcolors.HEADER, message, 'TempTupel wird mit dieser Variable überschrieben!',
                          bcolors.ENDC)  # True
                    self.TempTupel = message
                elif type(message.__getitem__(0)) is not str:
                    print(bcolors.OKGREEN, message, 'Ball wird mit dieser Variable überschrieben!', bcolors.ENDC)
                    self.ballcoords = message
            if type(message) == bool:
                self.canStart = True
            print('Server: ', message)

    def close_client(self):
        self.client.close()

    def sendReady(self, Player):
        # Special number: 101100 defines Player is ready
        readeyNumber = 101100
        playerCoordinates = (Player, readeyNumber)
        serialPC = pickle.dumps(playerCoordinates)
        print(bcolors.OKBLUE, playerCoordinates, "Send to Server!", bcolors.ENDC)
        self.client.send(serialPC)

    def sendCollision(self, collObject):
        coll = ("ball", collObject)
        serialPC = pickle.dumps(coll)
        self.client.send(serialPC)

    def sendcoordinate(self, Player, yCoordiante):
        print('Send: ', Player, yCoordiante)
        self.Y = yCoordiante
        playerCoordinates = (Player, yCoordiante)
        serialPC = pickle.dumps(playerCoordinates)
        self.client.send(serialPC)

    def main(self):
        lclient = local_client()
        receive_thread = threading.Thread(target=lclient.receive, args=())
        receive_thread.start()


if __name__ == "__main__":
    c = local_client
    c.main(self=local_client)
