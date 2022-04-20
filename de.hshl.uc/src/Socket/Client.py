import socket

client_socket = socket.socket(socket.AF_INET,
                              socket.SOCK_STREAM)
server_adr = ('34.159.99.140', 1666)
client_socket.connect(server_adr)
print(str(socket.gethostname()))
client_socket.send(bytes('Hi Marvin', "utf8"))

print(client_socket.recv(2048))

