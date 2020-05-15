# SERVIDOR DE CALCULADORA BASICA(SUMA,RESTA,MULTIPLICACION,DIVISION) 
# USANDO RPC
# @AUTHOR: DAVID BALTAZAR REAL 

import xmlrpc.client

connection = xmlrpc.client.ServerProxy('http://localhost:5432')
op = 1
r = 0

while True:
    signo = ''
    op = input('\n1) Suma\n2) Resta\n3) Multiplicacion\n4) Division\n5) Salir\nRespuesta: ')
    if op == '5':
        break
    else:
        print('---INTRODUZCA LOS NUMEROS---')
        num1 = float(input('num1 = '))
        num2 = float(input('num2 = '))
        if op == '1':
            signo = '+'
            r = connection.suma(num1,num2)
        elif op == '2':
            signo = '-'
            r = connection.resta(num1,num2)
        elif op == '3':
            signo = '*'
            r = connection.multiplicacion(num1,num2)
        elif op == '4':
            signo = '/'
            r = connection.division(num1,num2)
        else:
            print('Comando invalido')
            continue
    print('{} {} {} = {}'.format(num1, signo, num2, r))