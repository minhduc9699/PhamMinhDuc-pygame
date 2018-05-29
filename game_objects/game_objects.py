game_objects = []

def add_object_to_game_objects(object):
    game_objects.append(object)

def game_object_update():
    for game_object in game_objects:
        game_object.update()

def game_object_render(canvas):
    for game_object in game_objects:
        game_object.render(canvas)
