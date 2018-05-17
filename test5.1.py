# digit = int(input())
#
# while digit != 1:
#     print(int(digit), end=" ")
#     if digit%2 == 0:
#         digit /= 2
#     else:
#         digit = digit *3 +1
#
# print (int(digit))
#


def cd():
    i = 5
    while i > 0:
        yield i
        i -= 1


print (list(cd()))

for i in cd():
    print (i)