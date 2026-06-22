#write aprogram to check if a list contains a palindrome of elements.(hint:use copy() method.)

list1=[1,2,3,2,1]
list2=list1.copy()
list2.reverse()
if(list2==list1):
    print("it is a palindrome")
else:
    print("not a palindrome")    

list3=[4,5,6]
list4 =list3.copy()
list4.reverse()
if(list4 == list3):
    print("it is a palindrome")
else:
    print("not a palindrome")    