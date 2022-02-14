
def main():
    exit = False
    diccionario = {}
    while (not(exit)) :
        print("Inserte '1' para insertar una palabra.")
        print("Inserte '2' para consultar una palabra")
        print("Inserte '3' para borrar una palabra")
        print("Inserte '4' para cargar datos desde el diccionario almacenado")
        print("Inserte '0' para salir del programa")
        menuInput = input()
        if (menuInput == "0") :
            print("Hasta pronto!")
            exit = True
        if (menuInput == "1") :
            insertar_palabra(diccionario)
        if (menuInput == "2") :
            consultar_palabra(diccionario)
        if (menuInput == "3") :
            borrar_palabra(diccionario)
        if (menuInput == "4") : 
            cargar_diccionario(diccionario)

def cargar_diccionario(diccionario):
    f = open("Colecciones\diccionario.txt")
    for word in f.readlines() :
        diccionario[word.split(";")[0]] = word.removesuffix("\n").split(";")[1]
        print("Se ha cargado la palabra "+ word.split(";")[0])

def borrar_palabra(diccionario):
    print("Que palabra en castellano quieres eliminar?")
    wordInput = input()
    tuplaBorrada = str(diccionario.pop(wordInput))
    if (tuplaBorrada != None) :
        print("La entrada del diccionario '"+wordInput + "':'" + tuplaBorrada + "' ha sido borrada")
    else :
        print("La palabra "+ wordInput + " no existe")

def consultar_palabra(diccionario):
    print("Que palabra en castellano quieres consultar?")
    wordInput = input()
    if (diccionario.get(wordInput) != None) :
        print("La traducción de '"+ wordInput+ "' es '" + diccionario.get(wordInput) + "'")
    else :
        print("La traducción de '" + wordInput+ "' no está disponible en este diccionario")

def insertar_palabra(diccionario):
    print("Inserta la palabra en castellano")
    keyInput = input()
    print("Inserta la palabra en inglés")
    diccionario[keyInput]= input()

if __name__ == '__main__':
    main()