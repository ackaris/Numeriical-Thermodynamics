from scipy.integrate import quad
from scipy.misc import derivative
import math
import numpy as np


def calcDSIdeal(t1,t2,p1,p2):
    CPIdeal=0.846*44.01
    R = 8.314413
    DSIdeal=(CPIdeal*np.log(t2/t1))-(R*np.log(p2/p1))
    return DSIdeal

def Pfunc(t,tc,pc,w,vm):
    R=8.314413
    tr=t/tc
    a=(0.45724*R*R*tc*tc)/pc
    b=(0.07780*R*tc)/pc
    alpha=(1+(0.37464+1.54226*w-0.26992*w*w)*(1-math.sqrt(tr)))**2
    return ((R*t)/(vm-b))-((a*alpha)/(vm*vm+2*b*vm-b*b))


def DSDepintegralfunc(t,p,tc,pc,w,vm):
    R = 8.314413
    return (derivative(Pfunc, t, dx=1.0e-6, args=(tc, pc, w, vm)))-(R/vm)


def calcDSdep(t,p,tc,pc,w,vm):
    R = 8.314413
    v=(R*t)/p
    integral,err=quad(DSDepintegralfunc, np.inf, v, args=(p, tc, pc, w, vm))
    hdep=integral
    return hdep

t1=220
t2=230
p1=300
p2=300
tc=304.25
pc=7390
w=0.239
vm=44.01

DSIdeal=calcDSIdeal(220,230,300,300)
DSDep1=calcDSdep(t1,p1,tc,pc,w,vm)
DSDep2=calcDSdep(t2,p2,tc,pc,w,vm)
DSReal=DSIdeal+DSDep2-DSDep1
print("t1    t2    p1    p2")
print(str(t1)+"   "+str(t2)+"   "+str(p1)+"   "+str(p2))
print("ds Ideal=  "+ str(DSIdeal))
print("ds diff from ideal  " + str(DSDep2-DSDep1))
print("ds real=  " + str(DSReal))