from settings import *
import random

## Sprite class from pygame library needed for unique blocks
class Block(pg.sprite.Sprite):
    def __init__(self, tetrisShapes, pos):
        self.tetrisShapes = tetrisShapes
        self.pos = vec(pos) + INIT_POS
        super().__init__(tetrisShapes.tetris_two.sprite_group)
        self.image = pg.Surface([TILE_SIZE, TILE_SIZE]) ## Sets the sprite to be the size of a tile
        self.image.fill('red') ##Change later to match sprite
        self.rect = self.image.get_rect()

    ## The position is based from the top left of the board
    def set_pos(self):
        self.rect.topleft = self.pos * TILE_SIZE

    def update(self):
        self.set_pos()

class TetShape:
    def __init__(self, tetris_two):
        self.tetris_two = tetris_two
        self.shape = random.choice(list(TETRISBLOCK.keys())) ## Grabs a random shape
        self.blocks = [Block(self, pos) for pos in TETRISBLOCK[self.shape]]

    def move(self, dir):
        direction = DIRECTIONS[dir] ## Sets to a direction

        ## Adds the direction to the vector
        for block in self.blocks:
            block.pos += direction
    
    def update(self):
        self.move(dir='down')