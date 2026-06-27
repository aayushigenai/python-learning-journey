class Person:

    def __hello(self):              #private function
        print("hello person")

    def welcome(self):              #private function called through another 
        self.__hello()              #normal function inside the class itself


p1 = Person()

print(p1.welcome())