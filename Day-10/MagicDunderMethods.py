print(3+4)
print('a'+'b')
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


emp1 = Employee("Rachana","Mahesh",50000)
emp2 = Employee("Test","User",60000)
