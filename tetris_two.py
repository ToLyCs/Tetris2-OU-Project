from settings import *
from tetrisShapes import TetShape

class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group() ## Add sprites
        self.field_array = self.get_field_array()
        self.tetrisShapes = TetShape(self)

    def check_full_row(self):
        row = FIELD_H - 1

        for y in range(FIELD_H - 1, -1, - 1):
            for x in range(FIELD_W):
                self.field_array[row][x] = self.field_array[y][x]

                if self.field_array[y][x]:
                    self.field_array[row][x].pos = vec(x, y)
            
            if sum(map(bool, self.field_array[y])) < FIELD_W:
                row -= 1
            else:
                for x in range(FIELD_W):
                    self.field_array[row][x].alive = False
                    self.field_array[row][x] = 0

    ## Fills 2D array where current shapes have landed
    def put_shapes_in_array(self):
        for block in self.tetrisShapes.blocks:
            x = int(block.pos.x)
            y = int(block.pos.y)
            self.field_array[y][x] = block

    ## 2D array filled with 0's that is the size of the playing field 
    def get_field_array(self):
        return [[0 for x in range(FIELD_W)] for y in range(FIELD_H)]

    ## If current shape has landed, create a new shape and place where it landed in 2D array
    def has_landed(self):
        if self.tetrisShapes.landed:
            self.put_shapes_in_array()
            self.tetrisShapes = TetShape(self)

    ## Checks to see if the elft or right arrow key is pressed, if they are, set direction to left or right
    def controller(self, pressed_key):
        if pressed_key == pg.K_LEFT:
            self.tetrisShapes.move(dir='left')
        elif pressed_key == pg.K_RIGHT:
            self.tetrisShapes.move(dir='right')
        elif pressed_key == pg.K_UP:
            self.tetrisShapes.rotate()

    ## Makes the grid in the display
    def draw_grid(self):
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pg.draw.rect(self.app.screen, 'black', 
                             (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    ## Updates shapes and sprites
    def update(self):
        if self.app.animation_trigger:
            self.check_full_row()
            self.tetrisShapes.update()
            self.has_landed()
        self.sprite_group.update()

    ## Draws the grid and sprites
    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)