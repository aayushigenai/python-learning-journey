#write a function to find the factorial of n.(n is the parameter)

def fact_function(n):
    fact=1
    i=1
    while(i<=n):
        fact*=i
        i+=1
    print(fact)
    return fact

fact_function(5)    