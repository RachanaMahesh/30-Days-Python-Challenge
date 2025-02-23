# Classes grp up the data & functions in a way that's easy to use & also to buuild upon if need be
# class Employee:
#     pass

# emp1 = Employee()
# emp2 = Employee()
# print(emp1)
# print(emp2)

# emp1.fname = "Rachana"
# emp1.lname = "Mahesh"
# emp1.pay = 50000
# emp1.email = "rachana.mahesh@company.com"

# emp2.fname = "test"
# emp2.lname = "user"
# emp2.pay = 60000
# emp2.email = "test.user@company.com"

# print(emp1.email)

class Employee:
    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname+'.'+lname+'@company.com'

    def fullname(self): # self is to pass the instance as an argument
        return "{} {}".format(self.fname,self.lname)
    # def fullname():
    #     return "{} {}".format(self.fname,self.lname)

    
emp1 = Employee("Rachana","Mahesh",50000)
emp2 = Employee("Test","User",60000)
# print(emp1.email)
# print(emp2.email)
print(Employee.fullname(emp1)) # Need to pass the instance as an argument
# By default emp1.fullname() passes the instance during function call 
print(emp1.fullname()) # Error out when we don't self as a parameter while defining the function

