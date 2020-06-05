"""
Fourier Transform of box Function
"""
import numpy as np
import matplotlib.pyplot as plt

shift = np.fft.fftshift

def box(x):
	if -1<x<1:
		return 1
	return 0

def ft(data, xmin, dx):

	dft = np.fft.fft(data, norm = 'ortho')
	karr = 2*np.pi*np.fft.fftfreq(data.size, d = dx)
	
	factor = np.exp(-1j*karr*xmin)
	nft = dx*factor*np.sqrt(data.size/(2*np.pi))*dft
	
	return (shift(karr), shift(nft).real)
	

xmin, xmax = -50, 50
N = 512 

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

#1st
x1 = np.zeros(N)
sampled_data1 = np.zeros(N)
dx1 = (xmax-xmin)/(N-1)
for j in range(N):
	x1[j] = xmin + j*dx1
	sampled_data1[j] = box(x1[j])
	
k1, nft1 = ft(sampled_data1, xmin, dx1)
			
#2nd
x2 = np.zeros(2*N)
sampled_data2 = np.zeros(2*N)
dx2 = (xmax-xmin)/(2*N-1)
for j in range(2*N):
	x2[j] = xmin + j*dx2
	sampled_data2[j] = box(x2[j])
	
k2, nft2 = ft(sampled_data2, xmin, dx2)

#3rd
x3 = np.zeros(4*N)
sampled_data3 = np.zeros(4*N)
dx3 = (xmax-xmin)/(4*N-1)
for j in range(4*N):
	x3[j] = xmin + j*dx3
	sampled_data3[j] = box(x3[j])
	
k3, nft3 = ft(sampled_data3, xmin, dx3)



#plot of box function
ax1.plot(x3, sampled_data3, 'g')
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)')
ax1.set_xlim(-2,2)
ax1.set_title('Box function')

#plot of FT of box function
ax2.plot(k3, nft3, 'm.-', label = 'N = 2048')
ax2.plot(k2, nft2, 'g*', label = 'N = 1024')
ax2.plot(k1, nft1, 'C1.', label = 'N = 512')
ax2.set_xlim(-50,50)
ax2.set_xlabel('k')
ax2.set_ylabel('f(k)')
ax2.legend()
ax2.set_title('Fourier Transform of Box function')

plt.show()
	
