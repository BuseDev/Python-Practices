a = 5
def b():
    a = 10
    print(a)
b()

def c():
    global a
    a = 10
    print(a)

c()
print(a)
