a = 238
b = 30

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(a,b))