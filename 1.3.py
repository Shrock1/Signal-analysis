import numpy as np

a = np.loadtxt('mean1.txt')
print(a)

a1 = 0 
h1 = len(a)  



def estimate_variance(x, s, h1):
    mean = np.mean(x[s:s+h1])
    variance = np.mean((x[s:s+h1] - mean)**2)
    return variance

otwet1_1 = estimate_variance(a, a1, h1)
print(otwet1_1)