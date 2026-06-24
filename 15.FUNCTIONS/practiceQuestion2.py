#write a function to print the elements of a list in a single line.(list is the parameter)

def print_elements(list):
    for ele in list:
        print(ele, end=" ")
    return list

print_elements(list=[1,2,3,4,5,6,7,8,9,10])    