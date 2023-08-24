# Importing Libraries
import pygame
import random

# Initialising the modules in pygame
pygame.init()

# Screen
SCREEN = pygame.display.set_mode((457,700))

# Background
BACKGROUND_IMAGE = pygame.image.load('Background.jpg')

# Bird
BIRD_IMAGE = pygame.image.load('Bird.png')
bird_x = 50
bird_y = 300
bird_y_change = 0
bird_velocity = 0
gravity = 0.5


def display_bird(x,y):
    SCREEN.blit(BIRD_IMAGE, (x,y))

# Obstacles

OBSTACLE_WIDTH = 70
OBSTACLE_HEIGHT = random.randint(200,400)
OBSTACLE_COLOR = (255,255,0)
OBSTACLE_X_CHANGE = -3
obstacle_x = 457


# Display Obstacles

def display_obstacle(height):
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, 0, OBSTACLE_WIDTH, height))
    bottom_obstacle_height = 550 - height- 100
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, 550, OBSTACLE_WIDTH, bottom_obstacle_height))

# Collison Detection

def collison_detection (obstacle_x, obstacle_height, bird_y, bottom_obstacle_height):
    if obstacle_x <= bird_x + BIRD_IMAGE.get_width() and obstacle_x + OBSTACLE_WIDTH >= bird_x:
        if bird_y <= obstacle_height or bird_y + BIRD_IMAGE.get_height( )>= 550:
            return True
    return False

# Score

score = 0
SCORE_FONT = pygame.font.Font('freesansbold.ttf', 30)

def score_display(score):
    display = SCORE_FONT.render(f"Score: {score}", True, (255,255,255))
    SCREEN.blit(display, (10,10))

# Start Screen

startFont = pygame.font.Font('freesansbold.ttf', 30)
def start():
    display = startFont.render(f"Press space bar to start" , True, (255,255,255))
    SCREEN.blit(display, (20,200))
    pygame.display.update()

score_list = [0]

# Game ended
game_over_font1 = pygame.font.Font('freesansbold.ttf', 60)
game_over_font2 = pygame.font.Font('freesansbold.ttf', 30)

# Check max score
def game_over():
    maximum = max(score_list)
    display1 = game_over_font1.render(f"GAME OVER" , True, (200,35,35))
    SCREEN.blit(display1, (50,300))
    display2 = game_over_font2.render(f"SCORE: {score} MAX SCORE: {maximum}", True, (235,255,255))
    SCREEN.blit(display2, (50,400))
    if score == maximum:
        display3 = game_over_font2.render(f"NEW HIGH SCORE:", True, (210,30,35))
        SCREEN.blit(display3, (80,100))

running = True
waiting = False
collision = False

while running:
    SCREEN.fill((0,0,0)) #black


    # Display Background image
    SCREEN.blit(BACKGROUND_IMAGE, (0,0)) # Start drawing at top left corner
    while waiting:
        if collision:
            game_over()
            start()
        else:
            start()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    score = 0
                    bird_y = 300
                    obstacle_x = 457
                    waiting = False
            
            if event.type == pygame.QUIT:
                waiting = False
                running = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y_change= -4
        if  event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                bird_y_change= 2

    # Moving bird
    bird_velocity += gravity
    bird_y += bird_y_change
    if bird_y <= 0:
        bird_y = 0
    if bird_y >= 600:
        bird_y = 600

    # Moving obstacle
    obstacle_x += OBSTACLE_X_CHANGE

    # Collision
    collision = collison_detection(obstacle_x, OBSTACLE_HEIGHT, bird_y, OBSTACLE_HEIGHT + 100)
    if collision:
        score_list.append(score)
        waiting = True
        
    # New obstacles
    if obstacle_x <= -10:
        obstacle_x = 457
        OBSTACLE_HEIGHT = random.randint(200,400)
        score += 1

    # Display Obstacle
    display_obstacle(OBSTACLE_HEIGHT)
    
    
    # Display Bird
    display_bird(bird_x, bird_y)

    # Display Score
    score_display(score)

    # Update display
    pygame.display.update()
pygame.quit() # Quit the program


