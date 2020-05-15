# SERVIDOR DE CALCULADORA BASICA(SUMA,RESTA,MULTIPLICACION,DIVISION) 
# USANDO RPC
# @AUTHOR: DAVID BALTAZAR REAL 

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import logging

logging.basicConfig(level=logging.INFO)

class myRequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

def main():
    logging.info('Starting server on port: 5432 <<Ctrl + C>> to exit')
    with SimpleXMLRPCServer(('localhost',5432), requestHandler=myRequestHandler) as server:
        logging

        class my_functions:
            def multiplicacion(self, x, y):
                return x * y
            def suma(self, x, y):
                return x + y
            def resta(self, x, y):
                return x - y
            def division(self, x, y):
                return x/y
        server.register_instance(my_functions())

        server.serve_forever()

if __name__ == "__main__":
    main()