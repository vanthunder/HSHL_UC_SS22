import pickle
import socket
import threading
import pickle

# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('34.159.99.140', 1666))
tuple = (1, 2)
serial = pickle.dumps(tuple)


# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('utf8')
            if message == 'NICK':
                client.send(nickname.encode('utf8'))
            else:
                print(message)

        except:
            # Close Connection When Error
            print("An error occured! - New_Client.py")
            client.close()
            break


# Sending Messages To Server
def write():
    while True:

        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))
        #client.send(message.encode('utf8'))





# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
