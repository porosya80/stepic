import copy
# matrix = []
n = m = 0
while not (1 <= int(n) <= 100) or not (1 <= int(m) <= 100):
    n, m = map(int, input().split())



matrix = [[st for st in (input())] for n in (range(n))]
matrix_next = copy.deepcopy(matrix)


for y in range(n):
    for x in range(m):
        result = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if matrix[(y+j)%n][(x+i)%m] == "X":
                    # print("ccord {} {}".format(y+j,xp))
                    result += 1
        if result == 3 or (result == 2 and matrix[y][x] == "X"):
            matrix_next[y][x] = "X"
        else:
            matrix_next[y][x] = "."



for i in matrix_next:
    for j in i:
        print(j, end="")
    print()

