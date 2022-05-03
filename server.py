from socket import*

HOST = 'localhost'
PORT = 5000

server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
print('Aguardando conexão....')

while 1:
  conn, adr = server.accept()
  while 1:
    msg = conn.recv(1024)
    print(msg.decode())