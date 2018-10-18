def closest_mod_5(x):
    y = x
    while (not(y >= x and y % 5 == 0)):
        y += 1
    return y


print(closest_mod_5(29))
