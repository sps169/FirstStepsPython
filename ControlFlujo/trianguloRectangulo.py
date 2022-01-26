#Author: Sergio Perez Sanz(sps169@outlook.es)

from random import triangular

def triangulo(n, mod) :
    for i in range(n) :
        for j in range((i * mod) + 1) :
            print("*", end = '')
        print()

print("Give me the triangle height")
n = int(input())

print("Triangulo Rectángulo Isosceles")
triangulo(n, 1)

print("Triangulo Rectángulo Escaleno")
triangulo(n, 2)
