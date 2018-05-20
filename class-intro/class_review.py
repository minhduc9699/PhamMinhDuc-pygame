# abstraction
from random import randint, choice

class Food:
    # x,y, name, hp buff
    def __init__(self, x, y, name, hp_buff):
        self.x = x
        self.y = y
        self.name = name
        self.hp_buff = hp_buff
    def print(self):
        print("[ {0}, {1}, {2}, {3} ]".format(self.x, self.y, self.name, self.hp_buff))

name = ["pho", "com", "ca", "thit cho"]


for i in range(10):
    ran_x = randint(0, 100)
    ran_y = randint(0, 100)
    ran_name = choice(name)
    ran_hp_buff = randint(0,100)
    food = Food(ran_x, ran_y, ran_name, ran_hp_buff)
    food.print()
