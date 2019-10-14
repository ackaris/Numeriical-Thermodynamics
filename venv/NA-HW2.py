from math import *


def f(x):
    return sin(x)

def secant(x):
    # secant root finding method
    nmax = 1000
    tolerance = 1.0e-10
    dx=0.00001
    for i in range(0,nmax):
        fx=f(x)
        dfx=(f(x+dx)-f(x-dx))/(2.0*dx)
        x-=fx/dfx
        if abs(fx)<tolerance:
            return x
    return x


x=float(input("enter initial guess : "))
r=secant(x);
print(" ROOT : ",r,"\nFUNCTION VALUE : ",f(r));