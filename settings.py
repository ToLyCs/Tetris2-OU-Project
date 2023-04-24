## This file contains information about tile size, along with the size and resolution of the field
## The frames-per-second is also included here for use with the update method

import pygame as pg

vec = pg.math.Vector2

SPRITE_PATH = 'assets/sprites'
FONT_PATH = 'assets/fonts/BrickTetris.ttf'
BG_MUSIC_PATH = 'assets/music/Tetris.mp3'
SCORE_PATH = 'score.txt'

## Set tile size and playing field dimensions
TILE_SIZE = 45
FIELD_SIZE = FIELD_W, FIELD_H = 10,20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE
FIELD_PLACE = FIELD_SIZE[0] * 2

## Set window size
WIN_RES = WIN_W, WIN_H = FIELD_RES[0] * 1.7, FIELD_RES[1]

## Set Frames Per Second and the backfround field color
FPS = 60
FIELD_COLOR = (45, 45, 45)

## Time interval (in ms) between animations
ANIMATION_INTERVAL = 500
FAST_ANIMATION_INTERVAL = 50

INIT_POS = vec(FIELD_W // 2 - 1, 0) ## Sets vector to the center top of the playing field
NEXT_POS_LOCATION = vec(FIELD_W * 1.3, FIELD_H * 0.4)
DIRECTIONS = {'left': vec(-1, 0), 'right': (1,0), 'down': (0,1)} ## Sets directions in vector values

##Here, we have the various block shapes used in tetris
TETRISBLOCK = {
    'I' : [(0, 0), (0, 1), (0, -1), (0, -2)],
    'O' : [(0, 0), (0, -1), (1, 0), (1, -1)],
    'L' : [(0, 0), (1, 0), (0, -1), (0, -2)],
    'T' : [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'J' : [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'S' : [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z' : [(0, 0), (1, 0), (0, -1), (-1, -1)]
}

