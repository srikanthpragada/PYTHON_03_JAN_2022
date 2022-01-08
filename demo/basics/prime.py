# Display whether the given number is prime

num = int(input("Enter number :"))
prime = True
for n in range(2, num//2 + 1):
    if num % n == 0:
        print("Not a prime")
        prime = False
        break

if prime:
    print("Prime")


