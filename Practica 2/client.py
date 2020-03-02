#cliente
import socket
import threading
import os

host = input("Inserte ip: ")
port = int(input("Inserte el puerto: "))
os.system('cls')

def escucharSiempre(conn):
    while True:
        datos = conn.recv(1024)
        if datos:
            print(datos.decode('utf8'))


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((host,port))
    
    datos = s.recv(1024)
    print(datos.decode('utf8'))
    datos = s.recv(1024)
    print(datos.decode('utf8'))
    while True:
        threading.Thread(target=escucharSiempre, args=(s,)).start()
        message = input()
        message = message
        s.send(message.encode('utf8'))
        if message == 'quit':
            print("bye")
            break
        