import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x*x
def df(*args):#3-end
    if len(args)==1:
        x0=args[0]
        dx = 0.001
        dfx = ((1 / (2 * dx)) * (-3 * f(x0) + 4 * f(x0 + dx) - f(x0 + 2 * dx)))
        return dfx
    elif len(args)==3:
        x0=args[0]
        a = args[1]
        b = args[2]
        print(a)
        print(b)
        dx = 0.001
        xarr = np.arange(a,b,dx)
        dfx = ((1 / (2 * dx)) * (-3 * f(x0) + 4 * f(x0 + dx) - f(x0 + 2 * dx)))
        dfxarr=[]
        fx=[]
        for i in xarr:
            dfxarr.append(((1 / (2 * dx)) * (-3 * f(i) + 4 * f(i + dx) - f(i + 2 * dx))))
            fx.append(f(i))
        return fx,dfx, dfxarr,xarr


