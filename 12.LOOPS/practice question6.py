#search for a number x in this tuple using loop
#[1,4,9,16,25,36,49,64,81,100]
tup= (1,4,9,16,25,36,49,64,81,100)
x=int(input("enter the number x :"))
indx=0
for el in tup:
    if(el==x):
        print("found x at index :",indx)
    indx+=1



