import logging
import random
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )


def Lector(lock):
    logging.debug('intentando acceder')
    pause = random.random()+2
    time.sleep(pause)
    intentos = 0
    while True:
        entro = lock.acquire(0)
        time.sleep(2)
        try: 
            intentos += 1 
            if entro:
                logging.debug('Lock abierto, accediendo a la BD despues de %d intentos',intentos)
                time.sleep(3)   
            else:
                logging.debug('Lock cerrado, volviendo a intentar')                       
        finally:
            if entro:
                lock.release()
                logging.debug('Dejo de usar la BD')
                break
def Escritor(lock):
    logging.debug('intentando acceder')
    pause = random.random()+2
    time.sleep(pause)
    intentos = 0
    while True:
        entro = lock.acquire(0)
        time.sleep(2)
        try: 
            intentos += 1 
            if entro:
                logging.debug('Lock abierto, accediendo a la BD despues de %d intentos',intentos)
                time.sleep(3)   
            else:
                logging.debug('Lock cerrado, volviendo a intentar')                       
        finally:
            if entro:
                lock.release()
                logging.debug('Dejo de usar la BD')
                break

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s): %(message)s',
)
lock = threading.Lock()
for i in range(2):
    lectores=threading.Thread(name='Lector '+str(i+1), target=Lector, args=(lock,))
    escritores=threading.Thread(name='Escritor '+str(i+1),target=Escritor,args=(lock,))
    escritores.start()
    lectores.start()

main_thread = threading.currentThread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()
