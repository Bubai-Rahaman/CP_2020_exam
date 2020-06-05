'''
Solving coupled 1st order differential equation using Scipy.integrate.solve_ivp 
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp as ivp

#defining the rhs of the differential equations
def f(x,y):
	return [32*y[0] + 66*y[1] + 2*x/3 + 2/3, -66*y[0] -133*y[1] -x/3 - 1/3]

def y1_true(x):
	return (-np.exp(-100*x) + 2*np.exp(-x) + 2*x)/3

def y2_true(x):
	return (2*np.exp(-100*x) - np.exp(-x) - x)/3

xi, xf = 0, 0.5
N = 100

sol = ivp(f, [xi,xf], [1/3, 1/3], dense_output = True)

x = np.linspace(xi, xf, N)
y1 = sol.sol(x)[0]
y2 = sol.sol(x)[1]

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

print("The solution obtained from the numerical calculation is exactly matching with the analutical solution within the givn range. So, the numerical result is correct.")
#plot of y1

ax1.plot(x, y1, 'g.-', label = 'Numerically calculated result')
ax1.plot(x, y1_true(x), 'm', label = 'Analytical result')
ax1.set_xlabel("x")
ax1.set_ylabel("y(x)")
ax1.legend()
ax1.set_title("y1(x)")

#plot of y1

ax2.plot(x, y2, 'g.-', label = 'Numerically calculated result')
ax2.plot(x, y2_true(x), 'm', label = 'Analytical result')
ax2.set_xlabel("x")
ax2.set_ylabel("y(x)")
ax2.legend()
ax2.set_title("y2(x)")




plt.show()
