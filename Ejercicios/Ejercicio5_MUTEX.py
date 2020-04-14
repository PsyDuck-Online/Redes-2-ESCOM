import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def creador_mangas(mangas,LIMITE_MANGAS, condition_MAX_mangas, condition_MIN_mangas):
    while True:
        with condition_MAX_mangas:
            if len(mangas) >= LIMITE_MANGAS:
                logging.debug('LA CESTA DE MANGAS ESTA LLENA')
                condition_MAX_mangas.wait()
            else:
                mangas.append('m')
                time.sleep(1)
                logging.debug('Creando manga: '+str(len(mangas)))

        with condition_MIN_mangas:
            if len(mangas) >= 2:
                condition_MIN_mangas.notify()
        
        

def creador_cuerpo(cuerpos, LIMITE_CUERPOS, condition_MAX_cuerpos, condition_MIN_cuerpos):
    while True:
        with condition_MAX_cuerpos:
            if len(cuerpos) >= LIMITE_CUERPOS:
                logging.debug('LA CESTA DE CUERPOS ESTA LLENA')
                condition_MAX_cuerpos.wait()
            else:
                cuerpos.append('c')
                time.sleep(2)
                logging.debug('Creando cuerpo: '+str(len(cuerpos)))

        with condition_MIN_cuerpos:
            if len(cuerpos) >= 1:
                condition_MIN_cuerpos.notify()

def ensamblador(prendas,mangas, cuerpos, condition_MIN_cuerpos, condition_MAX_cuerpos, condition_MIN_mangas, condition_MAX_mangas):
    while True:
        with condition_MIN_mangas:
            while not len(mangas) >= 2:
                condition_MIN_mangas.wait()
        with condition_MIN_cuerpos:
            while not len(cuerpos) >= 1:
                condition_MIN_cuerpos.wait()
        
        mangas.pop()
        cuerpos.pop()
        mangas.pop()
        prendas.append('mCm')
        time.sleep(1)
        logging.debug('Creando prenda: '+ str(prendas))

        with condition_MAX_cuerpos:
            condition_MAX_cuerpos.notify()
        with condition_MAX_mangas:
            condition_MAX_mangas.notify()


mangas = []
cuerpos = []
prendas = []

LIMITE_MANGAS = 10
LIMITE_CUERPOS = 5

condition_MAX_cuerpos = threading.Condition()
condition_MIN_cuerpos = threading.Condition()

condition_MAX_mangas = threading.Condition()
condition_MIN_mangas = threading.Condition()

persona1 = threading.Thread(target=creador_mangas,args=(mangas, LIMITE_MANGAS, condition_MAX_mangas, condition_MIN_mangas))
persona2 = threading.Thread(target=creador_cuerpo, args=(cuerpos,LIMITE_CUERPOS, condition_MAX_cuerpos, condition_MIN_cuerpos))
persona3 = threading.Thread(target=ensamblador, args=(prendas,mangas, cuerpos, condition_MIN_cuerpos, condition_MAX_cuerpos, condition_MIN_mangas, condition_MAX_mangas))

persona1.setDaemon(True)
persona2.setDaemon(True)
persona3.setDaemon(True)

persona1.start()
persona2.start()
persona3.start()

while True:
    if len(prendas) > 9:
        exit()

persona1.join()
persona2.join()
persona3.join()

