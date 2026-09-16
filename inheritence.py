# inheritence -inherit proprties from head class in to sub class or it's child class
#

class Employe:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"name: {self.name} salary: {self.salary}")


class Manager(Employe):
    def __init__(self, name, salary, department): 
        Employe.__init__(self, name, salary)       #name and salary exract from employe
        self.department = department 
        self.team_size = 0

    def show_team_size(self):
        print(f"{self.name} manages a team of {self.team_size} members in {self.department}")



M1 = Manager("Ali",50000,"HR") 
M1.show_details() 
M1.show_team_size()
M1.team_size = 10
M1.show_team_size()