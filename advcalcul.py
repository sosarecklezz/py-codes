from math import pi

def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
def floor (x,y):
    return x // y
def power (x,y):
    return x ** y

while 1:
    print()
    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Floor")
    print("6. Power")
    print("7. Get Radius")
    print("0. EXIT")

    choice =input("Enter a choice 1/2/3/4/5/6/7/0: ")

    if choice == '0':
        break
    if choice >'7':
        print("Invalid input")
        continue
    if choice == '7':
        r =float(input("Enter radius of circle you want to compute: "))
        print("Circle with radius: " + str(r) + " is: " + str(pi*r**2))
        continue
    num =int(input("Enter a number: "))
    num2 =int(input("Enter another number: "))

    if choice == '1':
        print(num, "+", num2, "=", add(num,num2))
    elif choice == '2':
        print(num,"-",num2,"=", subtract(num,num2))
    elif choice == '3':
        print(num,"*",num2,"=",multiply(num,num2))
    elif choice == '4':
        print(num,"/",num2,"=",divide(num,num2))
    elif choice == '5':
        print(num,"//",num2,"=",floor(num,num2))
    elif choice == '6':
        print(num,"**",num2,"=",power(num,num2))
    
    
