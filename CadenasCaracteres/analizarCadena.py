from asyncio.windows_events import NULL


print("Escribe una cadena de texto")
cadena = str(input())

print("Estas son las características de tu cadena:")

print("Longitud de tu cadena: " + str(len(cadena)))

print("Espacios en blanco de tu cadena " + str(cadena.count(" ")))

print("Tu cadena en mayuscula: " + cadena.upper())

print("Tu cadena dos veces: " + cadena * 2)

lista_palabras = cadena.split()

for i in range(len(lista_palabras)) :
    lista_palabras[i] = str(i + 1) + ". " + lista_palabras[i]
print("Tu cadena numerando sus palabras:\n" + "\n".join(lista_palabras))
