# write a function that replaces all occurences of "java" with "python" in the above file.

def replacing_java():
    with open(r"C:\Users\Aayushi Bhatt\Desktop\python\20.DELETING A FILE\sample.txt","r") as f:
        data=f.read()
        new_data=data.replace("java","python")
        print(new_data)    
    with open(r"C:\Users\Aayushi Bhatt\Desktop\python\20.DELETING A FILE\sample.txt","w") as f:
        f.write(new_data)


replacing_java()