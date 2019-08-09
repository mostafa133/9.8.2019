# exercise:
# create Employee class
# __init__ (self, name, address, salary)
# create salary getter/setter to avoid negative salary
# implement __str__
#
# create Manager class
# __init__ (self, name, address, salary, numberOfEmployeesBenieth)
#     call super() ...
# implement __str__  and call super()__str__
# create a manager and chnage it salary to something invalid and print
#    then change it to something valid and print
class Employee:
    def __init__(self, name, address, salary):
        self.name = name
        self.adress = address
        self.salary = salary
    def __str__(self):
        return f'name : {self.name},' \
            f' adress : {self.adress},' \
            f' salary: {self.salary}'

class Manager(Employee):
    def __init__(self,name, address, salary, numberOfEmployeesBenieth ):
        #self.name = name
        #self.address = address
        #self.salary = salary
        super().__init__(name, address, salary)
        self.numberOfEmployeesBenieth = numberOfEmployeesBenieth
    def __str__(self):
        return super().__str__() + f' {self.numberOfEmployeesBenieth}'

moste = Manager('moste', 'kawkab', 8500, 98)
print(moste)


