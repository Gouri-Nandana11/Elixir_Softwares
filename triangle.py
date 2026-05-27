side1,side2,side3=int(input("enter the first side: ")),int(input("enter the second side: ")),int(input("enter the third side: "))
if side1==side2 and side2==side3:
    print("equilateral triangle")
elif side1==side2 or side2==side3 or side3==side1:
    print("isosceles triangle")
else:
    print("scalene triangle")