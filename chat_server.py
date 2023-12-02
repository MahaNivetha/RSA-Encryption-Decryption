from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
import re
from RSA import decrypt
PORT_NUMBER = 5000
SIZE = 1024


hostName = gethostbyname( 'localhost' )


mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )

print ("Test server listening on port {0}\n".format(PORT_NUMBER))
client_public_key=''
while True:
        (data,addr) = mySocket.recvfrom(SIZE)
        data=data.decode()
        if data.find('public_key')!=-1: #client has sent their public key\
            
            public = (int(re.findall(r'\d+', data)[0]), int(re.findall(r'\d+', data)[1]))
            print('public key is : %d, %d'%(public[0],public[1]))
            
        else:
            cipher=int(data)
            print (str(cipher)+':')
            
            data_decoded= decrypt(public, cipher)
            print (data_decoded)
            #python2: print data ,
sys.ext()


