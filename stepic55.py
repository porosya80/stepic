CONV_TABLE = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))


input_string = 1985
result = 0


result = ''
for arab, roman in CONV_TABLE:
   print(arab, roman)
   while input_string >= arab:
       result += roman
       input_string -= arab

print(result)