exList = []
chkText1 = []

for i in range(int(input())):
    exList.append(input().lower())

for i in range(int(input())):
    chkText1.extend(input().lower().split())
# exList = ["a","bb","cCc"]
# chkText1 = ["a","bb","aab","aba","ccc","c","bb","aaa"]

chkText = set(chkText1)

for i in set(exList).intersection(chkText):
    chkText.remove(i)

print("\n".join(chkText))
