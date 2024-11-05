from pico2d import *

from Project import game_framework
from Project.enum_define import Layer
import game_world

class Camera:
    def __init__(self):
        self.x = 0; self.y = 0
        self.width = 800 ; self.height = 600
        self.dir_x = 0; self.dir_y = 0
    def is_obj_in_camera(self, obj):
        # obj is tilemap
        if self.x < obj.adjust_x < self.x + self.width and self.y < obj.adjust_y < self.y + self.height:
            return True
        else:
            return False

    def update(self):
        pass
    def handle_event(self,event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                self.dir_x += -1
            elif event.key == SDLK_RIGHT:
                self.dir_x += 1
            elif event.key == SDLK_DOWN:
                self.dir_y += -1
            elif event.key == SDLK_UP:
                self.dir_y += 1
        if event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                self.dir_x += 1
            elif event.key == SDLK_RIGHT:
                self.dir_x += -1
            elif event.key == SDLK_DOWN:
                self.dir_y += +1
            elif event.key == SDLK_UP:
                self.dir_y += -1

    def move(self):
        tempx = self.x + 20 * self.dir_x
        tempy = self.y + 20 * self.dir_y
        doMove = True
        print(self.x, self.y)
        background = game_world.get_world()[Layer.backGround.value][0]

        camera_center_x = tempx + self.width / 2
        camera_center_y = tempy + self.height / 2
        if ((camera_center_x - self.width / 2 <= -background.width / 2)
            or (camera_center_y - self.height / 2 <= -background.height / 2)
            or (camera_center_x + self.width / 2 >= background.width / 2)
            or (camera_center_y + self.height / 2 >= background.height / 2)):
            doMove = False
        else:
            doMove = True


        # if ((tempx >= background.width / 2 - self.width) or (tempy >= background.height / 2 - self.height)
        #     or (tempx <= -(background.width / 2 - self.width))) or (tempy <= -(background.height / 2 - self.height)):
        #     doMove = False
        # else:
        #     doMove = True

        if doMove:
            self.x += 20 * self.dir_x
            self.y += 20 * self.dir_y
            for layer in range(Layer.end.value):
                for o in game_world.get_world()[layer]:
                    if (o.layer.value == Layer.mouse.value):
                        continue
                    o.move(-20 * self.dir_x, -20 * self.dir_y)
