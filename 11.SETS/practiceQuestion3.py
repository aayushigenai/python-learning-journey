#Write a Python program (WAP) to enter marks of 3 subjects from the user and store them in a dictionary.
#Requirements:
#Start with an empty dictionary.
#Add the subjects one by one.
#Use the subject name as the key.
#Use the marks as the value.

subj1=int(input("enter the marks of subject 1 :"))
subj2=int(input("enter the marks of subject 2 :"))
subj3=int(input("enter the marks of subject 3 :"))
subjects={}
subjects["subject1"]=subj1
subjects["subject2"]=subj2
subjects["subject3"]=subj3

print(subjects)


