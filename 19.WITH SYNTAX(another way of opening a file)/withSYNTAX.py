with open(r"C:\Users\Aayushi Bhatt\Desktop\python\19.WITH SYNTAX(another way of opening a file)\normalFile.txt","r") as f:
    data = f.read()
    print(data)

with open(r"C:\Users\Aayushi Bhatt\Desktop\python\19.WITH SYNTAX(another way of opening a file)\normalFile.txt","w") as f:
    f.write("new data")
       