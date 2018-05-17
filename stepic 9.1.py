CARDS = {"a":9,"k":8,"q":7,"j":6,"10":5,"9":4,"8":3,"7":2,"6":1}

result = ""

first ,second = input().lower().split()
kozir = input().lower()

mast_first = first[-1]
mast_second= second[-1]
value_first = first[:-1]
value_second = second[:-1]





if mast_first == mast_second:
    if CARDS[value_first] > CARDS[value_second]:
        result = "First"
    else:
        result = "Second"
elif  mast_first == kozir:
        result = "First"
elif  mast_second == kozir:
        result = "second"
else:
        result = "Error"



print(result)



