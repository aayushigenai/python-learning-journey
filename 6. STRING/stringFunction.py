#first function (str.endwith(" "))
str="i am studying python"
print(str.endswith("thon"))
print(str.endswith("am"))

#second function (str.capitalize())
print(str.capitalize())   #new string created that has captial letter from start.
print(str)    #old string same as it is.

#if wanting to make changes in old string only.
str=print(str.capitalize())


#third function(str.replace(old,new))
str1="i am happy learning python"
print(str1.replace("t","l"))
print(str1.replace("python","javascript"))

#fourth function(str.find(" "))
print(str1.find("i"))
print(str1.find("z"))


#fivth function(str.count(" "))
print(str1.count("p"))
