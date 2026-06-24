#when a text file is already been read using read() function it returns empty line 
# when tried to read it again using readline() function.

f = open(r"C:\Users\Aayushi Bhatt\Desktop\python\17.INPUT-OUTPUT-IN -PYTHON\demo.txt", "r")
line = f.read()
print(line)
line = f.readline()   #empty line
print(line)    
line1=f.readline()    #empty line
print(line1)