dic={

    "name" : "Aayushi",
    "age" : 34,
    "course": "CSE",
    "isAdult":True,

}

#to return all the keys
print(dic.keys())

#to return all the keys in the form of list(doing typecasting)
print(list(dic.keys()))

# to return length of the dic
print(len(dic))
print(len(list(dic.keys())))

#to return all the values
print(dic.values()) 

# to return all key value pairs as tuple
print(dic.items())

#to return the value of the key
print(dic["name"])
#-->returns an error when serched for a key that do not exsist
 # print(dic["name2"]) returns an error.


print(dic.get("name"))
#--> returns none when searched for a key that do not exsist.
print(dic.get("name2"))


#adding new key , value pair
dic.update({"city":"jaipur"})
print(dic)
