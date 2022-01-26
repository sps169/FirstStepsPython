#Author: Sergio Perez Sanz(sps169@outlook.es)
from random import random

lowerLimit = 0
upperLimit = 100
while (lowerLimit < upperLimit) :
    num = int(random() * (upperLimit - lowerLimit)) + lowerLimit
    print("Tu numero es mayor, menor o igual que "+ str(num))
    userData = input()
    if (userData == "mayor") :
        lowerLimit = num
    if (userData == "menor") :
        upperLimit = num
    if (userData == "igual"):
        print("Tu numero es "+ str(num))
        lowerLimit = num
        upperLimit = num
    else :
        print("Ese input es incorrecto")