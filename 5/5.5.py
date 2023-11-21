import numpy as np
import matplotlib.pyplot as plt


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


def O_P(x, N, number):
    k = np.arange(0, N, 1)
    t = (k - N / 2) / N
    if number == 1:
        Bartlett = 1 - 2 * abs(t)
        x_p = x * Bartlett
    elif number == 2:
        Hamming = 0.46 * np.cos(2 * np.pi * t) + 0.54
        x_p = x * Hamming
    elif number == 3:
        x_p = x
    return x_p


def Welch(x, N, window, n_number, number):
    C = (N - window) // n_number + 1
    y = O_P(x[:window], len(x[:window]), number)
    a_mas, b_mas = DFT(y, len(y))
    S = np.zeros(len(a_mas))
    h = np.arange(len(a_mas))
    for i in range(C):
        y = O_P(x[i * window:i * window + window],
                len(x[i * window:i * window + window]), number)
        a_mas, b_mas = DFT(y, len(y))
        for i in range(len(a_mas)):
            S[i] = S[i] + np.sqrt(pow(a_mas[i], 2) + pow(b_mas[i], 2))
    S = S / C
    return S

x = np.random.normal(size=1000)
window_size = 64
stride = 32
spectrum = Welch(x, len(x), window_size, stride, 2)


Fs = 1000  
N = len(x)  



Fs = 1000
freqs = np.arange(0, Fs/2, Fs/N)[:len(spectrum)]



freqs = np.arange(0, Fs/2, Fs/N)[:len(spectrum)]
plt.plot(freqs, spectrum)
plt.xlabel('Частота (Гц)')
plt.ylabel('Мощность')
plt.show()