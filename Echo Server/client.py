import socket


HOST = socket.gethostbyname(socket.gethostname())
PORT = 6969

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

msg = input("Type your message: ")
socket.send(msg.encode('utf-8'))