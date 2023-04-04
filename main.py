from settings import * ##import everything from settings.py
from tetris_two import Tetris
import sys

##Tetrace: have two players race to complete a row on the same board

class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Tetris2')
        self.screen = pg.display.set_mode(FIELD_RES) ## Make screen with given field resolution in settings
        self.clock = pg.time.Clock()
        self.tetris_two = Tetris(self)

    def update(self):
        self.tetris_two.update()
        self.clock.tick(FPS)
    
    def draw(self):
        self.screen.fill(color=FIELD_COLOR)
        self.tetris_two.draw()
        pg.display.flip() ## Update the full display service to screen

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    app = App()
    app.run()




        
        
        