string_under = input().split("_")
result = ""

for i in string_under:
    result += i.capitalize()

print(result)