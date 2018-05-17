n = int(input())

for i in range(n+1):
    if n==0: break
    for j in range(i):
        if n == 0:
            break
        print (i,end=" ")
        n -= 1

