import os 
import time 
import csv 
import random
clean= "cls"

menu = 0
os.system(clean)
cliente = []
pedido =["Numero Pedido", "Cliente", "Dirección", "Sector", "Saco 5kg", "Saco 10kg", "Saco 20kg"]
saco = 0
saco5kg =0
saco10kg=0
saco20kg=0
sector= 0
numero_pedido= random.randint(1, 1000)

def menu():
    print("Bienvenidos a CatPremiun, A continuación se mostrará el menu, selecione la opcion requerida")
    print("1. Número Cliente\n 2. Listar todos los pedidos\n 3. Imprimir hoja de ruta\n 4. Salir del programa\n ")
    print("")
os.system(clean)
                      
def registro_pedido():
    numero_pedido = pedido
    print(f"Ingrese el la opcion requerido {numero_pedido}")
    nombre= input("ingrese su nombre: ").title()
    direcion= input("Ingrese la direción: ").title()
    try:
        opcion=int(input("Ingrese la comuna para entregar su pedido \n 1. Calera de Tango\n 2. San Bernardo \n 3. Buin\n "))
        if opcion ==1:
            print("Has selecionado la comuna de Calera de Tango")
        elif opcion ==2:
            print("Has selecionado la comuna de San Bernardo")
        elif opcion==3: 
            print("Has selecionado la comuna de Buin")
        else:
            print("Porfavor ingresa la opcion correcta")
    except ValueError:
        print("Vuelve a ingresar una de las opciones dadas") 

    while saco==1:
        try:
            opcion=int(input(" Seleccione el saco de comida para gatos a agregar. \n 1. Saco 5kg\n 2.Saco 10kg\n 3. Saco 20 kg"))
            if opcion==1:
                saco=saco5kg
                print("Has seleccionado el saco de alimento de 5 kg")
            elif opcion==2:
                saco=saco10kg
                print("Has selecionado el saco de alimento de 10kg")
            elif opcion==3:
                saco=saco20kg
                print("Has selecionado el saco de 20kg")
            else:
                print("Seleciona una de las opciones dadas")
        except ValueError:
            print("Ingresa nuevamente la opcion, te has equivocado")
            pedido.append([numero_pedido, nombre, direcion, sector, saco5kg, saco10kg, saco20kg])
            print("su pedido es el siguiente: ")
os.system(clean)    

def lista_pedido():
    for elemento in pedido:
        print(elemento)

def guardar_pedido():
    with open ("archivo.csv" mode="w", newline="") as pedido:
        guardar=csv.writer(pedido)
        guardar.writerow(pedido)

def hojaderuta():
        try:
            with open ("archivo.csv", mode="w", newline="") as archivo:
                leer=csv.reader(pedido)
                for i in leer:
                    for fila in i:
                        print(fila)
        except FileNotFoundError:
            print("El documento no existe")
os.system(clean)

while menu==1:
    menu()
    try:
        opcion_ingresada=int(input("Selecciona una opcion requerida del menu: "))
        if opcion_ingresada==1:
            registro_pedido()
        elif opcion_ingresada==2:
            lista_pedido()
        elif opcion_ingresada==3:
            guardar_pedido()
        elif opcion_ingresada==4: 
            hojaderuta()
        else:
            print("Seleciona una opcion valida del menu")
    except ValueError:
        print("Te has equivocado, vuelve a ingresar una opcion valida")
    continue

            







    


