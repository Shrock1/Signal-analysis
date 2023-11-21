
x = np.loadtxt('ECG_50Hz.txt')


fs = 500


fc_low = 49.5
fc_high = 50.5


nyq = 0.5 * fs
order, wn = signal.buttord([fc_low/nyq, fc_high/nyq], [fc_low/nyq-1, fc_high/nyq+1], 3, 40) 


b, a = signal.butter(order, wn, btype='bandstop')


y = signal.filtfilt(b, a, x)


plt.figure(figsize=(12,6))
plt.plot(x, label='Исходный сигнал')
plt.plot(y, label='Отфильтрованный сигнал')
plt.legend()
plt.xlabel('Отсчеты')
plt.ylabel('Амплитуда')
plt.title('Электрокардиограмма')
plt.show()


f, Pxx = signal.periodogram(x, fs)
f, Pyy = signal.periodogram(y, fs)


plt.figure(figsize=(12,6))
plt.semilogy(f, Pxx, label='Исходный сигнал')
plt.semilogy(f, Pyy, label='Отфильтрованный сигнал')
plt.legend()
plt.xlabel('Частота (Гц)')
plt.ylabel('Спектр мощности')
plt.title('Спектр мощности')
plt.show()


w, h = signal.freqz(b, a, worN=8000)
f = w / (2 * np.pi) * fs
magnitude = np.abs(h)
plt.figure(figsize=(12,6))
plt.plot(f, magnitude, label='АЧХ')
plt.legend()
plt.xlabel('Частота (Гц)')
plt.ylabel('Амплитуда')
plt.title('АЧХ фильтра (линейный масштаб)')
plt.show()

plt.figure(figsize=(12,6))
plt.semilogx(f, 20*np.log10(magnitude), label='АЧХ')
plt.legend()
plt.xlabel('Частота (Гц)')
plt.ylabel('Амплитуда (дБ)')
plt.title('АЧХ фильтра (логарифмический масштаб)')
plt.show()

