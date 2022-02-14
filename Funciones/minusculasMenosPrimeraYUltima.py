from ast import Str
from re import U


def main():
    print("'hoLA Mundo' se convierte en " + "'" + toMinusExceptFirstAndLast("hoLA Mundo") + "'")
    print("'FEDE COME QLOTE' se convierte en " +  "'" +toMinusExceptFirstAndLast("FEDE COME QLOTE") + "'")
    print("'' se convierte en '" + toMinusExceptFirstAndLast("") + "'")

def toMinusExceptFirstAndLast(palabra :str):
    if (len(palabra) > 0) :
        return palabra[0].upper() + palabra[1:(len(palabra) - 1)].lower() + palabra[len(palabra) - 1].upper()
    else:
        return palabra

if (__name__ == "__main__"):
    main()