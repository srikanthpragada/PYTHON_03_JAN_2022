# Calculate net amount

price = int(input("Enter Price :"))
discount = price * 0.10
discounted_price = price - discount
tax = discounted_price * 7 / 100
net_amount = discounted_price + tax
print("Net Amount = ", net_amount)

