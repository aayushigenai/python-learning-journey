#write a program to find the factorial of first n numbers.

n=int(input("enter the first n numbers :"))


fact=1
i=1
for i in range(1,n+1):
    fact*=i
    i+=1
print(fact)    