import enum
class Layer(enum.Enum):
    backGround  = 0
    tile        = 1
    ore         = 2
    building    = 3
    milestone   = 8
    mouse       = 9
    end         = 10
# 숫자가 클수록 나중에 렌더링되서 위에 보여짐
class Blocks(enum.Enum):
    wall = 1
    conveyor = 2
    beryllium_ore = 3

class Items(enum.Enum):
    beryllium = 1
    coal = 2
    copper = 3
    pyratite = 4
    titanium = 5
    tungsten = 6