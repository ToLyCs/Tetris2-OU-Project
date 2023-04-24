from settings import * ##import everything from settings.py
from tetris_two import Tetris
import sys
import pathlib

##Tetrace: have two players race to complete a row on the same board

class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Tetris2')
        self.screen = pg.display.set_mode(WIN_RES) ## Make screen with given field resolution in settings
        self.clock = pg.time.Clock()
        self.set_timer()
        self.images = self.load_images()
        self.tetris_two = Tetris(self)

    ## Loads the images and sizes them to TILE_SIZE
    def load_images(self):
        files = [item for item in pathlib.Path(SPRITE_PATH).rglob('*.png') if item.is_file()]
        images = [pg.image.load(file).convert_alpha() for file in files]
        images = [pg.transform.scale(image, (TILE_SIZE, TILE_SIZE)) for image in images]
        return images

    ## Sets timer to ANIMATION_INTERVAL
    def set_timer(self):
        self.user_event = pg.USEREVENT + 0 ## Sets event ID
        self.fast_user_event = pg.USEREVENT + 1
        self.animation_trigger = False
        self.fast_animation_trigger = False
        pg.time.set_timer(self.user_event, ANIMATION_INTERVAL) ## Sets a timer (ANIMATION_INTERVAL) that will trigger an event with the ID of user_event
        pg.time.set_timer(self.fast_user_event, FAST_ANIMATION_INTERVAL)
    
    ## Sets the FPS and calls the update() method in tetris_two file
    def update(self):
        self.tetris_two.update()
        self.clock.tick(FPS)
    
    ## Draws the playing field and sets its color
    def draw(self):
        self.screen.fill(color=FIELD_COLOR)
        self.tetris_two.draw()
        pg.display.flip() ## Update the full display service to screen

    ## Checks to keys are pressed
    def check_events(self):
        self.animation_trigger = False
        self.fast_animation_trigger = False

        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE): ## Checks to see if escape key is pressed
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN: ## If any key is pressed, it gets input into the controller method in tetris_two
                self.tetris_two.controller(pressed_key=event.key) 
            elif event.type == pg.KEYUP: ## If down arow key is released, set fall speed back to normal
                if event.key == pg.K_DOWN:
                    self.tetris_two.fall_speed_up = False
            elif event.type == self.user_event: ## If the event is the ID of user_event, set animation_trigger to True
                self.animation_trigger = True
            elif event.type == self.fast_user_event:
                self.fast_animation_trigger = True

    ## Constantly runs the check_events(), update(), and draw() functions
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    app = App()
    app.run()




        
        
        