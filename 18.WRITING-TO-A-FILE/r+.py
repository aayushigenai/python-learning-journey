# the stream is positoined at the begning of the file. overwrite at the starting of the file.
# "r+"---> is for reading and writing.
#abcd is a good girl .

f=open(r"C:\Users\Aayushi Bhatt\Desktop\python\18.WRITING-TO-A-FILE\sample.txt","r+")
f.write("tbhd")   #tbhd is a good girl.
print(f.read())   #is a good girl.
f.close()


