import numpy as np
import matplotlib.pyplot as plt
import math


def DFT(x, N):
    if N % 2 == 0:
        M = N // 2
    else:
        M = (N // 2) + 1

    a_m = []
    b_m = []
    for h in range(0, M):
        a = 0
        b = 0
        for i in range(0, N):
            a += x[i] * np.cos(2 * np.pi * h * i / N)
            b += x[i] * np.sin(2 * np.pi * h * i / N)
        a_m.append(a * 2 / N)
        b_m.append(b * 2 / N)
    return (a_m, b_m)


def Data(): 
    x = np.loadtxt('lfp.txt', dtype=float) 
    f_d = 1000  
    df = f_d / len(x)  
  

    a_mas, b_mas = DFT(x, len(x))  
    S = np.zeros(len(a_mas))  
    h = np.arange(len(a_mas)) 

    f = h * df  

    for i in range(len(a_mas)):
        S[i] = np.sqrt(pow(a_mas[i], 2) + pow(b_mas[i], 2)) 

    max_p = max(S)  
    power = S / max_p 
    dec = np.zeros(len(power)) 

    for i in range(len(power)):
        dec[i] = 10 * math.log10(power[i])  

    return (S, f, dec)  


S, f, dec = Data()  

plt.subplot(1, 2, 1)
plt.plot(f, S,'purple')  
plt.ylabel('S(f)')

plt.subplot(1, 2, 2)
plt.plot(f, dec, 'm')  
plt.xlabel('f, Гц')
plt.ylabel('S(f), дБ')
plt.show()

