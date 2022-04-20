import socket

client_socket = socket.socket(socket.AF_INET,
                              socket.SOCK_STREAM)
server_adr = ('127.0.0.1', 1337)
client_socket.connect(server_adr)
client_socket.send(bytes('Hi', "utf8"))

