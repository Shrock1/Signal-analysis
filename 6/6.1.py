def convolution(xi, len_xi, hi, len_hi, i):  # Определение функции convolution, которая будет использоваться для считывания

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

xi = [1, 2, 3, 4, 5] 
n = len(xi) 
print(n)
hi = [0.5, 0.25, 0.125] 
m = len(hi) 
print(m)

y_arrow = [] 
for i in range(len(xi)): 
    y = convolution(xi, n, hi, m, i)
    y_arrow.append(y) 
   
print("Результат свёртки = ", y_arrow)



