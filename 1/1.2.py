import numpy as np


def F(mas):
    l = 0
    for i in range(0, len(mas) // 2):
        mas[i] = (mas[i] + mas[i + 1]) / 2
        mas = np.delete(mas, i + 1)
    return mas


mas = np.loadtxt('mean2.txt')
while (len(mas) > 1):
    mas = F(mas)
print(mas)
