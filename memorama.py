import random
import os
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
    def mostrar_tablero(self):
        for i in self.tablero_oculto:
            print(i)

    def tirada(self, jugador):
        while True and self.cont != 0:
            while True:
                try:
                    self.mostrar_puntuacion()
                    print("TURNO DE: {}\n\n".format(jugador.nombre))
                    self.mostrar_tablero()
                    x1 = x2 = int(input("x1: "))
                    y1 = y2 = int(input("y1: "))
                    if self.tablero_oculto[x1][y1] != '*':
                        x1 = int("/")
                    self.tablero_oculto[x1][y1] = self.tablero[x1][y1]
                    break
                except ValueError:
                    os.system("cls")
                    print("Valor no valido.")
                except IndexError:
                    os.system("cls")
                    print("El tablero no es tan grande")

            while ((x1 == x2) and (y1 == y2)):
                os.system("cls")
                while True:
                    try:
                        self.mostrar_puntuacion()
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

    def mostrar_puntuacion(self):
        print("##### PUNTUACION #####\n{}: {} puntos\n{}: {} puntos\n######################".format(player.nombre,player.puntos,pc.nombre,pc.puntos))

    def tirada_pc(self, jugador):
        while True and self.cont != 0:
            while True:
                try:
                    if self.dificultad == 1:
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
                        if self.dificultad == 1:
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
            self.mostrar_puntuacion()
            print("TURNO DE: {}\n\n".format(jugador.nombre))
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
            




if __name__ == "__main__":
    os.system("cls")
    mi_juego = memorama(int(input("Introduzca la dificultad\n1.- Facil\n2.- Dificil\nEntrada: ")))
    pc = jugador("computadora")
    player = jugador(input("Introdcue tu nombre: "))
    i = 1
    while mi_juego.cont > 0:
        os.system("cls")
        i = 1 - i
        if i == 0:
            mi_juego.tirada(player)
        elif i == 1:
            mi_juego.tirada_pc(pc) 
    if player.puntos > pc.puntos:
        print("###### {} gana ######\n".format(player.nombre))
        mi_juego.mostrar_puntuacion()
        mi_juego.mostrar_tablero()
    elif player.puntos < pc.puntos:
        print("###### {} gana ######\n".format(pc.nombre))
        mi_juego.mostrar_puntuacion()
        mi_juego.mostrar_tablero()
    else:
        print("###### FUE EMPATE ######\n")
        mi_juego.mostrar_puntuacion()
        mi_juego.mostrar_tablero()
    