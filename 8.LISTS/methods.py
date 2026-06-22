marks=[35,25,45,65,55]
print(marks.append(75))  
print(marks)
print(marks.sort())               #sorting in ascending order.
print(marks)            
print(marks.sort(reverse=True))   # sorting in descending order.
print(marks)  
print(marks.reverse())     
print(marks)        
print(marks.insert(1,10))
print(marks)

#all the functions are doing changes in the orignal lists, hence as an answer none is returned, cauze no new list is genrated, changes rae being done in orignal list.

list=["a","z","c","f","e","g"]
list.sort()
print(list)

list.remove("c") #removing first occurence of the element.
print(list)
list.pop(0)     #removing elemnet from particular index.
print(list)