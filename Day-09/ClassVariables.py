# Class variables are the variables that are shared among all instances of a class
# Instance variables can be unique for each instance like fname,lname,pay etc...

class Employee:
    raise_amount = 1.4
    no_of_employees = 0
    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname+'.'+lname+'@company.com'
        Employee.no_of_employees +=1

    def fullname(self): 
        return "{} {}".format(self.fname,self.lname)

    def apply_rise(self):
        self.pay = int(self.pay * self.raise_amount)
        # self.pay = int(self.pay * Employee.raise_amount)
#NOTE: when we try to access class variable we need to aceess it with a class itself i.e., Employee or instance of a class i.e., self
# using self.raise_amount will also allow subclass to override the constant if they wanted to 
print(Employee.no_of_employees)
emp1 = Employee("Rachana","Mahesh",50000)
emp2 = Employee("Test","User",60000)
print(emp1.no_of_employees) # or print(EMployeep1.no_of_employees) or print(emp2.no_of_employees) all are same 
# print(emp1.pay)
# emp1.apply_rise()

# when we try to access an attribute in an instance it first check if the instance contains taht attribute & if it doesn't then 
# it will see if the class or any class that it inherits from contains the attribute
print(emp1.__dict__)
# print(Employee.__dict__)

emp1.raise_amount = 1.5 # change the amount for the single instance 
print(emp1.__dict__)
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print(emp1.pay)
emp1.apply_rise()
print(emp1.pay)


