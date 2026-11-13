import pygame
import math
import colorsys

pygame.init()

#set colour
white = (255, 255, 255)
black = (0, 0, 0)
hue = 0

#wdith and height
WIDTH = 1920
HEIGHT = 1080

#starting position
x_start, y_start = 0, 0

#changes x and y coordinate
x_separator = 10
y_separator = 20

#resize screen
rows = HEIGHT//y_separator
columns = WIDTH//x_separator
screen_size = rows * columns

#draw donut in the middle of the screen by making it the half of screen_size
x_offset = columns / 2
y_offset = rows / 2

#rotating animation
A, B = 0, 0

theta_spacing = 10 #controls density of donut parameter circle
phi_spacing = 1  #controls donut density among parameter circle 360

chars = ".,-~:;=!*#$@" #characters to make up the donut

#display width and height on screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#make it fullscreen 
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Donut')

#set the font
font = pygame.font.SysFont('Arial', 18, bold=True)
#rainbow
def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

#add the font and display it
def text_display(letter, x_start, y_start):
    text = font.render(str(letter), True, hsv2rgb(hue, 1, 1))
    display_surface.blit(text, (x_start, y_start))

#while the window is running make the background black
#when you close the game, the event will quit and the run will be false
run = True
while run:
    
    screen.fill((black))

    z = [0] * screen_size #donut will fill donut space
    b = [' '] * screen_size #background fill empty space
    #dimensions for donut
    for j in range(0, 628, theta_spacing): # from 0 to 2pi
        for i in range(0, 628, phi_spacing): # from 0 to 2pi
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(x_offset + 40 * D * (l * h * m - t * n)) # 3D x coordinate after rotation
            y = int(y_offset + 20 * D * (l * h * n + t * m)) # 3D y coordinate after rotation
            o = int(x + columns * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if rows > y and y > 0 and x > 0 and columns > x and D > z[o]:
                z[o] = D
                b[o] = chars[N if N > 0 else 0]
#resets to the top of the grid
    if y_start == rows * y_separator - y_separator:
        y_start = 0
#rotation actions
    for i in range(len(b)):
        A += 0.000025 #control speed
        B += 0.000015 #control speed
        if i == 0 or i % columns: 
            text_display(b[i], x_start, y_start)
            x_start += x_separator
        else:
            y_start += y_separator
            x_start = 0
            text_display(b[i], x_start, y_start)
            x_start += x_separator
#hue and activate the change
    pygame.display.update()
    hue += 0.005
#when escape is pressed it exits the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
