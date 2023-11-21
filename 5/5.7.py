import numpy as np
import matplotlib.pyplot as plt


def DPF(x, N):
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


def Welch(x, N, window, s_number, number):
    C = (N - window) // s_number + 1
    y = O_P(x[:window], len(x[:window]), number)
    a_mas, b_mas = DPF(y, len(y))
    S = np.zeros(len(a_mas))
    h = np.arange(len(a_mas))
    for i in range(C):
        y = O_P(x[i * window:i * window + window],
                len(x[i * window:i * window + window]), number)
        a_mas, b_mas = DPF(y, len(y))
        for i in range(len(a_mas)):
            S[i] += np.sqrt(pow(a_mas[i], 2) + pow(b_mas[i], 2))
    S = S / C
    return S


def Danell(x, N, window):
    a_mas, b_mas = DPF(x, len(x))  # возвращаем значения ДПФ для основного ряда
    S = np.zeros(len(a_mas))  # массив для функции S основного ряда
    h = np.arange(len(a_mas))  # массив индексов основного ряда

    for i in range(len(a_mas)):  # цикл для определения S по формуле 3.15 из методички для основного ряда
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
    return S_d


def Data():
    N = 3000
    T = 30
    f_d = 1 / T
    df = f_d / N
    t = np.arange(N)
    x = np.sin(2 * np.pi * t / T)

    window = 300  # ширина окна усреднения
    n_number = window // 2
    number = 1

    S_w = Welch(x, N, window, n_number, number)
    h_w = np.arange(len(S_w))
    f_w = h_w * df  # частоты ряда

    S_d = Danell(x, N, window)
    h_d = np.arange(len(S_d))
    f_d = h_d * df

    return (S_w, f_w, S_d, f_d, window, n_number)


S_w, f_w, S_d, f_d, window, n_number = Data()

plt.subplot(2, 1, 1)
plt.plot(f_d, S_d, 'g', label='Danell')  # Спектр мощности Даньелла
plt.legend(loc='best')
plt.xlabel('f, Гц')
plt.ylabel('S(f), window = ' + str(window))

plt.subplot(2, 1, 2)
plt.plot(f_w, S_w, 'm', label='Welch')  # Спектр мощности Уэлча
plt.legend(loc='best')
plt.xlabel('f, Гц')
plt.ylabel('S(f), window = ' + str(window) + ' сдвиг = ' + str(n_number))
plt.show()
