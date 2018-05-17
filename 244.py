# seq = [[ int(i)  for i in (input()) if int(i) % 4 == 0] for n in range(int(input()))]
#
# print (seq)

seq = []
for i in range(int(input())):
    dec = int(input())
    if dec %4 == 0:
        seq.append(dec)
seq.sort()
print(seq[-1])