
def dft(x, N):
    Ah = [0] * N
    Bh = [0] * N

    for k in range(N):
        for n in range(N):

            Ah[k] += x[n] * math.cos(2 * math.pi * k * n / N)
            Bh[k] += x[n] * math.sin(2 * math.pi * k * n / N)


    return Ah, Bh


duration = 2  
sampling_rate = 100  # Гц
freq1 = 10  # Гц
amp1 = 1.2
freq2 = 20  # Гц
amp2 = 2


t = np.linspace(0, duration, num=int(duration * sampling_rate))
x = amp1 * np.sin(2 * np.pi * freq1 * t) + amp2 * np.sin(2 * np.pi * freq2 * t)


N = len(x)
Ah, Bh = dft(x, N)
amp_spec = [2 * math.sqrt(Ah[k]**2 + Bh[k]**2) / N for k in range(N//2)]
freqs = (np.arange(N//2) * sampling_rate)/ N * 2


fig, axs = plt.subplots(2)
fig.suptitle('Сумма синусоидальных сигналов (10 Гц, 1.2 амп.; 20 Гц, 2 амп.) при частоте дискретизации 100 Гц')
axs[0].plot(t, x)
axs[0].set_xlabel('Время (с)')
axs[0].set_ylabel('Амплитуда')
axs[1].stem(freqs, amp_spec)
axs[1].set_xlabel('Частота (Гц)')
axs[1].set_ylabel('Амплитуда')
plt.show()
