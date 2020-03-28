import socket
import threading

IP_DESTINO = input("Ip destino: ")
PORT = int(input("Puerto: "))
addres_dest = (IP_DESTINO,PORT)

def msg_recv(socket):
    while True:
        try:
            data = ''
            data = socket.recv(2048)
            if data:
                msg = data.decode('utf-8')  
                if msg.find("exit") > -1:
                    print('El servidor cerro la conexion')
                    break
                elif msg == 'Tu turno: ':
                    casillas = input(msg)
                    socket.send(casillas.encode('utf8'))  
                else:
                    print(msg)
        except:
            pass

if __name__ == "__main__":
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_client.connect(addres_dest)
    socket_client.setblocking(False)

    msg_recv = threading.Thread(target=msg_recv, args=(socket_client,))

    msg_recv.setDaemon(True)
    msg_recv.start()


    msg_recv.join()

    socket_client.close()
    
