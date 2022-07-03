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


class chat_client:
    TempChatList = []

    def __init__(self):
        # Connecting To Server
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.host = socket.gethostname()
        self.port = 8000
        self.client.connect((self.host, self.port))

    def receive(self):
        while True:

            # Receive Message From Server
            message = self.client.recv(8192)
            if len(message):
                message = (pickle.loads(message))
            self.TempChatList = message
            print(bcolors.OKBLUE, "Chat vom Server empfangen: ", self.TempChatList, bcolors.ENDC)

            # Close Connection When Error
            print("An error occured!")
            # break

    def close_client(self):
        self.client.close()

    def startClientThread(self):
        receive_thread = threading.Thread(target=self.receive, args=())
        receive_thread.start()
        print("Client Thread successfully started!")

    def main(self):
        lclient = chat_client()
        receive_thread = threading.Thread(target=lclient.receive, args=())
        receive_thread.start()


if __name__ == "__main__":
    c = chat_client
    c.main(self=chat_client)
