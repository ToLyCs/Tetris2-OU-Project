import pygame
from main import *

pygame.init()

# Set the width and height of the screen
size = (400, 300)
screen = pygame.display.set_mode(size)

# Set the caption for the window
pygame.display.set_caption("Login System")

def login_screen():
    # Clear the screen
    screen.fill((255, 255, 255))
   
    # Display the login prompt
    font = pygame.font.Font(None, 36)
    text = font.render("Enter your username and password:", True, (0, 0, 0))
    text_rect = text.get_rect(center=(size[0]/2, size[1]/2 - 50))
    screen.blit(text, text_rect)
   
    # Display the username 
    username_rect = pygame.Rect(size[0]/2 - 100, size[1]/2, 200, 30)
    pygame.draw.rect(screen, (0, 0, 0), username_rect, 2)
   
    # Display the password 
    password_rect = pygame.Rect(size[0]/2 - 100, size[1]/2 + 50, 200, 30)
    pygame.draw.rect(screen, (0, 0, 0), password_rect, 2)
   
    # Display the login button
    login_rect = pygame.Rect(size[0]/2 - 50, size[1]/2 + 100, 100, 30)
    pygame.draw.rect(screen, (0, 0, 0), login_rect, 2)
    login_text = font.render("Login", True, (0, 0, 0))
    login_text_rect = login_text.get_rect(center=login_rect.center)
    screen.blit(login_text, login_text_rect)
   
    # Update the display
    pygame.display.flip()
   
    # Loop until the user sucessfuly logs in 
    username = ""
    password = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if username_rect.collidepoint(pygame.mouse.get_pos()):
                        username = username[:-1]
                    elif password_rect.collidepoint(pygame.mouse.get_pos()):
                        password = password[:-1]
                elif event.key == pygame.K_RETURN:
                    if username == "username" and password == "password":
                        app = App()
                        app.run()
                    else:
                        print("wrong")
                        
                else:
                    if username_rect.collidepoint(pygame.mouse.get_pos()):
                        username += event.unicode
                    elif password_rect.collidepoint(pygame.mouse.get_pos()):
                        password += event.unicode
       
        # Update the screen with the current input
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), username_rect, 2)
        pygame.draw.rect(screen, (0, 0, 0), password_rect, 2)
        username_text = font.render(username, True, (0, 0, 0))
        username_text_rect = username_text.get_rect(center=username_rect.center)
        password_text = font.render("*" * len(password), True, (0, 0, 0))
        password_text_rect = password_text.get_rect(center=password_rect.center)
        screen.blit(username_text, username_text_rect)
        screen.blit(password_text, password_text_rect)
        screen.blit(login_text, login_text_rect)
        pygame.display.flip()

if login_screen():
    print("Logged in successfully!")
else:
    print("Login failed.")
