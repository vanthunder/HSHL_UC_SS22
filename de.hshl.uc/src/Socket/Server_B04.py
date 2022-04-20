# Tcp Chat server

import socket, select
from _thread import *

CONNECTION_LIST = []
RECV_BUFFER = 4096  # Advisable to keep it as an exponent of 2
PORT = 1666
IP = '34.159.99.140'

server_socket = socket.socket(socket.AF_INET,
                              socket.SOCK_STREAM)

user_name_dict = {}
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def setup_connection():
    server_socket = socket.socket(socket.AF_INET,
                                  socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((socket.gethostname(), 1666))
    server_socket.listen(100)

    CONNECTION_LIST.append(server_socket)


setup_connection()


# Function to broadcast chat messages to all connected clients
def broadcast_data(sock, message):
    # Do not send the message to master socket and the client who has send us the message
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock:
            # if not send_to_self and sock == socket: return
            try:
                socket.send(message)
            except:
                # broken socket connection may be, chat client pressed ctrl+c for example
                socket.close()
                CONNECTION_LIST.remove(socket)


def send_data_to(sock, message):
    try:
        sock.send(message)
    except:
        # broken socket connection may be, chat client pressed ctrl+c for example
        socket.close()
        CONNECTION_LIST.remove(sock)


def client_connect():
    print("Chat server started on port " + str(PORT))
    while 1:
        # Get the list sockets which are ready to be read through select
        read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST, [], [])

        for sock in read_sockets:
            # New connection
            if sock == server_socket:
                # Handle the case in which there is a new connection recieved through server_socket
                setup_connection()
            # Some incoming message from a client
            else:
                # Data recieved from client, process it
                try:
                    # In Windows, sometimes when a TCP program closes abruptly,
                    # a "Connection reset by peer" exception will be thrown
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        if user_name_dict[sock].username is None:
                            set_client_user_name(data, sock)
                        else:
                            broadcast_data(sock, "\r" + '<' + user_name_dict[sock].username + '> ' + data)

                except:
                    #broadcast_data(sock, "Client (%s, %s) is offline" % addr)
                    #print("Client (%s, %s) is offline" % addr)
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue

    server_socket.close()


def set_client_user_name(data, sock):
    user_name_dict[sock].username = data.strip()
    send_data_to(sock, data.strip() + ', you are now in the chat room\n')
    send_data_to_all_regesterd_clents(sock, data.strip() + ', has joined the cat room\n')


def setup_connection():
    sockfd, addr = server_socket.accept()
    CONNECTION_LIST.append(sockfd)
    print("Client (%s, %s) connected" % addr)
    send_data_to(sockfd, "please enter a username: ")
    user_name_dict.update({sockfd: Connection(addr)})


def send_data_to_all_regesterd_clents(sock, message):
    for local_soc, connection in user_name_dict.iteritems():
        if local_soc != sock and connection.username is not None:
            send_data_to(local_soc, message)


client_connect()


class Connection(object):
    def __init__(self, address):
        self.address = address
        self.username = None



# print(str(socket.gethostname()))
# print('Server ready!')
# while True:
#    (client_socket, addr) = server_socket.accept()
#    print(client_socket.recv(2048), addr)
#    client_socket.send(bytes('Hey vom Server!', "utf8"))
# server_socket.send(client_socket.get)

# ct = client_thread(client_socket)
# ct.run
