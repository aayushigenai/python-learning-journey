dic={

    "name" : "Aayushi",
    "age" : 34,
    "course": "CSE",
    "isAdult":True,

}
print(dic)

#accesing values
print(dic["name"])
print(dic["age"])
print(dic["course"])
print(dic["isAdult"])

#changing exsisting values and adding new key and value pair.
dic["name"]="Ayushi" #overwrite
dic["surname"]="Bhatt"

print(dic)

#null dic

dic={}