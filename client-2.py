import socket

HEADER = 64
PORT = 8098
SERVER = "192.168.1.7"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNET_MSG  = " diconctd"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def Client_send(message):
    message = message.encode(FORMAT)
    length_msg = len(message)
    length_send = str(length_msg).encode(FORMAT)
    length_send += b' ' * (HEADER - len(length_send))
    client.send(length_send)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

Client_send("test ")
input()
Client_send("test1 ")
input()
Client_send("test2 ")

Client_send(DISCONNET_MSG)