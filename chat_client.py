import sys
from socket import socket, AF_INET, SOCK_DGRAM, gethostbyname
from RSA import generate_keypair, encrypt, decrypt

SERVER_IP = gethostbyname('localhost')
PORT_NUMBER = 5000
SIZE = 1024

print("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))

mySocket = socket(AF_INET, SOCK_DGRAM)
message = 'hello'

p = 1297273
q = 1297651

public, private = generate_keypair(p, q)
message = 'public_key: %d %d' % (public[0], public[1])
mySocket.sendto(message.encode(), (SERVER_IP, PORT_NUMBER))

while True:
    message = input()
    message.join('\n')

    message_encoded = [str(encrypt(private, i)) for i in message]
    [mySocket.sendto(code.encode(), (SERVER_IP, PORT_NUMBER)) for code in message_encoded]

sys.exit()
