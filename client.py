import socket
import colorama 

userName = input("Enter your username(it will be visible to all in the chat)")
try:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.connect((socket.gethostname(),21000))
except: 
    print(Fore.red + 'Could not connect with the server')

welcomeMessage = serverSocket.recv(100)
print(welcomeMessage.decode("utf-8"))
serverSocket.send(bytes(userName, "utf-8"))
