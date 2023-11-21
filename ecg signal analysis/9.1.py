import numpy as np
import matplotlib.pyplot as plt


def fir_lpf(fc, fs, N):

    h = np.zeros(N)
    for n in range(N):
        if n == (N - 1) // 2:
            h[n] = 2 * fc / fs
        else:
            h[n] = 2 * fc / fs * np.sinc(2 * fc * (n - (N - 1) // 2) / fs)
    return h
# Загрузка данных
xi = np.loadtxt("xi.txt", skiprows=1)
X = xi[:, 1]


fs = 8000


fc = 1500


N = 101


h = fir_lpf(fc, fs, N)


Y = np.zeros_like(X)


for n in range(N-1, len(X)):
    Y[n] = np.sum(h * X[n-N+1:n+1])

plt.figure(figsize=(12,6))
plt.plot(X, label='Исходный сигнал')
plt.plot(Y, label='Отфильтрованный сигнал')
plt.legend()
plt.xlabel('Отсчеты')
plt.ylabel('Амплитуда')
plt.title('Сигнал до и после фильтрации')
plt.show()

Xf = np.fft.fft(X)
Yf = np
H = np.fft.fft(h)
f_H = np.fft.fftfreq(len(H), d=1/fs)
H_abs = np.abs(H)
H_ang = np.angle(H)
plt.figure(figsize=(12,6))
plt.plot(f_H, H_abs, label='АЧХ')
plt.xlabel('Частота, Гц')
plt.ylabel('Амплитуда')
plt.title('АЧХ ФНЧ КИХ-фильтра')
plt.legend()
plt.show()

plt.figure(figsize=(12,6))
plt.semilogx(f_H, H_abs)
plt.xlabel('Частота, Гц')
plt.ylabel('Амплитуда')
plt.title('АЧХ ФНЧ КИХ-фильтра в логарифмическом масштабе')
plt.grid()
plt.show()
plt.figure(figsize=(12,6))
plt.plot(f_H, H_ang)
plt.xlabel('Частота, Гц')
plt.ylabel('Фаза')
plt.title('Фазовая характеристика ФНЧ КИХ-фильтра')
plt.show()
Hf = np.fft.fft(h)
Pyyf = np.abs(Hf)**2 / len(h)
f_Hf = np.fft.fftfreq(len(h), d=1/fs)
plt.figure(figsize=(12,6))
plt.semilogx(f_Hf, Pyyf)
plt.xlabel('Частота, Гц')
plt.ylabel('Мощность')
plt.title('Спектр мощности ФНЧ КИХ-фильтра в логарифмическом масштабе')
plt.grid()
plt.show()