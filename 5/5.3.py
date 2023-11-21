import math
import matplotlib.pyplot as plt
import numpy as np

def DFT(S, N): 

  
    if N%2 == 0:
        M = round(N/2)
    else:
        M = round(N/2)+1



    a = []
    b = []
    
    for h in range(M):
        ah = 0
        bh = 0
        for i in range(N):
            ah += S[i] * math.cos(2 * math.pi * h * (i/N))
            bh += S[i] * math.sin(2 * math.pi * h * (i/N))
        ah *= (2/N)
        bh *= (-2/N)
  
        a.append(ah)
        b.append(bh)
    return a,b

def daniell_spectrum(mas, length, n): 
    Ah, Bh = DFT(mas, len(mas)) 
    S = [] 
    for i in range(len(Ah)):
        S.append(Ah[i]**2+Bh[i]**2)
  
    S_result = [] 
    for h in range(len(S)): 
        if h >= n and h <= len(Ah) - n - 1:
            x = 0
            for i in range(h-n, h+n):
                x += S[i]
            S_result.append(x/(2*n+1))
  

    return S_result 

def Welch(mas, length, Wn, Ws, win_code): 
    C = (length - Wn)//Ws + 1
    S = []
    for i in range(C):
      
        S_i = windowing(mas[Ws*i:Ws*(i)+Wn], Wn, win_code)

        Ah, Bh = DFT(S_i, len(S_i))
        S_i = []
        for j in range(len(Ah)):
            S_i.append(Ah[j]**2+Bh[j]**2)
  
        if i == 0:
            S = S_i
        else:
            S = [ S[i] + S_i[i] for i in range(len(S))]
 
    S = [i/C for i in S]
    return S


def windowing(mas, N, code):
    result_mas = []
   
    if code == 1:
        for i in range(len(mas)):
            if i >= 0 and i < N:
                result_mas.append(mas[i])
            else:
                result_mas.append(0)
  
    elif code == 2:
        for i in range(len(mas)):
            result_mas.append(mas[i]*(1-2*abs((i-N/2)/N)))

    elif code == 3:
        for i in range(len(mas)):
            result_mas.append(mas[i]*(0.53836-0.46164*math.cos(2*math.pi*i/(N-1))))


y = np.loadtxt("noise.txt")


S = daniell_spectrum(y, len(y), 100)
S1 = daniell_spectrum(y, len(y), 500)
S2 = daniell_spectrum(y, len(y), 1000)
S3 = daniell_spectrum(y, len(y), 2000)


plt.subplot(2,2,1)
plt.plot(range(len(S)), S)
plt.title('Спектр реализации белого шума')
plt.xlabel('Частота - Гц')
plt.ylabel('Мощность - дБ')
plt.subplot(2,2,2)
plt.plot(range(len(S1)), S1)
plt.title('Спектр реализации белого шума')
plt.xlabel('Частота - Гц')
plt.ylabel('Мощность - дБ')
plt.subplot(2,2,3)
plt.plot(range(len(S2)), S2)
plt.xlabel('Частота - Гц')
plt.ylabel('Мощность - дБ')
plt.subplot(2,2,4)
plt.plot(range(len(S3)), S3)
plt.xlabel('Частота - Гц')
plt.ylabel('Мощность - дБ')
plt.show()
