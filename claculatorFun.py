def add(x,y):
    return x+y;

def sub(x,y):
    return x-y;

def mul(x,y):
    return x*y;

def div(x,y):
    return float(x)/float(y);

def tryAgain():
    print("\tworng input")
    t= str(input("try again y/n => "))
        
    if(t=="y"):
        print("\n")
        userInput();
    else:
        print("\n\nGood bye............................")


def compute(x,y,z):
    if(z=="+"):
        print(f"\t{x} + {y} = {add(x,y)}")
    elif(z=="-"):
        print(f"\t{x} - {y} = {sub(x,y)}")
    elif(z=="*"):
        print(f"\t{x} x {y} = {mul(x,y)}")
    elif(z=="/"):
        print(f"\t{x} / {y} = {div(x,y)}")
    else:
        print(z," is invalid")
        tryAgain()

def userInput():
    try:
        n1= input("\nEnter First Number => ")
        n2= input("Enter Second Number => ")
        op= str(input("Select operator [+, -, *, /] => "))
        compute(n1,n2,op)
    except:
        tryAgain()
    



userInput()