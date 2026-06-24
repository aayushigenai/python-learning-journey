#factorial recursive function

def fact(n):
    if(n==0 or n==1):         #base case
        return 1
    return n * fact(n-1)     #recurrence relationship
    
    
print(fact(4))    
