# matrix = []
n = m = 0
while not (1 <= int(n) <= 100) or not (1 <= int(m) <= 100):
    n, m = input("n , m :").split()

m = int(m)
n = int(n)

matrix = [[st for st in (input())] for n in (range(n))]

for y in range(n):
    for x in range(m):
        if matrix[y][x] != "*":
            matrix[y][x] = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    elif -1 < (x + i) < m and -1 < (y + j) < n:
                        if matrix[y + j][x + i] == "*": matrix[y][x] += 1

for i in matrix:
    for j in i:
        print(j, end=" ")
    print()
