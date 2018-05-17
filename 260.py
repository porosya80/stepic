# x = int(input())

def summ(dig):
    result = 0
    # print (len(str(dig)))

    if len(str(dig)) == 1:
        # print(dig)
        if  dig/3 == 1 or dig/3 == 2 or dig/3 == 3:
            print("YES")
        else:
            print("NO")

        return
    for i in str(dig):
        result += int(i)
    # print(result)
    summ(result)


summ(int(input()))

# print(type(x/3))
# result = "YES" if isinstance((x/3), int) else "NO"
#
# print(result)