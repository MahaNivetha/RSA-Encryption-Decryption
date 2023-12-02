from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
from RSA import decrypt

PORT_NUMBER = 5000
SIZE = 1024

hostName = gethostbyname('localhost')

mySocket = socket(AF_INET, SOCK_DGRAM)
mySocket.bind((hostName, PORT_NUMBER))

print("Test server listening on port {0}\n".format(PORT_NUMBER))
client_public_key = ''

while True:
    data, addr = mySocket.recvfrom(SIZE)
    data = data.decode()

    if 'public_key' in data:
        # Client has sent their public key
        public = tuple(map(int, re.findall(r'\d+', data)))
        print('Public key is: %d, %d' % (public[0], public[1]))

    else:
        cipher = int(data)
        print(str(cipher) + ':')

        data_decoded = decrypt(public, cipher)
        print(data_decoded)
        # python2: print data ,
