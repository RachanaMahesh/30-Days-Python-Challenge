# print(3+4)
# print('a'+'b')
# depending on what objects we are working with, addition actually has different behaviour
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

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.fname,self.lname,self.pay)
    
    def __str__(self):
        return "{} -> {}".format(self.fullname(),self.email)
    
    def __add__(self,other):
        return self.pay+other.pay
    
    def __len__(self):
        return len(self.fullname())
    
emp1 = Employee("Rachana","Mahesh",50000)
emp2 = Employee("Test","User",60000)

# print(emp1)
# print(str(emp1))
# print(repr(emp1))
# print(emp1.__str__()) # results same as above 
# print(emp1.__repr__()) # results same as above 

print(int.__add__(2,3)) # print(3+4)
print(str.__add__('a','b')) # print('a'+'b')
print(emp1 + emp2) #print(emp1.__add__(emp2))

print(len("Hello"))
print("Hello".__len__())
print(len(emp1))
print(emp2.__len__())