# Calculate net amount

price = int(input("Enter Price :"))
qty = int(input("Enter Qty :"))

amount = price * qty
discount = amount * 0.10
discounted_amount = amount - discount
tax = discounted_amount * 7 / 100
net_amount = discounted_amount + tax

# Display invoice/bill

print(f"Amount          {amount:10.2f}")
print(f"- Discount      {discount:10.2f}")
print(f"                -----------")
print(f"                {discounted_amount:10.2f}")
print(f"+ Tax           {tax:10.2f}")
print(f"                -----------")
print(f"Net Amount      {net_amount:10.2f}")
print(f"                -----------")
