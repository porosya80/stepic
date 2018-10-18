digits = [i for i in [int(input()) for i in range(4)]]

for i in range(digits[2], digits[3]+1):
    print("\t", i, end="")


for i in range(digits[0], digits[1]+1):
    print("\n", i, end="")
    for n in range(digits[2], digits[3] + 1):
        print("\t", i*n, end="")
