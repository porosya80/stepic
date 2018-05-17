alphabet = [n for n in range(128512, 128592)]

sdvig = int(input())
text = input().strip()
result = []
dec = list(map(ord,text))

for i in dec:
    if i in alphabet:
        result.append(alphabet[(alphabet.index(i)+sdvig)%(len(alphabet))])


enc = list(map(chr,result))
# dec = map(chr,result)

print('Result: ' + '"' + ''.join(enc) + '"')