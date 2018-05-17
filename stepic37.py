
results = []
digits = input().split()
f_d = input()

for i in range(len(digits)):
    if digits[i] == f_d:
        results.append(str(i))


if len(results) > 0:
    print(" ".join(results))
else:
    print("None")