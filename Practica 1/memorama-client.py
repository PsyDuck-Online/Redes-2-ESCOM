import socket
import os

HOST = input("Ingrese una direccion IP destino: ")
PORT = int(input("Ingrese un numero de puerto valido: "))
buffer_size = 1024
casilla1 = ''
casilla2 = ''

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
    print("Conectando con el servidor...")
    clientSocket.connect((HOST,PORT))
    print("-Servidor conectado-")
    #DEFINIENDO DIFICULTAD
    dificultad = input("--MENU--\n1.- Facil\n2.- Dificil\nRespuesta: ")
    clientSocket.send(dificultad.encode('utf8'))
    os.system("cls")
    if dificultad == '1':
        limite = 3
    else:
        limite = 5
    
    while True:
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
            while True:
                casilla1 = input('Seleccione la casilla 1(x,y): ')
                aux = casilla1.split(',')
                if (int(aux[0]) <= limite) and (int(aux[1]) <= limite):
                    break
                
            clientSocket.send(casilla1.encode('utf8'))#ENVIA LA PRIMER TIRADA E3
            data = clientSocket.recv(buffer_size).decode('utf8')#R4 RECIBE EL TECLADO DESTAPADO DE LA TIRADA 1
            os.system('cls')
            print(data)
            while True:
                casilla2 = input('Seleccione la casilla 2(x,y): ')
                aux = casilla2.split(',')
                if (int(aux[0]) <= limite) and (int(aux[1]) <= limite):
                    break

            clientSocket.send(casilla2.encode('utf8'))#ENVIA LA SEGUNDA TIRADA E5
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