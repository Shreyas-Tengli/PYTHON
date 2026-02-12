import math

radius=float(input("Enter the readius of the circle: "))
cir=2*(math.pi)*radius
area=(math.pi)*pow(radius,2)
print(f"the circumference of the circle is {round(cir,2)} cm")
print(f"the area of the circle is {round(area,2)} cm^2")