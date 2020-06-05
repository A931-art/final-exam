from scipy.integrate import solve_bvp
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
        return np.vstack((y[1], 4*(y[0]-x)))
def bc(ya, yb):
        return np.array([ya[0]-0, yb[0]-2])

a=0
b=1
y0=0

x = np.linspace(a, b)
yd = np.zeros((2, x.size))
yd[0]=y0

sol =solve_bvp(f, bc, x, yd)
y = (((np.exp(2))/(np.exp(4)-1))*(np.exp(2*x)-np.exp(-2*x)))+x 
plt.subplots()
plt.plot(x,sol.sol(x)[0],'r',x,y,'g')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['solve_bvp','Analytical'])
plt.grid()
plt.show()

print("The relative error in percentage points: \n")
yerr = (abs(y-sol.sol(x)[0])/y)*100
print(yerr)
