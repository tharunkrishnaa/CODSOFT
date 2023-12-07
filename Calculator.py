#Calculator using Python
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
num1=int(input("Enter Number 1: "))
num2=int(input("Enter Number 2: "))
choice=int(input("Enter your choice number: "))
if choice==1:
    print("Result= ",num1+num2)
elif choice==2:
    print("Result= ",num1-num2)
elif choice==3:
    print("Result= ",num1*num2)
elif choice==4:
    if num2==0:
        print("Cannot Divide by zero")
        num2=int(input("Enter another number other than 0: "))
    else:
        print("Result= ",num1/num2)
else:
    print("Invalid Input")
        
