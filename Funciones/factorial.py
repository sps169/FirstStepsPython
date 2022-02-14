def main() :
    print("Factorial de 5: " + str(factorial(5)))
    print("Factorial de 0: " + str(factorial(0)))
    print("Factorial -10: " + str(factorial(-10)))

def factorial(n) :
    if (n > 1):
        return n * factorial (n - 1)
    if (n == 1):
        return n
    if (n == 0):
        return 1
    else:
        return 0
if (__name__ == "__main__") :
    main()