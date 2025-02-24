class Employee:
    raise_amount = 1.04
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
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount

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

class Developer(Employee):
    raise_amount = 1.10 # for Developer() instance 1.10 is updated without making any changes to the raise_amount in parent class
    def __init__(self, fname, lname, pay,prog_lang):
        super().__init__(fname, lname, pay)
        # Employee.__init__(self,fname,lname,pay) will result the same of the above line
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, fname, lname, pay,emp= None):
        super().__init__(fname, lname, pay)
        if emp == None:
            self.employees = []
        self.employees = emp

    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def display_employee(self):
        for employee in self.employees:
            print("->", employee.fullname())

emp1 = Employee("John","Smith",45000)
emp2 = Employee("Subiya","Siraj",80000)

dev1 = Developer("Rachana","Mahesh",50000,"Python")
dwv2 = Developer("Test","User",60000,"Java")

# print(dev1.email)
# print(dev1.fullname())
# print(dev1.prog_lang)

# print(dev1.pay)
# dev1.apply_rise()
# print(dev1.pay)

mng1 = Manager("Mayur","Bhushan",100000,[emp1])
mng1.add_employee(emp2)
mng1.display_employee()
mng1.remove_employee(emp1)
mng1.display_employee()
