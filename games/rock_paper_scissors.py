import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

# Load images
rock_img = pygame.image.load('rock.png')
paper_img = pygame.image.load('paper.png')
scissors_img = pygame.image.load('scissor.png')

# Scale images
rock_img = pygame.transform.scale(rock_img, (200, 200))
paper_img = pygame.transform.scale(paper_img, (200, 200))
scissors_img = pygame.transform.scale(scissors_img, (200, 200))

# Game variables
choices = ['rock', 'paper', 'scissors']
user_choice = None
computer_choice = None
result = None

# Fonts
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    screen.fill((255, 255, 255))  # Fill the screen with white color

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 100 <= x <= 300 and 400 <= y <= 600:
                user_choice = 'rock'
            elif 300 <= x <= 500 and 400 <= y <= 600:
                user_choice = 'paper'
            elif 500 <= x <= 700 and 400 <= y <= 600:
                user_choice = 'scissors'
            
            if user_choice:
                computer_choice = random.choice(choices)
                if user_choice == computer_choice:
                    result = 'Tie'
                elif (user_choice == 'rock' and computer_choice == 'scissors') or \
                     (user_choice == 'paper' and computer_choice == 'rock') or \
                     (user_choice == 'scissors' and computer_choice == 'paper'):
                    result = 'You Win!'
                else:
                    result = 'You Lose!'

    # Draw images for choices
    screen.blit(rock_img, (100, 400))
    screen.blit(paper_img, (300, 400))
    screen.blit(scissors_img, (500, 400))

    # Display choices and result
    if user_choice and computer_choice:
        user_text = font.render(f'You chose: {user_choice}', True, (0, 0, 0))
        computer_text = font.render(f'Computer chose: {computer_choice}', True, (0, 0, 0))
        result_text = font.render(result, True, (0, 0, 0))

        screen.blit(user_text, (50, 50))
        screen.blit(computer_text, (50, 100))
        screen.blit(result_text, (50, 150))

        # Draw user and computer choices images
        if user_choice == 'rock':
            screen.blit(rock_img, (100, 200))
        elif user_choice == 'paper':
            screen.blit(paper_img, (100, 200))
        elif user_choice == 'scissors':
            screen.blit(scissors_img, (100, 200))
        
        if computer_choice == 'rock':
            screen.blit(rock_img, (500, 200))
        elif computer_choice == 'paper':
            screen.blit(paper_img, (500, 200))
        elif computer_choice == 'scissors':
            screen.blit(scissors_img, (500, 200))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
