import matplotlib.pyplot as plt
import numpy as np
import df
def f(x):
    return x*x*x
def integral(a,b):#3-end
    dx=1e-5
    intarr=[]
    integ=0
    xarr=[]
    for d in np.arange(a,b,dx):
        x0=d
        x1=d+dx
        y0=f(x0)
        integ=integ+y0*(x1-x0)
        intarr.append(integ)
        xarr.append(d)
    return xarr,intarr,integ
xarr,intarr,integ=integral(0,5)
fx=[]
dfx,dfxarr,xarr=df.df(5,0,5)
print(dfxarr)
print(dfx)
plt.plot(xarr,intarr,label="integral")
plt.plot(xarr1,fx,label="fonksiyon")
plt.plot(xarr1,dfxarr,label="türev")
plt.legend()
plt.show()
