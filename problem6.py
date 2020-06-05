import numpy as np
import matplotlib.pyplot as plt

def f(x,y1,y2):
    return (32*y1+66*y2+(2/3)*x+(2/3))
def g(x,y1,y2):
    return (-66*y1-133*y2-(1/3)*x-(1/3))

h=0.001
a=0
b=0.5
n=int((b-a)/h)

y1_0=1/3
y2_0=1/3

x=np.linspace(a,b,n+1)

y1=[]
y2=[]

y1.append(y1_0)
y2.append(y2_0)

for i in range(n):
    k1=h*f(x[i],y1[i],y2[i])
    l1=h*g(x[i],y1[i],y2[i])
    k2=h*f(x[i]+h/2,y1[i]+k1/2,y2[i]+l1/2)
    l2=h*g(x[i]+h/2,y1[i]+k1/2,y2[i]+l1/2)
    k3=h*f(x[i]+h/2,y1[i]+k2/2,y2[i]+l2/2)
    l3=h*g(x[i]+h/2,y1[i]+k2/2,y2[i]+l2/2)
    k4=h*f(x[i]+h,y1[i]+k3,y2[i]+l3)
    l4=h*g(x[i]+h,y1[i]+k3,y2[i]+l3)

    y1_rk4=y1[i]+(k1+2*k2+2*k3+k4)/6
    y2_rk4=y2[i]+(l1+2*l2+2*l3+l4)/6
    y1.append(y1_rk4)
    y2.append(y2_rk4)

fig1,ax1=plt.subplots()
plt.plot(x,y1,'b')
ax1.set_xlabel('x')
ax1.set_ylabel('y1')
plt.grid(True)

fig2,ax2=plt.subplots()
plt.plot(x,y2,'r')
ax2.set_xlabel('x')
ax2.set_ylabel('y2')
plt.grid(True)
plt.show()
