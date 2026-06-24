#write a function to print "ODD", if the number is odd and "EVEN" if the number is even.
num=int(input("enter the number :"))
def even_OR_odd(num):
    if(num%2==0):
        print("EVEN")
    else:
        print("ODD")    


even_OR_odd(num)

