import numpy as np

a = np.loadtxt('mean1.txt')
print(a)

a1 = 0  
h1 = len(a)  


def em_sred(x, s, h1):  
    x_summ = 0
    for i in range(s, s + h1):
        x_summ = x_summ + x[i]
    return x_summ / (h1)


otwet1_1 = em_sred(a, a1, h1)
print(otwet1_1)