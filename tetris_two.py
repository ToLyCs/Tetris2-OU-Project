from settings import *
from tetrisShapes import TetShape
import pygame.freetype as ft

class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group() ## Add sprites
        self.field_array = self.get_field_array()
        self.tetrisShapes = TetShape(self)
        self.next_shape = TetShape(self, current=False)
        self.fall_speed_up = False

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
    
    ## If shape stays at intial location for 300 miliseconds, return true
    def game_over(self):
        if self.tetrisShapes.blocks[0].pos.y == INIT_POS[1]:
            pg.time.wait(300)
            return True

    ## If current shape has landed, check if game is over or not. If not, make a new shape
    def has_landed(self):
        if self.tetrisShapes.landed:
            if self.game_over():
                self.__init__(self.app)
            else:
                self.fall_speed_up = False
                self.put_shapes_in_array()
                self.next_shape.current = True
                self.tetrisShapes = self.next_shape
                self.next_shape = TetShape(self, current=False)

    ## Checks to see which arrow key is pressed and either moves/rotates it
    def controller(self, pressed_key):
        if pressed_key == pg.K_LEFT:
            self.tetrisShapes.move(dir='left')
        elif pressed_key == pg.K_RIGHT:
            self.tetrisShapes.move(dir='right')
        elif pressed_key == pg.K_UP:
            self.tetrisShapes.rotate()
        elif pressed_key == pg.K_DOWN:
            self.fall_speed_up = True

    ## Makes the grid in the display
    def draw_grid(self):
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pg.draw.rect(self.app.screen, 'black', 
                             (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    ## Updates shapes and sprites
    def update(self):
        trigger = [self.app.animation_trigger, self.app.fast_animation_trigger][self.fall_speed_up]

        if trigger:
            self.check_full_row()
            self.tetrisShapes.update()
            self.has_landed()
        self.sprite_group.update()

    ## Draws the grid and sprites
    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.app.screen)

class Text:
    def __init__(self, app):
        self.app = app
        self.font = ft.Font(FONT_PATH)
    
    def draw(self):
        self.font.render_to(self.app.screen, (WIN_W * 0.615, WIN_H * 0.05), text='TETRIS 2', fgcolor='white', size=TILE_SIZE * 1.5)
        self.font.render_to(self.app.screen, (WIN_W * 0.67, WIN_H * 0.22), text='NEXT:', fgcolor='white', size=TILE_SIZE * 1.6)
        self.font.render_to(self.app.screen, (WIN_W * 0.655, WIN_H * 0.8), text='SCORE:', fgcolor='white', size=TILE_SIZE * 1.6)
        self.font.render_to(self.app.screen, (WIN_W * 0.685, WIN_H * 0.9), text='0000', fgcolor='white', size=TILE_SIZE * 1.6)