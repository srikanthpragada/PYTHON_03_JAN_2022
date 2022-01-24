a = 1     # Global variable

def f1():
    global a
    b = 100  # Enclosing variable
    a = a + 1

    def f2():
        nonlocal b
        b = 10
        c = 200    # Local variable
        print(a, b, c)

    f2()  # call local function
    print(b)


f1()
