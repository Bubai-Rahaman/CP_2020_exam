"""
Linear congruential generator
"""

m = 429494
c = 10139
a = 16645
x = 1
x0 = x

n = 100000
for i in range(n):
	x = (a*x + c)%m
	if x == x0:
		print("Seed repeat in 1st case")
		break

print("Linear congruential generator gives random number with periodicity of m(modulus). If the numbers of random random number is very less then m then seed may never appears again. As in this case we generate 10000 random number but seed is never appears.")
x = x0
N = 10000
for i in range(N):
	x = (a*x + c)%m
	if x == x0:
		print("Seed repeat")
		break
	elif i == N-1:
		print("Seed value never appears again in the 2nd case")
