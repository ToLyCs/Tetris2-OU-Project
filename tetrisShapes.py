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

    ## Checks to see if a given block in a shape collided with the wall of playing field. Returns true if did collide
    def block_collide(self, pos):
        x = int(pos.x)
        y = int(pos.y)

        if 0 <= x < FIELD_W and y < FIELD_H:
            return False
        
        return True

class TetShape:
    def __init__(self, tetris_two):
        self.tetris_two = tetris_two
        self.shape = random.choice(list(TETRISBLOCK.keys())) ## Grabs a random shape
        self.blocks = [Block(self, pos) for pos in TETRISBLOCK[self.shape]]
        self.landed = False

    ## Checks to see if the whole shape collided with the end of playing field. Returns true if it did collide
    def shape_collide(self, block_positions):
        return any(map(Block.block_collide, self.blocks, block_positions))

    ## Moves block in direction given
    def move(self, dir):
        direction = DIRECTIONS[dir] ## Sets to a direction
        new_block_positions = [block.pos + direction for block in self.blocks] ## Gets the positions of the block after it moves
        collision = self.shape_collide(new_block_positions)

        ## If the shape did not collide with the wall, move the block
        if not collision:
            for block in self.blocks: ## Adds the direction to the vector
                block.pos += direction
        elif dir=='down': ## Checks to see if the shape is constantly colliding and only moving downward
            self.landed = True
        
    def update(self):
        self.move(dir='down')