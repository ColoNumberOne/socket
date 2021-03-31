#!/usr/bin/env python3
import socket
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224
sock_listen = socket.socket()
sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock_listen.bind((SERVER_ADDRESS, SERVER_PORT))
sock_listen.listen(5)
print("Server in ascolto su %s." %str((SERVER_ADDRESS, SERVER_PORT)))

protocollo = ["SYN", "SYN + ACK", "ACK + DATA", "ACK for Data"]
while True:
    sock_service, addr_client = sock_listen.accept()
    print("\nConnessione ricevuta da " + str(addr_client)) #finché la connesione esiste allora il server rimane in attes adi ricevere i dati 
    print("\nAspetto di ricevere i dati ")
    contConn=0
    while True:
        dati = sock_service.recv(2048) #riceve i dati
        contConn+=1
        if not dati:
            print("Fine dati dal client. Reset")
            break
            
        dati = dati.decode()
        print("Ricevuto: '%s'" % dati)
        if dati=='0':
            print("Chiudo la connessione con " + str(addr_client)) #se non riceviamo i dati la connnesione viene chiusa 
            break
        dati = "Risposta a : " + str(addr_client) + ". Il valore del contatore è : " + str(contConn) #stampiamo alla fine i dati che ci sono arrivati

        dati = dati.encode()

        sock_service.send(dati)
    sock_service.close()