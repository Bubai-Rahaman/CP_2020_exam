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
rel_error = 100*(y - y_plot)/y_true(x_plot)

#storing output to a text file
output = "question4_output.txt" #output stored in this file 
S = np.zeros([y.size,3])
S[:, 0] = y
S[:, 1] = y_plot
S[:, 2] = rel_error
print("The result stored in the txt file in this order")
print("Analytic result		numerical result	relative error\n")
np.savetxt(output, S)



plt.plot(x_plot, y,'r', label = 'Analytic soln')
plt.plot(x_plot, y_plot, 'k.', label = 'Numerical soln')
plt.legend()
plt.xlim(0,1)
#plt.ylim(0,150)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()
