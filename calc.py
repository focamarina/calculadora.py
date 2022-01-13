import time

n1 = float(input("Introduce tu primer numero: "))
n2 = float(input("Introduce tu segundo numero: "))

option = 0

while True:
    print("""
        Dime, ¿que operacion quieres realizar?

        1) Sumar los dos numeros
        2) Restar los dos numeros
        3) Multiplicar los dos numeros
        4) Dividir los dos numeros
        5) Cambiar los numeros elegidos
        6) Cerrar Calculadora
    """)
    option = int(input("Introduzca el numero de la opcion a realizar: "))

    if option == 1:
        print(" ")
        print(f"La suma de {n1} y {n2} da como resultado: ",n1+n2)
    elif option == 2:
        print(" ")
        print(f"La resta de {n1} y {n2} da como resultado: ",n1-n2)
    elif option == 3:
        print(" ")
        print(f"La multiplicacion de {n1} y {n2} da como resultado: ",n1*n2)
    elif option == 4:
        print(" ")
        print(f"La division de {n1} y {n2} da como resultado: ",n1/n2)
    elif option == 5:
        n1 = float(input("Introduce tu primer numero: "))
        n2 = float(input("Introduce tu segundo numero: "))
    elif option == 6:
        print("Hasta pronto!")
        time.sleep(5)
        break
    else:
        print(" ")
        print("Opcion Incorrecta!")