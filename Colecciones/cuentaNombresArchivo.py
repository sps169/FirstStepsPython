exit = False
words_len_5 = 0
list = []
fichero = open("D:\\2DAM\\SistemasGestionEmpresarial\\Tema 5\\Practica Python\\Colecciones\\nombres.txt")
while (not exit) :
    
    user_input = fichero.readline()
    user_input = user_input.removesuffix("\n")

    if (user_input != "exit") :
        list.append(user_input)
        if (len(user_input) >=5) :
            words_len_5 += 1
    else :
        exit = True
print("There are " + str(words_len_5) + " words with more than 5 characters")
print(list)
