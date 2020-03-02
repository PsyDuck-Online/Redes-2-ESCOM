import random
class memorama:
    t1 = ''
    t2 = ''
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

    def turno_jugador(self,socket,jugador):
        socket.send('4'.encode('utf8')) #E1 ENVIA QUE ES EL TURNO DEL JUGADOR
        socket.recv(1024).decode('utf8')
        self.enviar_tablero(socket)#E2 ENVIA EL TABLERO ACTUAL
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
    def tirada1(self,tirada):
        self.t1 = tirada
        x1 = int(tirada[0])
        y1 = int(tirada[1])
        self.tablero_oculto[x1][y1] = self.tablero[x1][y1]
    def tirada2(self,tirada):
        self.t2 = tirada
        x1 = int(tirada[0])
        y1 = int(tirada[1])
        self.tablero_oculto[x1][y1] = self.tablero[x1][y1]
    def validacion_global(self):
        if self.tablero[int(self.t1[0])][int(self.t1[1])] != self.tablero[int(self.t2[0])][int(self.t2[1])]:
            self.tablero_oculto[int(self.t1[0])][int(self.t1[1])] = '*'
            self.tablero_oculto[int(self.t2[0])][int(self.t2[1])] = '*'

