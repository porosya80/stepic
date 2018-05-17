

def modify_list(l):
    l[:] = [i//2 for i in l if  i%2 == 0]
    # return l


    # for i in lst:
    #     if not i%2 == 0:
    #         lst.remove(i)
    # for i in range(len(lst)):
    #     lst[i] = lst[i]//2





lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]


