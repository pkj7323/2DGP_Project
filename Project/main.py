from pico2d import open_canvas, close_canvas, hide_cursor
from Project import menu_mode as start_mode
from Project import game_framework

open_canvas()
hide_cursor()
game_framework.run(start_mode)
close_canvas()