from enemies.enemy import *
from enemies.virrut import *
from game_objects.game_objects import GameObjects, add_object_to_game_objects, recycle

class EnemySpawner(GameObjects) :
    def __init__(self, x, y):
        GameObjects.__init__(self, x, y)
        self.count = 0


    def spawn_enemy1(self):
        recycle(Enemy, self.x, self.y)

    def spawn_enemy2(self):
        recycle(Virrut, self.x, self.y)


