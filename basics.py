#functions
# A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the value that is sent to the function when it is called
# An array is a special variable, which can hold more than one value at a time.
# in order to use array you havre to import numpy library
# inorder to rempove an item in an array use: pop() or remove()
# example: cars.remove("Volvo")
# inorder to add an item into the array use: append()
# example:cars.append("Honda")

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = person("Eunice",22)

print(p1.name)
print(p1.age)

class vehicle:
    def __init__(self,model,year):
        self.model = model
        self.year = year

v1 = vehicle("axela",2016)
v2 = vehicle("camry",2018)    

print(v1.model,v1.year)
print(v2.model,v2.year)
