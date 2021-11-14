import socket 
# Allows us to seperate code out 
import threading



HEADER = 64
PORT = 5050
#This will get the IP address automatically from whatever computer it is running it.
SERVER = socket.gethostbyname(socket.gethostname())
#Address that is in a tuple
ADDR = (SERVER, PORT)
DISCONNECT_MSG = 'DISCONNECT'

#Created our socket.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#We bounded the socket with our ADDR
server.bind(ADDR)
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

#Handles the communication from the client and server
def handle_client(client):
    while True:
        try:
            msg = client.recv(HEADER)
            broadcast(msg)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break

#Starts new connections
def start():
    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')

        #Tells the user that we need their Nickname.
        client.send('NICK'.encode('ascii'))
        #Recieves what the client will send the server
        nickname = client.recv(HEADER).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}!')
        broadcast(f'{nickname} joined the chat!'.encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))
        
        #Run a thread for each client so we can run multiple clients at the same time.
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

        print(f'[ACTIVE CONNECTIONS] {threading.active_count() - 1}')


print("[STARTING] server is starting...")
start()