#In a+ mode the stream is posioned at the end of the file.
#opned for reading and writing the file.

f=open(r"C:\Users\Aayushi Bhatt\Desktop\python\18.WRITING-TO-A-FILE\sample3.txt","a+")
print(f.read())
f.write("abcd ")     #got written in the end of the file.
f.read()               #nothing got printed.
f.close()
