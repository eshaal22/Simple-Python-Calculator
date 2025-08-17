# python calculator

print("Welcome to the python calculator!")
while True:

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Choose operation: +  -  *  /  %  **")
    print("Choose operation from the list below:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Modulus (%)")
    print("5. Division (/)")
    print("6. Power (**)")

    op = input("Enter operation: ")
    #addition
    if op == "+" or op=="1":
        print("The sum of the numbers is:", num1 + num2)
    #subtraction
    elif op == "-" or op=="2":
        print("The difference of the numbers is:", num1 - num2)
    #multiplication
    elif op == "*"or op=="3":
        print("The product of the numbers is:", num1 * num2)
    #modulus
    elif op == "%" or op=="4":
        if num2 != 0:
            print("The remainder of the numbers is:", num1 % num2)
        else:
            print("Error: Cannot modulus by zero")
    #division
    elif op == "/" or op=="5":
        if num2 != 0:
            print("The division of the numbers is:", num1 / num2)
        else:
            print("Error: Cannot divide by zero")
    #power
    elif op == "**" or op=="6":
        print("The power is:", num1 ** num2)
    else:
        print("Invalid operation")

    choice = input("Do you want to continue? : ")
    if choice.lower() == "no":
        print("Thank you for using the calculator!")
        break
    elif choice.lower()=="yes":
        continue
    else:
        print("Invalid choice, exiting the calculator.")
        break
