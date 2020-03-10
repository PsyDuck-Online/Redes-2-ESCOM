#Actividad Lector-escritor con restriccion
#Author: David Baltazar Real

import logging
import random
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

dato = ''

def Lector(lock):
    global dato 
    logging.debug('intentando acceder')
    cont = 5
    #pause = random.random()*2
    #time.sleep(pause)
    intentos = 0
    while cont:
        time.sleep(random.random()*3)
        entro = lock.acquire(0)   
        try: 
            intentos += 1 
            if entro:
                #logging.debug('Lock abierto, accediendo a la VARIABLE despues de %d intentos',intentos)
                logging.debug('leyendo VARIABLE: %s', dato)
                cont -= 1
                logging.debug('cont: %s',cont)
            else:
                pass
                #logging.debug('Lock cerrado, volviendo a intentar')                       
        finally:
            if entro:
                lock.release()
    logging.debug('Cerrando proceso')
def Escritor(lock,barrera):
    global dato
    pause = 1
    time.sleep(pause)
    id_escritor = barrera.wait()
    logging.debug('intentando acceder')
    cont = 3
    intentos = 0
    while cont:
        time.sleep(random.random()*3)
        entro = lock.acquire(0)
        try: 
            intentos += 1 
            if entro:
                pause = random.random()*3+1
                logging.debug('Lock abierto, accediendo a la VARIABLE despues de %d intentos (durmiendo %d)',intentos,pause)
                dato = dato+' | ' + str(threading.current_thread().name)
                time.sleep(pause)  
                cont -= 1
            else:
                logging.debug('Lock cerrado, volviendo a intentar')                       
        finally:
            if entro:
                lock.release()
                #logging.debug('Dejo de usar la VARIABLE (%s)',dato)
                time.sleep(random.random()*4)
    logging.debug('Cerrando proceso')

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s): %(message)s',
)
if __name__ == "__main__":
    lock = threading.Lock()
    barrera = threading.Barrier(3)
    for i in range(3):
        lectores=threading.Thread(name='Lector '+str(i+1), target=Lector, args=(lock,))
        if i < 3:
            escritores=threading.Thread(name='Escritor '+str(i+1),target=Escritor,args=(lock,barrera))
        escritores.start()
        lectores.start()

    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()
