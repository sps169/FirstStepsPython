from random import random


class Saludo :

    def formal(self, nombre = "persona") :
        print ("Saludos, " + nombre)

    def informal(self, nombre = "persona"):
        print ("Hola, " + nombre + " :D")

    def aleatorio(self, nombre = "persona"):
        if (random() > 0.5) :
            self.formal(nombre)
        else :
            self.informal(nombre)

def main() :
    saludo = Saludo()
    print("Saludos al profesor: ")
    saludo.informal("profe")
    saludo.formal("Profesor")

    print("\nSaludos genericos: ")
    saludo.informal()
    saludo.formal()


if (__name__ == "__main__") :
    main()