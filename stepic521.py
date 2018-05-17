n = m = 0
while not(1 <= int(n) <= 100) or not(1 <= int(m) <= 100):
    n, m = input().split()


m = int(m)
n = int(n)

matrix = [[st for st in (input().split())] for n in (range(n))]

matrix_t = list(zip(*matrix))

for i in matrix_t:
    for j in i:
        print(j, end=" ")
    print()