# st = input()
st = "aaabccccCCaB"
count = 1


def spit(strin):
    res = []
    prev = ""
    buf = ""
    for i in range(1, len(st)):
        if strin[i] == strin[i-1]:
            buf += strin[i]
            # print(strin[i])
        else:
            buf += strin[i-1]
            print(buf)
            res.append(buf)
            buf = ""
        # prev = strin[i]

    return res





print(spit(st))




# for i in range(len(st) - 1):
#     if st[i] == st[i + 1]:
#         count += 1
#         lett = st[i]
#     else:
#         print(count, lett, st[i], sep="", end="")
#         count = 1
