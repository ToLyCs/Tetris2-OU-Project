## This file contains information about tile size, along with the size and resolution of the field
## The frames-per-second is also included here for use with the update method

import pygame as pg

vec = pg.math.Vector2
TILE_SIZE = 35
FIELD_SIZE = FIELD_W, FIELD_H = 10,20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE
FPS = 60
FIELD_COLOR = (50, 143, 168)

##Here, we have the various block shapes used in tetris
TETRISBLOCK = {
    'I' : [(0, 0), (0, 1), (0, -1), (0, -2)],
    'D' : [(0, 0), (0, -1), (1, 0), (1, -1)],
    'L' : [(0, 0), (1, 0), (0, -1), (0, -2)],
    'T' : [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'J' : [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'S' : [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z' : [(0, 0), (1, 0), (0, -1), (-1, -1)]
}


INIT_POS = vec(FIELD_SIZE) // 2 ##Integer division
