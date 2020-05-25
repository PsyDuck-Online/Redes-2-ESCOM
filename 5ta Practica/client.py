import xmlrpc.client
import datetime
import sys

def main(proxy):
    root = "/Users/david/OneDrive/Documentos/GitHub/Redes-2-ESCOM/4ta Practica"
    try:
        print('<< Ctrl+C >> para salir...') 
        while True:
            instruction = input('Instruccion >> ')

            if instruction.upper() == "CREATE":
                archivo = input("Archivo >> ")
                data = input('Texto >>\n')
                proxy.CREATE(archivo,data)

            elif instruction.upper() == "READ":
                archivo = input("Archivo >> ")
                print("Read<<\n{}\n".format(proxy.READ(archivo)))   

            elif instruction.upper() == "WRITE":
                archivo = input("Archivo >> ")
                data = input("Texto >>\n")
                proxy.WRITE(archivo, data)

            elif instruction.upper() == "REMOVE":
                archivo = input("Archivo >> ")
                proxy.REMOVE(archivo)

            elif instruction.upper() == "MKDIR":
                archivo = input("Archivo >> ")
                proxy.MKDIR(archivo)

            elif instruction.upper() == "RMDIR":
                archivo = input("Archivo >> ")
                proxy.RMDIR(archivo)

            elif instruction.upper() == "READDIR":
                print(proxy.READDIR(root))
                
            else:
                print("Opcion invalida.")

    except KeyboardInterrupt:
        print('\nSaliendo...')

    

if __name__ == "__main__":
    proxy = xmlrpc.client.ServerProxy('http://localhost:5432')
    main(proxy)