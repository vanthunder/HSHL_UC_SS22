# Connection Data
import pickle
import socket
import threading
from pymongo import MongoClient

host = '34.159.99.140'
port = int(1666)
# Only for debugging
testList = []
testtupel = (1,1)

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.3', 1666))
server.listen(120)
print('Server started!')
print('Booted: ', server.getsockname())



uri = "mongodb://awd-cluster1-shard-00-00.kbtax.mongodb.net:27017,awd-cluster1-shard-00-01.kbtax.mongodb.net:27017,awd-cluster1-shard-00-02.kbtax.mongodb.net:27017/?ssl=true&replicaSet=atlas-59yop8-shard-0&authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
client = MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile='X509-cert-2736298636718940233.pem')
db = client['Chat_Application']
collection = db['Chatmessages']
doc_count = collection.count_documents({})
print(doc_count)
y = []
while True:
    for x in collection.find():
        #print(x)
        document = x
        if not(y.__contains__(document)):
            print(document)
            y.append(document)



# Lists For Clients and Their Nicknames
clients = []
nicknames = []

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
        #print(message)
        client.send(message)




# Handling Messages From Clients
def handle(client):
    packets = []
    while True:
        try:

            # Broadcasting Messages

            message = client.recv(2048)

            received_tupel = pickle.loads(message)  ## Fehler Code
            #received_tupel = pickle.dumps(received_tupel)
            packets.append(received_tupel)
            # Player 1 Packet
            if(len(packets) == 4):
                serialPackets = pickle.dumps(packets)
                broadcast(serialPackets)
                packets.clear()
            # print('TUPLE: ', received_tupel)
            # Proof if message is a coordinate
            #if (type(received_tupel) == tuple):
            #    print("Tuple detectet")
            #    writeList(received_tupel)
            ##else:
            #    broadcast(message)




        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break


# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode('utf8'))
#        nickname = client.recv(1024).decode('ascii')
 #       nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
  #      print("Nickname is {}".format(nickname))
   #     broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()








receive()
