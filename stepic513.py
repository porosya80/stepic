string = [len(i) for i in input().split()]

ready = {}
print(string)

for i in string:
    if i in ready:
        ready[i] += 1
    else:
        ready[i] = 1

for i in sorted(ready):
    print("{}: {}".format(i, ready[i]))