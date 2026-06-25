# search if the word "learning" exsist in the file or not.

def chec_for_word():
    word="learning"
    with open(r"C:\Users\Aayushi Bhatt\Desktop\python\20.DELETING A FILE\sample.txt","r") as f:
        data=f.read()
        if(data.find(word) != -1):
            print("word found")
        else:
            print("not found")

chec_for_word()