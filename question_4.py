"""
Power spectrum of 1024 random number generated between 0 and 1
"""

import numpy as np
import matplotlib.pyplot as plt

shift = np.fft.fftshift
N = 1024

data = np.random.rand(N) #generating 1024 random number between 0 and 1
xarr = np.arange(1, N+1, 1)




#power spectrum
dft = np.fft.fft(data, norm = 'ortho')
karr = np.fft.fftfreq(N, d = 1)

p = dft*np.conj(dft)/dft.size

print("Minimum value of wavevector is",min(karr))
print("and the maximum value is",max(karr))

#bin
n = 5
bin_length = int(N/n)
bins_data = np.zeros(bin_length)

for i in range(bin_length):
	s = 0
	for j in range(n):
		s = s + p[i + j*bin_length]
	bins_data[i] = s/n
k_bin = 2*np.pi*np.fft.fftfreq(bin_length, d = 1)

#ploting the generated random number
plt.figure()
plt.plot(xarr, data, "m")
plt.xlabel('i')
plt.ylabel('y')
plt.title("Generated sample")
plt.xlim(-2,1030)

#ploting the power spectrum
plt.figure()
plt.plot(shift(karr), shift(p.real), "b.-")
plt.xlabel('k')
plt.ylabel('P')
plt.title("Power spectrum")

#plot of bin power spectrum
plt.figure()
plt.plot(shift(k_bin), shift(bins_data.real), c = "g")
plt.xlabel('bin number')
#plt.ylim(0,1e-4)
plt.ylabel('P')
plt.title("Binned Power spectrum")	




plt.show()

