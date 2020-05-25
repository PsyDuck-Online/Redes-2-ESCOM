from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from io import open
from os import remove, rmdir, listdir
from os import makedirs


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

try:
    print("Iniciando servidor RPC: <<Ctrl+C>> para salir...")
    with SimpleXMLRPCServer(('localhost',5432),requestHandler=RequestHandler, allow_none=True) as server:
        
        class MyFuncs:
            def CREATE(self,ruta_nombre,text):
                try:
                    textfile = open(ruta_nombre,"w")
                    textfile.write(text)
                except Exception as e:
                    print(e)
                finally:
                    textfile.close()

            def READ(self,nombre):
                try:
                    textfile = open(nombre,"r")
                    text = textfile.read()
                    textfile.close()
                    return text
                except Exception as e:
                    return e

            def WRITE(self,file,text):
                try:
                    textfile = open(file,'a')
                    textfile.write('\n' + text)
                    textfile.close()
                except Exception as e:
                    print(e)

            def REMOVE(self, file):
                try:
                    remove(file)
                except Exception as e:
                    print(e)

            def MKDIR(self, file):
                try:
                    makedirs(file)
                except Exception as e:
                    print(e)
                
            def RMDIR(self,file):
                try:
                    rmdir(file)
                except Exception as e:
                    print(e)
            
            def READDIR(self,dir):
                try:
                    return(listdir(dir))
                except Exception as e:
                    print(e)

        server.register_instance(MyFuncs())

        server.serve_forever()
except KeyboardInterrupt:
    print("Saliendo...")