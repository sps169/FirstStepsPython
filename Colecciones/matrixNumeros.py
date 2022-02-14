def main() :
    list = [[50,34,70,20], [5,70,30,25], [10,5], [75,43,56,32,89], [54,72]]
    print("Esta es la lista inicial")
    print(list)
    for i in range(len(list)) :
        for j in range(len(list[i])) :
            if (list[i][j] > 50) :
                list[i][j] = 0
    print("Esta es la lista sin numeros mayores a 50")
    print(list)


if __name__ == "__main__" :
    main()