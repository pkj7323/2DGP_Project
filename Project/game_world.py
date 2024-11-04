import enum_define
world = [[] for i in range(enum_define.Layer.end.value)]

def add_object(obj,layer):
    world[layer.value].append(obj)

def update():
    for layer in range(enum_define.Layer.end.value):
        for obj in world[layer]:
            obj.update()

def draw():
    for layer in range(enum_define.Layer.end.value):
        for obj in world[layer]:
            obj.draw()

def remove_object(obj):
    for layer in range(enum_define.Layer.end.value):
        if obj in world[layer]:
            world[layer].remove(obj)
            return

    print(f'월드 리스트에 없는거 삭제하려는 행동 감지')

def get_world():
    return world
