# Regular methods in a class automatically takes the instance as the first argument i.e., self
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
    
    @classmethod
    def set_raise_amount(cls,amount): #cls common convention for class we can use other name as well whic is passed as first argument
        cls.raise_amount = amount

    # Class method can be used as an alternate constructor 
    @classmethod
    def from_string(cls,empstr):
        first,last,pay = emp_str1.split("-")
        return cls(first,last,pay) # which is same as Employee(first,last,pay)
    
    #Static Method: don't pass anthing automatically like instance(self ) or class(cls)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1 = Employee("Rachana","Mahesh",50000)
emp2 = Employee("Test","User",60000)

Employee.set_raise_amount(1.5) # we can also run class method from instance variable i.e., emp1.set_raise_amount(1.5) but it doesn't make any sense
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

emp_str1 ="John-Doe-70000"
emp_str2 ="Steve-Job-30000"

# first,last,pay = emp_str1.split("-")
# new_emp1 = Employee(first,last,pay)
new_emp1 = Employee.from_string(emp_str1)

print(new_emp1.email)
print(new_emp1.fullname())

import datetime
my_date = datetime.date(2025,2,25)

print(Employee.is_workday(my_date))


#-----------------------------------------------------------------------------------------
