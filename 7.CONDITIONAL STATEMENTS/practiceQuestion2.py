#write a program to find greatest of three numbers entered by the user.

num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))

if(num1>num2 and num1>num3):
    print("greatest number is:",num1)
elif(num2>num3):
    print("gratest number is:",num2)
else:
    print(" greatest number is:",num3)        