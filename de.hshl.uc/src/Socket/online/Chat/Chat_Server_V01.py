# Connection Data
import pickle
import socket
import sys
import threading

from pymongo import MongoClient

host = '34.159.99.140'
port = int(1666)
# Only for debugging
testList = []
testtupel = (1, 1)

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
server.bind((socket.gethostname(), 1668))
server.listen(120)
print('Chat Server started!')
print('Booted: ', server.getsockname())
chat_Tag = "chat"
chatContainer = []
y = []
chat_Text = ("", "")

# Lists For Clients and Their Nicknames
clients = []
nicknames = ['Chat Server']
Is_closed = 'False'

uri = "mongodb://awd-cluster1-shard-00-00.kbtax.mongodb.net:27017,awd-cluster1-shard-00-01.kbtax.mongodb.net:27017,awd-cluster1-shard-00-02.kbtax.mongodb.net:27017/?ssl=true&replicaSet=atlas-59yop8-shard-0&authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
client = MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile='X509-cert-2736298636718940233.pem')
db = client['Chat_Application']
collection = db['chatmessages']
doc_count = collection.count_documents({})

def update_Chat():
    print("Update_Chat")
    for x in collection.find():
        # print(x)
        document = x
        if not (y.__contains__(document)):
            print(document)
            chat = (document, chat_Tag)
            chat_Text = chat
            chatContainer.append(chat)
            # chatContainer.append(chat, chat_Tag)
            # Adds Container here!
            y.append(document)


# Method for write list
def writeList(coordinates):
    testList.append(coordinates)
    print(coordinates, " added to the list!")
    coordinates = pickle.dumps(coordinates)
    broadcast(coordinates)
    print(testList)


# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients:
        # print(message)
        client.send(message)
        print("Server send: ", message, " to Client")


# Handling Messages From Clients
def handle(client):
    packets = []
    while True:
        try:
            # Broadcasting Messages
            print(clients)
            #message = client.recv(102048)

            print("Update_Chat")
            update_Chat()
            print("Update_Chat2")

            print("Update_Chat3!")
            #received_tupel = pickle.loads(message)  # Fehler Code
            print("Message: ", chatTuple)
            #received_tupel = pickle.dumps(received_tupel)
            chatTuple = pickle.dumps(chatContainer)
            broadcast(chatTuple)
            #broadcast(received_tupel)
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

        except:
            print('close Client')
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            clients.clear()
            client.close()

            # To Do Close Thread

            # nickname = nicknames[index]
            # broadcast('{} left!'.format(nickname).encode('ascii'))
            # nicknames.remove(nickname)


# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        # client.send('NICK'.encode('utf8'))
        #        nickname = client.recv(1024).decode('ascii')
        #       nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        #      print("Nickname is {}".format(nickname))
        #     broadcast("{} joined!".format(nickname).encode('ascii'))
        # client.send('Connected to server!'.encode('ascii'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
        print('Start Receive!')
        # thread.join()


receive()
