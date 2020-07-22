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
try:    
    while True:
        recvMessage = serverSocket.recv(1024)
        if len(recvMessage) != 0:
            print(recvMessage.decode("utf-8"))
        else:
            print("No message was recieved")
        sendMessage = input()
        serverSocekt.send(bytes(sendMessage,"utf-8"))
except:
    print("Lost connection with server")
