
from math import cos
from scipy import integrate
import numpy as np
from math import *
from pylab import * 

print('1.Ractangle method') 
def calculate_dx (a, b, n):
	return (b-a)/float(n)

def rect_rule (f, a, b, n):
	er = 0.0001
	dx = calculate_dx(a, b, n)
	for k in range (0, n):
        	er = er + f((a + (k*dx)))
	return dx*er

def f1(x):
    return 1/((x**2)+1)
def f2(x):
    return cos(x)/(x+1)
def f3(x):
    return 1/(1.5*(x**2)+0.7)**0.5

print('example 1:',rect_rule(f1, 0.2, 1.2, 10000))
print('example 2:',rect_rule(f2, 0.6, 1.4, 10))
print('example 3:',rect_rule(f3, 1.4, 2.6, 10))

print("\n2.Simpson's method")

def simps(f, a, b, n):
    if n % 2:
        raise ValueError("n must be even (received n=%d)" % n)

    h = (b - a) / n
    s = f(a) + f(b)

    for i in range(1, n, 2):
        s += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        s += 2 * f(a + i * h)

    return s * h / 3

print('example 1:', simps(f1, 0.2, 1.2, 8))
print('example 2:', simps(f2, 0.6, 1.4, 8))
print('example 3:', simps(f3, 1.4, 2.6, 8))

print("\n3.Метод трапецій")

def trapezoid(f, a, b, n):
    deltax = float(b - a)/(n)
    h = float(b - a) / n
    s = 0.0
    s += f(a)/2.0
    for i in range(1, n):
        s += f(a + i*h)
    s += f(b)/2.0
    return s * h

print('example 1:', trapezoid(f1, 0.2, 1.2, 20))
print('example 2:', trapezoid(f2, 0.6, 1.4, 20))
print('example 3:', trapezoid(f3, 1.4, 2.6, 20))

print('Сheck')
print('Num1:', integrate.quad(f1, 0.2, 1.2))
print('Num2:', integrate.quad(f2, 0.6, 1.4))
print('Num3:', integrate.quad(f3, 1.4, 2.6))
