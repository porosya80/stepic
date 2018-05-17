
CONV_TABLE = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))


input_string = input().upper()
result = 0

for arab, roman in CONV_TABLE:
    while input_string.startswith(roman):
        result += arab
        input_string = input_string[len(roman):]


print(result)
