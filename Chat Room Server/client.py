import socket
import threading

PORT = 8000
##########################################
# ENTER YOUR SERVER IP ADDRESS
SERVER = ""
##########################################
nickname = input("Choose a nickname: ")
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break
        
def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode("ascii"))
    
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
