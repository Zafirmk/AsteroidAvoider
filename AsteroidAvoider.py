import pygame
import random

pygame.init()

class asteroid:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

class hitbox:
    def __init__(self, width, height):
        self.width = width
        self.height = height

y_change = 0
x = 20
y = 70
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
width_screen = 900
height_screen = 200
height_plane = 52
width_plane = 66

hitbox_x = x + 15
hitbox_y = y + 10
spaceship_hitbox_height = 30

asteroid1_hitbox = hitbox(40, 40)
asteroid2_hitbox = hitbox(25, 25)
asteroid3_hitbox = hitbox(30, 30)
asteroid4_hitbox = hitbox(35, 35)
shooting_star_hitbox = hitbox(27, 40)

game_over = False
window = pygame.display.set_mode((width_screen, height_screen))
audio_menu = pygame.mixer.Sound("./Music/MainMenu.wav")
audio_ingame = pygame.mixer.Sound("./Music/InGame.wav")
audio_crashed = pygame.mixer.Sound("./Music/GameOver.wav")
pygame.display.set_caption("Astroid Avoider")
spaceship_img = pygame.image.load("./Images/Spaceship.png")
broken_spaceship_img = pygame.image.load("./Images/Spaceship_Broken.png")
game_name_img = pygame.image.load("./Images/GameName.png")
background_img = pygame.image.load("./Images/Background.png")
asteroid1_img = pygame.image.load("./Images/Asteroid1.png")
asteroid2_img = pygame.image.load("./Images/Asteroid2.png")
asteroid3_img = pygame.image.load("./Images/Asteroid3.png")
asteroid4_img = pygame.image.load("./Images/Asteroid4.png")
shooting_star_img = pygame.image.load("./Images/ShootingStar.png")
game_over_img = pygame.image.load("./Images/GameOver.png")
font = pygame.font.SysFont(None, 25)

def print_hitbox(asteroid1, asteroid2, asteroid3, asteroid4, shooting_star):
    pygame.draw.rect(window, red, [asteroid1.x, asteroid1.y, asteroid1_hitbox.width, asteroid1_hitbox.height])
    pygame.draw.rect(window, red, [asteroid2.x, asteroid2.y, asteroid2_hitbox.width, asteroid2_hitbox.height])
    pygame.draw.rect(window, red, [asteroid3.x, asteroid3.y, asteroid3_hitbox.width, asteroid3_hitbox.height])
    pygame.draw.rect(window, red, [asteroid4.x, asteroid4.y, asteroid4_hitbox.width, asteroid4_hitbox.height])
    pygame.draw.rect(window, green, [shooting_star.x, shooting_star.y, shooting_star_hitbox.width, shooting_star_hitbox.height])

def print_graphics(asteroid1, asteroid2, asteroid3, asteroid4, shooting_star,x ,y):
    window.blit(background_img, (0, 0))
    window.blit(spaceship_img, (x, y))
    window.blit(asteroid1_img, (asteroid1.x, asteroid1.y))
    window.blit(asteroid2_img, (asteroid2.x, asteroid2.y))
    window.blit(asteroid3_img, (asteroid3.x, asteroid3.y))
    window.blit(asteroid4_img, (asteroid4.x, asteroid4.y))
    window.blit(shooting_star_img, (shooting_star.x, shooting_star.y))

def score_display(msg, color):
    screen_text = font.render(msg, True, color)
    window.blit(screen_text, (0, 0))

def main_menu():
    main_menu = True

    pygame.mixer.Sound.play(audio_menu, 10)
    while main_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main_menu = False
        window.fill(black)
        window.blit(game_name_img, (0, 0))
        pygame.display.update()

def crashed(dodged):
    crash_value = True
    pygame.mixer.Sound.stop(audio_ingame)
    pygame.mixer.Sound.play(audio_crashed)
    while crash_value:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop(game_over, y, y_change, x, hitbox_y)
        window.blit(game_over_img, (230, 35))
        pygame.display.update()

        score_display("Score: " + str(dodged * 100), white)

def game_loop(game_over, y, y_change, x, hitbox_y):
    pygame.mixer.Sound.stop(audio_menu)
    pygame.mixer.Sound.stop(audio_ingame)
    pygame.mixer.Sound.play(audio_ingame, 100)

    asteroid1 = asteroid(1100, (random.randrange(0, 150)), -10)
    asteroid2 = asteroid(1100, (random.randrange(0, 175)), -15)
    asteroid3 = asteroid(1100, (random.randrange(0, 170)), -12.5)
    asteroid4 = asteroid(1100, (random.randrange(0, 165)), -10)
    shooting_star = asteroid(2000, (random.randrange(0, 173)), -25)

    dodged = 0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        y += y_change
        hitbox_y += y_change
        print_hitbox(asteroid1, asteroid2, asteroid3, asteroid4, shooting_star)
        window.fill(black)
        print_graphics(asteroid1, asteroid2, asteroid3, asteroid4, shooting_star, x, y)

        asteroid1.x += asteroid1.speed
        if dodged >= 10:
            asteroid2.x += asteroid2.speed
        if dodged >=25:
            asteroid3.x += asteroid3.speed
        if dodged >=70:
            asteroid4.x += asteroid4.speed
        if dodged >= 100:
         shooting_star.x += shooting_star.speed


        if y > height_screen - height_plane:
            y = height_screen - height_plane
        elif y < 0:
            y = 0
                                                                # Adding Borders
        if hitbox_y > height_screen - 45:
            hitbox_y = height_screen - 42
        elif hitbox_y < 10:
            hitbox_y = 10

        if asteroid1.x <= 0:
            asteroid1.x = 1100
            asteroid1.y = random.randrange(0, 150)
            dodged += 1
        if asteroid2.x <= 0:
            asteroid2.x = 1100
            asteroid2.y = random.randrange(0, 175)
            dodged += 1
        if asteroid3.x <= 0:                                        # Progressive Game difficulty increasing
            asteroid3.x = 1100
            asteroid3.y = random.randrange(0, 170)
            dodged += 1
        if asteroid4.x <= 0:
            asteroid4.x = 1500
            asteroid4.y = random.randrange(0, 165)
            dodged += 1
        if shooting_star.x <= 0:
            shooting_star.x = 2000
            shooting_star.y = random.randrange(0, 173)
            dodged += 1

        # Checking for Collisions

        if asteroid1.x <= 60:
            if hitbox_y in range(asteroid1.y, asteroid1.y + asteroid1_hitbox.height) or \
                    hitbox_y + spaceship_hitbox_height in\
                    range(asteroid1.y, asteroid1.y + asteroid1_hitbox.height):
                window.blit(broken_spaceship_img, (x,y))
                crashed(dodged)
        if asteroid2.x <= 60:
            if hitbox_y in range(asteroid2.y, asteroid2.y + asteroid2_hitbox.height) or\
                    hitbox_y + spaceship_hitbox_height in\
                    range(asteroid2.y, asteroid2.y + asteroid2_hitbox.height):
                window.blit(broken_spaceship_img, (x,y))
                crashed(dodged)

        if asteroid3.x <= 60:
            if hitbox_y in range(asteroid3.y, asteroid3.y + asteroid3_hitbox.height) or\
                    hitbox_y + spaceship_hitbox_height in\
                    range(asteroid3.y, asteroid3.y + asteroid3_hitbox.height):
                window.blit(broken_spaceship_img, (x,y))
                crashed(dodged)

        if asteroid4.x <= 60:
            if hitbox_y in range(asteroid4.y, asteroid4.y + asteroid4_hitbox.height) or\
                    hitbox_y + spaceship_hitbox_height in\
                    range(asteroid4.y, asteroid4.y + asteroid4_hitbox.height):
                window.blit(broken_spaceship_img, (x,y))
                crashed(dodged)
        if shooting_star.x <= 40:
            if hitbox_y in range(shooting_star.y, shooting_star.y + shooting_star_hitbox.height) or\
                    hitbox_y + spaceship_hitbox_height \
                    in range(shooting_star.y, shooting_star.y + shooting_star_hitbox.height):
                window.blit(broken_spaceship_img, (x,y))
                crashed(dodged)

        score_display("Score: " + str(dodged * 100), white)
        pygame.display.update()
main_menu()
game_loop(game_over, y, y_change, x, hitbox_y)
pygame.quit()
