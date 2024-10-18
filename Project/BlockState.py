import enum
class BlockState(enum.Enum):
    backGround  = 0
    wall        = 1
    ore         = 2
    building    = 3
    end         = 10
# 숫자가 클수록 나중에 렌더링되서 위에 보여짐