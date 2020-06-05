import numpy as np
import matplotlib.pyplot as plt

n=1024
x=np.linspace(0,1,1024)
np.random.seed(0)
f=np.random.rand(n)

k=2*np.pi*np.fft.fftfreq(n, d=1/(n-1))
dft=np.fft.fft(f,norm='ortho')
power_spectrum=(1/n)*(dft)**2
print("Maximum value of k: {}".format(max(k)))
print("Minimum Value of k: {}".format(min(k)))

fig1=plt.subplots()
plt.plot(x,f,'r')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)

fig2=plt.subplots()
plt.plot(k,dft,'c',label="DFT")
plt.xlabel('k')
plt.ylabel('f(k)')
plt.legend()
plt.grid(True)

fig3=plt.subplots()
plt.plot(k,power_spectrum,'b',label="Power spectrum")
plt.xlabel('k')
plt.ylabel('f(k)^2')
plt.legend()
plt.grid(True)

fig4=plt.subplots()
plt.hist(power_spectrum,range=(min(k),max(k)),bins=5,density=True,facecolor='green',label="Histogram")
plt.xlabel('k')
plt.legend()
plt.grid(True)
plt.show()
