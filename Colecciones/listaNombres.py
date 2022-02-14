def main():
    list = []
    print("Te voy a pedir 5 nombres de persona")
    for i in range(1, 6) :
        print("Inserta el nombre "+ str(i))
        list.append(input())
    print("Esta es la lista de nombres ordenada alfabeticamente:")
    list.sort()
    print(list)
    print("Y esta es la lista de nombres ordenada por tamaño de palabra")
    list.sort(key=lenghtSort)
    print(list)

def lenghtSort (a) :
    return len(a)

if __name__ == "__main__" :
    main()