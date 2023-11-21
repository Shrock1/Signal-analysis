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


def Data():
    x = np.loadtxt('Noise.txt', dtype=float)
    ##plt.plot(x)
    ##plt.show()
    f_d = 10
    df = f_d / len(x)

    window = 100  # ширина окна усреднения
    n_number = window // 2
    number = 1

    S = Welch(x, len(x), window, n_number, number)
    h = np.arange(len(S))
    f = h * df  # частоты ряда

    return (S, f, window, n_number, number)  # возвражение соответствующих значений


S, f, window, n_number, number = Data()  # возвражаем значения из функции

plt.plot(f, S, 'g')  # Спектр мощности Даньелла
plt.xlabel('f, Гц')
plt.ylabel('S(f), window = ' + str(window) + ' сдвиг = ' + str(n_number))
plt.show()
