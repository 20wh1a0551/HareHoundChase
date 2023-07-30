from tkinter import messagebox
import pygame
import math

pygame.init()
white = (255,255,255)
black = (0, 0, 0) 
red = (255, 0, 0) 
green = (0, 255, 0) 
blue = (0, 0, 255)
yellow = (255, 255, 0) 
lightblue = (51,161,201)
cyan = (0,139,139)
magenta = (255, 0, 255)


#board
display = pygame.display.set_mode((900,600))

def lines():
    pygame.draw.line(display,white,(50,250),(250,50),3)
    pygame.draw.line(display,white,(50,250),(250,450),3)
    pygame.draw.line(display,white,(250,50),(650,50),3)
    pygame.draw.line(display,white,(250,450),(650,450),3)
    pygame.draw.line(display,white,(650,50),(850,250),3)
    pygame.draw.line(display,white,(650,450),(850,250),3)
    pygame.draw.line(display,white,(50,250),(850,250),3)
    pygame.draw.line(display,white,(250,50),(250,450),3)
    pygame.draw.line(display,white,(650,50),(650,450),3)
    pygame.draw.line(display,white,(250,50),(650,450),3)
    pygame.draw.line(display,white,(250,450),(650,50),3)
    pygame.draw.line(display,white,(450,50),(450,450),3)

positions= {1 :(50,250),2:(250,50),3:(250,250), 4:(250,450), 5:(450,50), 6:(450,250), 7:(450,450), 8:(650,50), 9:(650,250), 10:(650,450), 11:(850,250)}

#labels
font = pygame.font.SysFont('comic sans',16)
def display_text(font, text):
    text_on_screen = font.render(text, True, white)
    return text_on_screen

def label_points():
    display.blit(display_text(font, "a"), (48, 259))
    display.blit(display_text(font, "b"), (248, 19))
    display.blit(display_text(font, "c"), (240, 225))
    display.blit(display_text(font, "d"), (248, 459))
    display.blit(display_text(font, "e"), (446, 19))
    display.blit(display_text(font, "f"), (440, 225))
    display.blit(display_text(font, "g"), (448, 459))
    display.blit(display_text(font, "h"), (648, 19))
    display.blit(display_text(font, "i"), (640, 225))
    display.blit(display_text(font, "j"), (648, 459))
    display.blit(display_text(font, "k"), (848, 259))

red_location = positions[1]
blue_location = positions[4]
green_location = positions[2]
yellow_location = positions[11]
def draw_initial():
    display.fill(black)
    lines()
    label_points()
    pygame.display.update()

def all_circles():
    # imp = pygame.image.load("C:\\Users\\lasya\\Downloads\\basset-hound.png").convert()
    # imp = pygame.transform.scale(imp, (100, 100))
    # display.blit(imp, locations[red])
    pygame.draw.circle(display, red, locations[red], 15)
    pygame.draw.circle(display, blue, locations[blue], 15)
    pygame.draw.circle(display, green, locations[green], 15)
    pygame.draw.circle(display, yellow, locations[yellow], 15)



colors = [blue, red, green, yellow]
locations = {blue: positions[4], red: positions[1], green:positions[2], yellow: positions[11]}
def move(x, color):
    display.fill(black)
    lines()
    draw_initial()
    flag = 0
    if(color == yellow):
        if(check_hare(x, color)):
            flag = 1
    else:
        if(check_hound(x, color)):
            flag = 1
    
    if flag == 1:
        if(positions[x]!=locations[red] and positions[x]!=locations[green] and positions[x]!=locations[yellow] and positions[x]!=locations[blue]):
            if(locations[color] == positions[5] or locations[color] == positions[7]):
                if(x != 3 and x != 9):
                    pygame.draw.circle(display, color, positions[x], 15)
                    locations[color] = positions[x]
            elif(locations[color] == positions[3] or locations[color] == positions[9]):
                if(x != 5 and x != 7):
                    pygame.draw.circle(display, color, positions[x], 15)
                    locations[color] = positions[x]
            else:
                pygame.draw.circle(display, color, positions[x], 15)
                locations[color] = positions[x]
        

    #     # for i in range(0, 4):
    #     #     if(colors[i] != color):
    #     #         pygame.draw.circle(display, colors[i], locations[i], 15)
    #     if color == blue:
    #         pygame.draw.circle(display, red, red_location, 15)
    #         pygame.draw.circle(display, green, green_location, 15)
    #         pygame.draw.circle(display, yellow, yellow_location, 15)
    #     elif color == red:
    #         pygame.draw.circle(display, blue, blue_location, 15)
    #         pygame.draw.circle(display, green, green_location, 15)
    #         pygame.draw.circle(display, yellow, yellow_location, 15)
    #     elif color == green:
    #         pygame.draw.circle(display, red, red_location, 15)
    #         pygame.draw.circle(display, blue, blue_location, 15)
    #         pygame.draw.circle(display, yellow, yellow_location, 15)
    #     else:
    #         pygame.draw.circle(display, red, red_location, 15)
    #         pygame.draw.circle(display, blue, blue_location, 15)
    #         pygame.draw.circle(display, green, green_location, 15)
    # else:
    all_circles()
    # if(flag == 0):
    #     messagebox.showinfo(message="Can't move there. Try again!")
    if(hound_win()):
        messagebox.showinfo(message="The Hounds Win!")
    
    if(hare_win()):
        messagebox.showinfo(message="The Hare Wins!")

    pygame.display.update()


def check_hound(p, color):
    x1, y1 = locations[color]
    x2, y2 = positions[p]
    if (x2 >= x1) and (x2 - x1 <= 200) and (math.fabs(y2 - y1) <= 200):
        return True

def check_hare(p, color):
    x1, y1 = locations[color]
    x2, y2 = positions[p]
    if (math.fabs(x2 - x1) <= 200) and (math.fabs(y2 - y1) <= 200):
        return True

def key_press(color):
    if event.key == pygame.K_a:
        move(1,color)
    if event.key == pygame.K_b:
        move(2,color)
    if event.key == pygame.K_c:
        move(3,color)
    if event.key == pygame.K_d:
        move(4,color)
    if event.key == pygame.K_e:
        move(5,color)
    if event.key == pygame.K_f:
        move(6,color)
    if event.key == pygame.K_g:
        move(7,color)
    if event.key == pygame.K_h:
        move(8,color)
    if event.key == pygame.K_i:
        move(9,color)
    if event.key == pygame.K_j:
        move(10,color)
    if event.key == pygame.K_k:
        move(11,color)
        
screen = pygame.display.set_mode((900, 600))

def click(screen, pos, text):
    font1 = pygame.font.SysFont("Helvectica", 70)
    text_render = font1.render(text, 1, (255, 255, 255))
    a, b, c, d = text_render.get_rect()
    a, b = pos
    return screen.blit(text_render, (a, b))
 
def start():
    draw_initial()
    all_circles()

def hound_win():
    if(locations[yellow] == positions[5]):
        pos1 = [positions[2], positions[6], positions[8]]
        for i in range(0, 3):
            if(locations[colors[i]] not in pos1):
                return False
        return True
    elif (locations[yellow] == positions[7]):
        pos2 = [positions[4], positions[6], positions[10]]
        for i in range(0, 3):
            if(locations[colors[i]] not in pos2):
                return False
        return True
    elif (locations[yellow] == positions[11]):
        pos3 = [positions[8], positions[9], positions[10]]
        for i in range(0, 3):
            if(locations[colors[i]] not in pos3):
                return False
        return True
    return False

def hare_win():
    if(locations[yellow] == positions[1]):
        return True
    return False

button1 = click(display, (350, 300), "Start")
button2 = click(display, (500, 300), "Quit")

open = True
possible = []
while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                color = green
            if event.key == pygame.K_2:
                color = red
            if event.key == pygame.K_3:
                color = blue
            if event.key == pygame.K_4:
                color = yellow
            key_press(color)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button1.collidepoint(pygame.mouse.get_pos()):
                start()
            elif button2.collidepoint(pygame.mouse.get_pos()):
                pygame.quit()
    pygame.display.update()


pygame.quit()
quit()
