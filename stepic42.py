# string = input()
string = "3ab4c2CaB"
enc = []
result = ""
i = 0
number = ""

while i < len(string):
    # print (i)

    if string[i].isdigit():
        number = ""
        while string[i].isdigit():
            number += string[i]
            i += 1

        enc.append((number, string[i]))
        i += 1
    elif string[i].isalpha():
        number = 1
        enc.append((number, string[i]))
        i += 1


for i ,b in enc:
    # print (int(i),b)
    print(int(i)*b,end="")

# print(enc)


# for  i in range(len(string)):
#     # print (ind)
#     if  string[i].isdecimal():
#         result += int(string[i]) * string[i + 1]
#         i += i
#     else:
#         result += string[i]




# string.
