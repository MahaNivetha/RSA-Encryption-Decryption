# RSA-Encryption-Decryption

# UDP Communication with RSA Encryption/Decryption

This repository contains Python scripts for a simple client-server communication using UDP sockets with RSA encryption/decryption. The communication is secured by encrypting and decrypting the messages exchanged between the client and the server using the RSA algorithm.

## Files

1. **server.py:**
   - Server script that listens for messages from the client.
   - Receives the client's public key and decrypts encrypted messages.

2. **client.py:**
   - Client script that sends messages to the server.
   - Generates RSA key pairs, sends the public key to the server, and encrypts messages before sending.

3. **RSA.py:**
   - Python script containing functions for RSA key pair generation, encryption, and decryption.

## Instructions

1. **Run Server:**
   - Execute the `server.py` script to start the server.
   - The server listens for incoming messages from the client.

2. **Run Client:**
   - Execute the `client.py` script to start the client.
   - The client generates RSA key pairs, sends the public key to the server, and allows the user to input messages to be encrypted and sent to the server.

3. **Encryption/Decryption:**
   - The messages sent between the client and the server are encrypted using RSA encryption on the client side and decrypted on the server side.
   - The server outputs the decrypted message received from the client.

4. **Note:**
   - The prime numbers `p` and `q` used for key pair generation are set in the `client.py` and `server.py` scripts.
   - Adjust the values of `p` and `q` based on your requirements.

## Dependencies

- Python 3.x
