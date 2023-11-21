import numpy as np
from math import pi, sin, cos
from matplotlib import pyplot as plt
import os
os.chdir(os.path.dirname(__file__))


def what_M(x):
    if len(x)%2==0:
        M=len(x)//2
    else:
        M=(len(x)//2)+1
    return(M)

def Discrete_Fourier_Transform(array, N, M):
    A=[]
    B=[]
    for h in range (M):
        sum_a=0
        sum_b=0
        for i in range (N):
            sum_a+=array[i]*cos((2*pi*h*i)/N)
            sum_b+=array[i]*sin((2*pi*h*i)/N)
        a = (2/N)*sum_a
        b = (-2/N)*sum_b
        A.append(a)
        B.append(b)
    return (A, B)

def create_Sfhi(sin_x, duration):
    M = what_M(sin_x)
    df= Fsamp/duration
    DFT = Discrete_Fourier_Transform(sin_x, duration, M)
    Sfhi=[]
    for i in range (len(DFT[0])):
        Sfhi.append(((DFT[0][i])**2 + (DFT[1][i])**2)**(1/2))
    return (Sfhi, M, df)


def bartlett(arr, N):
    W=[]
    for i in range (N):
        t = (i-(N/2))/N
        w = 1-2*abs(t)
        W.append(w)
    return(W)

def hamming(arr, N):
    W=[]
    for i in range (N):
        t = (i-(N/2))/N
        w = 0.46*cos(2*pi*t)+0.54
        W.append(w)
    return(W)

def rectangle_window(arr, N):
    W=[]
    for i in range (N):
        if 0<=i<=N-1:
            w=1
        else: w=0
        W.append(w)
    return(W)



duration1 = 3000#длительность ряда
duration3 = 2992
T = 1
dt = T/30
f = 1/T
Fsamp = 1/dt
dt_arr= np.arange(0, T*100, dt)
sin_x=[]
for i in range (duration1):#строит значения синуса
    x = sin(2*pi*f*i*dt)
    sin_x.append(x)

bartlett_original = bartlett(sin_x, len(sin_x))
hamming_original = hamming(sin_x, len(sin_x))
rectangle_window_original = rectangle_window(sin_x, len(sin_x))


bartlett_row=[]
hamming_row = []
rectangle_window_row=[]
for i in range (len(sin_x)):#умножаем исходный сигнал на результат оконных преобразований, чтобы получить преобразованный сигнал
    bartlett_row.append(bartlett_original[i]*sin_x[i])
    hamming_row.append(hamming_original[i]*sin_x[i])
    rectangle_window_row.append(rectangle_window_original[i]*sin_x[i])





Sfhi1 = create_Sfhi(sin_x, duration1)
Sfhi_row1 = Sfhi1[0]
df1=Sfhi1[2]
M1 = Sfhi1[1]

Sfhi1_1 = create_Sfhi(bartlett_row, duration1)
Sfhi_row1_1  = Sfhi1_1 [0]
df1_1 =Sfhi1_1 [2]
M1_1 = Sfhi1_1[1]

Sfhi1_2 = create_Sfhi(hamming_row, duration1)
Sfhi_row1_2 = Sfhi1_2[0]
df1_2=Sfhi1_2[2]
M1_2 = Sfhi1_2[1]

Sfhi1_3 = create_Sfhi(rectangle_window_row, duration1)
Sfhi_row1_3 = Sfhi1_3[0]
df1_3=Sfhi1_3[2]
M1_3 = Sfhi1_3[1]

plt.subplot(1,2,1)

'''for h in range (M1):
    plt.vlines(x=df1*h, ymin=0, ymax=Sfhi_row1[h], color = 'r')
for h in range (M1_1):
    plt.vlines(x=df1_1*h, ymin=0, ymax=Sfhi_row1_1[h], alpha = 0.8,color = 'g')
for h in range (M1_2):
    plt.vlines(x=df1_2*h, ymin=0, ymax=Sfhi_row1_2[h], alpha = 0.8,color = 'b')
for h in range (M1_3):
    plt.vlines(x=df1_3*h, ymin=0, ymax=Sfhi_row1_3[h], alpha = 0.8,color = 'm')'''

x_row=[]
x_row_1=[]
x_row_2=[]
x_row_3=[]
for h in range (M1):
    x_row.append(df1*h)
for h in range (M1_1):
    x_row_1.append(df1_1*h)
for h in range (M1_2):
    x_row_2.append(df1_2*h)
for h in range (M1_3):
    x_row_3.append(df1_3*h)


plt.plot (x_row,  Sfhi_row1, color = 'r', label = "оригинал")
plt.plot (x_row_1,  Sfhi_row1_1, alpha = 0.5, color = 'g', label = "барлетт")
plt.plot (x_row_2,  Sfhi_row1_2, alpha = 0.5, color = 'b', label = "хэмминг")
plt.plot (x_row_3,  Sfhi_row1_3, alpha = 0.5, color = 'm', label = "прямоугольное")


plt.title('3000 DFT для ряда')
plt.xlabel('f, Гц')
plt.ylabel('S(fhi)')
plt.grid()

bartlett_oroginal3 = bartlett(sin_x, duration3)
hamming_priginal3 = hamming(sin_x, duration3)
rectangle_window_original3 = rectangle_window(sin_x, duration3)


bartlett_row3=[]
hamming_row3 = []
rectangle_window_row3=[]
for i in range (len(sin_x[0:2992])):
    bartlett_row3.append(bartlett_oroginal3[i]*sin_x[i])
    hamming_row3.append(hamming_priginal3[i]*sin_x[i])
    rectangle_window_row3.append(rectangle_window_original3[i]*sin_x[i])

Sfhi3 = create_Sfhi(sin_x, duration3)
Sfhi_row3 = Sfhi3[0]
df3=Sfhi3[2]
M3 = Sfhi3[1]

Sfhi3_1 = create_Sfhi(bartlett_row3, duration3)
Sfhi_row3_1  = Sfhi3_1 [0]
df3_1 =Sfhi3_1 [2]
M3_1 = Sfhi3_1[1]

Sfhi3_2 = create_Sfhi(hamming_row3, duration3)
Sfhi_row3_2 = Sfhi3_2[0]
df3_2=Sfhi3_2[2]
M3_2 = Sfhi3_2[1]

Sfhi3_3 = create_Sfhi(rectangle_window_row3, duration3)
Sfhi_row3_3 = Sfhi3_3[0]
df3_3=Sfhi3_3[2]
M3_3 = Sfhi3_3[1]

plt.subplot(1,2,2)

x_row1=[]
x_row1_1=[]
x_row1_2=[]
x_row1_3=[]
for h in range (M3):
    x_row1.append(df3*h)
for h in range (M3_1):
    x_row1_1.append(df3_1*h)
for h in range (M3_2):
    x_row1_2.append(df3_2*h)
for h in range (M3_3):
    x_row1_3.append(df3_3*h)


plt.plot (x_row1,  Sfhi_row3, color = 'r', label = "original")
plt.plot (x_row1_1,  Sfhi_row3_1, alpha = 0.5, color = 'g', label = "бартлетт")
plt.plot (x_row1_2,  Sfhi_row3_2, alpha = 0.5, color = 'b', label = "хэмминг")
plt.plot (x_row1_3,  Sfhi_row3_3, alpha = 0.5, color = 'm', label = "прямоугольное")



plt.title('2992 DFT для ряда')
plt.xlabel('f, Гц')
plt.ylabel('S(fhi)')
plt. legend()
plt.grid()



plt.show()
