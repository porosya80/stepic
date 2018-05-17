


str1 = (input())
str2 = (input())
# str1 = "abcd"
# str2 = "*d%#"
to_sec = (input())
to_enc = (input())
# to_sec = "abacabadaba"
# to_enc = "#*%*d*%"
cipher = list(zip(str1, str2))

def decode(text):
    result = ""
    for i in text:
        for e, d in cipher:
            if i == d:
                result += e
    return result

def encode(text):
    result = ""
    for i in text:
        for e, d in cipher:

            if i == e:
                result += d
    return result


print(encode(to_sec))
print(decode(to_enc))


