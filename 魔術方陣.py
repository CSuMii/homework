import numpy as NP

N = int(input())
num = NP.zeros((N,N), dtype=int) #3*3,當無數字就補0

f = 1 #起始數字

x, y = 0, N//2 #(i,j=N//2取整數)
while f <= N**2: #N**2=平方
    num[x, y] = f
    f += 1
    nx, ny = (x-1) % N, (y+1)% N
    if num[nx, ny]: #新的
        x += 1
    else:
        x, y = nx, ny

print(num)