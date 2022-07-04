import pickle # For Serializing and Deserializing Objects
import socket # For Socket
import threading # For Threading


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


class chat_client: # For Chat Client
    TempChatList = []

    def __init__(self):
        # Connecting To Server
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates a socket object
        self.client.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1) # Disables Nagle's algorithm
        self.host = socket.gethostname # Get local machine name
        self.port = 1668 # Reserve a port for your service.
        self.client.connect((self.host, self.port)) # Connect to server

    def receive(self): # Receives Messages from Server
        while True:

            # Receive Message From Server
            message = self.client.recv(8192) # Receive message from server
            message = (pickle.loads(message)) # Decode message
            self.TempChatList = message # Save message to TempChatList
            print(bcolors.OKBLUE, "Chat vom Server empfangen: ", self.TempChatList, bcolors.ENDC)

            # Close Connection When Error
            #print("An error occured!")
            # break

    def close_client(self): # Close Connection
        self.client.close() # Close Connection

    def startClientThread(self): # Starts Client Thread
        receive_thread = threading.Thread(target=self.receive, args=()) # Starts Thread
        receive_thread.start() # Starts Thread
        print("Client Thread successfully started!")

    def main(self): # Main Function
        lclient = chat_client() # Creates Client Object
        receive_thread = threading.Thread(target=lclient.receive, args=()) # Starts Thread
        receive_thread.start() # Starts Thread


if __name__ == "__main__": # Main Function
    c = chat_client # Creates Client Object
    c.main(self=chat_client) # Starts Client Thread
