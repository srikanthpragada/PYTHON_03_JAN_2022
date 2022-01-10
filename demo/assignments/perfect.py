# Take a number and check whether it is prefect number

num = int(input("Enter a number :"))
total = 1
for n in range(2, num//2 + 1):
    if num % n == 0:
        total += n

if total == num:
    print("Perfect")
else:
    print("Not perfect")
