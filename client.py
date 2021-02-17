#!/usr/bin/env python3


input_string = 'Hello'
print(type(input_string))
input_bytes_encoded = input_string.encode()
print(type(input_bytes_encoded))
print(input_bytes_encoded)
output_string=input_bytes_encoded.decode()
print(type(output_string))
print(output_string)

import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224

def invia_comandi(sock_service):
    while True:
        try:
            dati = input("Inserisci i dati da inviare (0 per terminare la connessione): ")
        except EOFError:
            print("\nOkay. Exit")
            break
        if not dati:
            print("Non puoi inviare una stringa vuota!")
            continue
        if dati == '0':
            print("Chiudo la connessione con il server!")
            break
        
        dati = dati.encode()
        sock_service.send(dati)
        print("ti ho inviato ", dati)
        dati = sock_service.recv(2048)

        if not dati:

            print("Server non risponde. Exit")
            break
        
        
        dati = dati.decode()

        print("Ricevuto dal server:")
        print(dati + '\n')

    sock_service.close()
    

def connessione_server(address, port):
    sock_service = socket.socket()

    sock_service.connect((address, port))

    print("Connesso a " + str((address, port)))
    invia_comandi(sock_service)
    

if __name__=='__main__':
    connessione_server(SERVER_ADDRESS,SERVER_PORT)          