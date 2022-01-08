# Display grade of a student based on marks

m1 = int(input("Enter first marks :"))
m2 = int(input("Enter second marks :"))

if m1 > 80 and m2 > 80:
    print('A')
elif m1 > 80:
    print('B')
elif m2 > 80:
    print('C')
else:
    print('D')
