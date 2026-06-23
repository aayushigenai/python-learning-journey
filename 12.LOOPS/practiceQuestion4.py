#search for a number x in this tuple using loop.
#[1,4,9,16,25,36,49,64,81,100]


x= int(input("enter the number to be searched :"))
t=(1,4,9,16,25,36,49,64,81,100)
i=0
while(i<len(t)):
    if(x==t[i]):
        print(i) 
        break  
    i+=1
print("loop ended")            

