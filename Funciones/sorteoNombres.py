from random import random

def sorteo(list = []) :
    if (len(list) != 0) :
        print("Participantes:")
        print(list)
        print("El ganador del sorteo es " + list[int(random() * len(list))])
    else :
        print("No hay participantes")

def print_menu():
    print("Introduzca '1' para introducir un participante")
    print("Introduzca '2' para realizar el sorteo")
    print("Introduzca '3' para limpiar la lista")
    print("Introduzca '4' para realizar el sorteo con datos de un csv")
    print("Introduzca '0' para salir del programa")

def main():
    exit = False
    while (not exit) :
        print("Bienvenido al sorteo de absolutamente todo")
        print_menu()
        exit = user_input()

def user_input():
    user_input = -1
    list = []
    user_input = int(input())
    if (user_input >= 0 & user_input <= 4) :
        if (user_input == 4) :
            file = open("Funciones\\nombres.txt")
            list.clear()
            for line in file.readlines() :
                list.append(line.removesuffix("\n"))
            sorteo(list)
            return False
        if (user_input == 1) :
            print("Introduce un participante")
            list.append(input())
            return False
        if (user_input == 2) :
            sorteo(list)
            return False
        if (user_input == 3) : 
            list.clear()
            return False
        if (user_input == 0) :
            return True
    else : 
        print("Wrong input")
        return False

if (__name__ == "__main__") :
    main()