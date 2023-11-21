import numpy as np
import matplotlib.pyplot as plt

def em_sred(x, s, h1):
    x_sum = sum(x[s:s + h1])
    return x_sum / h1

def variance(x, s, h1):
    ff = em_sred(x, s, h1)
    y = 0
    for i in range(s, h1 + s):
        y = y + (x[i] - ff) ** 2
    return y / h1

def Correlation(X, Y, t, N):
    Mx = em_sred(X, 0, N)
    Dx = variance(X, 0, N)
    My = em_sred(Y, t, N)
    Dy = variance(Y, t, N)

    sum_M = 0
    for i in range(0, N):
        sum_M = (X[i] - Mx) * (Y[i + t] - My) + sum_M
    correl = (sum_M) / ((((Dx) * (Dy)) ** (1 / 2)) * N)
    return correl

t = 200
N = 1000
Y = np.zeros(t)

with open("Red_noise.txt") as file:
    X = [float(line.strip().replace(",", ".")) for line in file]

for i in range(t):
    correl = Correlation(X, X, i, N)
    Y[i] = correl

plt.subplot(2, 1, 1)
plt.title('АКФ ')
plt.plot(list(range(t)), Y, color='pink')
plt.xlabel('Длина ')
plt.ylabel('Корреляция')
plt.subplot(2, 1, 2)
plt.title('Исходный ряд')
plt.plot(list(range(len(X[:N]))), X[:N], color='orange')
plt.xlabel('Длина ')
plt.ylabel('Значение')
plt.grid(True)
plt.show()