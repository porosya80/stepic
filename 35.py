def f(x):
    return x + 1


dic = {}
lent = []
for i in range(int(input())):
    lent.append(int(input()))
for i in lent:
    if i not in dic.keys():
        dic[i] = f(i)

print(dic.items())

for i in lent:
    print(dic[i])