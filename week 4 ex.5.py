#addition
def addition(a, b):
    print("addition:",a + b)

#substraction
def subtraction(a, b):
    print("subtraction:",a - b)

#Multiplication
def multiplication(a, b):
    print("multiplication:",a * b)

#Division
def division(a, b):
    print("division:",a / b)

function={"addition":addition,"subtraction":subtraction,"multiplication":multiplication,"division":division}
choice=input("call function:").lower().strip()
a=float(input("enter first number:"))
b=float(input("enter second number:"))
if choice in function:
    function[choice](a,b)
else:
    print("please enter a valid choice")



