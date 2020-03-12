#Autor: David Baltazar Real
import logging
import threading
import queue
import time
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )
def persona1(*args):
    cola = args[1]
    condicion = args[2]
    while 1:
        if not(cola.full()):
            cola.put('M')
            logging.debug('Creando manga (Elementos en la canasta 1: %d)',cola.qsize())
        else:
            with condicion:
                condicion.wait() #bloquea el hilo hasta que haya espacio
        time.sleep(1)
def persona2(*args):
    cola = args[1]
    condicion = args[2]
    while 1:
        if not(cola.full()):
            cola.put('C')
            logging.debug('Ceando Cuerpo (Elementos en la canasta 2: %d)',cola.qsize())
        else:
            with condicion:
                condicion.wait()#bloquea el hilo hasta que haya espacio
        time.sleep(2)
def persona3(*args):
    cola1 = args[0]
    cola2 = args[1]
    condicion1 = args[2]
    condicion2 = args[3]
    while 1:
        if (cola1.qsize()>=2) and not(cola2.empty()):
            if cola1.full():
                condicion1.notifyAll()
            if cola2.full():
                condicion2.notifyAll()
            data = cola1.get()+'-'+cola2.get()+'-'+cola1.get()
            logging.debug('Creando prenda: %s',data)
            time.sleep(4)
        

LIMITE = 10


if __name__ == "__main__":
    condicion1 = threading.Condition()
    condicion2 = threading.Condition()
    condicion3 = threading.Condition()

    cola1 = queue.Queue(LIMITE)
    cola2 = queue.Queue(LIMITE)

    persona1 = threading.Thread(name='Persona 1', target=persona1,args=(cola1, condicion1))
    persona2 = threading.Thread(name='Persona 2', target=persona2,args=(cola2, condicion2))
    persona3 = threading.Thread(name='Persona 3',target=persona3,args=(cola1,cola2, condicion1, condicion2))
    persona1.start()
    persona2.start()
    persona3.start()
    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()
    
