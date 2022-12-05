n = int(input())
x = [[-1 for i in range(n)] for i in range(n)]

line = 0
col = n//2

cnt = 2
while cnt<=n**2:
    x[line][col] = cnt
    preline = line
    precol  =col
    line -= 1
    if line==-1:
        line = n-1
    col = (col+1)%n
    if x[line][col]!=-1 :
        line = preline +1
        col = precol
    cnt+=1

for item in x:
    print(item)