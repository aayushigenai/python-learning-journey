#write a recursive function to print all elements in a list.
#hint: use list and index as same parameters.

def printList(list,indx=0):
    if(indx==len(list)):
        return
    print(list[indx])
    printList(list,indx+1)

list=["mango", "licchi","papaya","grapes","pineapple"]
print(printList(list))    