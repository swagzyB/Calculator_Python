try:
    num1 = int(input("Enter First Number => "))
    num2 = int(input("Enter Second Number => "))
    operator = str(input("Select [+, -, *, /] => "))

    add = num1+num2
    sub=num1-num2
    mul=num1*num2
    div= float(num1) / float(num2)


    if(operator== "+"):
        print(f"{num1} + {num2} = {add}")
    elif(operator== "-"):
        print(f"{num1}  {num2} = {sub}")
    elif(operator== "*"):
        print(f"{num1} x {num2} = {mul}")
    elif(operator== "/"):
        print(f"{num1} / {num2} = {div}")
    else:
        print(operator," is an invaild operator")
except:
    print("Invaild number")

