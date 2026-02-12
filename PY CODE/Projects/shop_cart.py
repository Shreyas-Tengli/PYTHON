foods=[]
prices=[]
total=0

while True:
    food=input("Enter the food you want(enter q to quit): ")
    if food.lower()=="q":
        break
    else:
        price=float(input("Enter the value of the food: "))
        foods.append(food)
        prices.append(price)
print("\n------ YOUR CART ------")
print(f"{'Item':15} {'Price':>10}")
print("-" * 26)

for i in range(len(foods)):
    print(f"{foods[i]:15} ₹{prices[i]:>9.2f}")
    total += prices[i]

print("-" * 26)
print(f"{'Total':15} ₹{total:>9.2f}")

