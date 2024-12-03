from pico2d import load_font, get_canvas_height

from Project.enum_define import Layer, Items

world = [[] for i in range(Layer.end.value)]
collision_pairs = {}
#{key:[[][]]}
items={}
#{ Items.key : int}
degree = 0


def draw_item_counts():
    x = 0
    y = get_canvas_height() - 40  # Top-down 위치 설정
    _font = load_font('Resource/KCC_dodaumdodaum.ttf', 16)
    for item, count in items.items():
        text = f"{item}: {count}"
        _font.draw(x, y, text, (255, 255, 255))
        y -= 20  # 다음 줄로 내려가기 위한 y 좌표 조정

        # 화면 아래로 넘어가지 않도록 체크
        if y < 0:
            y = get_canvas_height() - 40
            x += 100  # 새로운 열로 이동


def add_collision_pair(key,obj1,obj2):
    if key not in collision_pairs:
        collision_pairs[key] =[[],[]]
    if obj1:
        collision_pairs[key][0].append(obj1)
    if obj2:
        collision_pairs[key][1].append(obj2)

def add_item_once(key):
    if key not in items:
        items[key] = 1
    else:
        items[key] += 1
    #item_num = items[key]


def handle_collision():
    collision_occurred = {}
    for key, pair in collision_pairs.items():
        for obj1 in pair[0]:
            if obj1 not in collision_occurred:
                collision_occurred[obj1] = False
            for obj2 in pair[1]:
                if obj2 not in collision_occurred:
                    collision_occurred[obj2] = False
                if collision_check(obj1,obj2):
                    obj1.handle_collision(key,obj2)
                    obj2.handle_collision(key,obj1)
                    collision_occurred[obj1] = True
                    collision_occurred[obj2] = True

    for obj in collision_occurred:
        if not collision_occurred[obj]:
            obj.handle_collision_end()


def remove_collision_object(obj):
    for pair in collision_pairs.items():
        if obj in pair[1][0]:
            pair[1][0].remove(obj)
        if obj in pair[1][1]:
            pair[1][1].remove(obj)
def collision_check(a,b):
    left_a, top_a, right_a, bottom_a = a.get_bb()
    left_b, top_b, right_b, bottom_b = b.get_bb()
    #top이 더 큼
    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True
def add_object(obj,layer):
    world[layer.value].append(obj)

def update():
    for layer in range(Layer.end.value):
        for obj in world[layer]:
            obj.update()

def draw():
    for layer in range(Layer.end.value):
        for obj in world[layer]:
            obj.draw()
    draw_item_counts()


def remove_object(obj):
    for layer in range(Layer.end.value):
        if obj in world[layer]:
            world[layer].remove(obj)
            remove_collision_object(obj)
            del obj
            return

    print(f'월드 리스트에 없는거 삭제하려는 행동 감지')

def get_world():
    return world
