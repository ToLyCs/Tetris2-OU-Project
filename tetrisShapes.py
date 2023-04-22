from settings import *
import random

## Sprite class from pygame library needed for unique blocks
class Block(pg.sprite.Sprite):
    def __init__(self, tetrisShapes, pos):
        self.tetrisShapes = tetrisShapes
        self.pos = vec(pos) + INIT_POS
        self.alive = True

        super().__init__(tetrisShapes.tetris_two.sprite_group)
        self.image = pg.Surface([TILE_SIZE, TILE_SIZE]) ## Sets the sprite to be the size of a tile
        pg.draw.rect(self.image, 'red', (1, 1, TILE_SIZE - 2, TILE_SIZE - 2), border_radius = 8) ##Change later to match sprite
        self.rect = self.image.get_rect()

    def is_alive(self):
        if not self.alive:
            self.kill()

    ## Rotates a block 90 degrees
    def rotate(self, pivot_pos):
        translate = self.pos - pivot_pos
        rotate = translate.rotate(90)
        return rotate + pivot_pos

    ## The position is based from the top left of the board
    def set_pos(self):
        self.rect.topleft = self.pos * TILE_SIZE

    def update(self):
        self.is_alive()
        self.set_pos()

    ## Checks to see if a given block in a shape collided with the wall of playing field or another shape. Returns true if did collide
    def block_collide(self, pos):
        x = int(pos.x)
        y = int(pos.y)

        if 0 <= x < FIELD_W and y < FIELD_H and (y < 0 or not self.tetrisShapes.tetris_two.field_array[y][x]):
            return False
        
        return True

class TetShape:
    def __init__(self, tetris_two):
        self.tetris_two = tetris_two
        self.shape = random.choice(list(TETRISBLOCK.keys())) ## Grabs a random shape
        self.blocks = [Block(self, pos) for pos in TETRISBLOCK[self.shape]]
        self.landed = False

    ## Rotates the shape if it will not collide with anything while rotating
    def rotate(self):
        pivot_pos = self.blocks[0].pos
        new_block_positions = [block.rotate(pivot_pos) for block in self.blocks]

        if not self.shape_collide(new_block_positions):
            for i, block in enumerate(self.blocks):
                block.pos = new_block_positions[i]

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