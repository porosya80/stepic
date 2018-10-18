

def power(a, n):
    if n < 0:
        return power(1 / a, -n)
    elif n == 0:
        return 1
    elif n == 1:
        return a
    elif n % 2 == 0:
        return power(a * a,  n / 2)
    elif n % 2 != 0:
        return a * power(a * a, (n - 1) / 2)


a = int(input())
n = int(input())

print(power(a, n))

# Function
# exp_by_squaring(x, n)
# if n < 0  then return exp_by_squaring(1 / x, -n);
# else if n = 0  then return 1;
# else if n = 1  then return x;
# else if n is even  then return exp_by_squaring(x * x, n / 2);
# else if n is odd  then return x * exp_by_squaring(x * x, (n - 1) / 2);
