cmd_list = []
new_cmd = ""


while new_cmd != "End":
    new_cmd = input()
    cmd_list.append(new_cmd)


cmd_list.remove("End")

for i in cmd_list:
    print('Processing "{}" command...'.format(i))

print("Good bye!")
