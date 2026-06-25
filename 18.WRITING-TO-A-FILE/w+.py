# open for reading and writing.
#the stream is positioned at the begning of the file.
# the file is created if it does not exsist, otherwise it is turnicated(whole data is wiped out).


f=open(r"C:\Users\Aayushi Bhatt\Desktop\python\18.WRITING-TO-A-FILE\sample2.txt","w+")
f.write("I am happy and hello hello.")
print(f.read())
f.write("i am unhappy and no hello hello")
f.close()