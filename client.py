from os import write
import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MSG = 'DISCONNECT'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)


nickname = input('choose a nickname: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def receive():
    while True:
        try:
            msg = client.recv(HEADER).decode('ascii')
            if msg == "NICK":
                client.send(nickname.encode('ascii'))
            else:
                print(msg)
        except:
            print('Error')
            client.close()
            break

def write():
    while True:
        msg = f'{nickname}: {input("")}'
        client.send(msg.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

