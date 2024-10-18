import pygame
from pico2d import *


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

    def move(self, world):
        self.x += 20 * self.dir_x
        self.y += 20 * self.dir_y
        for o in world:
            o.move(-20 * self.dir_x,-20 * self.dir_y)