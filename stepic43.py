alphabet = ' abcdefghijklmnopqrstuvwxyz'

sdvig = int(input())
text = input().strip()
result = ""

for i in text:
    if i in alphabet:
        result += alphabet[(alphabet.index(i)+sdvig)%(len(alphabet))]

print('Result: "{}"'.format(result))

