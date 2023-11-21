
import math

def rdft(Ah, Bh, M):


    N = len(Ah) 

    x = [0] * N

    for n in range(N):
        for k in range(M):
            x[n] += (Ah[k] * math.cos(2 * math.pi * k * n / N) + Bh[k] * math.sin(2 * math.pi * k * n / N))

    return x


Ah = [1, 0, 0, 0, 0, 0, 0, 0]
Bh = [0, 0, 0, 0, 0, 0, 1, 0]
M = 1

N = len(Ah)
x = [0] * N

for n in range(N):
    for k in range(M):
        x[n] += (Ah[k] * math.cos(2 * math.pi * k * n / N) + Bh[k] * math.sin(2 * math.pi * k * n / N))

print(x)

