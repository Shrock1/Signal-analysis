


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


def Danell(x, N, window): 
    a_mas, b_mas = DFT(x, len(x)) 
    S = np.zeros(len(a_mas))  
    h = np.arange(len(a_mas))  

    for i in range(len(a_mas)):
        S[i] = np.sqrt(pow(a_mas[i], 2) + pow(b_mas[i], 2))

    S_d = np.zeros(len(S))

    n = int((window + 1) / 2)
    m = len(h)
    for i in range(len(S)):
        if n <= h[i] <= m - n - 1:
            summa = 0
            for j in range(h[i] - n, h[i] + n + 1):
                summa += S[j]
            S_d[i] = summa / (2 * n + 1)
        else:
            S_d[i] = S[i]
    return S_d, a_mas, b_mas


def Data():  
    N = 3000
    T = 30
    f_d = 1 / T  
    t = np.arange(N)
    x = np.sin(2 * np.pi * t / T)
    df = f_d / len(x) 

    window = 300  

    S_d, a_mas, b_mas = Danell(x, N, window)
    S = np.zeros(len(a_mas))
    h = np.arange(len(a_mas))
    f = h * df  

    for i in range(len(a_mas)):
        S[i] = np.sqrt(pow(a_mas[i], 2) + pow(b_mas[i], 2))

    return (S_d, S, f, window)  


S_d, S, f, window = Data()  

plt.subplot(3, 1, 1)
plt.plot(f, S, 'g')  
plt.xlabel('f, Гц')
plt.ylabel('S(f)')

plt.subplot(3, 1, 2)
plt.plot(f, S_d, 'r')  
plt.xlabel('f, Гц')
plt.ylabel('S(f), window = ' + str(window))

plt.subplot(3, 1, 3)
plt.plot(f, S_d, 'r')  
plt.plot(f, S, 'g') 
plt.xlabel('f, Гц')
plt.ylabel('S(f), window = ' + str(window))
plt.show()