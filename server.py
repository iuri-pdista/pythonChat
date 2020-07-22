import socket
import colorama
try:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((socket.gethostname(),21000))
    serverSocket.listen(3)
except:
    print("Could not establish the server")

while True:
    try:
        clientsocket, address = serverSocket.accept()
        print(f"Connection from {address} has been established")
        clientsocket.send(bytes("W&LC0M3 T0 T#& C#H4T", "utf-8"))
        clientName = clientsocket.recv(15)
        print(f"The address: {address} joined the server as: {clientName}")
    except:
        print(Fore.red + 'Failed to connect with client ;-;(')
    clientsocket.close()
serverSocket.close()


