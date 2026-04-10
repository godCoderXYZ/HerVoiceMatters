# modules
import pygame
from pygame import display
import random
import time

pygame.init()

# global variables
screenHeight = 600
screenWidth = 800
screen = display.set_mode([screenWidth, screenHeight])
clock = pygame.time.Clock()
gameSpeed = 100
minigame = "Basketball"
running = True

# images
hoop = pygame.transform.flip(pygame.image.load("hoop.png"), flip_x=True, flip_y=False)
basketball = pygame.image.load("basketball 2.png")
dotImg = pygame.image.load("dot.png")

# basketball physics variables
basketballStartingX = 64  # 64
basketballStartingY = screenHeight - 64  # 536
basketballY = basketballStartingY
basketballX = basketballStartingX
basketballDY = 0
basketballDX = 0
basketball_Y_velocity = 0
basketballGravity = 0.5
basketball_X_speed = 10
basketballJumpForce = 10
basketballWallBounce = 10
basketballRotation = 1

# hoop position (don't know which section this fits into)
hoop_Y_Direction = 0
hoopPosition = [screenWidth - 64, 192]

# shot counters
opponentBuckets = 0
playerBuckets = 0
playerBasketballMisses = 0
playerBasketballAccuracy = 0
basketsRequired = 15

# GUI settings
basketballMinigameLargeFont = pygame.font.SysFont('impact', 64)
basketballMinigameLargeTextY_Iteration = -10
basketballMinigameFont = pygame.font.SysFont('inkfree', 32)
playerBucketsDisplayPosition = (64, 32)
playerBasketballAccuracyDisplayPosition = (64, 64)
opponentBucketsDisplayPosition = (256, 32)
basketballMinigameStatsForNerdsDisplayPosition = (64, 96)
basketballMinigameGUI_StartTime = False
basketballMinigameStatsForNerdsFont = pygame.font.SysFont('ebrima', 18)
StatsForNerdsButton = pygame.Rect(basketballMinigameStatsForNerdsDisplayPosition[0],
                                  basketballMinigameStatsForNerdsDisplayPosition[1], 192, 32)
basketballMinigameShowStatsForNerds = False

# mouse
holdableMouseDown = False
mousePos = False

# basketball power
basketballPower = 0
basketballPowerIncrement = 1

# dot variables (physics var)
basketballDotX = 0
basketballDotY = 0
basketballDotDX = 0
basketballDotDY = 0
basketballDot_Y_velocity = 0

# quadratic equation variables for nerds
vertex = [basketballX, basketballY]
vertexForm = "y = a(x - h)^2 + k"
vertex_a_value = False

# win and round counter variables
basketballMinigameRoundWinner = False
playerWins = 0
opponentWins = 0
basketballRound = 0
maximumBasketballRounds = 3


# functions
def blit_text(string, color, font, position):
    text_image = font.render(string, True, color)
    screen.blit(text_image, position)


# loop
while running:
    mousePos = pygame.mouse.get_pos()
    # if minigame == "Basketball":
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if minigame == "Basketball":
                    if StatsForNerdsButton.collidepoint(mousePos):
                        if basketballMinigameShowStatsForNerds:
                            basketballMinigameShowStatsForNerds = False
                        else:
                            basketballMinigameShowStatsForNerds = True
                    else:
                        holdableMouseDown = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if minigame == "Basketball":
                    holdableMouseDown = False
                    if basketballY + basketballDY + 96 >= screenHeight:
                        # fires the basketball
                        basketball_Y_velocity = (-basketballJumpForce * basketballPower) / 22
                    basketballPower = 0
    if minigame == "Basketball":
        # aims the ball and draws dots code
        if holdableMouseDown and basketballY + basketballDY + 96 >= screenHeight and \
                basketballX == basketballStartingX and basketballRound > 0 and not \
                basketballMinigameRoundWinner:
            basketballPower += basketballPowerIncrement
            if basketballPower >= 100:
                basketballPower = 100
            basketballDotX = basketballX
            basketballDotY = basketballY
            basketballDotDX = 0
            basketballDotDY = 0
            basketballDot_Y_velocity = (-basketballJumpForce * basketballPower) / 22
            if basketballPower > 20:
                for i in range(100):
                    basketballDotDX += basketball_X_speed

                    basketballDot_Y_velocity += basketballGravity
                    basketballDotDY += basketballDot_Y_velocity

                    if basketballDotY + basketballDotDY + 64 > screenHeight:
                        basketballDotDY = 0
                        if basketballDotX == basketballStartingX:
                            basketballDot_Y_velocity = 0
                        else:
                            basketballDot_Y_velocity = -basketballWallBounce
                    elif basketballDotY + basketballDotDY < 0:
                        basketballDotDY = 0
                        basketballDot_Y_velocity = 0

                    basketballDotX += basketballDotDX
                    basketballDotY += basketballDotDY
                    if i % 15 == 5:
                        screen.blit(pygame.transform.scale(dotImg, (32 / i ** 0.25, 32 / i ** 0.25)),
                                    (basketballDotX, basketballDotY))

                    basketballDotDX = 0
                    basketballDotDY = 0

    if minigame == "Basketball":
        # basketball physics code
        if basketball_Y_velocity != 0:
            basketballDX += basketball_X_speed

        basketball_Y_velocity += basketballGravity
        basketballDY += basketball_Y_velocity

        if basketballY + basketballDY + 64 > screenHeight:
            basketballDY = 0
            if basketballX == basketballStartingX:
                basketball_Y_velocity = 0
            else:
                basketball_Y_velocity = -basketballWallBounce
        elif basketballY + basketballDY < 0:
            basketballDY = 0
            basketball_Y_velocity = 0

        if basketballY + basketballDY < vertex[1]:
            vertex[1] = basketballY + basketballDY
            vertex[0] = basketballX + basketballDX

        # hoop and ball collision
        basketballRect = basketball.get_rect(center=(basketballX, basketballY))
        hoopRect = hoop.get_rect(center=hoopPosition)
        if basketballX + basketballDX + 64 > screenWidth or basketballRect.colliderect(hoopRect):
            if basketballRect.colliderect(hoopRect):
                playerBuckets += 1
                if playerBuckets == basketsRequired:
                    basketballMinigameRoundWinner = "Player"
                elif basketballRound == maximumBasketballRounds:
                    hoopPosition[1] = random.randint(96, screenHeight - 160)
            else:
                playerBasketballMisses += 1
            playerBasketballAccuracy = round((playerBuckets / (playerBuckets + playerBasketballMisses)) * 100)

            vertex_a_value = ((screenHeight - basketballStartingX) - (screenHeight - vertex[1])) / \
                             (basketballStartingX - vertex[0]) ** 2
            vertexForm = "y = " + str(vertex_a_value) + "(x - " + str((vertex[0])) + ")^2 + " + \
                         str(screenHeight - vertex[1])

            # resetting ball physics if basket scored
            basketballDX = 0
            basketballDY = 0
            basketball_Y_velocity = 0
            basketballX = basketballStartingX
            basketballY = basketballStartingY

            vertex = [basketballX, basketballY]

        basketballX += basketballDX
        basketballY += basketballDY

        basketballDX = 0
        basketballDY = 0

    if minigame == "Basketball":
        # wins and round management and GUI
        if basketballRound > 0 and not basketballMinigameRoundWinner:
            blit_text(("Buckets: " + str(playerBuckets) + "/" + str(basketsRequired)), (255, 255, 255),
                      basketballMinigameFont, playerBucketsDisplayPosition)
            blit_text(("Accuracy: " + str(playerBasketballAccuracy) + "%"), (255, 255, 255), basketballMinigameFont,
                      playerBasketballAccuracyDisplayPosition)
            blit_text(("Opponent's Buckets: " + str(opponentBuckets) + "/" + str(basketsRequired)), (255, 255, 255),
                      basketballMinigameFont, opponentBucketsDisplayPosition)

            if basketballMinigameShowStatsForNerds:
                if StatsForNerdsButton.collidepoint(mousePos):
                    pygame.draw.rect(screen, (100, 0, 0), StatsForNerdsButton)
                    blit_text(vertexForm, (255, 255, 255), basketballMinigameStatsForNerdsFont,
                              (basketballMinigameStatsForNerdsDisplayPosition[0],
                               basketballMinigameStatsForNerdsDisplayPosition[1] + 8))
                else:
                    pygame.draw.rect(screen, (255, 255, 255), StatsForNerdsButton)
                    blit_text(vertexForm, (0, 0, 255), basketballMinigameStatsForNerdsFont,
                              (basketballMinigameStatsForNerdsDisplayPosition[0],
                               basketballMinigameStatsForNerdsDisplayPosition[1] + 8))
            else:
                if StatsForNerdsButton.collidepoint(mousePos):
                    pygame.draw.rect(screen, (100, 0, 0), StatsForNerdsButton)
                    blit_text("Quadratic Function for Nerds", (255, 255, 255), basketballMinigameStatsForNerdsFont,
                              (basketballMinigameStatsForNerdsDisplayPosition[0] + 8,
                               basketballMinigameStatsForNerdsDisplayPosition[1] + 8))
                else:
                    pygame.draw.rect(screen, (255, 255, 255), StatsForNerdsButton)
                    blit_text("Quadratic Function for Nerds", (0, 0, 0), basketballMinigameStatsForNerdsFont,
                              (basketballMinigameStatsForNerdsDisplayPosition[0] + 8,
                               basketballMinigameStatsForNerdsDisplayPosition[1] + 8))

            # hoop position
            if basketballRound == maximumBasketballRounds - 1:
                if hoop_Y_Direction == 0:
                    hoop_Y_Direction = 1
                else:
                    if hoopPosition[1] <= 96:
                        hoop_Y_Direction = 1
                    elif hoopPosition[1] >= screenHeight - 160:
                        hoop_Y_Direction = -1
            else:
                hoop_Y_Direction = 0
            hoopPosition[1] += hoop_Y_Direction
            screen.blit(hoop, hoopPosition)

            if basketball_Y_velocity == 0:
                screen.blit(basketball, (basketballX, basketballY))
            else:
                screen.blit(pygame.transform.rotate(basketball, basketballRotation), (basketballX, basketballY))
            basketballRotation -= 4

            if random.randint(1, 300) == random.randint(1, 300):
                opponentBuckets += 1
                if opponentBuckets == basketsRequired:
                    basketballMinigameRoundWinner = "Opponent"
        elif basketballRound == 0:
            if basketballMinigameGUI_StartTime:
                if basketballMinigameGUI_StartTime + 3 < time.time():
                    basketballRound = 1
                    basketballMinigameGUI_StartTime = False
                else:
                    blit_text("First to make " + str(basketsRequired) + " buckets WINS", (255, 0, 255),
                              basketballMinigameLargeFont, (0, ((1 / 6) * (basketballMinigameLargeTextY_Iteration ** 3 -
                                                                           9 * basketballMinigameLargeTextY_Iteration
                                                                           ** 2 + 10 *
                                                                           basketballMinigameLargeTextY_Iteration
                                                                           + 1776))))
                    basketballMinigameLargeTextY_Iteration += 0.1
            else:
                basketballMinigameGUI_StartTime = time.time()
        elif basketballMinigameRoundWinner:
            if basketballMinigameGUI_StartTime:
                if basketballMinigameGUI_StartTime + 3 < time.time():
                    basketballMinigameRoundWinner = False
                    basketballMinigameGUI_StartTime = False

                    if basketballRound >= maximumBasketballRounds:
                        minigame = False
                    else:
                        basketballRound += 1
                        hoopPosition[1] = 192
                else:
                    blit_text(str(playerWins) + " : " + str(opponentWins), (255, 255, 0), basketballMinigameLargeFont,
                              (256, screenHeight / 2 - 64))
                    blit_text(("ROUND " + str(basketballRound)),
                              (255, 0, 255),
                              basketballMinigameLargeFont,
                              (256, screenHeight / 2 + 64))
                    if basketballRound >= maximumBasketballRounds:
                        if playerWins > opponentWins:
                            blit_text("PLAYER WINS", (0, 255, 255),
                                      basketballMinigameLargeFont,
                                      (256, screenHeight / 2 - 128))
                        elif opponentWins > playerWins:
                            blit_text("OPPONENT WINS", (0, 255, 255),
                                      basketballMinigameLargeFont,
                                      (256, screenHeight / 2 - 192))
            else:
                basketballMinigameGUI_StartTime = time.time()
                playerBuckets = 0
                playerBasketballMisses = 0
                playerBasketballAccuracy = 0
                opponentBuckets = 0
                if basketballMinigameRoundWinner == "Player":
                    playerWins += 1
                else:
                    opponentWins += 1

    display.flip()

    clock.tick(gameSpeed)
