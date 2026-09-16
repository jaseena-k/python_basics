# oops - Object oriented programming
# class -blue print of object (structure of object) class is a user define data type
# object-instence of class (data store as propertiies)
# why oops ? - modular,reusable,maintainability,scalable,flexible

class Employee:
    def __init__(self,name,address,place):  #self is a internal usecase did'nt pass anything in to self \ __init__(constructor of class)
        self.name = name
        self.address = address
        self.place = place

    def print_details(self):
        print(f"name :{self.name}")
        print(f"address :{self.address}")    
        print(f"place :{self.place}")    

    def clock_in(self):
        print("clockin function called")

    def clock_out(self):
        print
        ("clock out function called") 

    def change_address(self,new_address):
        self.address = new_address


emp1 =Employee("jaseena","kondadan","parambil peedika")
emp2 =Employee("thanseef","pattarparambil","thalappara")

emp1.print_details()
emp1.clock_in()
emp2.change_address("valiyaparambu") #change properties
emp2.print_details()
print(emp1.name)


# Encapsulation -an action of enclosing somthing in a capsule (pacakged the data and code in a programming)
# Internal details of an object is hidden from outside world
# Impliment encapsulation :private ,public and protected

#protected 

# class parners:
#     def __init__(self,name,job,salary):  #self is a internal usecase did'nt pass anything in to self \ __init__(constructor of class)
#         self.name = name
#         self.job =job
#         self.salary =salary
#         self._bonus_percentage =10          #it's protected (start with underscore)

#     def display_info(self):
#         print(f"Name:{self.name},job :{self.job},salary:{self.salary}")

#     def print_bonus(self):
#         return self.salary * self._bonus_percentage / 100

# parner1 = parners("john","software engneer",1000)   
# parner1.display_info()
# print(f"bonus:{parner1.print_bonus()}")   # you can only access protected member like this and also only access their sub class
# print(parner1._bonus_percentage)

#private member
# class students:
#     def __init__(self,name,sub,mark):  #self is a internal usecase did'nt pass anything in to self \ __init__(constructor of class)
#         self.name = name
#         self.sub = sub 
#         self.mark =mark
#         self.__percentage =80         #it's private member(start with 2 underscore) theprivate variable only access as funtion not in method

#     def display_info(self):
#         print(f"Name:{self.name},sub :{self.sub},mark:{self.mark}")

#     def print_percentage(self):
#         return self.__percentage

#     def change_percentage(self,new_percentage):
#         self.__percentage =new_percentage  

#     def calculate_percentage(self):
#         percentage =0
#         return percentage

# parner1 = parners("john","english",85)   
# parner1.display_info()
# print(parner1.print_percentage())


class employees:
    def __init__(self,name,job,salary):  #self is a internal usecase did'nt pass anything in to self \ __init__(constructor of class)
        self.name = name
        self.job =job
        self.salary =salary
        self.__bonus =5000         #it's protected (start with underscore)

    def display_info(self):
        print(f"Name:{self.name},job :{self.job},salary:{self.salary}")

    def print_bonus(self):
        return self.__bonus

    def change_bonus(self,new_bonus):
        self.__bonus =new_bonus 

    def __calculate_percentage(self): #it is a private method ,it can only use in the class ,can't access in outside
        bonus =0
        return bonus    

   
empl2 = employees("john","software engneer",1000)   
empl2.display_info()
#print(empl2.__bonus)  # AttributeError: 'employees' object has no attribute '__bonus'
print(empl2.print_bonus()) # you can only access private members using function
empl2.change_bonus(6000)
print(empl2.print_bonus())





