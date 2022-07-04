import pickle
import socket
import threading


class bcolors: # For Coloring Console Output
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class local_client: # For Chat Client
    canStart = False
    player = 'Left'  # 'Left' Only for instancing variable. Client will be defined in mainWindow
    TempTupel = (player, 0)
    ballcoords = (111, 111)

    def __init__(self):

        # Connecting To Server
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a socket object
        self.client.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1) # Disables Nagle's algorithm
        self.host = socket.gethostname() # Get local machine name
        self.port = 1667 # Reserve a port for your service.
        self.client.connect((self.host, self.port)) # Connect to the server
        receive_thread = threading.Thread(target=self.receive, args=()) # Starts a new thread for receiving
        receive_thread.start()

    def receive(self): # Receives Messages from Server
        while True:
            message = self.client.recv(102048) # Receive message from server
            if not message == None: # If message is not empty
                message = pickle.loads(message) # Decode message
                print(message)

            if type(message) is not bool: # If message is not empty
                if type(message.__getitem__(0)) is str: # If message is not empty
                    print(bcolors.HEADER, message, 'TempTupel wird mit dieser Variable überschrieben!',
                          bcolors.ENDC)  # True
                    self.TempTupel = message # Overwrites TempTupel with message
                elif type(message.__getitem__(0)) is not str: # If message is not empty
                    print(bcolors.OKGREEN, message, 'Ball wird mit dieser Variable überschrieben!', bcolors.ENDC)
                    self.ballcoords = message # Overwrites ballcoords with message
            if type(message) == bool: # If message is not empty
                self.canStart = True # Sets canStart to True
            print('Server: ', message)

    def close_client(self): # Closes Client
        self.client.close() # Closes Client

    def sendReady(self, Player): # Sends Ready Message to Server
        # Special number: 101100 defines Player is ready
        readeyNumber = 101100 # Defines Player is ready
        playerCoordinates = (Player, readeyNumber) # Defines Player Coordinates
        serialPC = pickle.dumps(playerCoordinates) # Encodes message
        print(bcolors.OKBLUE, playerCoordinates, "Send to Server!", bcolors.ENDC)
        self.client.send(serialPC) # Sends message to Server

    def sendCollision(self, collObject): # Sends Collision Message to Server
        coll = ("ball", collObject) # Defines Collision
        serialPC = pickle.dumps(coll) # Encodes message
        self.client.send(serialPC) # Sends message to Server

    def sendcoordinate(self, Player, yCoordiante): # Sends Coordinates to Server
        print('Send: ', Player, yCoordiante)
        self.Y = yCoordiante # Sets Y Coordinate
        playerCoordinates = (Player, yCoordiante) # Defines Player Coordinates
        serialPC = pickle.dumps(playerCoordinates) # Encodes message
        self.client.send(serialPC) # Sends message to Server

    def main(self): # Main Function
        lclient = local_client() # Instances local_client
        receive_thread = threading.Thread(target=lclient.receive, args=()) # Starts a new thread for receiving
        receive_thread.start() # Starts thread


if __name__ == "__main__": # Main Function
    c = local_client # Instances local_client
    c.main(self=local_client) # Starts main function
