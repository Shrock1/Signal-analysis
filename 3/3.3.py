

def dft(x, N):
    Ah = [0] * N
    Bh = [0] * N

    for k in range(N):
        for n in range(N):
            Ah[k] += x[n] * math.cos(2 * math.pi * k * n / N)
            Bh[k] += x[n] * math.sin(2 * math.pi * k * n / N)

    return Ah, Bh



freq = 10  
period = 2 * np.pi / freq
t = np.linspace(0, 5 * period, num=50)  
x = np.sin(freq * t)


N = len(x)
Ah, Bh = dft(x, N)
amp_spec = [2 * math.sqrt(Ah[k]**2 + Bh[k]**2) / N for k in range(N//2)]



fig, axs = plt.subplots(2)
fig.suptitle('Синусоидальная волна с 10 отсчетами за период')
axs[0].plot(t, x)
axs[0].set_xlabel('Время (с)')
axs[0].set_ylabel('Амплитуда')
axs[1].stem(amp_spec)
axs[1].set_xlabel('Частота')
axs[1].set_ylabel('Амплитуда')
plt.show()
