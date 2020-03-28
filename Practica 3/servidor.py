import socket
import threading
import memorama
import logging
import time
import sys
import pickle

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )
MAIN_THREAD = threading.current_thread()

lista_conexiones = []
IP_SERV = input("Direccion del servidor: ")
PORT_SERV = int(input("Puerto: "))
address_server = (IP_SERV,PORT_SERV)

LIMITE_JUGADORES = int(input("Introduzca el numero total de jugadores: "))
dificultad = input("---DIFICULTAD--\n1.-Facil\n2.-Dificil\nEnter: ")
game = memorama.memorama(dificultad)

def cerrar_servidor(lista_conexiones):
    msg_to_all(lista_conexiones,'exit')
    msg_to_all(lista_conexiones,'exit')
    msg_to_all(lista_conexiones,'exit')

def msg_to_all(lista_conexiones,msg):
    for conexion in lista_conexiones:
        try:
            conexion.send('\n'.encode('utf-8'))
            conexion.send(msg.encode('utf-8'))
        except:
            lista_conexiones.remove(conexion)

def aceptar_jugadores(socket, lista_conexiones, LIMITE_JUGADORES, jugadores): #Acepta todas las conexiones necesarias
    id = 1
    nombre_jugador = 'JUGADOR '
    while len(lista_conexiones) < LIMITE_JUGADORES:
        try:
            conn, addr = socket.accept()
            print('Conectado a ',addr)
            jugador = memorama.memorama_jugador(nombre_jugador + str(id) + '->' + str(addr[0]))
            id += 1
            jugadores.append(jugador) #Se agrega a la lista objetos jugador con el nombre de la ip + port
            
            msg = 'Bienvenido: '+jugador.nombre+'\n'
            conn.send(msg.encode('utf-8'))

            lista_conexiones.append(conn)
            text = 'Jugadores conectados: '+str(len(lista_conexiones))+'/'+str(LIMITE_JUGADORES)
            msg_to_all(lista_conexiones=lista_conexiones, msg=text)
        except:
            pass

def manejo_jugadores(conn, jugador, lista_conexiones, game, condition):
    conn.send('---El JUEGO EMPEZO---'.encode('utf-8'))
    while True:
        logging.debug('Al empezar TURNO contador: '+ str(game.contador))
        with condition:

            if game.contador <= 0:
                condition.notify_all()
                break

            msg = game.get_hiddenBoard()
            conn.send(msg.encode('utf-8'))

            #Parte 1(Avisar que es turno del jugador activo)
            logging.debug('Comenzo su TURNO: ' + jugador.nombre)
            msg = 'Tu turno: '
            conn.send(msg.encode('utf-8'))

            #Parte 2(Recibe y evalua la respuesta del jugador)
            msg = conn.recv(1024).decode('utf-8')
            if msg == 'exit':
                msg = 'El jugador: ' + jugador.nombre + ' abandono el juego'
                msg_to_all(lista_conexiones,msg)
                cerrar_servidor(lista_conexiones)
                condition.notify_all()
                break
            msg = game.tirada(msg,jugador)

            #Parte 3(Enviar el tablero actualizado)
            conn.send(msg.encode('utf-8'))
            logging.debug('El tablero queda: \n'+game.get_hiddenBoard())
            logging.debug('Al terminar TURNO contador: '+ str(game.contador))
            logging.debug('Termino su TURNO')
            condition.notify_all()
            condition.wait()

if __name__ == "__main__":
    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_server.bind(address_server)
    socket_server.listen(LIMITE_JUGADORES)

    jugadores = [] #Lista de objetos tipo memorama.memorama_jugador

    condition = threading.Condition()
    threads_jugadores = []
    
    print('Esperando conexiones')
    aceptar_jugadores(socket_server,lista_conexiones,LIMITE_JUGADORES, jugadores)
    try:
        id = 0
        for conn in lista_conexiones:
            threads_jugadores.append(threading.Thread(target=manejo_jugadores, args=(conn,jugadores[id], lista_conexiones, game, condition)).start())
            id += 1

        for t in threading.enumerate():
            if t is not MAIN_THREAD:
                t.join()
    except:
        print('Hubo un error al crear hilos')
    print('El juego TERMINO')

    #Ordenamiento de los jugadores
    marcador = sorted(jugadores, key=lambda objeto: objeto.puntuacion, reverse=True)
    msg = '\n----PUNTUACION FINAL----\n'
    posicion = 1
    for jugador in marcador:
        msg = msg +  str(posicion) + ')' + jugador.nombre + ' con ' + str(jugador.puntuacion) + '\n'
        posicion += 1
    
    msg_to_all(lista_conexiones, msg)
    print(msg)
    cerrar_servidor(lista_conexiones)
    socket_server.close()