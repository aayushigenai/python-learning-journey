#print the multiplication table of a number n.
n=int(input("enter the number :"))
seq=range(1,11,1)
for i in seq:
    print(n*i)
    i+=1