#!/usr/bin/env python3
import socket



SERVER_ADDRESS = '127.0.0.1'

SERVER_PORT = 22224

sock_listen = socket.socket()

sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock_listen.bind((SERVER_ADDRESS, SERVER_PORT))

sock_listen.listen(5)

print("Server in ascolto su %s." % str((SERVER_ADDRESS, SERVER_PORT)))


while True:
    sock_service, addr_client = sock_listen.accept()
    print("\nConnessione ricevuta da " + str(addr_client))
    print("\nAspetto di ricevere i dati ")
    contConn=0
    while True:
        dati = sock_service.recv(2048)
        contConn+=1
        if not dati:
            print("Fine dati dal client. Reset")
            break
        
        dati = dati.decode()
        print("Ricevuto: '%s'" % dati)
        if dati=='0':
            print("Chiudo la connessione con " + str(addr_client))
            break

        op,n1,n2 = dati.split(";")

        print(op)
        print(n1)
        print(n2)

        if (op=="piu"):
            risultato= float(n1)+float(n2)
            
        elif(op=="meno"):
            risultato=float(n1)-float(n2)
            
        elif(op=="per"):
            risultato=float(n1)*float(n2)
            
        elif(op=="diviso"):
            risultato=float(n1)/float(n2)

        print(risultato)
        
        dati = "Il risultato dell'operazione : " + str(n1) + " " + str(op) + " " + str(n2) + " = " + str(risultato)

        dati = dati.encode()

        sock_service.send(dati)

    sock_service.close()