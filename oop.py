class Phone:
    def make_call(self):
        print("Lets make a phone call")
    def play_game(self):
        print("Let's play a game")




class Phone1:
    def set_color(self, color):
        self.color = color

    def set_cost(self, cost):
        self.cost = cost
        
    def show_color(self):
        return self.color
        
    def show_cost(self):
        return self.cost
        
    def play_game(self):
        print("Playing a game")
        
    def make_call(self):
        print("making a call")

# Creating an instance of Phone1
p2 = Phone1()

# Setting the cost of the phone
p2.set_cost(500)

# Printing the cost of the phone
print(p2.show_cost())  # Output: 500
