#Form a file containing numbers seprated by comma , print the count of even numbers.
cout=0
with open(r"C:\Users\Aayushi Bhatt\Desktop\python\20.DELETING A FILE\practice.txt","r") as f:
    data=f.read()
    print(data)

    nums=data.split(",")
    for val in nums:
        if(int(val)%2==0):
            cout+=1

print(cout)             