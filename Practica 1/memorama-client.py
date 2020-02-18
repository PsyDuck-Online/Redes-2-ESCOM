import socket
import os

HOST = "192.168.100.20"#input("Ingrese una direccion IP destino: ")
PORT = 65432#int(input("Ingrese un numero de puerto valido: "))
buffer_size = 1024


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
    print("Conectando con el servidor...")
    clientSocket.connect((HOST,PORT))
    print("-Servidor conectado-")
    #DEFINIENDO DIFICULTAD
    clientSocket.send(input("--MENU--\n1.- Facil\n2.- Dificil\nRespuesta: ").encode('utf8'))
    os.system("cls")
    
    while True:
        #TURNO DEL JUGADOR
        data = clientSocket.recv(buffer_size).decode('utf8') #R1 RECIBE LA OPCION
        if data == '1' or data == '2':
            break
        elif data == '3':
            clientSocket.send('blowjob4'.encode('utf8'))
            data = clientSocket.recv(buffer_size).decode('utf8') #R2 RECIBE EL TABLERO CON LA TIRADA DE LA PC
            print(data)
            input('Presione enter...')
            os.system('cls')
            clientSocket.send('blowjob3'.encode('utf8')) #E3
            #data = clientSocket.recv(buffer_size).decode('utf8') #R4 RECIBE EL TABLERO 
            #print(data)
            
        elif data=='4':
            print('---Tu turno---')
            clientSocket.send('blowjob4'.encode('utf8'))
            print('Turno del jugador\n\n')
            data = clientSocket.recv(buffer_size).decode('utf8') #R2 RECIBE EL TABLERO ACTUAL
            print(data)
            clientSocket.send(input('Seleccione la casilla 1(x,y): ').encode('utf8'))#ENVIA LA PRIMER TIRADA E3
            data = clientSocket.recv(buffer_size).decode('utf8')#R4 RECIBE EL TECLADO DESTAPADO DE LA TIRADA 1
            os.system('cls')
            print(data)
            clientSocket.send(input('Seleccione la casilla 2(x,y): ').encode('utf8'))#ENVIA LA SEGUNDA TIRADA E5
            data = clientSocket.recv(buffer_size).decode('utf8')#R6 RECIBE EL TECLADO DESTAPADO DE LA SEGUNDA TIRADA
            os.system('cls')
            print(data)
            input('Presione enter..')
            clientSocket.send('kkk'.encode('utf8')) #E7 ENVIA CUALQUIER COSA PARA QUE PUEDA RECIBIR EL RESULTADO
            os.system('cls')
            data = clientSocket.recv(buffer_size).decode('utf8')#R8 RECIBE EL TABLERO CON EL RESULTADO
            print(data)
            input("Enter para continuar TURNO..")
            clientSocket.send("blowjob".encode('utf8'))#E9 ENVIA CUALQUIER COSA PARA CONTINUAR EL TURNO
            os.system("cls")


    if data == '1':
        print("!!!EL JUGADOR GANA!!!!")
    else:
        print("LA COMPUTADORA GANA :(")