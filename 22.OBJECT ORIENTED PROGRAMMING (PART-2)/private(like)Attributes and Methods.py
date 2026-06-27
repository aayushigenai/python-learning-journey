#error occurs as the private attribute was accessed outside the class

"""class Account:

    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass

    #def acc_pass(self):
    #    print(self.__acc_pass)

a1=Account("1234","abcd")
print(a1.acc_no)
print(a1.__acc_pass) """   # error will occur as its a private attribute


class Account:

    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass

    def acc_pass(self):
        print(self.__acc_pass)

a1=Account("1234","abcd")
print(a1.acc_no)
print(a1.acc_pass())     #no error will occur as it accesed through a function that is declared inside 
                         #class only.