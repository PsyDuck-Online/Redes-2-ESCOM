import socket
import random
import os
import time
import struct

class jugador:
    puntos = 0
    def __init__(self,nombre):
        self.nombre = nombre

class memorama:
    def __init__(self, dificultad):
        self.dificultad = dificultad
        if dificultad == "1":
            self.tablero = [['arbol','casa','casa','escom'],
            ['redes','aplicaciones','aplicaciones','arbol'],
            ['clase','redes','clase','palabras'],
            ['escom','palabras','interfaz','interfaz']]
            self.tablero_oculto = [['*','*','*','*'],
            ['*','*','*','*'],
            ['*','*','*','*'],
            ['*','*','*','*']]
            self.cont = 8
            print("Dificultad principiante")
        elif dificultad == "2":
            self.tablero = [['arbol','escom','palabras','comunicaciones','internet','computadora'],
            ['python','tecnologias','tecnologias','interfaz','clase','arbol'],
            ['TCP','UDP','computadora','interfaz','clase','casa'],
            ['datagrama','IP','telefono','telefono','casa','palabras'],
            ['comunicaciones','TCP','IP','redes','aplicaciones','aplicaciones'],
            ['python','UDP','datagrama','internet','redes','escom']]
            self.tablero_oculto = [['*','*','*','*','*','*'],
            ['*','*','*','*','*','*'],
            ['*','*','*','*','*','*'],
            ['*','*','*','*','*','*'],
            ['*','*','*','*','*','*'],
            ['*','*','*','*','*','*']]
            self.cont = 18
            print("Dificultad avanzada")
        else:
            print("Es otra cosa rara: ",dificultad)
    def mostrar_tablero(self):
        for i in self.tablero_oculto:
            print(i)
    """
    def tirada(self, jugador,tirada_1,tirada_2):
        error = False
        while True and self.cont != 0:
            while True:
                try:
                    print("TURNO DE: {}\n\n".format(jugador.nombre))
                    self.mostrar_tablero()
                    x1 = x2 = int(tirada_1[0])
                    y1 = y2 = int(tirada_2[1])
                    if self.tablero_oculto[x1][y1] != '*':
                        x1 = int("/")
                    self.tablero_oculto[x1][y1] = self.tablero[x1][y1]
                    break
                except ValueError:
                    os.system("cls")
                    print("Valor no valido.")
                    error = True
                except IndexError:
                    os.system("cls")
                    print("El tablero no es tan grande")
                    error = True

            while ((x1 == x2) and (y1 == y2)):
                os.system("cls")
                if error:
                    break
                while True:
                    try:
                        print("TURNO DE: {}\n\n".format(jugador.nombre))
                        self.mostrar_tablero()
                        x2 = int(input("x2: "))
                        y2 = int(input("y2: "))
                        if self.tablero_oculto[x2][y2] != '*':
                            x2 = int("/")
                        self.tablero_oculto[x2][y2] = self.tablero[x2][y2]
                        break
                    except ValueError:
                        os.system("cls")
                        print("Valor introducido no valido")
                    except IndexError:
                        os.system("cls")
                        print("El tablero no es tan grande")
            self.mostrar_tablero()
            if self.tablero[x1][y1] != self.tablero[x2][y2]:
                self.tablero_oculto[x1][y1] = '*'
                self.tablero_oculto[x2][y2] = '*'
                break
            else:
                self.cont -= 1
                jugador.puntos += 1
                os.system("cls")
        input("Enter para continuar")
    
    def tirada(self,jugador,tirada):
        try:
            x = int(tirada[0])
            y = int(tirada[1])
            if self.tablero_oculto[x][y] != '*':
                        x = int("/")
            self.tablero_oculto[x][y] = self.tablero[x][y]
        except ValueError:
            print("Casilla ya descubierta")
            
    def turno(self,jugador, conn):
        tirada1 = tirada2 = ''
        while True:
            tirada1 = Client_conn.recv(1024).decode('utf8').split(',')
            if tirada1:
                break
        self.tirada(jugador,tirada1)
        enviar_tablero(conn,game)
        while True:
            tirada2 = Client_conn.recv(1024).decode('utf8').split(',')
            if tirada2:
                break
        self.tirada(jugador,tirada2)
        enviar_tablero(conn,game)
        if self.tablero[int(tirada1[0])][int(tirada1[1])] != self.tablero[int(tirada2[0])][int(tirada2[1])]:
            self.tablero_oculto[int(tirada1[0])][int(tirada1[1])] = '*'
            self.tablero_oculto[int(tirada2[0])][int(tirada2[0])] = '*'
        else:
            self.cont -= 1
            jugador.puntos += 1
        enviar_tablero(conn,game)

    def mostrar_puntuacion(self, player, pc):
        print("##### PUNTUACION #####\n{}: {} puntos\n{}: {} puntos\n######################".format(player.nombre,player.puntos,pc.nombre,pc.puntos))
"""
    def turno_jugador(self,socket,jugador):
        socket.send('4'.encode('utf8')) #E1 ENVIA QUE ES EL TURNO DEL JUGADOR
        socket.recv(1024).decode('utf8')
        game.enviar_tablero(Client_conn)#E2 ENVIA EL TABLERO ACTUAL
        tirada1 = socket.recv(1024).decode('utf8').split(',')#R3 RECIBE LA PRIMER TIRADA
        print("TIRADA 1")
        x1 = int(tirada1[0])
        y1 = int(tirada1[1])
        self.tablero_oculto[x1][y1] = self.tablero[x1][y1]
        self.enviar_tablero(socket)#E4 ENVIA EL TABLERO DESTAPANDO LA PRIMER CASILLA
        tirada2 = socket.recv(1024).decode('utf8').split(',')#R5 RECIBE LA SEGUNDA TIRADA
        print("TIRADA 2")
        x2 = int(tirada2[0])
        y2 = int(tirada2[1])
        self.tablero_oculto[x2][y2] = self.tablero[x2][y2]
        self.enviar_tablero(socket)#E6 ENVIA EL TABLERO DESTAPANDO LA SEGUNDA CASILLA

        if self.tablero[x1][y1] != self.tablero[x2][y2]:
            self.tablero_oculto[x1][y1] = '*'
            self.tablero_oculto[x2][y2] = '*'
        else:
            self.cont -= 1
            jugador.puntos += 1
        socket.recv(1024).decode('utf8')#R7 RECIVE CUALQUIER COSA PARA ENVIAR EL RESULTADO
        self.enviar_tablero(socket)#E8 ENVIA EL TABLERO CON EL RESULTADO (DESTAPADO SI SON IGUALES O TAPANDO SI SON DIFERENTES)
        socket.recv(1024).decode('utf8')#R9 RECIBE CUALQUIER COSA PARA TERMINAR EL TURNO
        print("Termina el turno")
        

    def tirada_pc(self, jugador, conn):
        while True and self.cont != 0:
            while True:
                try:
                    if self.dificultad == "1":
                        x1 = x2 = random.randrange(0,4)
                        y1 = y2 = random.randrange(0,4)
                    else:
                        x1 = x2 = random.randrange(0,5)
                        y1 = y2 = random.randrange(0,5)
                    if self.tablero_oculto[x1][y1] != '*':
                        x1 = int("/")
                    self.tablero_oculto[x1][y1] = self.tablero[x1][y1]
                    break
                except ValueError:
                    pass
                except IndexError:
                    pass

            while ((x1 == x2) and (y1 == y2)):
                while True:
                    try:
                        if self.dificultad == "1":
                            x2 = random.randrange(0,4)
                            y2 = random.randrange(0,4)
                        else:
                            x2 = random.randrange(0,6)
                            y2 = random.randrange(0,6)
                        if self.tablero_oculto[x2][y2] != '*':
                            x2 = int("/")
                        self.tablero_oculto[x2][y2] = self.tablero[x2][y2]
                        break
                    except ValueError:
                        pass
                    except IndexError:
                        pass
            conn.send('3'.encode('utf8'))#ENVIA QUE ES UNA TIRADA DE LA PC E1
            conn.recv(1024).decode('utf8')
            self.enviar_tablero(conn)#ENVIA EL TABLERO DESPUES DE LA TIRADA DE LA PC E2
            conn.recv(1024) #ESPERA A RECIBIR CUALQUIER COSA PARA ENVIAR EL RESULTADO (DESPUES DE LA COMPARACION) R3
            if self.tablero[x1][y1] != self.tablero[x2][y2]:
                self.tablero_oculto[x1][y1] = '*'
                self.tablero_oculto[x2][y2] = '*'
                break
            else:
                self.cont -= 1
                jugador.puntos += 1
            self.enviar_tablero(conn) #ENVIA EL TABLERO CON EL RESULTADO E4
            print('tirada pc')


    def enviar_tablero(self,socket_oirgen):
        text = self.tablero_oculto.__str__().replace('], [','\n').replace('[[','').replace(']]','')
        socket_oirgen.send(text.encode('utf8'))



if __name__ == "__main__":
    HOST = "10.100.68.67" #input("Insertar IP del servidor: ")
    PORT = 65432#int(input("Inserte el PUERTO: "))
    buffer_size = 8
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
        serverSocket.bind((HOST, PORT))
        while True:
            serverSocket.listen() #Estado SYN RCVD, mensaje SYN, ACK.
            print("El servidor MEMORAMA está disponible y en espera de solicitudes")

            Client_conn, Client_addr = serverSocket.accept() #Estado Established, mensaje SYN, ACK
            with Client_conn:
                pc = jugador("pc")
                player = jugador("player")
                print("Conectado a", Client_addr)
                #definiendo dificultad
                data = Client_conn.recv(1024).decode('utf8') 
                #Creando juego
                game = memorama(data)
                #game.mostrar_tablero()
                i = 1
                while game.cont:
                    i = 1 - i
                    if i == 0:
                        #TIRA EL JUGADOR
                        print('jugador: {}'.format(player.puntos))
                        game.turno_jugador(Client_conn,player)
                    else:
                        #TIRA LA PC
                        print('pc: {}'.format(pc.puntos))
                        game.tirada_pc(pc, Client_conn)
                if player.puntos > pc.puntos:
                    Client_conn.send('1'.encode('utf8'))
                else:
                    Client_conn.send('2'.encode('utf8'))
                
                """
                while True:
                    pass
                    
                    print("Esperando a recibir datos... ")
                    data = Client_conn.recv(buffer_size)
                    print ("Recibido,", data,"   de ", Client_addr)
                    if not data:
                        break
                    print("Enviando respuesta a", Client_addr)
                    Client_conn.sendall(data)
                    """