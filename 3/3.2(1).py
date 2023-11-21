

import math

def rdft(Ah, Bh, M):
    N = len(Ah) + len(Bh) - 1 # Длина выходного временного ряда

    x = [0] * N

    for n in range(N):
        for k in range(M):
            if k < len(Ah):
                x[n] += Ah[k] * math.cos(2 * math.pi * k * n / N)
            if k < len(Bh):
                x[n] += Bh[k] * math.sin(2 * math.pi * k * n / N)

    return x



Ah = [1, 2, 3]
Bh = [0, 0, 0, 0]
M = 3

x = rdft(Ah, Bh, M)

print(x)
