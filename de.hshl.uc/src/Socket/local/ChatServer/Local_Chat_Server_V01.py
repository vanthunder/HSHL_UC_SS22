import pickle # Import the pickle module
import socket # Imports the socket module
import threading # Imports the threading module

from pymongo import MongoClient # Import MongoDB Client

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Defines the type of socket
server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1) # Defines the type of socket
host = socket.gethostname() # Defines the host
port = 1668 # Defines the port
server.bind((host, port)) # Defines the host and the port
server.listen(120)  # Defines the number of clients which can conect to the server
print('ChatServer Server started!')
print('Booted: ', server.getsockname())
chat_Tag = "chat" # Defines the tag for the chat
chatContainer = []
tmpMongoDBDocumentContainer = [] # Container for MongoDB Documents
clients = [] # List of Clients
# Defines the MongoDB Collection
uri = "mongodb://awd-cluster1-shard-00-00.kbtax.mongodb.net:27017,awd-cluster1-shard-00-01.kbtax.mongodb.net:27017,awd-cluster1-shard-00-02.kbtax.mongodb.net:27017/?ssl=true&replicaSet=atlas-59yop8-shard-0&authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
client = MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile='X509-cert-2736298636718940233.pem')
db = client['Chat_Application']
collection = db['chatmessages']
doc_count = collection.count_documents({})


def update_Chat(): # Updates the Chat Container
    print("Update_Chat")
    for x in collection.find(): # Finds all documents in the collection
        # print(x)
        document = x # Defines the document
        if not (tmpMongoDBDocumentContainer.__contains__(document)): # Checks if the document is already in the container
            print(document)
            chat = (document, chat_Tag) # Defines the chat
            chatContainer.append(chat) # Adds the chat to the container
            tmpMongoDBDocumentContainer.append(document) # Adds the document to the container


# Sending Messages To All Connected Clients
def broadcast(message): # Sends the message to all connected clients
    for client in clients: # Iterates over all clients
        client.send(message) # Sends the message to the client
        print("Server send: ", message, " to Client")


# Handling Messages From Clients
def handle(client): # Handles the messages from the client
    print(clients)
    while True: # While the client is connected
        try: # Try to receive the message
            # Broadcasting Messages
            update_Chat() # Updates the chat container
            print("Message: ", chatTuple)
            chatTuple = pickle.dumps(chatContainer) # Encodes the chat container
            broadcast(chatTuple) # Sends the chat container to all clients

        except: # If the client is disconnected
            print('close Client')
            # Removing And Closing Clients
            index = clients.index(client) # Defines the index of the client
            clients.remove(client) # Removes the client from the list
            clients.clear() # Clears the list
            client.close() # Closes the client


# Receiving / Listening Function
def receive(): # Receives the messages from the clients
    while True: # While the server is running
        # Accept Connection
        client, address = server.accept() # Accepts the connection
        print("Connected with {}".format(str(address))) # Prints the address of the client
        clients.append(client) # Adds the client to the list
        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,)) # Starts the thread for the client
        thread.start() # Starts the thread
        print('Start Receive!')


receive() # Starts the receiving function
