import socket

server_socket = socket.socket(socket.AF_INET,
                              socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 1337))
server_socket.listen(1)
while True:
    (client_socket, addr) = server_socket.accept()
    print(client_socket.recv(2048), addr)


    # ct = client_thread(client_socket)
    # ct.run
