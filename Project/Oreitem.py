from Project.state_machine import StateMachine


class move:
    @staticmethod
    def enter(ore, e):
        pass
    @staticmethod
    def exit(ore, e):
        pass
    @staticmethod
    def do():
        pass
    @staticmethod
    def draw():
        pass
class Idle:
    @staticmethod
    def enter(ore, e):
        pass

    @staticmethod
    def exit(ore, e):
        pass

    @staticmethod
    def do():
        pass

    @staticmethod
    def draw():
        pass


class Oreitem:
    def __init__(self, name, price):
        self.state_machine = StateMachine(self)
        self.name = name
        self.price = price
        self.state_machine.start(Idle)
        self.state_machine.set_transitions(
            {
                Idle: {},
            }
        )  # dict전달 #함수이름이 똑같아야함 time_out,space_down
    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        #event : 입력 이벤트
        #우리가 넘겨줄거 튜플 형식
        self.state_machine.add_event(('INPUT',event))

    def draw(self):
        self.state_machine.draw()
