# @property decorator allows us to define a method but we can access it like an attribute
class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        # self.email = fname+'.'+lname+'@company.com'

    @property
    def email(self): 
        return "{}.{}@company.com".format(self.fname,self.lname)
    
    @property
    def fullname(self): 
        return "{} {}".format(self.fname,self.lname)

    @fullname.setter # nameoftheproperty.setter
    def fullname(self,name): 
        fname, lname = name.split(" ")
        self.fname = fname
        self.lname = lname

    @fullname.deleter # nameoftheproperty.deleter
    def fullname(self):
        print("Deleted!")
        self.fname = None
        self.lname = None

      
emp1 = Employee("Rachana","Mahesh")
emp2 = Employee("Test","User")

# print(emp1.fname)
# print(emp1.email)
# print(emp1.fullname())

#-----GETTERS Example-------
# emp1.fname = "Madhu"

# print(emp1.fname)
# print(emp1.email) # email will still have old fname but it shld get updated whenever fname or lname is updated
# print(emp1.fullname())

#-----SETTERS Example-------
emp1.fullname = "John Smith"

# print(emp1.fname)
# print(emp1.email)
# print(emp1.fullname)

#-----DELETERS Example-------
del emp1.fullname
# print(emp1.fullname)

# It allows us to access attributes without getters & setters everywherebut if we need that functionality then its easy to add in with the 
# property decorator & if u do this correctly then people using our class won't even need to change any of there code bcoz they'll still be 
# to access those attributes in the same way that they did before now
# In below example we have changes fullname() [methos] into fullname [attribute] as setter to change first & lastname