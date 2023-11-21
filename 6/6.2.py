import numpy as np
import matplotlib.pyplot as plt

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


x = np.loadtxt("xi.txt", skiprows=1) 
X = x[:, 1]
print(X) 
h = np.loadtxt("hi.txt", skiprows=1) 

H = h[:, 1]
print(H) 

y_arrow = [] 
for i in range(len(X)):
    y = convolution(X, len(X), H, len(H), i)
    y_arrow.append(y)
print("Результат свёртки = ", y_arrow)

plt.subplot(2, 2, 1)
for k in range(len(X)):
    plt.vlines(x=1 * k, ymin=0, ymax=X[k]) 
plt.title('x. Временная реализация')
plt.xlabel('f, Гц')
plt.ylabel('S(fhi)')
plt.grid()

plt.subplot(2, 2, 2)
for k in range(len(H)):
    plt.vlines(x=1 * k, ymin=0, ymax=H[k]) 
plt.title('h. Импульсная характеристика')
plt.xlabel('f, Гц')
plt.ylabel('S(fhi)')
plt.grid()

plt.subplot(2, 2, 3)
for k in range(len(y_arrow)):
    plt.vlines(x=1 * k, ymin=0, ymax=y_arrow[k])
plt.title('Реализация свёртки')
plt.xlabel('f, Гц')
plt.ylabel('S(fhi)')
plt.grid()

plt.show()
