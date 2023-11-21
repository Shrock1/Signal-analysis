



fa = 10 
fb = 15
A=1 
B=1.5 
Fsamp = 100 
dt = 0.001   

N=3000

x=[]  
T_points=[]
for i in range (N):
    xi = A*sin(2*pi*fa*i*dt)+B*cos(2*pi*fb*i*dt)
    x.append(xi)
    T_points.append(i*dt)
print(len(x))

plt.subplot(1,2,1)
plt.plot(T_points, x, "blue")
plt.title('signal')
plt.xlabel('Длительность ряда')
plt.ylabel('Амплитуда сигнала')
plt.grid()
plt.show()

def DPF(X, N): #функция быстро преобразования ,сначала определяем колчиество гармоник M ,где h-индекс гармоники,N-длина временного ряда
    if (N % 2 == 0):
        M = N // 2
    else:
        M = ((N // 2) + 1)
    A_k = np.zeros(N)  #массив нулевой , для того , чтобы обращаться к индексам и менять их на нули
    B_k = np.zeros(N)
    for h in range(0, M):
        S_a = 0
        S_b = 0
        for i in range(0, N):
            S_a = X[i] * np.cos(2 * np.pi * h * i / N) + S_a
            S_b = X[i] * np.sin(2 * np.pi * h * i / N) + S_b
        A_k[h] = (2 / N) * S_a
        B_k[h] = ((-2) / N) * S_b
    return A_k, B_k
Signal = x
f1 = 100


df1 = f1 / (len(Signal))


mAk1, mBk1 = DPF(Signal, len(Signal))

S1 = np.zeros(len(mAk1))
h1 = np.arange(len(mAk1))
F1 = df1 * h1


for i in range(len(mAk1)):
    S1[i] = np.sqrt((mAk1[i]) ** 2 + (mBk1[i]) ** 2)


P=2453

y=[]  
T_points=[]
for i in range (P):
    yi = A*sin(2*pi*fa*i*dt)+B*cos(2*pi*fb*i*dt)
    y.append(yi)
    T_points.append(i*dt)
print(len(y))



def DPF(X, P): 
    if (P % 2 == 0):
        M = P // 2
    else:
        M = ((P // 2) + 1)
    A_k = np.zeros(P)  
    B_k = np.zeros(P)
    for h in range(0, M):
        S_a = 0
        S_b = 0
        for i in range(0, P):
            S_a = X[i] * np.cos(2 * np.pi * h * i / N) + S_a
            S_b = X[i] * np.sin(2 * np.pi * h * i / N) + S_b
        A_k[h] = (2 / P) * S_a
        B_k[h] = ((-2) / P) * S_b
    return A_k, B_k
Signal1 = y
f11 = 100


df11 = f11 / (len(Signal1))


mAk11, mBk11 = DPF(Signal1, len(Signal1))

S11 = np.zeros(len(mAk11))
h11 = np.arange(len(mAk11))
F11 = df11 * h11


for i in range(len(mAk11)):
    S11[i] = np.sqrt((mAk11[i]) ** 2 + (mBk11[i]) ** 2)



I=2756

u=[]  #массив временного ряда гармонического сигнала
T_points=[]
for i in range (I):#строит значения синуса
    ui = A*sin(2*pi*fa*i*dt)+B*cos(2*pi*fb*i*dt)
    u.append(ui)
    T_points.append(i*dt)
print(len(u))


def DPF(X, I): #функция быстро преобразования ,сначала определяем колчиество гармоник M ,где h-индекс гармоники,N-длина временного ряда
    if (I % 2 == 0):
        M = I // 2
    else:
        M = ((I // 2) + 1)
    A_k = np.zeros(I)  #массив нулевой , для того , чтобы обращаться к индексам и менять их на нули
    B_k = np.zeros(I)
    for h in range(0, M):
        S_a = 0
        S_b = 0
        for i in range(0, I):
            S_a = X[i] * np.cos(2 * np.pi * h * i / N) + S_a
            S_b = X[i] * np.sin(2 * np.pi * h * i / N) + S_b
        A_k[h] = (2 / I) * S_a
        B_k[h] = ((-2) / I) * S_b
    return A_k, B_k
Signal11 = u
f111 = 100


df111 = f111 / (len(Signal11))


mAk111, mBk111 = DPF(Signal11, len(Signal11))

S111 = np.zeros(len(mAk111))
h111 = np.arange(len(mAk111))
F111 = df111 * h111


for i in range(len(mAk111)):
    S111[i] = np.sqrt((mAk111[i]) ** 2 + (mBk111[i]) ** 2)


fig1 = plt.figure()
ax0 = fig1.add_subplot(4, 1, 1)
ax0.plot(F1, S1, label='signal N=3000', color='red')
ax0.set_xlabel('F')
ax0.set_ylabel('S')
plt.xlim(0.5,3)
plt.legend(loc=0)
ax1 = fig1.add_subplot(4, 1, 2)
ax1.plot(F111, S111, label='signal2 N=2999', color='purple')
ax1.set_xlabel('F')
plt.xlim(0.5,3)
ax1.set_ylabel('S')
ax2 = fig1.add_subplot(4, 1, 3)
ax2.plot(F11, S11, label='signal2 N=2992', color='green')
ax2.set_xlabel('F')
plt.xlim(0.5,3)
ax2.set_ylabel('S')
ax3 = fig1.add_subplot(4, 1, 4)
ax3.plot(F1, S1, label='signal2 3000', color='red')
ax3.plot(F111, S111, label='signal2 2999', color='purple')
ax3.plot(F11, S11, label='signal2 2992', color='blue')
ax3.set_xlabel('F')
plt.xlim(0.5,3)
ax3.set_ylabel('S')
plt.show()


