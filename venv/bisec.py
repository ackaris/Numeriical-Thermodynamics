from math import *


def f(x):
    return sin(x)

def bisec(xl,xu):
    # bisection root finding method
    maxit = 100
    iter = 0
    es = 0.0000001
    ea = 1.1 * es
    s = ""
    fxl = f(xl)
    fxu = f(xu)
    xr = xl
    while ea > es and iter < maxit:
        xold = xr
        xr = (xl + xu) / 2.0;
        fxr = f(xr);
        iter = iter + 1;
        if xr != 0:
            ea = abs((xr - xold) / xr) * 100
        test = fxl * fxr;
        if test == 0.0:
            ea = 0;
        elif test < 0.0:
            xu = xr;fxu = fxr;
        elif test > 0:
            xl = xr;fxl = fxr;
        else:
            ea = 0;
        if iter >= maxit:
            print("Maximum number of iteration is exceeded \n result might not be valid")
    return xr


a=float(input("enter lower guess : "))
b=float(input("enter upper guess : "))
r=bisec(a,b);
print(" ROOT : ",r,"\nFUNCTION VALUE : ",f(r));