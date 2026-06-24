#first function
def sum_function(a ,b ):
    sum=a+b
    print(sum)
    return sum

sum_function(10,30)
sum_function(20,20) 

#second function
def calc_sum(x,y):
    sum=x+y
    return sum

sum1= calc_sum(25,25)
print(sum1)


#third function
def print_hello(): # no parameters passed
    print("hello")

print_hello()  
output=print_hello()
print(output)       #output is none as the function is not returning anything.