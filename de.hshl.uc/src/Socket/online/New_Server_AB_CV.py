# Connection Data
import pickle
import socket
import threading

host = '34.159.99.140'
port = int(1666)
# Only for debugging
testList = []
testtupel = (1,1)

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 1666))
server.listen()
print('Server started!')
print('Booted: ', server.getsockname())

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
    while True:
        try:
            # Broadcasting Messages

            message = client.recv(1024)

            received_tupel = pickle.loads(message)  ## Fehler Code
            received_tupel = pickle.dumps(received_tupel)
            broadcast(received_tupel)
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
