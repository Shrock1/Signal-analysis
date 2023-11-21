
def what_M(x): 
    if len(x) % 2 == 0:
        M = len(x) // 2
    else:
        M = (len(x) // 2) + 1
    return (M)

def Discrete_Fourier_Transform(array, N, M): 
    A = []
    B = []
    for h in range(M):
        sum_a = 0
        sum_b = 0
        for i in range(N):
            sum_a += array[i] * cos((2 * pi * h * i) / N)
            sum_b += array[i] * sin((2 * pi * h * i) / N)
        a = (2 / N) * sum_a
        b = (-2 / N) * sum_b
        A.append(a)
        B.append(b)
    return (A, B)


def create_Sfhi(chanell, duration):
    M = what_M(chanell)
    df = Fsamp / duration
    DFT = Discrete_Fourier_Transform(chanell, duration, M)
    Sfhi = []
    for i in range(len(DFT[0])):
        Sfhi.append(((DFT[0][i]) ** 2 + (DFT[1][i]) ** 2) ** (1 / 2))
    return (Sfhi, M, df)


def convolution(xi, len_xi, hi, len_hi, i):
    M = len_hi
    yi = 0
    for k in range(M - 1):
        if i - k < 0:
            zero = 0
        else:
            zero = xi[i - k]
        y_sum = hi[k] * zero
        yi += y_sum
    return (yi)

X = np.loadtxt("xi_3sin.txt", skiprows=1) 
H = np.loadtxt("hi_BandPass100Hz_1kHz.txt", skiprows=1) 
Fsamp = 1000 

y_arrow = []
for i in range(len(X)):
    y = convolution(X, len(X), H, len(H), i)
    y_arrow.append(y)
print ("Результат свёртки = ", y_arrow)




SfhiX = create_Sfhi(X, len(X)) 
Sfhi_rowX = SfhiX[0] 
dfX = SfhiX[2] 
MX = SfhiX[1] 
plt.subplot(1, 4, 1)
for h in range(MX): 
    plt.vlines(x=dfX * h, ymin=0, ymax=Sfhi_rowX[h])
plt.title('X(f)')
plt.xlabel('f, Гц')
plt.ylabel('S(fhi)')


SfhiH = create_Sfhi(H, len(H))
Sfhi_rowH = SfhiH[0]
dfH = SfhiH[2]
MH = SfhiH[1]
plt.subplot(1, 4, 2)
for h in range(MH):
    plt.vlines(x=dfH * h, ymin=0, ymax=Sfhi_rowH[h])
plt.title('H(f)')
plt.xlabel('f, Гц')
plt.ylabel('S(fhi)')



Sfhiy = create_Sfhi(y_arrow, len(y_arrow))
Sfhi_rowy = Sfhiy[0]
dfy = Sfhiy[2]
My = Sfhiy[1]
plt.subplot(1, 4, 3)
for h in range(My):
    plt.vlines(x=dfy * h, ymin=0, ymax=Sfhi_rowy[h])
plt.title('Образ фурье канала Y')
plt.xlabel('f, Гц')
plt.ylabel('S(fhi)')

H_full=[] 
for i in range (len(H)): 
    H_full.append(H[i])
for i in range (len(X)-len(H)):
    H_full.append(0) 

print(len(H_full))
print(len(X))

xh=[]
for i in range (len(X)): 
    xh.append(H_full[i]*X[i])
print(H_full[i]*X[i]) 
Sfhixh = create_Sfhi(xh, len(xh)) 

Sfhi_rowxh = Sfhixh[0] 
dfxh=Sfhixh[2]
Mxh = Sfhixh[1]
plt.subplot(1,4,4)
for h in range (Mxh):
    plt.vlines(x=dfxh*h, ymin=0, ymax=Sfhi_rowxh[h])

Sfhi_rowy = Sfhiy[0]
Sfhi_rowy_new = []
for i in range(len(Sfhi_rowy)):
    Sfhi_rowy_new.append(Sfhi_rowy[i] * 0.1)
dfy = Sfhiy[2]
My = Sfhiy[1]
plt.subplot(1, 4, 4)
for h in range(My):
    plt.vlines(x=dfy * h, ymin=0, ymax=Sfhi_rowy_new[h])

plt.title('Образ фурье канала X*H')
plt.xlabel('f, Гц')
plt.ylabel('S(fhi)')

plt.show()
