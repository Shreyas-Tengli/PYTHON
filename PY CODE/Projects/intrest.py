p=0
r=0
t=0

while p<=0:
    p=float(input("Enter the principle amount: "))
    if p<=0:
        print("The amount shld be more than zero")

while r<=0:
    r=float(input("Enter the intrest rate: "))
    if r<=0:
        print("The rate shld be more than zero")

while t<=0:
    t=float(input("Enter the time in years: "))
    if t<=0:
        print("The amount shld be more than zero")

total= p * pow((1+r/100),t)

print(f"The interst after {t} year(s) is ${total:.2f}")