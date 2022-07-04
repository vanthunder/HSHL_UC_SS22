import pickle # Imports the pickle module
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


class Server: # Defines the server
    xC = 500 # Ball X Coordinate
    yC = 500 # Ball Y Coordinate
    canStart = False # Bool for starting the game
    startCounter = 0 # Counter for the start of the game
    xPositive = True # Bool for the x-axis
    yPositive = True # Bool for the y-axis
    ballStartCoords = (625, 375) # Ball Start Coordinates
    playerLeft = False # Bool for the left player
    playerRight = False # Bool for the right player

    def __init__(self): # Defines the server

        self.host = '34.159.99.140' # Host IP
        self.port = 1667 # Port
        # Only for debugging
        self.testList = [] # List for the test
        self.testtupel = (1, 1) # Tuple for the test

        # Bools for Player
        # Asks is the player is ready

        # Starting Server
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a socket object
        self.server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1) # Disables Nagle's algorithm
        self.server.bind((socket.gethostname(), self.port)) # Binds the socket to the port
        self.server.listen(120)  # Defines the number of clients which can conect to the server
        print('Server started!') # Prints the server started
        print('Booted: ', self.server.getsockname()) # Prints the booted IP and Port
        self.clients = [] # List for the clients
        self.Is_closed = 'False' # Bool for the server
        self.msgTuple = ("", 1) # Tuple for the message
        self.receive() # Starts the receiving function
        # Ball start Coordinates
        self.ballStartCoords = (625, 375) # Ball Start Coordinates
        self.positive = True # Bool for the x-axis
        self.canStart = False # Bool for starting the game

    def updateBall(self, collisionObject): # Updates the ball

        if collisionObject == 'paddleR': # If the ball hits the right paddle
            self.xPositive = False  # Changes the x-axis
        elif collisionObject == 'paddleL': # If the ball hits the left paddle
            self.xPositive = True # Changes the x-axis
        elif collisionObject == 'bandeO': # If the ball hits the top bande
            self.yPositive = True # Changes the y-axis
        elif collisionObject == 'bandeU': # If the ball hits the bottom bande
            self.yPositive = False # Changes the y-axis

        if self.xPositive == True: # If the x-axis is positive
            self.ballMovementpositivex() # Moves the ball to the right
        elif self.xPositive == False: # If the x-axis is negative
            self.ballMovementnegativex() # Moves the ball to the left

        if self.yPositive: # If the y-axis is positive
            self.ballMovementpositivey() # Moves the ball to the bottom
        elif self.yPositive == False: # If the y-axis is negative
            self.ballMovementnegativey() # Moves the ball to the top

        if collisionObject == 'torL': # If the ball hits the left wall
            self.xC = self.ballStartCoords.__getitem__(0) # x-axis is set to the ball start coordinates
            self.yC = self.ballStartCoords.__getitem__(1) # y-axis is set to the ball start coordinates
        elif collisionObject == 'torR': # If the ball hits the right wall
            self.xC = self.ballStartCoords.__getitem__(0) # x-axis is set to the ball start coordinates
            self.yC = self.ballStartCoords.__getitem__(1) # y-axis is set to the ball start coordinates

    def ballMovementpositivex(self): # Moves the ball to the right
        self.xC += 2 # Moves the ball to the right

    def ballMovementpositivey(self): # Moves the ball to the bottom
        self.yC += 2 # Moves the ball to the bottom

    def ballMovementnegativex(self): # Moves the ball to the left
        self.xC -= 2 # Moves the ball to the left

    def ballMovementnegativey(self): # Moves the ball to the top
        self.yC -= 2 # Moves the ball to the top

    # Sending Messages To All Connected Clients
    def broadcast(self, message): # Sends the message to all connected clients
        for client in self.clients: # For every client in the clients list
            client.send(message) # Sends the message to the client
            print("Server send: ", message, " to Client") # Prints the message sent to the client

    # Handling Messages From Clients
    def handle(self, client): # Handles the messages from the clients
        while True:
            try: # Trys to receive the message
                # Broadcasting Messages
                print(self.clients)
                print(bcolors.WARNING, "Oben", "Player L: ", self.playerLeft, " Player R: ", self.playerRight,
                      bcolors.ENDC,
                      self.startCounter) # Prints the players and the start counter
                if self.startCounter == 0: # If the start counter is 0
                    message = client.recv(102048) # Receives the message
                    print(message)
                    message = pickle.loads(message) # encodes the message
                self.msgTuple = message # Sets the message tuple to the message
                # Checks if one player is ready
                # If the number is 101100 the player is ready
                # If the number is 101101 the player is not ready
                if message.__getitem__(0) == 'Left': # If the message is from the left player
                    if message.__getitem__(1) == 101100: # If the message is 101100
                        self.playerLeft = True # The player is ready
                    elif message.__getitem__(1) == 101101: # If the message is 101101
                        self.playerLeft = False  # The player is not ready
                elif message.__getitem__(0) == 'Right': # If the message is from the right player
                    if message.__getitem__(1) == 101100: # If the message is 101100
                        self.playerRight = True # The player is ready
                    elif message.__getitem__(1) == 101101: # If the message is 101101
                        self.playerRight = False # The player is not ready
                received_tupel = pickle.dumps(message) # Encodes the message
                print(bcolors.HEADER, "Player L: ", self.playerLeft, " Player R: ", self.playerRight, bcolors.ENDC,
                      self.startCounter)
                if self.playerLeft == self.playerRight: # If both players are ready
                    if self.startCounter == 1: # If the start counter is 1
                        # time.sleep(0.5)
                        msg = pickle.dumps(self.playerLeft) # Encodes the message
                        self.broadcast(msg) # Sends the message to all connected clients
                        # One of them must be different because of bool bug in the client!
                        self.playerLeft = True # Sets the player to ready
                        self.playerRight = False # Sets the player to not ready
                        self.canStart = True # Sets the canStart to True
                        self.startCounter = 0 # Sets the startCounter to 0
                    else: # If the start counter is 0
                        self.startCounter += 1 # Adds 1 to the startCounter

                ## Ball code
                if self.canStart == True: # If the game can start
                    print('Can Start', self.xC, self.yC, message.__getitem__(1)) # Prints the ball coordinates
                    self.updateBall(message.__getitem__(1)) # Updates the ball
                    if message.__getitem__(1) == 'torL': # If the ball hits the left wall
                        # msg 1011101 for torL
                        # msg 1011100 for torR
                        msgT = (1011101, 0) # Sets the message tuple to the message
                        msgT = pickle.dumps(msgT) # Encodes the message
                        self.broadcast(msgT) # Sends the message to all connected clients
                    elif message.__getitem__(1) == 'torR': # If the ball hits the right wall
                        msgT = (1011100, 0) # Sets the message tuple to the message
                        msgT = pickle.dumps(msgT) # Encodes the message
                        self.broadcast(msgT) # Sends the message to all connected clients
                    msg = (self.xC, self.yC) # Sets the message tuple to the message
                    msg = pickle.dumps(msg) # Encodes the message
                    self.broadcast(msg) # Sends the message to all connected clients
                if not self.msgTuple.__getitem__(1) == 101100 and not self.msgTuple.__getitem__(
                        1) == 101101 and not self.msgTuple.__getitem__(0) == 'ball': # If the message is not from the left or right player
                    self.broadcast(received_tupel) # Sends the message to all connected clients

            except: # If the message is not received
                print('close Client') # Prints the message
                self.reset() # Resets the Server
                # Removing And Closing Clients
                index = self.clients.index(client) # Gets the index of the client
                self.clients.remove(client) # Removes the client from the clients list
                self.clients.clear() # Clears the clients list
                client.close() # Closes the client
                self.reset() # Resets the game

            print(bcolors.BOLD, "Unten", "Player L: ", self.playerLeft, " Player R: ", self.playerRight, bcolors.ENDC,
                  self.startCounter)

    def reset(self): # Resets the Server
        self.xC = 500 # Sets the x-axis to 500
        self.yC = 500 # Sets the y-axis to 500
        self.canStart = False # Sets the canStart to False
        self.startCounter = 0 # Sets the startCounter to 0
        self.xPositive = True # Sets the xPositive to True
        self.yPositive = True # Sets the yPositive to True
        self.ballStartCoords = (625, 375) # Sets the ballStartCoords to (625, 375)
        self.playerLeft = False # Sets the playerLeft to False
        self.playerRight = False # Sets the playerRight to False
        print(bcolors.WARNING, "Sever Reset wurde durchgeführt!", bcolors.ENDC)

    # Receiving / Listening Function
    def receive(self): # Receives the message from the clients
        while True: # While true
            # Accept Connection
            client, address = self.server.accept() # Accepts the connection
            print("Connected with {}".format(str(address))) # Prints the connection
            self.clients.append(client) # Adds the client to the clients list
            thread = threading.Thread(target=self.handle, args=(client,)) # Creates a thread for the client
            thread.start() # Starts the thread

    def main(self): # Main function

        server_inst = Server() # Creates a new Server
        receive_thread = threading.Thread(target=server_inst.receive, args=()) # Creates a thread for the receiving function
        receive_thread.start() # Starts the thread


if __name__ == "__main__": # If the program is called directly
    c = Server() # Creates a new Server
    c.main(self=Server) # Calls the main function
