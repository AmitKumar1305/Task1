# Year = int(input("enter the year"))
#
# if Year % 4 == 0 and Year % 100 != 0 or Year % 400 == 0:
#     print("Year is leap year")
# else:
#     print("this is not leap year")
num1 = int(input("enter first number"))
num2 = int(input("enter first number"))
num3 = int(input("enter first number"))

if num1 == num2 == num3:
    print("That is triangle")
elif num1 == num2 != num3:
    print("that is bilateral")
else:
    print("this is square")
