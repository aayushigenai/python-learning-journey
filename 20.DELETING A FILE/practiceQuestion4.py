#write a function in which line of the file does the word "learning" occur first.
#Print -1  if word not found

def chec_for_word():
    word="learning"
    with open(r"C:\Users\Aayushi Bhatt\Desktop\python\20.DELETING A FILE\sample.txt","r") as f:
        data=f.read()
        if(data.find(word) != -1):
            print("word found")
        else:
            print("not found")

def check_for_line():
    word="learning"
    data=True
    line_no=1
    with open(r"C:\Users\Aayushi Bhatt\Desktop\python\20.DELETING A FILE\sample.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            else:
                line_no+=1
    return -1
check_for_line()