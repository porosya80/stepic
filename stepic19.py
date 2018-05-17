def t():
    print('true')
    return True

def f():
    print('false')
    return False
print ("1")
if t() and f():
    print('t and f')
print("2")
if f() and t():
    print('f and t')
print("3")
if t() or f():
    print('t or f')
print("4")
if f() or t():
    print('f or t')