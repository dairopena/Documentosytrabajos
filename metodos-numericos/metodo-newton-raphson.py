# desarrollo del método de newton raphson para hallar ceros y raíces

# importar librerías
import math as m
import numpy as np
from numpy import *
import sympy as sp
from sympy import *


def newton(f,df,xi,tol):
    x = xi
    error = 1e3
    n=1
    while error > tol:
        x = x - f(x)/df(x)
        error = abs(f(x))
        n += 1
    print("La raíz es: {:.4f} ".format(x)) 
    print("Numero de iteraciones:{:d}".format(n))

# definir la función
f = lambda x: x**15-10 ; df = lambda x: 15*x**14

newton(f,df,6,1e-8)

