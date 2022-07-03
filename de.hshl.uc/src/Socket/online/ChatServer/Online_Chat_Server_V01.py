import pickle
import socket
import threading

from pymongo import MongoClient

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
host = socket.gethostname()
port = 1668
server.bind((host, port))
server.listen(120)  # Defines the number of clients which can conect to the server
print('ChatServer Server started!')
print('Booted: ', server.getsockname())
chat_Tag = "chat"
chatContainer = []
tmpMongoDBDocumentContainer = []
clients = []

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
        if not (tmpMongoDBDocumentContainer.__contains__(document)):
            print(document)
            chat = (document, chat_Tag)
            chatContainer.append(chat)
            tmpMongoDBDocumentContainer.append(document)


# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients:
        client.send(message)
        print("Server send: ", message, " to Client")


# Handling Messages From Clients
def handle(client):
    print(clients)
    while True:
        try:
            # Broadcasting Messages
            update_Chat()
            print("Message: ", chatTuple)
            chatTuple = pickle.dumps(chatContainer)
            broadcast(chatTuple)

        except:
            print('close Client')
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            clients.clear()
            client.close()


# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))
        clients.append(client)
        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
        print('Start Receive!')


receive()
