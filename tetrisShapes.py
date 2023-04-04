from settings import *
import random

## Sprite class from pygame library needed for unique blocks
class Block(pg.sprite.Sprite):
    def __init__(self, tetrisShapes, pos):
        self.tetrisShapes = tetrisShapes
        self.pos = vec(pos) + INIT_POS
        super().__init__(tetrisShapes.tetris_two.sprite_group)
        self.image = pg.Surface([TILE_SIZE, TILE_SIZE])
        self.image.fill('red') ##Change later to match sprite
        self.rect = self.image.get_rect()
        ##The position is based from the top left of the board
        self.rect.topleft = self.pos * TILE_SIZE

class TetShape:
    def __init__(self, tetris_two):
        self.tetris_two = tetris_two
        self.shape = random.choice(list(TETRISBLOCK.keys()))
        self.blocks = [Block(self, pos) for pos in TETRISBLOCK[self.shape]]
    
    def update(self):
        pass