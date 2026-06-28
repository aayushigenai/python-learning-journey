#create a class called Order which stores item and its priice.
# use dunder function__get__() to convey that:
# order1 >order2 if price of order1> price of order2.

class Order:

    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,o2):
        return self.price > o2.price

o1= Order("chips",60)
o2= Order("kurkure",50)

print(o1>o2)

