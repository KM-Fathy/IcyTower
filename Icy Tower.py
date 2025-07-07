import pygame as pg
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import random
import math as mm

def draw_rectangle(x1, y1, x2, y2, r, g, b):
    glBegin(GL_QUADS)
    glColor3f(r, g, b)  
    glVertex2f(x1, y1)
    glColor3f(r, g, b) 
    glVertex2f(x1, y2)
    glColor3f(r, g, b) 
    glVertex2f(x2, y2)
    glColor3f(r, g, b) 
    glVertex2f(x2, y1)
    glEnd()

def draw_circle(center_x, center_y, radius, num_segments, r, g, b):
    glColor3f(r, g, b)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(num_segments + 1):  
        angle = 2.0 * mm.pi * i / num_segments
        x = center_x + radius * mm.cos(angle)
        y = center_y + radius * mm.sin(angle)
        glVertex2f(x, y)
    glEnd()

def draw_point(x, y, r, g, b):
    glPointSize(5)
    glBegin(GL_POINTS)
    glColor3f(r, g, b)
    glVertex2f(x, y)
    glEnd()

def draw_3d_triangle(x, y, z, size, rotation=0):
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(rotation, 0, 1, 0)

    #Tip of the pyramid
    Tip = (0.0, size, 0.0)

    #Base vertices
    v1 = (-size, -size, size)  
    v2 = (size, -size, size)   
    v3 = (size, -size, -size)  
    v4 = (-size, -size, -size)  

    #Draw pyramid sides
    glBegin(GL_TRIANGLES)

    glColor3f(1.0, 0.0, 0.0) 
    glVertex3fv(Tip)
    glVertex3fv(v1)
    glVertex3fv(v2)

    glColor3f(1.0, 0.5, 0.0)  
    glVertex3fv(Tip)
    glVertex3fv(v2)
    glVertex3fv(v3)

    glColor3f(1.0, 1.0, 0.0)  
    glVertex3fv(Tip)
    glVertex3fv(v3)
    glVertex3fv(v4)

    glColor3f(1.0, 0.3, 0.0)  
    glVertex3fv(Tip)
    glVertex3fv(v4)
    glVertex3fv(v1)
    glEnd()

    glPopMatrix()

def draw_main_wall():
    #Main wall background
    draw_rectangle(-1,-1,1,1,92/255,91/255,118/255)
    
    #Horizontal lines for main wall
    y = -1
    while y < 1:
        draw_rectangle(-0.7, y, 0.7, y + 0.01, 116/255, 115/255, 142/255)
        y += 0.1

    #Vertical lines for mid wall
    start = 0.0
    end = 2
    step = 0.2
    i= start
    while i < end:
        draw_rectangle(0.6, 0.9-i, 0.61, 1-i, 116/255, 115/255, 142/255)
        draw_rectangle(0.45, 0.9-i, 0.46, 1-i, 116/255, 115/255, 142/255)
        draw_rectangle(0.25, 0.9-i, 0.26, 1-i, 116/255, 115/255, 142/255)
        draw_rectangle(0, 0.9-i, 0.01, 1-i, 116/255, 115/255, 142/255)
        draw_rectangle(-0.6, 0.9-i, -0.61, 1-i, 116/255, 115/255, 142/255)
        draw_rectangle(-0.45, 0.9-i, -0.46, 1-i, 116/255, 115/255, 142/255)
        draw_rectangle(-0.25, 0.9-i, -0.26, 1-i, 116/255, 115/255, 142/255)

        draw_rectangle(0.525, 0.8-i, 0.535, 0.9-i, 116/255, 115/255, 142/255)
        draw_rectangle(0.35, 0.8-i, 0.36, 0.9-i, 116/255, 115/255, 142/255)
        draw_rectangle(0.125, 0.8-i, 0.135, 0.9-i, 116/255, 115/255, 142/255)
        draw_rectangle(-0.525, 0.8-i, -0.535, 0.9-i, 116/255, 115/255, 142/255)
        draw_rectangle(-0.35, 0.8-i, -0.36, 0.9-i, 116/255, 115/255, 142/255)
        draw_rectangle(-0.125, 0.8-i, -0.135, 0.9-i, 116/255, 115/255, 142/255)
        i += step
   
def draw_side_wall():
    #Left wall
    draw_rectangle(-1, -1, -0.7, 1, 153/255, 153/255, 187/255)
    draw_rectangle(-0.7, -1, -0.71, 1, 16/255, 8/255, 41/255)
    draw_rectangle(-0.69, -1, -0.7, 1, 46/255, 48/255, 73/255)

    #Horizontal lines for left wall
    y = -1
    while y < 1:
        draw_rectangle(-1, y, -0.7, y + 0.01, 16/255, 8/255, 41/255)
        y += 0.2

    #Vertical lines for left wall
    start = 0.0
    end = 2
    step = 0.4
    i= start
    while i < end:
        draw_rectangle(-0.9, 0.8-i, -0.91, 1-i, 16/255, 8/255, 41/255)
        draw_rectangle(-1, 0.81-i, -0.91, 1-i, 218/255, 219/255, 247/255)
        draw_rectangle(-0.89, 0.81-i, -0.9, 1-i, 46/255, 48/255, 73/255)
        
        draw_rectangle(-0.8, 0.6-i, -0.81, 0.8-i, 16/255, 8/255, 41/255)
        draw_rectangle(-1, 0.61-i, -0.81, 0.8-i, 187/255, 187/255, 221/255)
        draw_rectangle(-0.8, 0.61-i, -0.71, 0.8-i, 117/255, 117/255, 151/255)
        draw_rectangle(-0.79, 0.61-i, -0.8, 0.8-i, 46/255, 48/255, 73/255)
        i += step
  
    #Right wall
    draw_rectangle(0.7, -1, 1, 1, 153/255, 153/255, 187/255)
    draw_rectangle(0.71, -1, 0.7, 1, 16/255, 8/255, 41/255)
    draw_rectangle(0.69, -1, 0.7, 1, 46/255, 48/255, 73/255)

    #Horizontal lines for right wall
    y = -1
    while y < 1:
        draw_rectangle(0.7, y, 1, y + 0.01, 16/255, 8/255, 41/255)
        y += 0.2

    #Vertical lines for right wall
    start = 0.0
    end = 2
    step = 0.4
    i= start
    while i < end:
        draw_rectangle(0.8, 0.8-i, 0.81, 1-i, 16/255, 8/255, 41/255)
        draw_rectangle(1, 0.81-i, 0.81, 1-i, 187/255, 187/255, 221/255)
        draw_rectangle(0.8, 0.81-i, 0.71, 1-i, 117/255, 117/255, 151/255)
        draw_rectangle(0.79, 0.81-i, 0.8, 1-i, 46/255, 48/255, 73/255)

        draw_rectangle(0.9, 0.6-i, 0.91, 0.8-i, 16/255, 8/255, 41/255)
        draw_rectangle(1, 0.61-i, 0.91, 0.8-i, 218/255, 219/255, 247/255)
        draw_rectangle(0.89, 0.61-i, 0.9, 0.8-i, 46/255, 48/255, 73/255)
        i += step

def draw_torch(rotation):
    # Left wall torch
    draw_rectangle(-0.58, 0.05, -0.56, 0.15, 0.4, 0.2, 0.1)
    draw_3d_triangle(-0.57, 0.17, -1, 0.025, rotation)

    # Mid torch
    draw_rectangle(0.01, 0.05, -0.01, 0.15, 0.4, 0.2, 0.1)
    draw_3d_triangle(0, 0.17, -1, 0.025, rotation)

    # Right wall torch
    draw_rectangle(0.56, 0.05, 0.58, 0.15, 0.4, 0.2, 0.1)
    draw_3d_triangle(0.57, 0.17, -1, 0.025, rotation)

def draw_shield(center_x, center_y):
    # Outer Circle
    draw_circle(center_x, center_y, 0.12, 50, 0.5, 0.5, 0.5)  

    # Inner Cicrle
    draw_circle(center_x, center_y, 0.10, 50, 0.6, 0.3, 0.1)  

    # Center Circle
    draw_circle(center_x, center_y, 0.03, 30, 0.8, 0.8, 0.8)  

    # Cross lines 
    glColor3f(0.3, 0.2, 0.1)
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(center_x - 0.05, center_y)
    glVertex2f(center_x + 0.05, center_y)
    glVertex2f(center_x, center_y - 0.05)
    glVertex2f(center_x, center_y + 0.05)
    glEnd()


def draw_window(x, y, width, height):                     
    #Window Frame
    draw_rectangle(x - width/2, y - height/2, x + width/2, y + height/2, 0.4, 0.4, 0.5)

    #Glass
    draw_rectangle(x - width/2 + 0.02, y - height/2 + 0.02, x + width/2 - 0.02, y + height/2 - 0.02, 0.7, 0.85, 1.0)

    #Top Part
    draw_rectangle(x - width/2, y + height/2, x+ width/2 , y + height/2 + width/2, 0.4, 0.4, 0.5)  

    #Vertical bar
    draw_rectangle(x - 0.01, y - height/2 + 0.02, x + 0.01, y + height/2 - 0.02, 0.4, 0.4, 0.5)

    #Horizontal bar
    draw_rectangle(x - width/2 + 0.02, y, x + width/2 - 0.02, y + 0.01, 0.4, 0.4, 0.5)

class Platform:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1  
        self.y1 = y1  
        self.x2 = x2  
        self.y2 = y2  

    def update(self, speed):
        self.y1 -= speed
        self.y2 -= speed

    def draw(self):
        # main rectangle
        draw_rectangle(self.x1, self.y1, self.x2, self.y2, 155/255, 155/255, 189/255)
        # top highlight
        draw_rectangle(self.x1, self.y2 - 0.02, self.x2, self.y2, 227/255, 222/255, 252/255)
    
platforms = [
    Platform(-0.69, -0.9, 0.69, -0.82),
    Platform(-0.2, -0.64, 0.4, -0.56),
    Platform(0.1, -0.38, 0.45, -0.3),
    Platform(-0.1, -0.12, 0.6, -0.04),
    Platform(-0.15, 0.14, 0.15, 0.22),
    Platform(-0.67, 0.4, 0.1, 0.48),
    Platform(-0.17, 0.66, 0.38, 0.74)
]

def draw_platforms():
    for plat in platforms:
        plat.draw()

def update_platforms(speed):
    for plat in platforms:
        plat.update(speed)

    #Regenerate platforms that fall below the screen
    for i in range(len(platforms)):
        if platforms[i].y2 < -1.0:
            highest = max(p.y2 for p in platforms)
            x1New = random.uniform(-0.6, 0.4)
            width = random.uniform(0.2, 0.5)
            x2New = x1New + width
            y2New = highest + 0.3
            y1New = y2New - 0.08
            platforms[i] = Platform(x1New, y1New, x2New, y2New)

def reset_platforms():
    global platforms
    platforms = [
        Platform(-0.69, -0.9, 0.69, -0.82),
        Platform(-0.2, -0.64, 0.4, -0.56),
        Platform(0.1, -0.38, 0.45, -0.3),
        Platform(-0.1, -0.12, 0.6, -0.04),
        Platform(-0.15, 0.14, 0.15, 0.22),
        Platform(-0.67, 0.4, 0.1, 0.48),
        Platform(-0.17, 0.66, 0.38, 0.74)
    ]

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 0.01
        self.jumpForce = 0.035
        self.gravity = -0.001
        self.velocity_y = 0
        self.grounded = True
        self.leftLimit = -0.66
        self.rightLimit = 0.67
        self.score = 0
        self.facing_left = False

    def move_left(self):
        if self.x - self.speed >= self.leftLimit:
            self.x -= self.speed
            self.facing_left = True

    def move_right(self):
        if self.x + self.speed <= self.rightLimit:
            self.x += self.speed
            self.facing_left = False

    def jump(self):
        if self.grounded:
            self.velocity_y = self.jumpForce
            self.grounded = False

    def apply_gravity(self, platforms):
        self.velocity_y += self.gravity
        self.y += self.velocity_y
        self.grounded = False

        player_bottom = self.y - 0.82
        player_left = self.x - 0.01
        player_right = self.x + 0.02

        for plat in platforms:
            platform_top = plat.y2
            if (player_bottom <= platform_top <= player_bottom - self.velocity_y  and
                player_right > plat.x1 and player_left < plat.x2):
                self.y = platform_top + 0.82
                self.velocity_y = 0
                self.grounded = True
                break

    def reset(self):
        self.x = 0
        self.y = 0
        self.velocity_y = 0
        self.grounded = True
        self.score = 0

    def draw_character(self):
        glPushMatrix()

        glTranslatef(self.x, self.y, 0)

        # Flip if facing left
        if self.facing_left:
            glRotatef(180, 0, 1, 0)

        # Body
        draw_rectangle(-0.03, -0.76, 0.03, -0.69, 1, 1, 1)
        draw_rectangle(0.02, -0.69, 0.03, -0.69, 1, 1, 1)
        draw_rectangle(-0.02, -0.78, -0.01, -0.76, 232/255, 232/255, 232/255)
        draw_rectangle(0.01, -0.70, 0.02, -0.69, 18/255, 19/255, 39/255)
        draw_rectangle(0.0, -0.736, 0.02, -0.746, 232/255, 232/255, 232/255)

        # Muffler
        draw_rectangle(-0.03, -0.69, 0.02, -0.68, 84/255, 80/255, 80/255)
        draw_rectangle(-0.01, -0.70, 0.01, -0.69, 84/255, 80/255, 80/255)
        draw_rectangle(0, -0.73, 0.01, -0.69, 84/255, 80/255, 80/255)

        # Head
        draw_rectangle(-0.03, -0.68, 0.02, -0.63, 205/255, 149/255, 126/255)
        draw_point(-0.035, -0.65, 196/255, 143/255, 112/255)
        draw_point(-0.035, -0.66, 196/255, 143/255, 112/255)
        draw_rectangle(-0.02, -0.635, 0.01, -0.62, 196/255, 143/255, 112/255)
        draw_rectangle(-0.02, -0.645, 0.0, -0.635, 196/255, 143/255, 112/255)
        draw_rectangle(-0.02, -0.655, 0.0, -0.645, 196/255, 143/255, 112/255)
        draw_point(-0.0242, -0.674, 196/255, 143/255, 112/255)

        # Eyes
        draw_point(-0.005, -0.65, 0, 0, 0)
        draw_point(0.015, -0.65, 0, 0, 0)

        # Hair
        draw_rectangle(-0.04, -0.645, -0.03, -0.62, 150/255, 147/255, 132/255)
        draw_rectangle(-0.03, -0.63, -0.02, -0.61, 150/255, 147/255, 132/255)
        draw_rectangle(-0.02, -0.62, 0.01, -0.61, 150/255, 147/255, 132/255)
        draw_rectangle(0.02, -0.63, 0.01, -0.617, 150/255, 147/255, 132/255)
        draw_point(-0.0142, -0.627, 166/255, 154/255, 133/255)
        draw_rectangle(-0.02, -0.645, -0.03, -0.63, 166/255, 154/255, 133/255)
        draw_rectangle(-0.02, -0.666, -0.03, -0.645, 150/255, 147/255, 132/255)

        # Hands
        draw_point(-0.025, -0.754, 205/255, 149/255, 126/255)
        draw_point(0.025, -0.754, 205/255, 149/255, 126/255)
        draw_rectangle(-0.03, -0.73, -0.02, -0.69, 18/255, 19/255, 39/255)
        draw_rectangle(0.02, -0.73, 0.03, -0.69, 18/255, 19/255, 39/255)

        # Legs
        draw_rectangle(0.02, -0.82, 0.01, -0.78, 18/255, 19/255, 39/255)
        draw_point(0.015, -0.814, 145/255, 81/255, 25/255)
        draw_rectangle(-0.01, -0.82, 0, -0.78, 18/255, 19/255, 39/255)
        draw_point(-0.005, -0.814, 145/255, 81/255, 25/255)

        # Pelvis
        draw_rectangle(-0.01, -0.746, 0.02, -0.78, 18/255, 19/255, 39/255)
        draw_point(-0.005, -0.75, 232/255, 232/255, 232/255)

        glPopMatrix()
 
def draw_background_gameover():
    draw_main_wall()
    draw_window(0.35, 0.1, 0.2, 0.6)
    draw_window(-0.35, 0.1, 0.2, 0.6)
    draw_side_wall()

def draw_background(rotation):
    draw_main_wall()
    draw_window(0.35, 0.1, 0.2, 0.6)
    draw_window(-0.35, 0.1, 0.2, 0.6)
    draw_torch(rotation)
    draw_shield(-0.35, -0.4)
    draw_shield(0.35, -0.4)
    draw_platforms()
    draw_side_wall()

def draw_text(text, x, y, font_size, color=(252, 171, 0)):
    font = pg.font.SysFont('Arial', font_size, bold=True)
    text_surface = font.render(text, True, color)
    text_data = pg.image.tostring(text_surface, "RGBA", True)
    width, height = text_surface.get_size()
    glRasterPos2f(x, y)  
    glDrawPixels(width, height, GL_RGBA, GL_UNSIGNED_BYTE, text_data)

def enable_transparency():
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

def show_game_over_screen():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_background_gameover()
    draw_text("Game Over", -0.5, 0.1, 120)
    draw_text("Press R to Restart", -0.2, -0.05, 30)
    pg.display.flip()

def main():
    pg.init()
    pg.mixer.init()

    #Load and play background music
    pg.mixer.music.load("assets\Background.mp3")
    pg.mixer.music.set_volume(0.05)
    pg.mixer.music.play(-1)

    #Load sounds
    jump_sound = pg.mixer.Sound("assets\Jump.mp3")
    jump_sound.set_volume(0.3)

    game_over_sound = pg.mixer.Sound("assets\Gameover 2.wav")
    game_over_sound.set_volume(0.5)

    display = (1000, 750)
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)
    enable_transparency()

    gluOrtho2D(-1, 1, -1, 1)

    rotation = 0
    player = Player()
    reset_platforms()
    game_over = False

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    player.jump()
                    jump_sound.play()

        keys = pg.key.get_pressed()

        if game_over:
            show_game_over_screen()
            if keys[pg.K_r]:
                player.reset()
                reset_platforms()
                game_over = False
                pg.mixer.music.unpause()
            pg.time.wait(10)
            continue

        if keys[pg.K_a]:
            player.move_left()
        if keys[pg.K_d]:
            player.move_right()

        player.apply_gravity(platforms)

        if player.y < -1:
            game_over = True
            pg.mixer.music.pause()
            game_over_sound.play()

        if player.y > 0.35:
            scroll_speed = player.y - 0.35
            update_platforms(scroll_speed)
            player.y = 0.35
            player.score += int(scroll_speed * 100)

        glClear(GL_COLOR_BUFFER_BIT)
        draw_background(rotation)
        draw_text(f"Score: {player.score}", 0.72, 0.9, 30)
        player.draw_character()

        rotation += 1
        if rotation >= 360:
            rotation = 0

        pg.display.flip()
        pg.time.wait(10)
main()
