item=input("enter the food u want to eat: ")
price=float(input("Enter the Price of the item: "))
quantity=int(input("Enter the number of items you want to buy: "))

total=price*quantity

print(f"You are being billed for {item} of quntity {quantity}")

print(f"Your total bill is ${total}")