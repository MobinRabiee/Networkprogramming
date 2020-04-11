import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
server_address = (host,port)
server_socket.bind(server_address)
print("server socket object %s %s"%server_address)
server_socket.listen(5)

while True :
        client_socket , addr = server_socket.accept()
        print("connection accepted from %s " %str(addr))
        try:
            message = client_socket.recv(1024)
            string = "dear client "+str(addr)+" your message is "
            message = string.encode('ascii')+message
            client_socket.sendall(message)
        except Exception as e:
            client_socket.sendall(str(e))
        finally:
            client_socket.close()
