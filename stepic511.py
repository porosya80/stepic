jolly_list = []
flag = 1

numbers = input().split()
for count in range(len(numbers)-1):
    jolly_list.append (abs(int(numbers[count]) - int(numbers[count+1])))

jolly_list = sorted(jolly_list)
for count in range(len(jolly_list)) :
    flag = 0
    if count+1 == jolly_list[count] :
        flag = 1
    else :
        flag = 0
        print ("Not jolly")
        break
if flag == 1:
    print ("Jolly")