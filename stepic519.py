txt = input()
fnd = input()

result = ""
if fnd not in txt: result = "-1"


for i in range(len(txt)):
    if txt[i:i+len(fnd)] == fnd:
        result = result + str(i) + " "

print (result)


#
# # if fnd in txt:
# pos = 0
# # indexx = 0
# result = ""
# for i in range(len(txt)-(len(fnd)-1)):
#     # print(pos)
#
#     indexx = (txt.find(fnd, i))
#     print(indexx)
#
#     listr.append(indexx)
# listrr=set(listr)
# listr=list(listrr)
# listr.sort()
#
# print (*listr)
# # print(" ".join(listr))

