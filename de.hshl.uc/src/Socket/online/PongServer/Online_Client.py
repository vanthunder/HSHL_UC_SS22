import pickle # Import the pickle module
import socket # Imports the socket module
import threading # Imports the threading module


class bcolors: # Defines the colors for the console
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class local_client: # Defines the local client
    canStart = False
    player = 'Left'  # 'Left' Only for instancing variable. Client will be defined in mainWindow
    TempTupel = (player, 0) # Defines the TempTupel
    ballcoords = (111, 111) # Ball Coordinates

    def __init__(self):# Defines the local client

        # Connecting To Server
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Defines the client
        self.client.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1) # Disables Nagle's algorithm
        self.host = '34.159.99.140' # Defines the host
        self.port = 1667 # Defines the port
        self.client.connect((self.host, self.port)) # Connects to the server
        receive_thread = threading.Thread(target=self.receive, args=()) # Starts the thread
        receive_thread.start() # Starts the thread

    def receive(self): # Defines the receive function
        while True:
            message = self.client.recv(102048) # Receives the message from the server
            if not message == None: # Checks if the message is not empty
                message = pickle.loads(message) # Decodes the message
                print(message)

            if type(message) is not bool: # Checks if the message is not a bool
                if type(message.__getitem__(0)) is str: # Checks if the message is a string
                    print(bcolors.HEADER, message, 'TempTupel wird mit dieser Variable überschrieben!',
                          bcolors.ENDC)  # True
                    self.TempTupel = message # Overwrites the TempTupel
                elif type(message.__getitem__(0)) is not str: # Checks if the message is not a string
                    print(bcolors.OKGREEN, message, 'Ball wird mit dieser Variable überschrieben!', bcolors.ENDC)
                    self.ballcoords = message # Overwrites the ballcoords
            if type(message) == bool: # Checks if the message is a bool
                self.canStart = True # Sets the canStart variable to true
            print('Server: ', message)

    def close_client(self): # Defines the close_client function
        self.client.close() # Closes the client

    def sendReady(self, Player): # Defines the sendReady function
        # Special number: 101100 defines Player is ready
        readeyNumber = 101100 # Defines the readyNumber
        playerCoordinates = (Player, readeyNumber) # Defines the playerCoordinates
        serialPC = pickle.dumps(playerCoordinates) # Encodes the playerCoordinates
        print(bcolors.OKBLUE, playerCoordinates, "Send to Server!", bcolors.ENDC)
        self.client.send(serialPC) # Sends the playerCoordinates to the server

    def sendCollision(self, collObject): # Defines the sendCollision function
        coll = ("ball", collObject) # Defines the coll
        serialPC = pickle.dumps(coll) # Encodes the coll
        self.client.send(serialPC) # Sends the coll to the server

    def sendcoordinate(self, Player, yCoordiante): # Defines the sendcoordinate function
        print('Send: ', Player, yCoordiante)
        self.Y = yCoordiante # Defines the Y
        playerCoordinates = (Player, yCoordiante) # Defines the playerCoordinates
        serialPC = pickle.dumps(playerCoordinates) # Encodes the playerCoordinates
        self.client.send(serialPC) # Sends the playerCoordinates to the server

    def main(self): # Defines the main function
        lclient = local_client() # Instances the local_client
        receive_thread = threading.Thread(target=lclient.receive, args=()) # Starts the thread
        receive_thread.start() # Starts the thread


if __name__ == "__main__": # Defines the main function
    c = local_client # Instances the local_client
    c.main(self=local_client) # Calls the main function
