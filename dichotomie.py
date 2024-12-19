
# Calcule la racine carrée d'un nombre positif en utilisant la méthode de la dichotomie
import numpy


def f(x):
    return x**2 - 8 * numpy.log(x) 
"""
x = numpy.array([1, 2, 3,])
y = f(x)
"""
def dichotomie(f, left, right, precision=10**-(3)):
    while right - left >= precision:
        middle = (left + right) / 2

        if f(middle) == 0:
            return middle

        elif f(left) * f(middle) < 0:
            right = middle

        elif f(middle) * f(right) < 0:
            left = middle

    return middle

result = dichotomie(f, 1, 2, 10**-3)
print(result)
print(f(result))

#left = 1
#rigth = 3
#precission = 10**-(3)

#while rigth - left >= precission:
#    middle = (left + rigth) / 2

#    if f(middle) == 0:
#        break

#    elif f(left) * f(middle) < 0:
#       left = middle
    
    
#print(middle)
#print(f(middle))
