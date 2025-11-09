from random import randint
import pygame

exit = False

#pygme initializations
pygame.init()

# Settings
SIZE = width, height = 1280, 960  # Resolution. (4:3)!
BG_COLOR = (0, 0, 0)  # Background color in RGB
fullscreen = False  # Fullscreen

# initalizing logo, clock and screen 
logo = pygame.image.load('logo.png')
logo = pygame.transform.scale(logo, (100, 50))
clock = pygame.time.Clock()
img_size = logo.get_rect().size
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('DVD Corner')

# initialize cheer sound

cheer = pygame.mixer.Sound("sounds/cheer.mp3")

#initialize flash
flash_duration = 4000
flash_start = 0
flash_color = BG_COLOR

#initializing text
font = pygame.font.SysFont("Ubuntu", 36)
score = 0
text = "Hits: " + str(score)
text_x = screen.get_width() // 2
text_y = 20


if fullscreen:
    DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.mouse.set_visible(False)

#configuring speed and beginning position
x = randint(50, width-60)
y = randint(50, height-60)
x_speed = 20
y_speed = 20



# cleaner move within the loop
def move(x, y):
    screen.blit(logo, (x, y))

corner_prev = False

while exit == False:
    #checking if needs to flash background
    now = pygame.time.get_ticks()
    if now - flash_start < flash_duration:
        screen.fill(flash_color)
    else:
        screen.fill(BG_COLOR)
    #check if the logo is in the corner
    corner_now = ((x + img_size[0] >= width) or (x <= 0)) \
             and ((y + img_size[1] >= height) or (y <= 0))
    
    #text rendering
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(text_x, text_y))
    screen.blit(text_surface, text_rect)


    #check if logo is in the corner and change backgroun flash color, and play sound 
    if corner_now and not corner_prev:
        cheer.play()
        score += 1
        text = "Hits: " + str(score)
        flash_start = pygame.time.get_ticks()
        flash_color = (randint(0, 255), randint(0, 255), randint(0, 255))

    #bounce the logo
    if (x + img_size[0] >= width) or (x <= 0):
        x_speed = -x_speed
    if (y + img_size[1] >= height) or (y <= 0):
        y_speed = -y_speed
    x += x_speed
    y += y_speed
    move(x, y)


    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

pygame.quit()