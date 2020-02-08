#Solving A
#We get error from someVar + someOtherVar because the two variables both have contrasting data types. When combining two variables, they both have to be converted into the same data types, through the process of type casting.
someVar = 1
someOtherVar = "one"

print(str(someVar) + str(someOtherVar))

#Solving B
someList = [3, "S", "B", 21]
strs = [i for i in someList if type(i) == str]
ints = [i for i in someList if type(i) == int]

print(strs)
print(ints)

#Solving E
someList =  [3, -3, 4, -5]
neg = [i for i in someList if i < 0]
pos = [i for i in someList if i > 0]

print(neg)
print(pos)