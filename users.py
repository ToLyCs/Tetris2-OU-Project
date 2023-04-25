from pickle import APPEND
import pygame
import sys
from main import * # import everything from main.py
import webbrowser
from highscore import *
class Account:
    def __init__(self):  
        self.username = None
        self.password = None
    
    def create_account(self):
        """Creates a new account and saves it to a file"""
        # Initialize Pygame
        pygame.init()
        width, height = 600, 400
        screen = pygame.display.set_mode((width, height))
        
        # Get username and password
        username = ""
        password = ""
        font = pygame.font.Font(None, 26)
        username_text = font.render("Username: ", True, (255, 255, 255))
        password_text = font.render("Password: ", True, (255, 255, 255))
        create_text = font.render("Create account", True, (155, 255, 255))

        # Define the Return button        
        return_button = font.render("Return", True, (155, 255, 255))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if username:
                            username = username[:-1]
                        elif password:
                            password = password[:-1]
                    elif event.key == pygame.K_RETURN:
                        if username and password:
                            # Save account to file
                            with open("users.txt", "a") as file:
                                file.write(f"{username},{password}\n")
                            #Run the app
                            app = option()
                            app.run()
                        
                        else:
                            # Username or password is empty
                            print("Username or password is empty!")
                    else:
                        if a.collidepoint(pygame.mouse.get_pos()):
                            username += event.unicode
                        elif b.collidepoint(pygame.mouse.get_pos()):
                            password += event.unicode
                # Return button mouse click
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if c.collidepoint(event.pos):
                        return Account()
            
            # Fill the background color
            screen.fill((0, 0, 0))
            # Render the username and password text on the screen
            screen.blit(username_text, (width/2 - 200, height/2 - 60))
            screen.blit(password_text, (width/2 - 200, height/2))
            screen.blit(create_text, (width/2 - 80, height/4.5))            
            a = pygame.draw.rect(screen, (255, 255, 255), (width/2 - 90, height/2 - 70, 160, 32), 2)
            b = pygame.draw.rect(screen, (255, 255, 255), (width/2 - 90, height/2 - 10, 160, 32), 2) 
            # Render the username and password input on the screen           
            username_input = font.render(username, True, (255, 255, 255))
            password_input = font.render("*" * len(password), True, (255, 255, 155))
            screen.blit(username_input, (width/2 - 80, height/2 - 60))
            screen.blit(password_input, (width/2 - 80, height/2 ))
            # Render return button
            screen.blit(return_button, (20, 20)) 
            c = pygame.draw.rect(screen, (255, 255, 255), (10, 10, 80, 32), 2) 
            # Update display
            pygame.display.update()

    
    def login(self):
        """Logs in the user"""
        # Initialize Pygame
        pygame.init()
        width, height = 600, 400
        screen = pygame.display.set_mode((width, height))
        
        # Get username and password
        username = ""
        password = ""
        font = pygame.font.Font(None, 26)
        username_text = font.render("Username: ", True, (255, 255, 255))
        password_text = font.render("Password: ", True, (255, 255, 255))
        login_text = font.render("Sign in", True, (155, 255, 255))

        # Display when Invalid username or password
        error_text = font.render("Invalid username or password.", True, (255, 0, 0))
        error = False

        # Define the Return button        
        return_button = font.render("Return", True, (155, 255, 255))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        if username:
                            username = username[:-1]
                        elif password:
                            password = password[:-1]
                    elif event.key == pygame.K_RETURN:
                        if username and password:
                            # Check if account exists and password is correct
                            with open("users.txt", "r") as file:
                                for line in file:
                                    fields = line.strip().split(",")
                                    if fields[0] == username and fields[1] == password:
                                        print("Login successful!")
                                        # Run the app
                                        app = option()
                                        app.run()
                                        return username
                            
                            # Login failed
                            error = True
                            
                    else:
                        if a.collidepoint(pygame.mouse.get_pos()):
                            username += event.unicode
                        elif b.collidepoint(pygame.mouse.get_pos()):
                            password += event.unicode
                # Return button mouse click                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if c.collidepoint(event.pos):
                        return Account()                        
            # Fill the background color
            screen.fill((0, 0, 0))
            
            # Render the username and password text on the screen
            screen.blit(username_text, (width/2 - 200, height/2 - 60))
            screen.blit(password_text, (width/2 - 200, height/2))
            screen.blit(login_text, (width/2 - 40, height/4.5))                   
            a = pygame.draw.rect(screen, (255, 255, 255), (width/2 - 90, height/2 - 70, 160, 32), 2)
            b = pygame.draw.rect(screen, (255, 255, 255), (width/2 - 90, height/2 - 10, 160, 32), 2)              
            # Render the username and password input on the screen
            username_input = font.render(username, True, (255, 255, 255))
            password_input = font.render("*" * len(password), True, (255, 255, 155))
            screen.blit(username_input, (width/2 - 80, height/2 - 60))
            screen.blit(password_input, (width/2 - 80, height/2 ))       
            # Display error message if login fails
            if error:
                screen.blit(error_text, (width/2 - 140, height/2 + 40))
            # Return button
            screen.blit(return_button, (20, 20)) 
            c = pygame.draw.rect(screen, (255, 255, 255), (10, 10, 80, 32), 2)     
            # Update the display
            pygame.display.update()


# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris 2")

# Set up fonts
font = pygame.font.SysFont("Arial", 20)
small_font = pygame.font.SysFont("Arial", 16)

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Set up buttons
button_width = 150
button_height = 50
create_account_button = pygame.Rect(125, 75, button_width, button_height)
login_button = pygame.Rect(125, 150, button_width, button_height)
info_button = pygame.Rect(125, 150, button_width, button_height)
# Set up account variables
current_user = None

# Set up loop variables
running = True

# Set up login loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Create account button
            if create_account_button.collidepoint(event.pos):
                account = Account()
                current_user = account.create_account()
                login = True
            # Login button
            elif login_button.collidepoint(event.pos):
                account = Account()
                current_user = account.login()
                if current_user:
                    login = True
            # Get info button
            elif info_button.collidepoint(event.pos):
                # Open the website in the default browser
                webbrowser.open ("https://group7tetris2.000webhostapp.com/")


    # Draw login screen
    screen.fill(BLACK)
    create_account_button = pygame.draw.rect(screen, BLACK, (screen_width/2 - button_width/2, 75, button_width, button_height))
    login_button = pygame.draw.rect(screen, BLACK, (screen_width/2 - button_width/2, 150, button_width, button_height))
    info_button = pygame.draw.rect(screen, BLACK, (screen_width/2 - button_width/2, 225, button_width, button_height))
    create_account_text = font.render("Create New Account", True, WHITE)
    login_text = font.render("Sign in", True, WHITE)
    info_text = font.render("About", True, WHITE)
    screen.blit(create_account_text, (screen_width/2 - create_account_text.get_width()/2, 85))
    screen.blit(login_text, (screen_width/2 - login_text.get_width()/2, 160))
    screen.blit(info_text, (screen_width/2 - info_text.get_width()/2, 235))
    pygame.display.update()


    # Option to start the game
    def option ():
        pygame.init()
        width, height = 600, 400
        screen = pygame.display.set_mode((width, height))
        font = pygame.font.Font(None, 28)
        pygame.display.set_caption("Option")

        # Define the options
        new_game_text = font.render("New Game", True, (255, 255, 255))
        high_score_text = font.render("High Score", True, (255, 255, 255))
        quit_text = font.render("Quit", True, (255, 255, 255))

        # Define the positions of the options
        new_game_pos = pygame.Rect(width/2 - 80, height/2 - 60, 160, 32)
        high_score_pos = pygame.Rect(width/2 - 80, height/2, 160, 32)
        quit_pos = pygame.Rect(width/2 - 80, height/2 + 60, 160, 32)
         
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if new_game_pos.collidepoint(event.pos):
                        print("Starting new game...")
                        app = App()
                        app.run()
                    elif high_score_pos.collidepoint(event.pos):
                        app = highscore()
                        app.run()
                    elif quit_pos.collidepoint(event.pos):
                        pygame.quit()
                        quit()

            # Fill the background color
            screen.fill((0, 0, 0))
            
            # Render the options on the screen
            screen.blit(new_game_text, (width/2 - 50, height/2 - 50))
            screen.blit(high_score_text, (width/2 - 50, height/2 + 10))
            screen.blit(quit_text, (width/2 - 20, height/2 + 70))
            
            # Draw the rectangles for the options
            pygame.draw.rect(screen, (255, 255, 255), new_game_pos, 2)
            pygame.draw.rect(screen, (255, 255, 255), high_score_pos, 2)
            pygame.draw.rect(screen, (255, 255, 255), quit_pos, 2)

            # Update the display
            pygame.display.update()


    def highscore():
        pygame.init()
        clock = pygame.time.Clock()

        # Define colors
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)

        # Set the window dimensions
        screen_width = 600
        screen_height = 400
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("High Score")

        # Set the font and font size
        font = pygame.font.Font(None, 28)

        # Define the Return button        
        return_button = font.render("Return", True, (155, 255, 255))
        # Render return button
        screen.blit(return_button, (20, 20)) 
        return_button = pygame.draw.rect(screen, (255, 255, 255), (10, 10, 80, 32), 2) 

        # Read the scores from the score.txt file
        scores = []
        with open('score.txt', 'r') as file:
            for line in file:
                scores.append(line.strip())

        # Display the scores on the screen
        y = 50
        for score in scores:
            text = font.render(score, True, WHITE)
            text_rect = text.get_rect(center=(screen_width/2, y))
            screen.blit(text, text_rect)
            y += 50

        # Main loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # Return button mouse click
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if return_button.collidepoint(event.pos):
                        return option() 

            # Update the screen
            pygame.display.update()
            clock.tick(60)

   
