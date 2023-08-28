import socket 


HOST = socket.gethostbyname(socket.gethostname())
PORT = 6969


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen()


while True: 
    conn, addr = server.accept()
    print(f"CONNECTED TO {addr}")
    msg = conn.recv(1024 * 3).decode('utf-8')
    print(f"CLIENT : {msg}")
    conn.send(f"RECIEVED MESSAGE FROM {addr} ".encode('utf-8'))
    conn.close()
    print(f"CONNECTION WITH {addr} ENDED.")