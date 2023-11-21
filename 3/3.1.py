

def dft(x, N):
    Ah = [0] * N
    Bh = [0] * N

    for k in range(N):
        for n in range(N):

            Ah[k] += x[n] * math.cos(2 * math.pi * k * n / N)
            Bh[k] += x[n] * math.sin(2 * math.pi * k * n / N)


    return Ah, Bh

x = [1, 2, 3, 4, 5, 6, 7, 8]
N = 8
Ah, Bh = dft(x, N)

print(Ah)
print(Bh)
