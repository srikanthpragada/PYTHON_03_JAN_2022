# Display biggest of 3 numbers

a, b, c = 10, 60, 30

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
elif b > c:
    print(b)
else:
    print(c)
