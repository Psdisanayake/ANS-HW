import socket

IP = "127.0.0.1"  #lopback
PORT = 8091
AMT_DATA = 64

#socket created

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySocket:
    mySocket.bind((IP, PORT)) #bind()

    mySocket.listen()

    conn, addr = mySocket

    with conn:
        print("Conected by: ", addr)
        while True:
            data = conn.recv(AMT_DATA)
            if not data:
                break
                conn.sendall(data)



