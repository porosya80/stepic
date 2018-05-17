def get_int(start_message, error_message, end_message):
    print(start_message)
    x=input()
    while True:
        try:
            x = int(x)
            print(end_message)
            return x
            break
        except:
            print(start_message)
            x = input()




print(get_int("begin","eroor","end"))