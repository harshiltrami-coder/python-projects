try:
    a = int(input("Enter the first number:- "))

    b = int(input("Enter the second number:- "))

    print("What kind of operation do you want to perform   press + for addition \n  press - for subtraction \n   press / for division \n  press * for multiplication ")

    o = input("Enter the operaion:- ")
    match o:
        case "+":
            print(f"The result is: {a+b}")
        case "-":
            print(f"The result is: {a-b}")
        case "/":
            print(f"The result is: {a/b}")
        case "*":
            print(f"The result is: {a*b}")
        case default:
            print("Please enter the valid operation!")

except Exception as e:
    print("Enter the valid value of a & b!!!")