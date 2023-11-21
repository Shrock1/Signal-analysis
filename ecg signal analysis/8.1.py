
num = [0.2, 0.4, 0.2]
den = [1, -0.4, 0.2]

h = np.zeros(1000) 
h[0] = 1 / den[0] 
for i in range(1, 1000): 
    r = 0 
    for j in range(min(i+1, len(num))): 
        r += num[j] * h[i-j]
    q = np.zeros(i+1) 
    q[0] = r / den[0] 
    for j in range(1, i+1): 
        s = 0 
        for k in range(min(j+1, len(num))):
            s += num[k] * q[j-k]
        q[j] = (r + s) / den[0]
    h[i] = q[i] 


print(h[:10])


n = np.arange(1000)
plt.figure(figsize=(8, 5))
plt.stem(n, h)
plt.title('Импульсная характеристика')
plt.xlabel('n') 
plt.ylabel('h[n]') 
plt.grid()
plt.show()


w = np.linspace(0, np.pi, 1000) 
z = np.exp(1j*w) 
H = (0.2 + 0.4*z**(-1) + 0.2*z**(-2)) / (1 - 0.4*z**(-1) + 0.2*z**(-2)) 

plt.figure(figsize=(8, 5))
plt.plot(w/np.pi, np.abs(H)) 
plt.title('Частотная характеристика')
plt.xlabel('Нормализованная частота')
plt.ylabel('Величина')
plt.grid()
plt.show()


epsilon = 1e-6 
if np.max(np.abs(np.roots(den))) < 1 + epsilon: 
    if np.min(np.abs(H)) < np.sqrt(2)/2 - epsilon: 

        print('Фильтр представляет собой БИХ ФНЧ')
        cutoff_index = np.argmin(np.abs(np.abs(H) - np.sqrt(2)/2))
        cutoff_freq = np.linspace(0, np.pi, 1000)[cutoff_index]/(2*np.pi)
        print('Частота среза на уровне -3 дБ составляет:', cutoff_freq)

