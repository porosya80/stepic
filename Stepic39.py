list_d=[int(i) for i in input().split()]

set_d = set(list_d)

for dec in set_d:
    if dec in list_d:
        list_d.remove(dec)

new_set = set(list_d)
print (" ".join(map(str,new_set)))