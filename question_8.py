"""
solving boundary value problem using solve_bvp
"""
#Differential equation
"""
y''[x] = -4(y[x]-x) with  y[0] = 0, y[1] = 2 
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp as bvp

def fun(x,y):
	return np.vstack((y[1], 4*(y[0]-x)))
	

def bc(ya, yb):
	return np.array([ya[0], yb[0]-2])

def y_true(x):
	return (np.exp(2)/(np.exp(4)-1))*(np.exp(2*x) - np.exp(-2*x)) + x 


x = np.linspace(0,1,10)
y = np.zeros((2, x.size))
res = bvp(fun, bc, x, y)


x_plot = np.linspace(0,1,100)
y_plot = res.sol(x_plot)[0]
y = y_true(x_plot)
#Percentage relative error
rel_error = abs(y - y_plot)/y_true(x_plot)

print("Actual value		Calculated value		relative percentage error")
for i in range(y_plot.size):
	print(y[i],"	",y_plot[i],"	",rel_error[i]*100)




plt.plot(x_plot, y,'r', label = 'Analytic soln')
plt.plot(x_plot, y_plot, 'k.', label = 'Numerical soln')
plt.legend()
plt.xlim(0,1)
#plt.ylim(0,150)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()
