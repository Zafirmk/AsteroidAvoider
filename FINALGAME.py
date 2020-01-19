from GameSettings import *


def game_loop():
    spaceship = player()
    asteroids = [0,
     asteroid(1, playable_height-39, 10.5, 35, 39, 0),
     asteroid(2, playable_height-25, 15, 25, 25, 5),
     asteroid(3, playable_height-30, 12.5, 30, 30, 10),
     asteroid(4, playable_height-35, 10, 35, 35, 30)]


    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    spaceship.moveUP()
                elif event.key == pygame.K_DOWN:
                    spaceship.moveDOWN()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    spaceship.change = 0

        spaceship.y += spaceship.change

        if spaceship.y > playable_height - spaceship.height:
            spaceship.y = playable_height - spaceship.height
        elif spaceship.y < 0:
            spaceship.y = 0

        window.fill((0, 0, 0))
        window.blit(bg_img, (0, 0))

        spaceship.draw()
        for n in range(1, 5):
            if asteroids[n].x < 0:
                spaceship.score += 1
            asteroids[n].move(spaceship)
            if asteroids[n].collision(spaceship):
                asteroids[n].reset(asteroids)



        Text_display("Score: " + str(spaceship.score * 100), white, 0, 200)
        Text_display("Asteroid 1: " + str(GetDistance(1, spaceship, asteroids)), white, 0, 220)
        Text_display("Asteroid 2: " + str(GetDistance(2, spaceship, asteroids)), white, 0, 240)
        Text_display("Asteroid 3: " + str(GetDistance(3, spaceship, asteroids)), white, 0, 260)
        Text_display("Asteroid 4: " + str(GetDistance(4, spaceship, asteroids)), white, 0, 280)
        Text_display("Space Ship Position: " + str(spaceship.y / 169), white, 0, 300)


        pygame.display.update()

game_loop()
