from socket import*

HOST = '127.0.0.1'
PORT = 5000

client = socket(AF_INET, SOCK_STREAM)
client.connect((HOST, PORT))

while 1:
    msg = input('Digite: ')
    client.send(msg.encode())