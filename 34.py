words = input().lower().split()
res = {}

for word in words:
    if word in res.keys():
        res[word] += 1
    else:
        res[word] = 1

for key, val in res.items():
    print(val, key)


















# a aa abC aa ac abc bcd a