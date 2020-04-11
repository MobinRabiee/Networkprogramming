import socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
server_address = (host , port)
try:
    client_socket.connect(server_address)
    print("connection established . . . . . .")
    message = "this message is an echo message"
    client_socket.send(message.encode('ascii'))
    recv_message = client_socket.recv(1024)
    print("this message recived from server : %s"%str(recv_message))
except Exception as e:
    print(str(e))
finally:
    client_socket.close()
