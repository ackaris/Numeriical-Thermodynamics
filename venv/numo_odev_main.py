from scipy.optimize import curve_fit
from scipy.integrate import quad
from scipy.optimize import fsolve
from scipy.misc import derivative
import matplotlib.pyplot as plt
import pandas as pd
import math
import numpy as np

x=pd.read_csv("kitap1.csv",delimiter=';')
tarr=x['t']
cpa=x['cp']
cp=[]

def CPfunc(t,a,b,c,d,e,f):
    return a*t*t*t*t*t+b*t*t*t*t+c*t*t*t+d*t*t+e*t+f

def Zfunc(z,t,p,tc,pc,w):
    tr = t / tc
    pr = p / pc
    alpha = (1 + (0.37464 + 1.54226 * w - 0.26992 * w * w) * (1 - math.sqrt(tr))) ** 2
    A = 0.45724 * alpha * (pr / (tr * tr))
    B = 0.07780 * (pr / tr)
    a2 = A * B - B * B - B * B * B
    a1 = A - 3 * B * B - 2 * B
    a0 = 1-B
    return z*z*z-a0*z*z+a1*z-a2

def findcpconst():
    c,co=curve_fit(CPfunc,tarr,cpa)
    for i in tarr:
        cp.append(CPfunc(i,c[0],c[1],c[2],c[3],c[4],c[5]))
    return c

def calcDHIdeal(c,t0,t1):
    DHIdeal,err=quad(CPfunc,t0,t1,args=(c[0],c[1],c[2],c[3],c[4],c[5]))
    return DHIdeal

def Pfunc(t,tc,pc,w,vm):
    R=8.314413
    tr=t/tc
    a=(0.45724*R*R*tc*tc)/pc
    b=(0.07780*R*tc)/pc
    alpha=(1+(0.37464+1.54226*w-0.26992*w*w)*(1-math.sqrt(tr)))**2
    return ((R*t)/(vm-b))-((a*alpha)/(vm*vm+2*b*vm-b*b))

def calcZ(t,p,tc,pc,w):
    return fsolve(Zfunc,1,args=(t,p,tc,pc,w))

def DHDepintegralfunc(t,p,tc,pc,w,vm):
    return (t*derivative(Pfunc, t, dx=1.0e-6, args=(tc, pc, w, vm)))-p

def calcDHdep(t,p,tc,pc,w,z,vm):
    R = 8.314413
    v=(R*t)/p
    integral,err=quad(DHDepintegralfunc, np.inf, v, args=(p, tc, pc, w, vm))
    hdep=(R*t*(z-1))+integral
    return hdep

t1=220
t2=240
p1=100
p2=100
tc=304.25
pc=7390
w=0.239
z1=calcZ(t1,p1,tc,pc,w)
z2=calcZ(t2,p2,tc,pc,w)
vm=44.01
h1dep=calcDHdep(t1,p1,tc,pc,w,z1,vm)
h2dep=calcDHdep(t1,p2,tc,pc,w,z2,vm)
c=findcpconst()
DHIdeal=calcDHIdeal(c,t1,t2)
DHdep=h2dep-h1dep
DH=DHIdeal+DHdep
print("t1    t2    p1    p2")
print(str(t1)+"   "+str(t2)+"   "+str(p1)+"   "+str(p2))
print("dh ideal  "+str(DHIdeal))
print("dh diff from ideal   "+str(DHdep))
print("real dh=  "+str(DH))

plt.figure()
plt.plot(tarr,cpa,label="")
plt.plot(tarr,cp)
plt.show()

