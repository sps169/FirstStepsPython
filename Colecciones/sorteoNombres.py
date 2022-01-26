from random import random

def sorteo(list = []) :
    if (len(list) != 0) :
        print("Participantes:")
        print(list)
        print("El ganador del sorteo es " + list[int(random() * len(list))])
    else :
        print("No hay participantes")


exit = False
print("Bienvenido al sorteo de absolutamente todo")
user_input = -1
list = []
while (not exit) :
    print("Introduzca '1' para introducir un participante")
    print("Introduzca '2' para realizar el sorteo")
    print("Introduzca '3' para limpiar la lista")
    print("Introduzca '4' para realizar el sorteo con datos de un csv")
    print("Introduzca '0' para salir del programa")

    user_input = int(input())
    if (user_input >= 0 & user_input <= 4) :
        if (user_input == 4) :
            file = open("D:\\2DAM\\SistemasGestionEmpresarial\\Tema 5\\Practica Python\\Colecciones\\nombres.txt")
            list.clear()
            for line in file.readlines() :
                list.append(line.removesuffix("\n"))
            sorteo(list)
        if (user_input == 1) :
            print("Introduce un participante")
            list.append(input())
        if (user_input == 2) :
            sorteo(list)
        if (user_input == 3) : 
            list.clear()
        if (user_input == 0) :
            exit = True
    else : 
        print("Wrong input")

