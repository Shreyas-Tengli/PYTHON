operator=input("Enter the operator to use (+ - * /): ")
a=int(input("enter the number a: "))
b=int(input("enter the number b: "))

if operator == "+":
    result=print(f"The ADDITION of {a} and {b} is ", (round(a+b,3)))
elif operator == "-":
    result=print(f"The SUBTRACTION of {a} and {b} is ", (round(a-b,3)))
elif operator == "*":
    result=print(f"The MULTIPLICATION of {a} and {b} is ", (round(a*b,3)))
elif operator == "/":
    result=print(f"The DIVISION of {a} and {b} is ", (round(a/b,3)))
else:
    print(f"please enter a valid operator ")

#how to call operator itself without exiting the code?