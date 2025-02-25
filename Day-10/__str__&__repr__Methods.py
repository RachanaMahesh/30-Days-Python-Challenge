# Difference Btw __str__() & __repr__(). __ meand dunder
# Example 1:
import datetime
import pytz # type: ignore

date = datetime.datetime.now() #The result is a naive datetime object (it does not have timezone info).
print(date)
print(str(date))
print(repr(date))
print(eval("datetime.datetime(2025, 2, 25, 14, 0, 44, 668912)"))

#Example 3:

a = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC) #replace(tzinfo=pytz.UTC) attaches the UTC timezone explicitly to the datetime object.
b= str(a) #The str() function converts the datetime object into a string representation.

print("str(a) : {}".format(str(a)))
print("str(b) : {}".format(str(b)))
print()
print("repr(a) : {}".format(repr(a))) #repr(a): Shows the datetime object with all its details. gives an unambiguous representation useful for debugging.
print("repr(b) : {}".format(repr(b))) #repr(b): Shows a string representation of a, since b is already a string.repr(b) just shows b as a string, since b is already a string.

# Example 2:
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def __repr__(self):
        return f"Person('{self.name}',{self.age})"
    
p = Person("Abhi", 25)
# print(p.__str__())
# print(str(p))
# print(p.__repr__())
# print(repr(p))