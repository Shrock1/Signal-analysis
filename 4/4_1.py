

def DPF(X, N): 
    if (N % 2 == 0):
        M = N // 2
    else:
        M = ((N // 2) + 1)
    A_k = np.zeros(N)  
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


Signal = np.loadtxt('X2000Hz.txt')
Signal = Signal[:,1]
Signal2 = Signal[::10]
f1 = 2000
f2 = 200

df1 = f1 / (len(Signal))
df2 = f2 / (len(Signal2))

mAk1, mBk1 = DPF(Signal, len(Signal))
mAk2, mBk2 = DPF(Signal2, len(Signal2))

S1 = np.zeros(len(mAk1))
S2 = np.zeros(len(mAk2))
h1 = np.arange(len(mAk1))
h2 = np.arange(len(mAk2))
F1 = df1 * h1
F2 = df2 * h2

for i in range(len(mAk1)):
    S1[i] = np.sqrt((mAk1[i]) ** 2 + (mBk1[i]) ** 2)
for i in range(len(mAk2)):
    S2[i] = np.sqrt((mAk2[i]) ** 2 + (mBk2[i]) ** 2)

fig1 = plt.figure()
ax0 = fig1.add_subplot(3, 1, 1)
ax0.plot(F1, S1, label='signal 2000Hz', color='red')
ax0.set_xlabel('F')
ax0.set_ylabel('S')
plt.legend(loc=0)
ax1 = fig1.add_subplot(3, 1, 2)
ax1.plot(F2, S2, label='signal2 200Hz', color='blue')
ax1.set_xlabel('F')
ax1.set_ylabel('S')
ax2 = fig1.add_subplot(3, 1, 3)
ax2.plot(F1, S1, label='signal2 2000Hz', color='red')
ax2.plot(F2, S2, label='signal2 200Hz', color='blue')
ax2.set_xlabel('F')
ax2.set_ylabel('S')
plt.show()
print(Signal)
print(len(Signal2))
