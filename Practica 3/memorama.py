class memorama:
    def __init__(self, dificultad):
        self.dificultad = dificultad
        if self.dificultad == "1":
            self.tablero = [['arbol','casa','casa','escom'],
            ['redes','aplicaciones','aplicaciones','arbol'],
            ['clase','redes','clase','palabras'],
            ['escom','palabras','interfaz','interfaz']]
            self.tablero_oculto = [['*','*','*','*'],
            ['*','*','*','*'],
            ['*','*','*','*'],
            ['*','*','*','*']]
            self.contador = 8
        elif self.dificultad == "2":
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
            self.contador = 18

    def get_board(self,board):
        return '\n----------\n' + board.__str__().replace('], [','\n').replace('[[','').replace(']]','') + '\n----------\n'

    def get_hiddenBoard(self):
        return self.get_board(self.tablero_oculto)

    def casilla_en_tablero(self, casilla):
        if self.dificultad == 1:
            if (casilla[0] > 3) or (casilla [1] > 3):
                return False
        else:
            if (casilla[0] > 5) or (casilla[1] > 5):
                return False
        return True
    
    def casillas_diferentes(self,casilla1,casilla2):
        if casilla1 == casilla2:
            return False
        else:
            return True

    def casilla_disponible(self, casilla):
        if self.tablero_oculto[casilla[0]][casilla[1]] == '*':
            return True
        else:
            return False

    def tirada(self, tirada, jugador):
        casillas = tirada.split("/")

        #Cambia el formato de las tiradas de 'x1,y1/x2,y2' -> [x1,y1] & [x2,y2]
        casilla1 = casillas[0].split(',')

        for i in casilla1:
            if not(i.isdigit()):
                return self.get_hiddenBoard()

        casilla1[0] = int(casilla1[0])
        casilla1[1] = int(casilla1[1])
        x1 = casilla1[0]
        y1 = casilla1[1]

        casilla2 = casillas[1].split(',')

        for i in casilla2:
            if not(i.isdigit()):
                return self.get_hiddenBoard()

        casilla2[0] = int(casilla2[0])
        casilla2[1] = int(casilla2[1])
        x2 = casilla2[0]
        y2 = casilla2[1]

        #Valida que las casillas esten dentro del rango y sean validas
        if (self.casilla_en_tablero(casilla1)) and (self.casilla_en_tablero(casilla2)):
            pass
        else:
            return self.get_hiddenBoard()
        if self.casillas_diferentes(casilla1,casilla2):
            pass
        else: 
            return self.get_hiddenBoard()
        if self.casilla_disponible(casilla1) and self.casilla_disponible(casilla2):
            pass
        else:
            return self.get_hiddenBoard()

        #Compara el contenido de las casillas y devuelve un resultado
        if self.tablero[x1][y1] == self.tablero[x2][y2]:
            print('\nValores iguales\n')
            self.tablero_oculto[x1][y1] = self.tablero[x1][y1]
            self.tablero_oculto[x2][y2] = self.tablero[x2][y2]
            self.contador -= 1
            jugador.puntuacion += 1
            return self.get_hiddenBoard()
        else:
            print('\nValores diferentes\n')
            tablero_auxiliar = [x[:] for x in self.tablero_oculto]
            tablero_auxiliar[x1][y1] = self.tablero[x1][y1]
            tablero_auxiliar[x2][y2] = self.tablero[x2][y2]
            return self.get_board(tablero_auxiliar)

class memorama_jugador:
    def __init__(self,nombre):
        self.puntuacion = 0
        self.nombre = nombre
