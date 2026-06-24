#recusrsive function

def show(n):
    if(n==0):     ## base case , condition when the function stops or return.
        return
    print(n)
    show(n-1)

show(5)    