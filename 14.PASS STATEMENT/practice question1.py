#write a program to find the sum of first n numbers.(using while)

n=int(input("enter the first n numbers :"))
i=1
sum=0
while(i<=n):
    sum+=i
    i+=1
print(sum)    