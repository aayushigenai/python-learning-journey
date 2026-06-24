#default parameters are parameters where assigned a default value to the parameter.
def prod_calc(a=4,b=4):
    product=a*b
    print(product)
    return product

prod_calc()

def cal_sum(a,b=4):
    sum=a+b
    print(sum)
    return sum

cal_sum(10)

