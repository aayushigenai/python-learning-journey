# creating complex number 


class Complex:

    def __init__(self,real,img):
        self.real=real
        self.img=img


    def showNumber(self):
        print(self.real,"i +",self.img,"j")   

    def __add__(self,num2):                #dunder function
        newReal = self.real+num2.real
        newimag= self.img+num2.img
        return Complex(newReal , newimag)  

    def __sub__(self,num2):                #dunder function
        newReal = self.real-num2.real
        newimag= self.img-num2.img
        return Complex(newReal , newimag)    

c1=Complex(5,5)
c1.showNumber()     

c2=Complex(2,4)
c2.showNumber()

#c3=c1.add(c2)
#c3.showNumber()

c3=c1+c2
c3.showNumber()

c3=c1-c2
c3.showNumber()