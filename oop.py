class Phone:
    def make_call(self):
        print("Lets make a phone call")
    def play_game(self):
        print("Let's play a game")




# class Phone1:
#     def set_color(self, color):
#         self.color = color

#     def set_cost(self, cost):
#         self.cost = cost
        
#     def show_color(self):
#         return self.color
        
#     def show_cost(self):
#         return self.cost
        
#     def play_game(self):
#         print("Playing a game")
        
#     def make_call(self):
#         print("making a call")

# # Creating an instance of Phone1
# p2 = Phone1()

# # Setting the cost of the phone
# p2.set_cost(500)

# # Printing the cost of the phone
# print(p2.show_cost())  # Output: 500


class Employee:
    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def show_details(self):
        print("The name of Employee is", self.name)
        print("The age of Employee is", self.age)
        print("The salary of Employee is", self.salary)
        print("The gender of Employee is", self.gender)

e1 = Employee('Julia',25,11200,'Female')
e1.show_details()