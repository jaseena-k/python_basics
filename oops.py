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