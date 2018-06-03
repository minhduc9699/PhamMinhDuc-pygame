game_objects = []


def recycle(type_obj, x, y):
    for game_object in game_objects:
        if type(game_object) == type:
            if not game_object.is_active:
                game_object.is_active = True
                game_object.x = x
                game_object.y = y
                return game_object
    new_game_object = type_obj(x, y)
    add_object_to_game_objects(new_game_object)


def add_object_to_game_objects(object):
    game_objects.append(object)

def game_object_update():
    for game_object in game_objects:
        if game_object.is_active:
            game_object.update()

def game_object_render(canvas):
    for game_object in game_objects:
        if game_object.is_active:
            game_object.render(canvas)


class GameObjects:
    def __init__(self, x, y ):
        self.x = x
        self.y = y
        self.image = None
        self.is_active = True


    def update(self):
        pass

    def render(self, canvas):
        if self.image is not None:
            width = self.image.get_width()
            height = self.image.get_height()
            draw_position = (self.x - width * 0.5, self.y - height * 0.5)
            canvas.blit(self.image, draw_position)
