

def bartlett(arr, N):
    W=[]
    for i in range (N):
        t = (i-(N/2))/N
        w = 1-2*abs(t)
        W.append(w)

    return(W)

fa = 10 
fb = 15
A=1 
B=1.5 
Fsamp = 100 
dt = 0.001   

N=3000

x=[]  

for i in range (N):
    xi = A*sin(2*pi*fa*i*dt)+B*cos(2*pi*fb*i*dt)
    x.append(xi)
print(len(x))



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

bartlett_original = bartlett(x, len(x))
hamming_original = hamming(x, len(x))
rectangle_window_original = rectangle_window(x, len(x))

bartlett_row=[]
hamming_row = []
rectangle_window_row=[]
for i in range (len(x)):
    bartlett_row.append(bartlett_original[i]*x[i])
    hamming_row.append(hamming_original[i]*x[i])
    rectangle_window_row.append(rectangle_window_original[i]*x[i])

print(bartlett_row)
print(hamming_row)
print(rectangle_window_row)

