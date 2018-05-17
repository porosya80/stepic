result = [0, 0]
for i in range(int(input())):
    mass = list(input().lower().split())

    if mass[0] == "восток":
        result[0] += int(mass[1])
    elif mass[0] == "запад":
        result[0] -= int(mass[1])
    elif mass[0] == "север":
        result[1] += int(mass[1])
    elif mass[0] == "юг":
        result[1] -= int(mass[1])


print(result[0],result[1])
