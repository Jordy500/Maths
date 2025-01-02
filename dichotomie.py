
# Calcule la racine carrée d'un nombre positif en utilisant la méthode de la dichotomie
import numpy
import matplotlib.pyplot as plt
from Config_file import *


def f(x):
    return x**2 - 8 * numpy.log(x) 


def dichotomie(f, left, right, precision=10**-(3)):
    while right - left >= precision:
        middle = (left + right) / 2

        if f(middle) == 0:
            break

        elif f(left) * f(middle) < 0:
            right = middle

        elif f(middle) * f(right) < 0:
            left = middle

    return middle

result = dichotomie(f, 1, 2, 10**-3)


def plot_fonction(f, start=0.01, end=2, step=0.01):
    x = numpy.arange(start, end, step)
    y = f(x)


    plt.figure(figsize=(LENGTH, WIDTH))
    

    plt.plot(x, y, label="f(x) = x^2 - 8 * log(x)")
    plt.axhline(0, color="black", lw=1)

    plt.title("Fonction")
    plt.xlabel("x")
    plt.show()



if __name__ == "__main__":
    plot_fonction(f, 0.01, 2, 0.01)

"""
x = numpy.array([1, 2, 3,])
y = f(x)
"""
#print(result)
#print(f(result))

#left = 1
#rigth = 3
#precission = 10**-(3)

#while rigth - left >= precission:
#    middle = (left + rigth) / 2

#    if f(middle) == 0:
#        break

#    elif f(left) * f(middle) < 0:
#       left = middle

