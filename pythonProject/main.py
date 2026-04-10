import pygame
import random
import time
from pygame import display

pygame.init()

# cursors
ibeam_cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_IBEAM)
default_cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_ARROW)
clickable_cursor = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_HAND)

# time
expectedTime = 0
clock = pygame.time.Clock()

# controller
playerController = False
cutscene = False

# fonts
text_font = pygame.font.Font("AtarianSystem.ttf", 40)
text_font2 = pygame.font.Font("Turok.otf", 30)
menu_start_font = pygame.font.Font("NineTsuki.otf", 65)
nineTsukiFont = pygame.font.Font("NineTsuki.otf", 36)

# display settings
screenWidth = 800
screenHeight = 600
running = True
screen = display.set_mode((screenWidth, screenHeight))
display.set_caption("We're no strangers to love")
iconImg = pygame.image.load("player_front_face.png")
age12Img = pygame.image.load("age_12.png")
coinImg = pygame.image.load("coin.png")
display.set_icon(iconImg)
text_string = ""
cutsceneStage = 0
cutsceneTransition = False
gameSpeed = 100
scenario = 1
minigame = False
gameStarted = False
gameDescription = False
cutsceneServerColor = [0, 0, 0]
defaultServerColor = [0, 0, 30]
spaceToSkipImg = text_font.render("Press SPACE to skip", True, (255, 255, 255))
centralizeBalance = False

# SOUND FILES
# cutscenes
trash_talk_sound_file = pygame.mixer.Sound("trash_talk.wav")
laugh_sound_file = pygame.mixer.Sound("laugh.wav")
tryouts_apology_sound_file = pygame.mixer.Sound("tryouts_apology.wav")
so_random_sound_file = pygame.mixer.Sound("so_random.wav")
basic_course_teaching_sound_file = pygame.mixer.Sound("basic_course_teaching.wav")
basic_course_boring_sound_file = pygame.mixer.Sound("basic_course_boring.wav")
student_complaint_sound_file = pygame.mixer.Sound("student_complaint.wav")
pfft_sound_file = pygame.mixer.Sound("pfft.wav")
injustice_sound_file = pygame.mixer.Sound("injustice.wav")
worker_conversation_sound_file = pygame.mixer.Sound("worker_conversation.wav")

# background tracks and minigame tracks
hills_of_radiant_winds_sound_file = pygame.mixer.Sound("hills_of_radiant_winds.wav")
cipher_sound_file = pygame.mixer.Sound("cipher.wav")
math_minigame_theme_track_sound_file = pygame.mixer.Sound("math_minigame_theme_track.wav")
basketball_minigame_theme_track_sound_file = pygame.mixer.Sound("basketball_minigame_theme_track.wav")
wire_minigame_theme_track_sound_file = pygame.mixer.Sound("wire_minigame_theme_track.wav")

# set volume
hills_of_radiant_winds_sound_file.set_volume(1)
cipher_sound_file.set_volume(0)
math_minigame_theme_track_sound_file.set_volume(0)
basketball_minigame_theme_track_sound_file.set_volume(0)
wire_minigame_theme_track_sound_file.set_volume(0)

# play tracks
hills_of_radiant_winds_sound_file.play(-1)
cipher_sound_file.play(-1)
math_minigame_theme_track_sound_file.play(-1)
basketball_minigame_theme_track_sound_file.play(-1)
wire_minigame_theme_track_sound_file.play(-1)

# Sound FX
beep_sound_file = pygame.mixer.Sound("beep.wav")
whistle_sound_file = pygame.mixer.Sound("whistle.wav")
basketball_score_sound_file = pygame.mixer.Sound("basketball_score.wav")
wire_connect_sound_file = pygame.mixer.Sound("wire_connect.wav")

# set volume
whistle_sound_file.set_volume(0.6)
basketball_score_sound_file.set_volume(0.6)

# player data?
ageConfirmation = False
age = False

# Rectangles and text
menuStartPosition = (64, (screenHeight / 2))
menuStartRectangle = pygame.Rect(menuStartPosition[0], menuStartPosition[1], 256, 64)
menuStartOutlineRectangle = pygame.Rect(menuStartPosition[0] - 5, menuStartPosition[1] - 5, 266, 74)

menuDescriptionPosition = (64, (screenHeight / 2) + 128)
menuDescriptionRectangle = pygame.Rect(menuDescriptionPosition[0], menuDescriptionPosition[1], 256, 64)
menuDescriptionOutlineRectangle = pygame.Rect(menuDescriptionPosition[0] - 5, menuDescriptionPosition[1] - 5, 266, 74)

menuButtonPosition = (256, screenHeight - 128)
menuButtonRectangle = pygame.Rect(menuButtonPosition[0], menuButtonPosition[1], 256, 64)
menuButtonOutlineRectangle = pygame.Rect(menuButtonPosition[0] - 5, menuButtonPosition[1] - 5, 266, 74)

decisionPromptDimensions = (screenWidth - 100, 32)
decisionPromptPosition = ((screenWidth - decisionPromptDimensions[0]) / 2, 0)
decisionPromptRectangle = pygame.Rect(decisionPromptPosition[0], decisionPromptPosition[1], decisionPromptDimensions[0],
                                      decisionPromptDimensions[1])

apriSlipDimensions = (screenWidth - 256, 352)
apriSlipPosition = (128, 128)
apriSlipRectangle = pygame.Rect(apriSlipPosition[0], apriSlipPosition[1], apriSlipDimensions[0], apriSlipDimensions[1])
apriSlipRectangleBorder = pygame.Rect(apriSlipPosition[0] - 16, apriSlipPosition[1] - 16,
                                      apriSlipDimensions[0] + 32, apriSlipDimensions[1] + 32)

endButtonPosition = (32, screenHeight - 128)
endButtonRectangle = pygame.Rect(endButtonPosition[0], menuButtonPosition[1], 256, 64)
endButtonOutlineRectangle = pygame.Rect(endButtonPosition[0] - 5, menuButtonPosition[1] - 5, 266, 74)

retryButtonPosition = (480, screenHeight - 128)
retryButtonRectangle = pygame.Rect(retryButtonPosition[0], menuButtonPosition[1], 256, 64)
retryButtonOutlineRectangle = pygame.Rect(retryButtonPosition[0] - 5, menuButtonPosition[1] - 5, 266, 74)

choiceDimensions = (192, 32)
rectActiveColor = 'yellow'
rectInactiveColor = 'darkgreen'
rectHoverColor = 'green'
textActive = False
playerTyping = False
selectedChoice = False
textStage = 0

# player setup
player_size = [128, 128]
playerY_offset = player_size[1]
playerImgFront = pygame.transform.scale(pygame.image.load("player_front.png"), player_size)
playerImgLeft = pygame.transform.scale(pygame.image.load("player_left.png"), player_size)
playerImgRight = pygame.transform.scale(pygame.image.load("player_right.png"), player_size)

# cutscene images
boyImg = pygame.transform.scale(pygame.image.load("boy.png"), (96, 96))
basicTeacherImg = pygame.transform.scale(pygame.image.load("basic_teacher.png"), (128, 128))
advancedTeacherImg = pygame.transform.scale(pygame.image.load("advanced_teacher.png"), (96, 96))
husbandImg = pygame.image.load("husband.png")
workerImg = pygame.image.load("worker.png")

# player physics
playerX = screenWidth / 2
playerY = screenHeight - playerY_offset
playerDirection = 0
playerJumpVelocity = 0
playerJumpForce = 20
playerSpeed = 4
playerMaxJumps = 2
playerJumps = 0
wallDown = False
playerFallingDown = False
playerGravity = 1.8

# mouse and key
holdableMouseDown = False
holdableSpaceDown = False
mouseDown = False
keyEnterDown = False

# other variables
playerBalance = 100
playerBalanceHighscore = 0
cutscenesUnlocked = []
totalCutscenes = 6
minigamesUnlocked = []
totalMinigames = 3

# BASKETBALL MINIGAME VARIABLES
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
basketsRequired = 10

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
holdClickToShootImg = text_font2.render('Hold CLICK to SHOOT', True, (255, 165, 0))

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

# MATH MINIGAME VARIABLES
# settings
mathMinigameFont = pygame.font.SysFont("Arial", 20)
coverSize = (621, 877)
questionSize = (800, 269)
coverY = 0
scrollSpeed = 0.3
Course = False
mathQuestion = False
answerInputPosition = (25, 250)
answerDisplayPosition = (400, 500)
answerDisplayDelay = 2
questionBoxWidth = 750
basicAnswers = [["x = -2", "x=-2", "-2", "negative two"],
                ["x=6", "x = 6", "6", "six"], False]
advancedAnswers = [["x = 7", "x=7", "7", "seven"], ["x=8", "x = 8", "8", "eight"],
                   ["x = 1", "x=1", "1", "one", "trick question!"]]
advancedCorrectAnswerCount = 0
maximumCoverY = 300
answerDisplayTimeStart = False
answerCorrect = False
spaceToQuickScrollImg = nineTsukiFont.render("Hold SPACE to QUICK SCROLL", True, (0, 0, 0))
TTT_IMG = mathMinigameFont.render("Type Here", True, (0, 0, 0))  # TTT stands for 'Type to Type', however, the text was
ShowTTT = False                                                  # later changed to 'Type Here'

# rectangles
mathMinigameTextRectangle = pygame.Rect(20, 230, 760, 180)

# win counter
basicWin = False
advancedWin = False

# images
basicCourseCover = pygame.image.load("Basic Course Cover.jpeg")
basicCourseQ1 = pygame.image.load("Basic Course Q1.png")
basicCourseQ2 = pygame.image.load("Basic Course Q2.png")
basicCourseQ3 = pygame.image.load("Basic Course Q3.png")
basicQuestions = [basicCourseQ1, basicCourseQ2, basicCourseQ3]

advancedCourseCover = pygame.image.load("Advanced Course Cover.jpeg")
advancedCourseQ1 = pygame.image.load("Advanced Course Q1.png")
advancedCourseQ2 = pygame.image.load("Advanced Course Q2.png")
advancedCourseQ3 = pygame.image.load("Advanced Course Q3.png")
advancedQuestions = [advancedCourseQ1, advancedCourseQ2, advancedCourseQ3]

# WIRE MINIGAME VARIABLES
# text settings
heart_img = pygame.transform.scale(pygame.image.load('heart.png'), (32, 32))

# wire variables
wireCount = 4
wireLives = 3
leftWireSelected = False
rightWireSelected = False
leftWiresActive = []
rightWiresActive = []
leftWireColors = []
rightWireColors = []
wireColorPossibilities = ['red', 'yellow', 'magenta', 'blue', 'green', 'orange', 'indigo', 'aquamarine', 'brown',
                          'silver', 'ivory', 'darkgreen', 'dodgerblue', 'greenyellow', 'midnightblue',
                          'mediumslateblue', 'aliceblue']

for i in range(wireCount):
    leftWiresActive.append(False)
    rightWiresActive.append(False)
    color = wireColorPossibilities[i]
    leftWireColors.append(color)
    rightWireColors.append(color)
    random.shuffle(leftWireColors)
    random.shuffle(rightWireColors)

# wire settings
wireCircleBorderColor = "black"
wireCircleHoverColor = 'white'

wireCircleY_Starting = (screenHeight / 2) / wireCount
wireCircleY_Distance = screenHeight / wireCount
wireCircleRadius = 16
wireCircleBorderSize = 4
wireCircleScreenEdgeOffset = 100
wireCircleX_Left = wireCircleScreenEdgeOffset
wireCircleX_Right = screenWidth - wireCircleScreenEdgeOffset
wireMinigameWin = False


def draw_age_confirmation():
    do_text(text_type=3, string="Please enter your age", text_color="black", rect_color="white",
            text_position=(32, 192))

    if text_string or not ShowTTT:
        string = do_text(text_type=2, string=text_string,
                         text_color="red", rect_color="yellow", text_position=(32, 256),
                         rectangle_dimensions=(256, 32), font=text_font2, do_cursor=True)
    else:
        do_text(text_type=2, string="Type Here",
                    text_color="red", rect_color="yellow", text_position=(32, 256),
                    rectangle_dimensions=(256, 32), font=text_font2, do_cursor=True)
        string = ""
    rect = pygame.Rect(screenWidth - 320, screenHeight / 2, 256, 256)
    pygame.draw.rect(screen, (255, 255, 255), rect)
    screen.blit(age12Img, (screenWidth - 320, screenHeight / 2))
    if keyEnterDown:
        if string.isdigit():
            pygame.mouse.set_cursor(default_cursor)
            return [string, True]
        else:
            string = ""
            return [string, False]
    else:
        return [string, False]


def draw_apri_slip():
    pygame.draw.rect(screen, (150, 75, 0), apriSlipRectangleBorder)
    pygame.draw.rect(screen, (196, 164, 132), apriSlipRectangle)

    blit_multi_lined_text("____________GROUP 8____________"
                          " Please meet your group at ROOM 1600"
                          " ______________________________"
                          " Group Members: Real Cool Zombie, Lemon, Acrocan, Tank Destroyer, The Epics, Sleepy, "
                          "A Gaming Noob, Master Yeet, Chess Master, United Soups, Chu Chu Train",
                          (92, 64, 51), text_font, apriSlipPosition,
                          max_width=apriSlipDimensions[0] + apriSlipPosition[0])


def draw_menu():
    screen.blit((pygame.transform.scale(pygame.image.load("player_front.png"), (256, 256))),
                ((screenWidth / 2) + 64, (screenHeight / 2)))
    screen.blit((pygame.transform.scale(pygame.image.load("player_left.png"), (256, 256))),
                ((screenWidth / 2), (screenHeight / 2)))
    screen.blit((pygame.transform.scale(pygame.image.load("player_right.png"), (256, 256))),
                ((screenWidth / 2) + 160, (screenHeight / 2)))

    pygame.draw.rect(screen, (230, 190, 78), menuStartOutlineRectangle)
    if menuStartRectangle.collidepoint(mousePos):
        pygame.draw.rect(screen, (90, 90, 90), menuStartRectangle)
        pygame.mouse.set_cursor(clickable_cursor)
        if mouseDown:
            beep_sound_file.play()
            pygame.mouse.set_cursor(default_cursor)
            return 1
    else:
        pygame.draw.rect(screen, (0, 0, 0), menuStartRectangle)

    pygame.draw.rect(screen, (230, 190, 78), menuDescriptionOutlineRectangle)
    if menuDescriptionRectangle.collidepoint(mousePos):
        pygame.draw.rect(screen, (90, 90, 90), menuDescriptionRectangle)
        pygame.mouse.set_cursor(clickable_cursor)
        if mouseDown:
            beep_sound_file.play()
            pygame.mouse.set_cursor(default_cursor)
            return 2
    else:
        pygame.draw.rect(screen, (0, 0, 0), menuDescriptionRectangle)
        if not menuStartRectangle.collidepoint(mousePos):
            # if both buttons are not hovered on
            pygame.mouse.set_cursor(default_cursor)

    blit_text("START", (230, 190, 78), menu_start_font, (menuStartPosition[0] + 32, menuStartPosition[1]))
    blit_text("Description", (230, 190, 78), menu_start_font, (menuStartPosition[0], menuStartPosition[1] + 128))
    blit_text("Presented to you by Micah Shaw", (230, 190, 78), text_font2,
              (16, screenHeight - 48))
    blit_text("Her voice matters", (230, 230, 230), menu_start_font, (128, 64))
    return False


def draw_description():
    blit_multi_lined_text('''This is an interactive story which allows you to experience the life of a 13 year old 
            female in the Present Day, and the life of a 28 year old wife living through World War II. Hopefully 
            you are able to learn more about gender inequality, and learn how important it is to promote gender 
            equality and spread awareness about the topic. Thank you so much for spending your time to experience 
            the adventures of these two females in a world of gender inequality.''', (230, 190, 78), text_font, (0, 0))

    pygame.draw.rect(screen, (230, 190, 78), menuButtonOutlineRectangle)
    if menuButtonRectangle.collidepoint(mousePos):
        pygame.draw.rect(screen, (90, 90, 90), menuButtonRectangle)
        pygame.mouse.set_cursor(clickable_cursor)
        if mouseDown:
            pygame.mouse.set_cursor(default_cursor)
            return True
    else:
        pygame.mouse.set_cursor(default_cursor)
        pygame.draw.rect(screen, (0, 0, 0), menuButtonRectangle)

    blit_text("MENU", (230, 190, 78), menu_start_font, (menuButtonPosition[0] + 64, menuButtonPosition[1]))

    return False


def draw_present_day_end():
    blit_multi_lined_text('''After lots of effort and dedication, you were able to prove yourself to be capable, 
    despite being a girl. However, many other girls like yourself are not so lucky, and are thought of as incapable, 
    especially in areas such as sports or maths. This affects the career they pursue and makes females less likely 
    to choose career paths typically 'belonging' to men, such as sports and maths. Therefore, it is very important to 
    promote gender equality and awareness on this topic, in order to prevent other girls from going through what you 
    went through. Now you will experience the life of a 28 year old wife living through World War II. Hopefully you 
    are able to learn something from this experience and compare how gender inequality has changed from the WWII to 
    the Present Day.''', (230, 190, 78), nineTsukiFont, (0, 0))

    pygame.draw.rect(screen, (230, 190, 78), menuButtonOutlineRectangle)
    if menuButtonRectangle.collidepoint(mousePos):
        pygame.draw.rect(screen, (90, 90, 90), menuButtonRectangle)
        pygame.mouse.set_cursor(clickable_cursor)
        if mouseDown:
            pygame.mouse.set_cursor(default_cursor)
            return True
    else:
        pygame.mouse.set_cursor(default_cursor)
        pygame.draw.rect(screen, (0, 0, 0), menuButtonRectangle)

    blit_text("WWII", (230, 190, 78), menu_start_font, (menuButtonPosition[0] + 64, menuButtonPosition[1]))

    return False


def draw_ww2_end():
    blit_multi_lined_text('''This story shows the struggle of females like yourself during World War II, and why it
     is crucial to promote gender equality as quickly as possible to raise awareness on the topic and prevent other
      girls from going through what you went through. Hopefully you have learned something about gender inequality
       through reading these stories, and thank you once again for spending your time to experience this
        adventure.''', (230, 190, 78), nineTsukiFont, (0, 0))
    blit_text("Cutscenes Unlocked: " + str(len(cutscenesUnlocked)) + "/" + str(totalCutscenes), (230, 190, 78),
              nineTsukiFont,
              (0, screenHeight / 2))
    blit_text("Minigames Unlocked: " + str(len(minigamesUnlocked)) + "/" + str(totalMinigames), (230, 190, 78),
              nineTsukiFont,
              (0, (screenHeight / 2) + 32))

    blit_text("Balance: ", (230, 190, 78), nineTsukiFont, (screenWidth - 224, screenHeight / 2))
    blit_text("Balance Highscore: ", (230, 190, 78), nineTsukiFont, (screenWidth - 352, (screenHeight / 2) + 40))

    pygame.draw.rect(screen, (230, 190, 78), endButtonOutlineRectangle)
    pygame.draw.rect(screen, (230, 190, 78), retryButtonOutlineRectangle)

    if endButtonRectangle.collidepoint(mousePos):
        pygame.mouse.set_cursor(clickable_cursor)
        pygame.draw.rect(screen, (90, 90, 90), endButtonRectangle)
        if mouseDown:
            pygame.mouse.set_cursor(default_cursor)
            return 1
    else:
        pygame.draw.rect(screen, (0, 0, 0), endButtonRectangle)

    if retryButtonRectangle.collidepoint(mousePos):
        pygame.mouse.set_cursor(clickable_cursor)
        pygame.draw.rect(screen, (90, 90, 90), retryButtonRectangle)
        if mouseDown:
            pygame.mouse.set_cursor(default_cursor)
            return 2
    else:
        pygame.draw.rect(screen, (0, 0, 0), retryButtonRectangle)
        if not endButtonRectangle.collidepoint(mousePos):
            pygame.mouse.set_cursor(default_cursor)

    blit_text("END", (230, 190, 78), menu_start_font, (endButtonPosition[0], endButtonPosition[1]))
    blit_text("RETRY", (230, 190, 78), menu_start_font, (retryButtonPosition[1], retryButtonPosition[1]))

    return False


def draw_balance():
    balance_x = screenWidth - 112
    balance_y = screenHeight - 36
    if minigame == "Wire" and wireCount >= 10:
        balance_x = (screenWidth / 2) - 80
    elif centralizeBalance:
        if scenario == 1:
            balance_x = (screenWidth / 2) - 80
            balance_y = screenHeight - 48
        elif scenario == 2:
            balance_x = screenWidth - 128
            balance_y = screenHeight / 2

            do_text(text_type=3, string="     " + str(playerBalanceHighscore), text_color="white",
                    rect_color=(0, 0, 90), text_position=(balance_x, balance_y + 40), font=text_font2)
            screen.blit(coinImg, (balance_x, balance_y + 40))
    do_text(text_type=3, string="     " + str(playerBalance), text_color="white", rect_color=(0, 0, 90),
            text_position=(balance_x, balance_y), font=text_font2)
    screen.blit(coinImg, (balance_x, balance_y))


def check_string_length(string, color, font, max_width):
    text_image = font.render(string, True, color)

    # delete a character if text image is longer than question box
    if text_image.get_width() > max_width:  # text_image.get_width() - max_width
        while True:
            string = string[:-1]
            text_image = font.render(string, True, color)
            if text_image.get_width() <= max_width:
                break

        text_image = font.render(string, True, color)
        return [text_image, string]
    else:
        return [text_image, string]


def player(x, y, direction):
    if direction == 0:
        screen.blit(playerImgFront, (x, y))
    elif direction == 1:
        screen.blit(playerImgRight, (x, y))
    elif direction == -1:
        screen.blit(playerImgLeft, (x, y))


def blit_text(string, color, font, position):
    text_image = font.render(string, True, color)
    screen.blit(text_image, position)


def blit_multi_lined_text(string, color, font, position, max_width=screenWidth):
    x, y = position
    space_size = font.size(' ')
    for word in string.split():
        word_image = font.render(word, True, color)
        if word_image.get_width() + x >= max_width:
            x = position[0]
            y += word_image.get_height()
        screen.blit(word_image, (x, y))
        x += word_image.get_width() + space_size[0]

    return y + space_size[1]


def draw_default_continue(prompt, choice="CONTINUE", choice_rectangle_color=[173, 216, 230]):
    return do_text(text_type=1, string=prompt,
                   choices=[choice], text_color="black", rect_color="white",
                   choice_rect_color=choice_rectangle_color, choice_text_color="black", text_position=(0, 0))


def draw_default_decision(prompt, choices):
    return do_text(text_type=1, string=prompt,
                   choices=choices, text_color="black", rect_color="white",
                   choice_rect_color=[255, 51, 51], choice_text_color="white")


def blit_lives(x, y):
    for iteration in range(wireLives):
        screen.blit(heart_img, (x + (32 * iteration), y))


def draw_wire_circle(side, row, mouse_pos):
    if side == "left":
        border = pygame.draw.circle(screen,
                                    wireCircleBorderColor,
                                    (wireCircleX_Left, wireCircleY_Starting + wireCircleY_Distance * (row - 1)),
                                    wireCircleRadius + wireCircleBorderSize)
        if border.collidepoint(mouse_pos):
            pygame.draw.circle(screen, wireCircleHoverColor,
                               (wireCircleX_Left, wireCircleY_Starting + wireCircleY_Distance * (row - 1)),
                               wireCircleRadius)
            if mouseDown:
                return "left " + str(row)
            else:
                pygame.mouse.set_cursor(clickable_cursor)
                return "hover"
        else:
            pygame.draw.circle(screen, leftWireColors[row - 1],
                               (wireCircleX_Left, wireCircleY_Starting + wireCircleY_Distance * (row - 1)),
                               wireCircleRadius)
            return False
    else:
        border = pygame.draw.circle(screen,
                                    wireCircleBorderColor,
                                    (wireCircleX_Right, wireCircleY_Starting + wireCircleY_Distance * (row - 1)),
                                    wireCircleRadius + wireCircleBorderSize)
        if border.collidepoint(mouse_pos):
            pygame.draw.circle(screen, wireCircleHoverColor,
                               (wireCircleX_Right, wireCircleY_Starting + wireCircleY_Distance * (row - 1)),
                               wireCircleRadius)
            if mouseDown:
                return "right " + str(row)
            else:
                pygame.mouse.set_cursor(clickable_cursor)
                return "hover"
        else:
            pygame.draw.circle(screen, rightWireColors[row - 1],
                               (wireCircleX_Right, wireCircleY_Starting + wireCircleY_Distance * (row - 1)),
                               wireCircleRadius)
            return False


def draw_active_line(left_row, right_row):
    pygame.draw.line(screen, leftWireColors[left_row - 1], (wireCircleX_Left + wireCircleRadius + wireCircleBorderSize,
                                                            wireCircleY_Starting + wireCircleY_Distance * (
                                                                    left_row - 1)),
                     (wireCircleX_Right - wireCircleRadius - wireCircleBorderSize,
                      wireCircleY_Starting + wireCircleY_Distance * (right_row - 1)), width=10)


def draw_selected_line(side):
    if side == "left":
        pygame.draw.line(screen, leftWireColors[leftWireSelected - 1],
                         (wireCircleX_Left + wireCircleRadius + wireCircleBorderSize,
                          wireCircleY_Starting + wireCircleY_Distance * (leftWireSelected - 1)),
                         mousePos, width=10)
    else:
        pygame.draw.line(screen, rightWireColors[rightWireSelected - 1],
                         (wireCircleX_Right - wireCircleRadius - wireCircleBorderSize,
                          wireCircleY_Starting + wireCircleY_Distance * (rightWireSelected - 1)),
                         mousePos, width=10)


def draw_all_active_lines():
    for x in leftWiresActive:
        if x:
            draw_active_line(leftWiresActive.index(x) + 1, x)


def do_text(text_type, string, text_color, rect_color, choices=False,
            choice_rect_color=False, choice_text_color=False, max_width=False,
            font=text_font, rectangle_position=False, rectangle_dimensions=False, text_position=False, do_cursor=False):
    # if the position of rectangle is not stated, automatically set it to same pos as text
    if not rectangle_position and text_position:
        rectangle_position = text_position

    if text_type == 1:
        # decision, create a text prompt and multiple choices underneath
        if not rectangle_dimensions:
            text_image = font.render(string, True, text_color)
            if text_image.get_width() >= screenWidth:
                y = blit_multi_lined_text(string, text_color, text_font, (0, 0))
                rectangle_dimensions = (screenWidth, y)
            else:
                rectangle_dimensions = (text_image.get_width(), text_image.get_height())

        if not text_position and not rectangle_position:
            text_position = ((screenWidth / 2) - (rectangle_dimensions[0] / 2), 0)
            rectangle_position = text_position

        choice1_rect_position = (rectangle_position[0],
                                 (rectangle_position[1] + rectangle_dimensions[1] + 8))

        prompt_rect = pygame.Rect(rectangle_position[0], rectangle_position[1], rectangle_dimensions[0],
                                  rectangle_dimensions[1])

        choice1_text_image = text_font2.render(choices[0], True, choice_text_color)
        choice1_rect = pygame.Rect(choice1_rect_position[0], choice1_rect_position[1],
                                   max(choiceDimensions[0], choice1_text_image.get_width()),
                                   choiceDimensions[1])

        if len(choices) == 2:
            choice2_rect_position = rectangle_position[0] + (rectangle_dimensions[0] - choiceDimensions[0]), \
                                    (rectangle_position[1] + rectangle_dimensions[1] + 8)

            choice2_text_image = text_font2.render(choices[1], True, choice_text_color)
            choice2_rect = pygame.Rect(choice2_rect_position[0], choice2_rect_position[1],
                                       max(choiceDimensions[0], choice2_text_image.get_width()),
                                       choiceDimensions[1])

        pygame.draw.rect(screen, rect_color, prompt_rect)

        # mouse hover and mouse down on choices
        selected_choice = False

        if len(choices) == 1:
            if keyEnterDown:
                selected_choice = choices[0]
                beep_sound_file.play()

        if choice1_rect.collidepoint(mousePos):
            pygame.draw.rect(screen, (min(choice_rect_color[0] + 100, 255), min(choice_rect_color[1] + 100, 255),
                                      min(choice_rect_color[2] + 100, 255)), choice1_rect)
            pygame.mouse.set_cursor(clickable_cursor)

            if mouseDown:
                pygame.mouse.set_cursor(default_cursor)
                selected_choice = choices[0]
                beep_sound_file.play()
        else:
            pygame.draw.rect(screen, choice_rect_color, choice1_rect)
            if len(choices) == 1:
                pygame.mouse.set_cursor(default_cursor)

        if len(choices) == 2:
            if choice2_rect.collidepoint(mousePos):
                pygame.draw.rect(screen, (min(choice_rect_color[0] + 100, 255), min(choice_rect_color[1] + 100, 255),
                                          min(choice_rect_color[2] + 100, 255)), choice2_rect)
                pygame.mouse.set_cursor(clickable_cursor)

                if mouseDown:
                    pygame.mouse.set_cursor(default_cursor)
                    selected_choice = choices[1]
                    beep_sound_file.play()
            else:
                pygame.draw.rect(screen, choice_rect_color, choice2_rect)
                if not choice1_rect.collidepoint(mousePos):
                    # mouse not hovering on either buttons
                    pygame.mouse.set_cursor(default_cursor)

        # text blit
        blit_multi_lined_text(string, text_color, font, text_position)
        blit_multi_lined_text(choices[0], choice_text_color, text_font2, choice1_rect_position)
        if len(choices) == 2:
            blit_multi_lined_text(choices[1], choice_text_color, text_font2, choice2_rect_position)

        return selected_choice

    elif text_type == 2:
        # player input, do the check string length and stuff
        if not max_width and rectangle_dimensions:
            max_width = rectangle_dimensions[0]

        return_list = check_string_length(string, text_color, font, max_width)

        if not rectangle_dimensions:
            rectangle_dimensions = (return_list[0].get_width(), return_list[0].get_height())

        rect = pygame.Rect(rectangle_position[0], rectangle_position[1], rectangle_dimensions[0],
                           rectangle_dimensions[1])
        pygame.draw.rect(screen, rect_color, rect)

        screen.blit(return_list[0], text_position)

        if do_cursor:
            if rect.collidepoint(mousePos):
                pygame.mouse.set_cursor(ibeam_cursor)
            else:
                pygame.mouse.set_cursor(default_cursor)
        return return_list[1]

    elif text_type == 3:
        # text display, simple, display the text
        if not rectangle_dimensions:
            text_image = font.render(string, True, text_color)
            rectangle_dimensions = (text_image.get_width(), text_image.get_height())

        rect = pygame.Rect(rectangle_position[0], rectangle_position[1], rectangle_dimensions[0],
                           rectangle_dimensions[1])
        pygame.draw.rect(screen, rect_color, rect)

        blit_text(string, text_color, font, text_position)


serverColor = defaultServerColor

while running:
    # mouse
    mousePos = pygame.mouse.get_pos()
    # set background
    if not minigame:
        screen.fill(serverColor)
    else:
        if minigame == "Basketball":
            screen.fill((0, 0, 0))
        elif minigame == "Math":
            screen.fill((0, 0, 0))
        elif minigame == "Wire":
            screen.fill('darkgrey')

    # events
    for event in pygame.event.get():
        # if close tab, close tab
        if event.type == pygame.QUIT:
            running = False
            break
        if cutscene or playerController:
            if event.type == pygame.KEYDOWN:
                # if player presses jump key and has enough jumps, set jump velocity to jump force (12)
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w:
                    if playerJumps < playerMaxJumps:
                        playerJumpVelocity = playerJumpForce
                        playerJumps += 1
                        # wall jump
                        if playerX <= 0:
                            playerX += 50
                        elif playerX >= screenWidth - 64:
                            playerX -= 50
        if playerController and not minigame:  # code for when player has full movement control
            if event.type == pygame.KEYDOWN:
                # set player direction to the direction of the key (left is -1, right is 1)
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    playerDirection = -1
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    playerDirection = 1

                # if player presses down while wall jumping, make the player move down faster basically
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if playerX <= 0 or playerX >= screenWidth - 64:
                        wallDown = True

            elif event.type == pygame.KEYUP:
                # if player lets go of left or right, set direction to 0 (stationary)
                if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or
                        event.key == pygame.K_d):
                    playerDirection = 0

                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    wallDown = False

        if playerTyping:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text_string = text_string[0:-1]
                elif event.key == pygame.K_RETURN:
                    # used to filter out the else line below
                    pass
                else:
                    text_string += event.unicode
        else:
            text_string = ""

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                keyEnterDown = True

        if cutscene:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    laugh_sound_file.stop()
                    trash_talk_sound_file.stop()
                    tryouts_apology_sound_file.stop()
                    so_random_sound_file.stop()
                    basic_course_teaching_sound_file.stop()
                    basic_course_boring_sound_file.stop()
                    student_complaint_sound_file.stop()
                    pfft_sound_file.stop()
                    injustice_sound_file.stop()
                    worker_conversation_sound_file.stop()

                    cutsceneStage = 0
                    cutscene = False
                    cutsceneTransition = False
                    serverColor = defaultServerColor
                    textStage += 1

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 1 means left click
                mouseDown = True
                if minigame == "Basketball" and gameStarted:
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                holdableSpaceDown = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                holdableSpaceDown = False

    if cutscene:
        if cutscene == 1:
            if cutsceneStage == 0:
                cutsceneTransition = True
                if round(max(max(serverColor[0], serverColor[1]), serverColor[2])) <= 10:
                    serverColor = [0, 0, 0]
                    cutsceneServerColor = [250, 120, 35]
                    playerX = screenWidth / 2
                    playerY = screenHeight - playerY_offset
                    cutsceneStage += 1
                else:
                    if max(max(serverColor[0], serverColor[1]), serverColor[2]) > 100:
                        serverColor = [serverColor[0] * 0.9, serverColor[1] * 0.9, serverColor[2] * 0.9]
                    else:
                        serverColor = [serverColor[0] * 0.99, serverColor[1] * 0.99, serverColor[2] * 0.99]
            elif cutsceneStage == 1:
                if round(serverColor[0]) == round(cutsceneServerColor[0]) and round(serverColor[1]) == \
                        round(cutsceneServerColor[1]) and round(serverColor[2]) == round(cutsceneServerColor[2]):
                    serverColor = cutsceneServerColor
                    cutsceneStage += 1
                else:
                    serverColor[0] += cutsceneServerColor[0] * 0.01
                    serverColor[1] += cutsceneServerColor[1] * 0.01
                    serverColor[2] += cutsceneServerColor[2] * 0.01
            elif cutsceneStage == 2:
                playerDirection = 0
                cutsceneTransition = False
                expectedTime = time.time() + 0.5
                cutsceneStage += 1
            elif cutsceneStage == 3:
                if time.time() >= expectedTime:
                    playerDirection = 1
                    playerJumpVelocity = playerJumpForce
                    expectedTime = time.time() + 0.3
                    cutsceneStage += 1
                screen.blit(boyImg, ((screenWidth / 2) + 256, screenHeight - playerY_offset))
                screen.blit(boyImg, ((screenWidth / 2) + 192, screenHeight - playerY_offset))
            elif cutsceneStage == 4:
                if time.time() >= expectedTime:
                    playerDirection = 0
                    trash_talk_sound_file.play()
                    expectedTime = time.time() + 6
                    cutsceneStage += 1
                screen.blit(boyImg, ((screenWidth / 2) + 256, screenHeight - playerY_offset))
                screen.blit(boyImg, ((screenWidth / 2) + 192, screenHeight - playerY_offset))
            elif cutsceneStage == 5:
                if time.time() >= expectedTime:
                    laugh_sound_file.play()
                    expectedTime = time.time() + 7
                    cutsceneStage += 1
                screen.blit(boyImg, ((screenWidth / 2) + 256, screenHeight - playerY_offset))
                screen.blit(boyImg, ((screenWidth / 2) + 192, screenHeight - playerY_offset))
            elif cutsceneStage == 6:
                if time.time() >= expectedTime:
                    playerJumpVelocity = playerJumpForce
                    playerDirection = -1
                    expectedTime = time.time() + 1.4
                    cutsceneStage += 1
                screen.blit(boyImg, ((screenWidth / 2) + 256, screenHeight - playerY_offset))
                screen.blit(boyImg, ((screenWidth / 2) + 192, screenHeight - playerY_offset))
            elif cutsceneStage == 7:
                if time.time() >= expectedTime:
                    playerDirection = 0
                    expectedTime = time.time() + 0.6
                    cutsceneStage += 1
                screen.blit(boyImg, ((screenWidth / 2) + 256, screenHeight - playerY_offset))
                screen.blit(boyImg, ((screenWidth / 2) + 192, screenHeight - playerY_offset))
            elif cutsceneStage == 8:
                if time.time() >= expectedTime:
                    cutsceneTransition = True
                    if round(max(max(serverColor[0], serverColor[1]), serverColor[2])) <= 10:
                        serverColor = [0, 0, 0]
                        cutsceneStage += 1
                    else:
                        if max(max(serverColor[0], serverColor[1]), serverColor[2]) > 100:
                            serverColor = [serverColor[0] * 0.9, serverColor[1] * 0.9, serverColor[2] * 0.9]
                        else:
                            serverColor = [serverColor[0] * 0.99, serverColor[1] * 0.99, serverColor[2] * 0.99]
                else:
                    screen.blit(boyImg, ((screenWidth / 2) + 256, screenHeight - playerY_offset))
                    screen.blit(boyImg, ((screenWidth / 2) + 192, screenHeight - playerY_offset))
            elif cutsceneStage == 9:
                if round(serverColor[0]) == round(defaultServerColor[0]) and round(defaultServerColor[1]) == \
                        round(defaultServerColor[1]) and round(serverColor[2]) == round(defaultServerColor[2]):
                    serverColor = defaultServerColor
                    cutsceneStage += 1
                else:
                    serverColor[0] += defaultServerColor[0] * 0.01
                    serverColor[1] += defaultServerColor[1] * 0.01
                    serverColor[2] += defaultServerColor[2] * 0.01
            elif cutsceneStage == 10:
                cutsceneTransition = False
                cutsceneStage = 0
                cutscene = False
                textStage += 1
        elif cutscene == 2:
            if cutsceneStage == 0:
                cutsceneTransition = True
                if round(max(max(serverColor[0], serverColor[1]), serverColor[2])) <= 10:
                    serverColor = [0, 0, 0]
                    cutsceneServerColor = [250, 120, 35]
                    playerX = screenWidth / 2
                    playerY = screenHeight - playerY_offset
                    cutsceneStage += 1
                else:
                    if max(max(serverColor[0], serverColor[1]), serverColor[2]) > 100:
                        serverColor = [serverColor[0] * 0.9, serverColor[1] * 0.9, serverColor[2] * 0.9]
                    else:
                        serverColor = [serverColor[0] * 0.99, serverColor[1] * 0.99, serverColor[2] * 0.99]
            elif cutsceneStage == 1:
                if round(serverColor[0]) == round(cutsceneServerColor[0]) and round(serverColor[1]) == \
                        round(cutsceneServerColor[1]) and round(serverColor[2]) == round(cutsceneServerColor[2]):
                    serverColor = cutsceneServerColor
                    cutsceneStage += 1
                else:
                    serverColor[0] += cutsceneServerColor[0] * 0.01
                    serverColor[1] += cutsceneServerColor[1] * 0.01
                    serverColor[2] += cutsceneServerColor[2] * 0.01
            elif cutsceneStage == 2:
                playerDirection = 0
                cutsceneTransition = False
                expectedTime = time.time() + 0.5
                cutsceneStage += 1
            elif cutsceneStage == 3:
                if time.time() >= expectedTime:
                    playerDirection = 1
                    playerJumpVelocity = playerJumpForce
                    expectedTime = time.time() + 0.3
                    cutsceneStage += 1
                screen.blit(boyImg, ((screenWidth / 2) + 256, screenHeight - playerY_offset))
                screen.blit(boyImg, ((screenWidth / 2) + 192, screenHeight - playerY_offset))
            elif cutsceneStage == 4:
                if time.time() >= expectedTime:
                    playerDirection = 0
                    tryouts_apology_sound_file.play()
                    expectedTime = time.time() + 9
                    cutsceneStage += 1
                screen.blit(boyImg, ((screenWidth / 2) + 256, screenHeight - playerY_offset))
                screen.blit(boyImg, ((screenWidth / 2) + 192, screenHeight - playerY_offset))
            elif cutsceneStage == 5:
                if time.time() >= expectedTime:
                    playerDirection = 0
                    so_random_sound_file.play()
                    expectedTime = time.time() + 10
                    cutsceneStage += 1
                screen.blit(boyImg, ((screenWidth / 2) + 256, screenHeight - playerY_offset))
                screen.blit(boyImg, ((screenWidth / 2) + 192, screenHeight - playerY_offset))
            elif cutsceneStage == 6:
                if time.time() >= expectedTime:
                    cutsceneTransition = True
                    if round(max(max(serverColor[0], serverColor[1]), serverColor[2])) <= 10:
                        serverColor = [0, 0, 0]
                        cutsceneStage += 1
                    else:
                        if max(max(serverColor[0], serverColor[1]), serverColor[2]) > 100:
                            serverColor = [serverColor[0] * 0.9, serverColor[1] * 0.9, serverColor[2] * 0.9]
                        else:
                            serverColor = [serverColor[0] * 0.99, serverColor[1] * 0.99, serverColor[2] * 0.99]
                else:
                    screen.blit(boyImg, ((screenWidth / 2) + 256, screenHeight - playerY_offset))
                    screen.blit(boyImg, ((screenWidth / 2) + 192, screenHeight - playerY_offset))
            elif cutsceneStage == 7:
                if round(serverColor[0]) == round(defaultServerColor[0]) and round(defaultServerColor[1]) == \
                        round(defaultServerColor[1]) and round(serverColor[2]) == round(defaultServerColor[2]):
                    serverColor = defaultServerColor
                    cutsceneStage += 1
                else:
                    serverColor[0] += defaultServerColor[0] * 0.01
                    serverColor[1] += defaultServerColor[1] * 0.01
                    serverColor[2] += defaultServerColor[2] * 0.01
            elif cutsceneStage == 8:
                cutsceneTransition = False
                cutsceneStage = 0
                cutscene = False
                textStage += 1
        elif cutscene == 3:
            if cutsceneStage == 0:
                cutsceneTransition = True
                if round(max(max(serverColor[0], serverColor[1]), serverColor[2])) <= 10:
                    serverColor = [0, 0, 0]
                    cutsceneServerColor = [202, 164, 114]
                    playerX = screenWidth / 2
                    playerY = screenHeight - playerY_offset
                    cutsceneStage += 1
                else:
                    if max(max(serverColor[0], serverColor[1]), serverColor[2]) > 100:
                        serverColor = [serverColor[0] * 0.9, serverColor[1] * 0.9, serverColor[2] * 0.9]
                    else:
                        serverColor = [serverColor[0] * 0.99, serverColor[1] * 0.99, serverColor[2] * 0.99]
            elif cutsceneStage == 1:
                if round(serverColor[0]) == round(cutsceneServerColor[0]) and round(serverColor[1]) == \
                        round(cutsceneServerColor[1]) and round(serverColor[2]) == round(cutsceneServerColor[2]):
                    serverColor = cutsceneServerColor
                    cutsceneStage += 1
                else:
                    serverColor[0] += cutsceneServerColor[0] * 0.01
                    serverColor[1] += cutsceneServerColor[1] * 0.01
                    serverColor[2] += cutsceneServerColor[2] * 0.01
            elif cutsceneStage == 2:
                student_complaint_sound_file.play()
                playerDirection = 0
                cutsceneTransition = False
                expectedTime = time.time() + 6
                cutsceneStage += 1
            elif cutsceneStage == 3:
                if time.time() >= expectedTime:
                    playerJumpVelocity = playerJumpForce
                    expectedTime = time.time() + 0.6
                    cutsceneStage += 1
                screen.blit(advancedTeacherImg, ((screenWidth / 2) + 256, screenHeight - playerY_offset + 16))
                screen.blit(boyImg, ((screenWidth / 2) - 128, screenHeight - playerY_offset + 16))
                screen.blit(boyImg, ((screenWidth / 2) - 192, screenHeight - playerY_offset + 16))
                screen.blit(boyImg, ((screenWidth / 2) + 64, screenHeight - playerY_offset + 16))
            elif cutsceneStage == 4:
                if time.time() >= expectedTime:
                    playerJumpVelocity = playerJumpForce
                    expectedTime = time.time() + 0.2
                    cutsceneStage += 1
                screen.blit(advancedTeacherImg, ((screenWidth / 2) + 256, screenHeight - playerY_offset + 16))
                screen.blit(boyImg, ((screenWidth / 2) - 128, screenHeight - playerY_offset + 16))
                screen.blit(boyImg, ((screenWidth / 2) - 192, screenHeight - playerY_offset + 16))
                screen.blit(boyImg, ((screenWidth / 2) + 64, screenHeight - playerY_offset + 16))
            elif cutsceneStage == 5:
                if time.time() >= expectedTime:
                    playerJumpVelocity = playerJumpForce
                    expectedTime = time.time() + 6
                    cutsceneStage += 1
                screen.blit(advancedTeacherImg, ((screenWidth / 2) + 256, screenHeight - playerY_offset + 16))
                screen.blit(boyImg, ((screenWidth / 2) - 128, screenHeight - playerY_offset + 16))
                screen.blit(boyImg, ((screenWidth / 2) - 192, screenHeight - playerY_offset + 16))
                screen.blit(boyImg, ((screenWidth / 2) + 64, screenHeight - playerY_offset + 16))
            elif cutsceneStage == 6:
                if time.time() >= expectedTime:
                    # say smth idk
                    cutsceneStage += 1
                screen.blit(advancedTeacherImg, ((screenWidth / 2) + 256, screenHeight - playerY_offset + 16))
                screen.blit(boyImg, ((screenWidth / 2) - 128, screenHeight - playerY_offset + 16))
                screen.blit(boyImg, ((screenWidth / 2) - 192, screenHeight - playerY_offset + 16))
                screen.blit(boyImg, ((screenWidth / 2) + 64, screenHeight - playerY_offset + 16))
            elif cutsceneStage == 7:
                if time.time() >= expectedTime:
                    cutsceneTransition = True
                    if round(max(max(serverColor[0], serverColor[1]), serverColor[2])) <= 10:
                        serverColor = [0, 0, 0]
                        cutsceneStage += 1
                    else:
                        if max(max(serverColor[0], serverColor[1]), serverColor[2]) > 100:
                            serverColor = [serverColor[0] * 0.9, serverColor[1] * 0.9, serverColor[2] * 0.9]
                        else:
                            serverColor = [serverColor[0] * 0.99, serverColor[1] * 0.99, serverColor[2] * 0.99]
                else:
                    screen.blit(advancedTeacherImg, ((screenWidth / 2) + 256, screenHeight - playerY_offset + 16))
                    screen.blit(boyImg, ((screenWidth / 2) - 128, screenHeight - playerY_offset + 16))
                    screen.blit(boyImg, ((screenWidth / 2) - 192, screenHeight - playerY_offset + 16))
                    screen.blit(boyImg, ((screenWidth / 2) + 64, screenHeight - playerY_offset + 16))
            elif cutsceneStage == 8:
                if round(serverColor[0]) == round(defaultServerColor[0]) and round(defaultServerColor[1]) == \
                        round(defaultServerColor[1]) and round(serverColor[2]) == round(defaultServerColor[2]):
                    serverColor = defaultServerColor
                    cutsceneStage += 1
                else:
                    serverColor[0] += defaultServerColor[0] * 0.01
                    serverColor[1] += defaultServerColor[1] * 0.01
                    serverColor[2] += defaultServerColor[2] * 0.01
            elif cutsceneStage == 9:
                cutsceneTransition = False
                cutsceneStage = 0
                cutscene = False
                textStage += 1

        elif cutscene == 4:
            if cutsceneStage == 0:
                cutsceneTransition = True
                if round(max(max(serverColor[0], serverColor[1]), serverColor[2])) <= 10:
                    serverColor = [0, 0, 0]
                    cutsceneServerColor = [202, 164, 114]
                    playerX = screenWidth / 2
                    playerY = screenHeight - playerY_offset
                    cutsceneStage += 1
                else:
                    if max(max(serverColor[0], serverColor[1]), serverColor[2]) > 100:
                        serverColor = [serverColor[0] * 0.9, serverColor[1] * 0.9, serverColor[2] * 0.9]
                    else:
                        serverColor = [serverColor[0] * 0.99, serverColor[1] * 0.99, serverColor[2] * 0.99]
            elif cutsceneStage == 1:
                if round(serverColor[0]) == round(cutsceneServerColor[0]) and round(serverColor[1]) == \
                        round(cutsceneServerColor[1]) and round(serverColor[2]) == round(cutsceneServerColor[2]):
                    serverColor = cutsceneServerColor
                    cutsceneStage += 1
                else:
                    serverColor[0] += cutsceneServerColor[0] * 0.01
                    serverColor[1] += cutsceneServerColor[1] * 0.01
                    serverColor[2] += cutsceneServerColor[2] * 0.01
            elif cutsceneStage == 2:
                basic_course_teaching_sound_file.play()
                playerDirection = 0
                cutsceneTransition = False
                expectedTime = time.time() + 11
                cutsceneStage += 1
            elif cutsceneStage == 3:
                if time.time() >= expectedTime:
                    playerJumpVelocity = playerJumpForce
                    basic_course_boring_sound_file.play()
                    expectedTime = time.time() + 6
                    cutsceneStage += 1
                screen.blit(boyImg, ((screenWidth / 2) - 128, screenHeight - playerY_offset + 16))
                screen.blit(basicTeacherImg, ((screenWidth / 2) + 128, screenHeight - playerY_offset))
            elif cutsceneStage == 4:
                if time.time() >= expectedTime:
                    cutsceneTransition = True
                    if round(max(max(serverColor[0], serverColor[1]), serverColor[2])) <= 10:
                        serverColor = [0, 0, 0]
                        cutsceneStage += 1
                    else:
                        if max(max(serverColor[0], serverColor[1]), serverColor[2]) > 100:
                            serverColor = [serverColor[0] * 0.9, serverColor[1] * 0.9, serverColor[2] * 0.9]
                        else:
                            serverColor = [serverColor[0] * 0.99, serverColor[1] * 0.99, serverColor[2] * 0.99]
                else:
                    screen.blit(boyImg, ((screenWidth / 2) - 128, screenHeight - playerY_offset + 16))
                    screen.blit(basicTeacherImg, ((screenWidth / 2) + 128, screenHeight - playerY_offset))
            elif cutsceneStage == 5:
                if round(serverColor[0]) == round(defaultServerColor[0]) and round(defaultServerColor[1]) == \
                        round(defaultServerColor[1]) and round(serverColor[2]) == round(defaultServerColor[2]):
                    serverColor = defaultServerColor
                    cutsceneStage += 1
                else:
                    serverColor[0] += defaultServerColor[0] * 0.01
                    serverColor[1] += defaultServerColor[1] * 0.01
                    serverColor[2] += defaultServerColor[2] * 0.01
            elif cutsceneStage == 6:
                cutsceneTransition = False
                cutsceneStage = 0
                cutscene = False
                textStage += 1

        elif cutscene == 5:
            if cutsceneStage == 0:
                cutsceneTransition = True
                if round(max(max(serverColor[0], serverColor[1]), serverColor[2])) <= 10:
                    serverColor = [0, 0, 0]
                    cutsceneServerColor = [47, 53, 42]
                    playerX = screenWidth / 2
                    playerY = screenHeight - playerY_offset
                    cutsceneStage += 1
                else:
                    if max(max(serverColor[0], serverColor[1]), serverColor[2]) > 100:
                        serverColor = [serverColor[0] * 0.9, serverColor[1] * 0.9, serverColor[2] * 0.9]
                    else:
                        serverColor = [serverColor[0] * 0.99, serverColor[1] * 0.99, serverColor[2] * 0.99]
            elif cutsceneStage == 1:
                if round(serverColor[0]) == round(cutsceneServerColor[0]) and round(serverColor[1]) == \
                        round(cutsceneServerColor[1]) and round(serverColor[2]) == round(cutsceneServerColor[2]):
                    serverColor = cutsceneServerColor
                    cutsceneStage += 1
                else:
                    serverColor[0] += cutsceneServerColor[0] * 0.01
                    serverColor[1] += cutsceneServerColor[1] * 0.01
                    serverColor[2] += cutsceneServerColor[2] * 0.01
            elif cutsceneStage == 2:
                pfft_sound_file.play()
                cutsceneTransition = False
                expectedTime = time.time() + 6
                cutsceneStage += 1
            elif cutsceneStage == 3:
                if time.time() >= expectedTime:
                    injustice_sound_file.play()
                    playerJumpVelocity = playerJumpForce
                    expectedTime = time.time() + 0.4
                    cutsceneStage += 1
                screen.blit(husbandImg, ((screenWidth / 2) + 192, screenHeight - playerY_offset))
            elif cutsceneStage == 4:
                if time.time() >= expectedTime:
                    playerJumpVelocity = playerJumpForce
                    expectedTime = time.time() + 7
                    cutsceneStage += 1
                screen.blit(husbandImg, ((screenWidth / 2) + 192, screenHeight - playerY_offset))
            elif cutsceneStage == 5:
                if time.time() >= expectedTime:
                    cutsceneTransition = True
                    if round(max(max(serverColor[0], serverColor[1]), serverColor[2])) <= 10:
                        serverColor = [0, 0, 0]
                        cutsceneStage += 1
                    else:
                        if max(max(serverColor[0], serverColor[1]), serverColor[2]) > 100:
                            serverColor = [serverColor[0] * 0.9, serverColor[1] * 0.9, serverColor[2] * 0.9]
                        else:
                            serverColor = [serverColor[0] * 0.99, serverColor[1] * 0.99, serverColor[2] * 0.99]
                else:
                    screen.blit(husbandImg, ((screenWidth / 2) + 192, screenHeight - playerY_offset))
            elif cutsceneStage == 6:
                if round(serverColor[0]) == round(defaultServerColor[0]) and round(defaultServerColor[1]) == \
                        round(defaultServerColor[1]) and round(serverColor[2]) == round(defaultServerColor[2]):
                    serverColor = defaultServerColor
                    cutsceneStage += 1
                else:
                    serverColor[0] += defaultServerColor[0] * 0.01
                    serverColor[1] += defaultServerColor[1] * 0.01
                    serverColor[2] += defaultServerColor[2] * 0.01
            elif cutsceneStage == 7:
                cutsceneTransition = False
                cutsceneStage = 0
                cutscene = False
                textStage += 1

        elif cutscene == 6:
            if cutsceneStage == 0:
                cutsceneTransition = True
                if round(max(max(serverColor[0], serverColor[1]), serverColor[2])) <= 10:
                    serverColor = [0, 0, 0]
                    cutsceneServerColor = [133, 94, 66]
                    playerX = screenWidth / 2
                    playerY = screenHeight - playerY_offset
                    cutsceneStage += 1
                else:
                    if max(max(serverColor[0], serverColor[1]), serverColor[2]) > 100:
                        serverColor = [serverColor[0] * 0.9, serverColor[1] * 0.9, serverColor[2] * 0.9]
                    else:
                        serverColor = [serverColor[0] * 0.99, serverColor[1] * 0.99, serverColor[2] * 0.99]
            elif cutsceneStage == 1:
                if round(serverColor[0]) == round(cutsceneServerColor[0]) and round(serverColor[1]) == \
                        round(cutsceneServerColor[1]) and round(serverColor[2]) == round(cutsceneServerColor[2]):
                    serverColor = cutsceneServerColor
                    cutsceneStage += 1
                else:
                    serverColor[0] += cutsceneServerColor[0] * 0.01
                    serverColor[1] += cutsceneServerColor[1] * 0.01
                    serverColor[2] += cutsceneServerColor[2] * 0.01
            elif cutsceneStage == 2:
                worker_conversation_sound_file.play()
                cutsceneTransition = False
                expectedTime = time.time() + 57
                cutsceneStage += 1
            elif cutsceneStage == 3:
                if time.time() >= expectedTime:
                    cutsceneTransition = True
                    if round(max(max(serverColor[0], serverColor[1]), serverColor[2])) <= 10:
                        serverColor = [0, 0, 0]
                        cutsceneStage += 1
                    else:
                        if max(max(serverColor[0], serverColor[1]), serverColor[2]) > 100:
                            serverColor = [serverColor[0] * 0.9, serverColor[1] * 0.9, serverColor[2] * 0.9]
                        else:
                            serverColor = [serverColor[0] * 0.99, serverColor[1] * 0.99, serverColor[2] * 0.99]
                else:
                    screen.blit(workerImg, ((screenWidth / 2) + 96, screenHeight - playerY_offset))
                    screen.blit(boyImg, ((screenWidth / 2) - 96, screenHeight - playerY_offset + 16))
                    screen.blit(boyImg, ((screenWidth / 2) - 192, screenHeight - playerY_offset + 16))
                    screen.blit(boyImg, ((screenWidth / 2) - 288, screenHeight - playerY_offset + 16))
                    screen.blit(boyImg, ((screenWidth / 2) - 384, screenHeight - playerY_offset + 16))
            elif cutsceneStage == 4:
                if round(serverColor[0]) == round(defaultServerColor[0]) and round(defaultServerColor[1]) == \
                        round(defaultServerColor[1]) and round(serverColor[2]) == round(defaultServerColor[2]):
                    serverColor = defaultServerColor
                    cutsceneStage += 1
                else:
                    serverColor[0] += defaultServerColor[0] * 0.01
                    serverColor[1] += defaultServerColor[1] * 0.01
                    serverColor[2] += defaultServerColor[2] * 0.01
            elif cutsceneStage == 5:
                cutsceneTransition = False
                cutsceneStage = 0
                cutscene = False
                textStage += 1

        if not cutsceneTransition:
            spaceToSkipImg.set_alpha((time.time() * 100) % 255)
            screen.blit(spaceToSkipImg, ((screenWidth / 2) - 128, 64))

    # if the player will not walk out of the screen, move the playerX towards its direction
    if (playerController and not minigame) or (cutscene and not cutsceneTransition):
        if not (playerX >= screenWidth - 64 and playerDirection == 1) and not (playerX <= 0
                                                                               and playerDirection == -1):
            playerX += playerDirection * playerSpeed
            playerGravity = 1.8
        elif playerX >= screenWidth - 64:
            if playerController:
                playerX = screenWidth - 64
                # allows wall jump on right side
                playerJumps = 1
                if wallDown:
                    playerGravity = 3.0
                else:
                    playerGravity = 0.4
            else:
                if not textActive:
                    playerX = 16
                    serverColor = [random.randint(1, 225), random.randint(1, 225), random.randint(1, 225)]
        elif playerX <= 0:
            if playerController:
                # allows wall jump on left side
                playerJumps = 1
                if wallDown:
                    playerGravity = 3.0
                else:
                    playerGravity = 0.4

        # doesn't let player go above the ceiling
        if playerY <= 0:
            playerY = 0

        # just sets player pos to the player Y and X and blits it
        player(playerX, playerY, playerDirection)

        # subtract playerY by jump velocity (will be 12 on the iteration the player presses jump)
        # (subtracting Y = move upwards)
        playerY -= playerJumpVelocity

        # if the player is not grounded, move the player down by gravity
        # the part you add after gravity is just to make the player move down faster if the player is falling
        # so falling from a wall jump isn't like a parachute
        # if the player is grounded, makes sure that the player is on the exact height on ground and sets
        # player jumps to 0
        if playerY < screenHeight - playerY_offset:
            playerY += playerGravity
            if playerFallingDown:
                playerY += 2 * playerGravity
        else:
            playerY = screenHeight - playerY_offset
            playerJumpVelocity = 0
            playerJumps = 0

        if playerJumpVelocity > 0:
            playerJumpVelocity -= playerGravity
            playerFallingDown = False
        else:
            if playerY < screenHeight - playerY_offset:
                playerFallingDown = True
            else:
                playerFallingDown = False
    elif minigame:
        if minigame == "Basketball":
            # aims the ball and draws dots code
            if basketballY + basketballDY + 96 >= screenHeight and \
                    basketballX == basketballStartingX and basketballRound > 0 and not \
                    basketballMinigameRoundWinner:
                if holdableMouseDown:
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
                else:
                    if playerBasketballMisses + playerBuckets == 0 and basketball_Y_velocity == 0:
                        screen.blit(holdClickToShootImg, (basketballStartingX + 32, basketballStartingY - 128))

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
                    basketball_score_sound_file.play()
                else:
                    playerBasketballMisses += 1
                playerBasketballAccuracy = round((playerBuckets / (playerBuckets + playerBasketballMisses)) * 100)

                vertex_a_value = ((screenHeight - basketballStartingX) - (screenHeight - vertex[1])) / \
                                 (basketballStartingX - vertex[0]) ** 2
                vertexForm = "y = " + str(round(vertex_a_value * 100000) / 100000) + "(x - " + \
                             str(vertex[0]) + ")^2 + " + \
                             str(round((screenHeight - vertex[1]) * 1000) / 1000)

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
                        blit_text("FOR MATHEMATICIANS", (255, 255, 255), basketballMinigameStatsForNerdsFont,
                                  (basketballMinigameStatsForNerdsDisplayPosition[0] + 8,
                                   basketballMinigameStatsForNerdsDisplayPosition[1] + 8))
                    else:
                        pygame.draw.rect(screen, (255, 255, 255), StatsForNerdsButton)
                        blit_text("Quadratic Function of Ball", (0, 0, 0), basketballMinigameStatsForNerdsFont,
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
                        whistle_sound_file.play()
                    else:
                        blit_text("First to make " + str(basketsRequired) + " buckets WINS", (255, 0, 255),
                                  basketballMinigameLargeFont,
                                  (0, ((1 / 6) * (basketballMinigameLargeTextY_Iteration ** 3 -
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
                            if playerWins > opponentWins:
                                playerBalance += 300
                            minigame = False
                        else:
                            whistle_sound_file.play()
                            basketballRound += 1
                            hoopPosition[1] = 192
                    else:
                        blit_text(str(playerWins) + " : " + str(opponentWins), (255, 255, 0),
                                  basketballMinigameLargeFont,
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
        elif minigame == "Math":
            if Course and not answerDisplayTimeStart and mathQuestion:
                playerTyping = True
                if keyEnterDown:
                    if Course == "Basic":
                        # first checks there is a correct answer (only basic q3 has no 'right' answer)
                        if not basicAnswers[mathQuestion - 1]:
                            # no correct answer
                            answerCorrect = True
                        else:
                            if text_string.lower() in basicAnswers[mathQuestion - 1]:
                                answerCorrect = True
                            else:
                                # wrong answer
                                answerCorrect = False

                        answerDisplayTimeStart = time.time()

                    elif Course == "Advanced":
                        # this doesn't need to check if there is correct answer as they all have 'right' answers
                        if text_string.lower() in advancedAnswers[mathQuestion - 1]:
                            # if player got correct answer
                            advancedCorrectAnswerCount += 1
                            answerCorrect = True

                        else:
                            # if player got wrong answer
                            answerCorrect = False

                        answerDisplayTimeStart = time.time()
                if mathMinigameTextRectangle.collidepoint(mousePos):
                    pygame.mouse.set_cursor(ibeam_cursor)
                else:
                    pygame.mouse.set_cursor(default_cursor)
            else:
                playerTyping = False

            if text_string != "":
                ShowTTT = False

            if Course == "Basic":
                if mathQuestion:
                    # if player is answering math question then blit the current question
                    screen.blit(basicQuestions[mathQuestion - 1], ((screenWidth - questionSize[0]) / 2,
                                                                   (screenHeight - questionSize[1]) / 2))
                    # check
                    returnList = check_string_length(text_string, 'black', mathMinigameFont, questionBoxWidth)
                    text_string = returnList[1]

                    # blit player answer input
                    if ShowTTT:
                        screen.blit(TTT_IMG, (answerInputPosition[0], answerInputPosition[1]))
                    else:
                        screen.blit(returnList[0], (answerInputPosition[0], answerInputPosition[1]))

                else:
                    # if player is not currently answering a math question, then blit the cover instead of the question
                    screen.blit(basicCourseCover, ((screenWidth - coverSize[0]) / 2, - coverY))

            elif Course == "Advanced":
                if mathQuestion:
                    # if player is answering math question then blit the current question
                    screen.blit(advancedQuestions[mathQuestion - 1], ((screenWidth - questionSize[0]) / 2,
                                                                      (screenHeight - questionSize[1]) / 2))

                    # check
                    returnList = check_string_length(text_string, 'black', mathMinigameFont, questionBoxWidth)
                    text_string = returnList[1]

                    # blit player answer input
                    if ShowTTT:
                        screen.blit(TTT_IMG, (answerInputPosition[0], answerInputPosition[1]))
                    else:
                        screen.blit(returnList[0], (answerInputPosition[0], answerInputPosition[1]))
                else:
                    # if player is not currently answering a math question, then blit the cover instead of the question
                    screen.blit(advancedCourseCover, ((screenWidth - coverSize[0]) / 2, - coverY))

            if coverY < maximumCoverY:
                if holdableSpaceDown:
                    coverY = round((coverY + (scrollSpeed * 10)) * 10) / 10
                else:
                    coverY = round((coverY + scrollSpeed) * 10) / 10
                if coverY >= maximumCoverY:
                    mathQuestion = 1
                    ShowTTT = True
                else:
                    spaceToQuickScrollImg.set_alpha((time.time() * 100) % 255)
                    screen.blit(spaceToQuickScrollImg, ((screenWidth / 2) - 192, 256))

            if answerDisplayTimeStart:
                if time.time() >= answerDisplayTimeStart + answerDisplayDelay:
                    if Course == "Advanced":
                        if mathQuestion == 3:
                            if advancedCorrectAnswerCount > 0:
                                advancedWin = True
                            else:
                                advancedWin = False
                            advancedCorrectAnswerCount = 0
                            minigame = False
                            mathQuestion = False
                            Course = False
                            coverY = 0
                            pygame.mouse.set_cursor(default_cursor)
                        else:
                            mathQuestion += 1
                            ShowTTT = True

                    elif Course == "Basic":
                        mathQuestion += 1
                        ShowTTT = True

                    text_string = ""
                    answerDisplayTimeStart = False
                else:
                    if Course == "Advanced":
                        if answerCorrect:
                            blit_text(("CORRECT! CORRECT ANSWERS: " + str(advancedCorrectAnswerCount)), 'green',
                                      mathMinigameFont, answerDisplayPosition)
                        else:
                            blit_text(("WRONG - ANSWER: " + advancedAnswers[mathQuestion - 1][0]), 'red',
                                      mathMinigameFont, answerDisplayPosition)
                    elif Course == "Basic":
                        if answerCorrect:
                            basicWin = True
                            minigame = False
                            mathQuestion = False
                            Course = False
                            coverY = 0
                            pygame.mouse.set_cursor(default_cursor)

                            text_string = ""
                            answerDisplayTimeStart = False
                        else:
                            blit_text(("WRONG - ANSWER: " + basicAnswers[mathQuestion - 1][0]), 'red',
                                      mathMinigameFont, answerDisplayPosition)
        elif minigame == "Wire":
            # draw wire circles
            returnValues = []
            for i in range(wireCount):
                returnValues.append(draw_wire_circle("left", i + 1, mousePos))
                returnValues.append(draw_wire_circle("right", i + 1, mousePos))
            if "hover" not in returnValues:
                # if no wires are being clicked
                pygame.mouse.set_cursor(default_cursor)
            for i in returnValues:
                if i and i.find("hover") == -1:
                    wireRow = int(i.split()[1])
                    if not leftWireSelected and not rightWireSelected:
                        if i.find("left") != -1:
                            if leftWiresActive[wireRow - 1]:  # if wire clicked is already active do nothing
                                pass
                            else:  # if wire clicked is not already active and no other wires are selected,
                                # then select wire
                                leftWireSelected = wireRow

                        elif i.find("right") != -1:
                            if rightWiresActive[wireRow - 1]:  # if wire clicked is already active do nothing
                                pass
                            else:  # if wire clicked is not already active and no other wires are selected,
                                # then select wire
                                rightWireSelected = wireRow

                    else:  # is wire selected opposite side of wire touching mouse
                        if i.find("left") != -1:
                            if rightWireSelected:  # wire selected is opposite side of wire touching mouse
                                if leftWiresActive[wireRow - 1]:  # if wire clicked is already occupied
                                    pass
                                else:
                                    # are wire colors correctly matched up
                                    if leftWireColors[wireRow - 1] == rightWireColors[rightWireSelected - 1]:
                                        leftWireSelected = wireRow
                                        rightWireSelected = rightWireSelected
                                    else:  # lose a life if incorrectly matched up
                                        wireLives -= 1
                                        rightWireSelected = False
                                        if wireLives == 0:
                                            wireMinigameWin = False
                                            minigame = False

                            else:  # wire selected is same side of wire touching mouse
                                if wireRow == leftWireSelected:  # when wire circle receives/clicks itself
                                    leftWireSelected = False
                                else:
                                    if leftWiresActive[wireRow - 1]:  # is same side wire already active?
                                        pass
                                    else:
                                        leftWireSelected = wireRow  # when wire circle receives from same side

                        elif i.find("right") != -1:
                            if leftWireSelected:  # wire selected is opposite side of wire touching mouse
                                if rightWiresActive[wireRow - 1]:  # if wire clicked is already occupied
                                    pass
                                else:
                                    # are wire colors correctly matched up
                                    if leftWireColors[leftWireSelected - 1] == rightWireColors[wireRow - 1]:
                                        rightWireSelected = wireRow
                                        leftWireSelected = leftWireSelected
                                    else:  # lose a life if incorrectly matched up
                                        wireLives -= 1
                                        leftWireSelected = False
                                        if wireLives == 0:
                                            wireMinigameWin = False
                                            minigame = False

                            else:  # wire selected is same side of wire touching mouse
                                if wireRow == rightWireSelected:  # when wire circle receives/clicks itself
                                    rightWireSelected = False
                                else:
                                    if rightWiresActive[wireRow - 1]:  # is same side wire already active?
                                        pass
                                    else:
                                        rightWireSelected = wireRow  # when wire circle receives from same side

            # draw lines and convert selected lines into active lines
            if leftWireSelected or rightWireSelected:
                if leftWireSelected and rightWireSelected:
                    wire_connect_sound_file.play()
                    leftWiresActive[leftWireSelected - 1] = rightWireSelected
                    rightWiresActive[rightWireSelected - 1] = leftWireSelected

                    leftWireSelected = False
                    rightWireSelected = False

                    if leftWiresActive.count(False) == 0:
                        wireMinigameWin = True
                        minigame = False
                else:
                    if leftWireSelected:
                        draw_selected_line("left")
                    elif rightWireSelected:
                        draw_selected_line("right")

            draw_all_active_lines()

    # if game didn't start and not in age confirm or description page, then draw menu
    if not gameStarted and not ageConfirmation and not gameDescription and not minigame:
        menuReturn = draw_menu()
        if menuReturn == 1:
            ShowTTT = True
            ageConfirmation = True
            playerTyping = True
        elif menuReturn == 2:
            gameDescription = True

    if not minigame:
        if ageConfirmation:
            age_confirmation_data = draw_age_confirmation()
            text_string = age_confirmation_data[0]
            if text_string:
                ShowTTT = False
            if age_confirmation_data[1]:
                age = int(text_string)
                beep_sound_file.play()
                playerTyping = False
            elif age:
                if age == 69 or age == 420 or age == 69420:
                    if not selectedChoice:
                        selectedChoice = draw_default_continue("Baka. What have you done.")
                    else:
                        running = False
                        break
                elif age < 12:
                    if not selectedChoice:
                        selectedChoice = draw_default_continue("Sorry, you are too young for the game")
                    else:
                        running = False
                        break
                elif 18 >= age >= 12:
                    if not selectedChoice:
                        selectedChoice = draw_default_continue("This game is perfect for you, please enjoy.")
                    else:
                        selectedChoice = False
                        ageConfirmation = False
                        gameStarted = True
                elif age > 18:
                    if not selectedChoice:
                        selectedChoice = draw_default_continue("The game may be more entertaining for a younger "
                                                               "audience, however you may proceed if you wish",
                                                               choice="PROCEED")
                    else:
                        selectedChoice = False
                        ageConfirmation = False
                        gameStarted = True
        elif gameDescription:
            if draw_description():
                gameDescription = False

    if gameStarted:
        draw_balance()
        if scenario == 1:
            # PRESENT DAY SCENARIO
            if textStage == 0:
                if selectedChoice:
                    if selectedChoice == "Join":
                        textStage += 1
                        selectedChoice = False
                        playerBalance -= 100
                    else:
                        textStage = 9
                        selectedChoice = False
                else:
                    selectedChoice = draw_default_decision('''You are living the life of a 13 year old girl in middle 
                    school. You love playing basketball, and considers joining the boy-girl basketball school team, 
                    despite the team not having any girls.''', ["Join", "Don't Join"])
            elif textStage == 1:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue('''The tryout costs $100, but you heard that you receive 
                    $300 for making the school team.''')
            elif textStage == 2:
                if selectedChoice:
                    cutscene = 1
                    selectedChoice = False

                    if cutscene not in cutscenesUnlocked:
                        cutscenesUnlocked.append(cutscene)
                else:
                    if not cutscene:
                        selectedChoice = draw_default_continue('''On the day of the tryout, you get nervous as you are 
                    the only girl trying out for the basketball school team. Boys all around seem to be looking at 
                    you like you don't belong. As you walk into the gym where the tryout takes place, you hear a 
                    boy whispering, 'Hey look, there's a girl trying out! I bet I can beat her 10 nil with only my 
                    left hand!' You can't stand it, and you are motivated to prove them wrong.''')
                    else:
                        pass
            elif textStage == 3:
                if selectedChoice:
                    textStage += 1

                    # basketball minigame setup
                    playerWins = 0
                    opponentWins = 0
                    basketballRound = 0
                    basketballMinigameLargeTextY_Iteration = -10
                    hoopPosition = [screenWidth - 64, 192]

                    minigame = "Basketball"
                    selectedChoice = False

                    if "Basketball" not in minigamesUnlocked:
                        minigamesUnlocked.append("Basketball")
                else:
                    selectedChoice = draw_default_continue('''You get your opportunity when you are told to compete in
                    speed shooting''', choice="START", choice_rectangle_color=[0, 180, 0])
            elif textStage == 4 and not minigame:
                if playerWins > opponentWins:
                    if selectedChoice:
                        textStage += 1
                        selectedChoice = False
                    else:
                        selectedChoice = draw_default_continue('''You become a respected member of the basketball school 
                        team, and make new friends.''')
                else:
                    if selectedChoice:
                        textStage = 8
                        selectedChoice = False
                    else:
                        selectedChoice = draw_default_continue('''You didn't make it into the team.''')
            elif textStage == 5:
                if selectedChoice:
                    cutscene = 2
                    selectedChoice = False

                    if cutscene not in cutscenesUnlocked:
                        cutscenesUnlocked.append(cutscene)
                else:
                    if not cutscene:
                        selectedChoice = draw_default_continue('''The boys in the team come to respect you and you 
                        forgive them for being rude.''')
                    else:
                        # code during cutscene (probably going to stay blank)
                        pass
            elif textStage == 6:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue('''You are a symbol of hope and inspiration for girls in your 
                    school, showing them that female students can be just as capable as male students.''')
            elif textStage == 7:
                if draw_present_day_end():
                    centralizeBalance = False
                    textStage = 0
                    scenario = 2
                    selectedChoice = False
                else:
                    centralizeBalance = True

            elif textStage == 8:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue(''' You are upset that you weren't able to prove yourself, 
                    but you tell yourself that at least you tried.''')
            elif textStage == 9:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("A few days pass. When you are at home, you like to keep "
                                                           "yourself busy by doing revision on maths, "
                                                           "the subject you love most.")
            elif textStage == 10:
                if selectedChoice:
                    if selectedChoice == "Basic":
                        textStage += 1
                        selectedChoice = False
                    else:
                        textStage = 16
                        selectedChoice = False
                else:
                    selectedChoice = draw_default_decision("When school starts, you are allowed to select the math "
                                                           "course you take. Which do you chose?",
                                                           ["Basic", "Advanced"])
            elif textStage == 11:
                if selectedChoice:
                    cutscene = 4
                    selectedChoice = False

                    if cutscene not in cutscenesUnlocked:
                        cutscenesUnlocked.append(cutscene)
                else:
                    if not cutscene:
                        selectedChoice = draw_default_continue("The teacher teaches very slowly, "
                                                               "and you find the class way too easy.")
            elif textStage == 12:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("You also notice that the majority of the class are girls, "
                                                           "with only 6 boys in the class of 30 students.")
            elif textStage == 13:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                    minigame = "Math"
                    Course = "Basic"

                    if "Math" not in minigamesUnlocked:
                        minigamesUnlocked.append("Math")
                else:
                    selectedChoice = draw_default_continue("When the assessment comes, you are completely prepared and "
                                                           "ready to prove to "
                                                           "your teacher that you understood everything he taught.",
                                                           choice="START",
                                                           choice_rectangle_color=[0, 180, 0])
            elif textStage == 14 and not minigame:
                if basicWin:
                    if selectedChoice:
                        textStage += 1
                        selectedChoice = False
                        playerBalance += 800
                    else:
                        selectedChoice = draw_default_continue("Your teacher is mindblown by your scores, and "
                                                               "immediately promotes you to the advanced math class.")
                else:
                    # you can't lose in basic course.
                    pass
            elif textStage == 15:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("You receive a math improvement scholarship for "
                                                           "your hard work and effort. $$$")
            elif textStage == 16:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("The next day, you are ready and excited to be"
                                                           " in the advanced class", choice="ENTER ROOM",
                                                           choice_rectangle_color=[255, 165, 0])
            elif textStage == 17:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("The teacher is teaching the class on solving quadratic "
                                                           "equations, however, you don't understand.")
            elif textStage == 18:
                if selectedChoice:
                    cutscene = 3
                    selectedChoice = False

                    if cutscene not in cutscenesUnlocked:
                        cutscenesUnlocked.append(cutscene)
                else:
                    if not cutscene:
                        # pre-cutscene text
                        selectedChoice = draw_default_continue(
                            "You raise your hand, but the teacher doesn't really notice "
                            "you, "
                            "and you realise that he is paying more attention to the "
                            "boys "
                            "in the class than the girls.")
            elif textStage == 19:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue(
                        "At the end of class, the teacher announces that the class will "
                        "have a math assessment next lesson.")
            elif textStage == 20:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("You feel motivated to prove the teacher that you can be as "
                                                           "capable as the boys in the class. After coming back home, "
                                                           "you search online and look at the school math textbooks, "
                                                           "which help you understand the concepts taught at class.")
            elif textStage == 21:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                    minigame = "Math"
                    Course = "Advanced"

                    if "Math" not in minigamesUnlocked:
                        minigamesUnlocked.append("Math")
                else:
                    selectedChoice = draw_default_continue("You are prepared.", choice="START",
                                                           choice_rectangle_color=[0, 180, 0])

            elif textStage == 22 and not minigame:
                if selectedChoice:
                    if advancedWin:
                        textStage += 1
                        selectedChoice = False
                        playerBalance += 1000
                    else:
                        textStage = 27
                        selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("You anxiously wait for your score. "
                                                           "The teacher passes out the assessment paper to everybody "
                                                           "in the "
                                                           "class. On the front page, the teacher's comment reads: "
                                                           "'Well Done!' With high hopes, you open the the worksheet.")
            elif textStage == 23:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("You are mindblown and surprised at how well you did in the "
                                                           "assessment, and you realise that you have the highest "
                                                           "score "
                                                           "in the entire class. You receive a maths academics "
                                                           "scholarship "
                                                           "for your amazing work in the assessment.")
            elif textStage == 24:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue(
                        "The next day, you notice that the teacher pays more attention "
                        "to you, and not just you, but pays equal attention to all the"
                        " boys and girls in the class.")
            elif textStage == 25:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("Math class feels completely different, "
                                                           "and you start learning more and more every lesson.")
            elif textStage == 26:
                if selectedChoice:
                    textStage = 7
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue(
                        "As days become weeks, you are quickly known as the strongest"
                        " math student in your year, and not only do you become "
                        "respected by all male students in your year, but you also "
                        "become a symbol of hope and inspiration for all the girls in "
                        "your school, showing them that female students can be just as "
                        "capable as male students.")
            elif textStage == 27:
                # fails advanced course
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("You are let down as you realise that you were unprepared"
                                                           " for the assessment, not being able to achieve your target"
                                                           " grade. You make sure it will not happen again, and push"
                                                           " yourself to study harder than ever.")
            elif textStage == 28:
                if selectedChoice:
                    textStage = 22
                    selectedChoice = False
                    minigame = "Math"
                    Course = "Advanced"

                    if "Math" not in minigamesUnlocked:
                        minigamesUnlocked.append("Math")
                else:
                    selectedChoice = draw_default_continue("A few days pass. It is the day of the next assessment. "
                                                           "This will be the day you prove yourself worthy of the "
                                                           "advanced course. You can do this!", choice="START",
                                                           choice_rectangle_color=[0, 180, 0])
        else:
            # WW2 SCENARIO
            if textStage == 0:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("You find yourself in World War II, and now live the "
                                                           "life of a 28 year old wife.")
            elif textStage == 1:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("War is breaking out across the country. Males "
                                                           "like your husband are busy fighting the war as soldiers, "
                                                           "while for once, females like yourself are finally given "
                                                           "the opportunity to take industrial jobs, instead of staying"
                                                           " at home as a housewife or being a domestic worker.")
            elif textStage == 2:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("You find two jobs which look very appealing, a power"
                                                           " plant industry and an industry focused on using"
                                                           " atomic physics to assist your country in war, called APRI,"
                                                           " short for Atomic Physics Research Industry")
            elif textStage == 3:
                if selectedChoice:
                    if selectedChoice == "APRI":
                        textStage += 1
                    else:
                        textStage = 47
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_decision("Which job do you chose to apply for", ["Power Plant",
                                                                                                   "APRI"])
            elif textStage == 4:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("Your husband doesn't approve of this, as he strongly "
                                                           "believes that jobs requiring brain power, like researching "
                                                           "on Atomic Physics, should only be given to men.")
            elif textStage == 5:
                if selectedChoice:
                    cutscene = 5
                    selectedChoice = False

                    if cutscene not in cutscenesUnlocked:
                        cutscenesUnlocked.append(cutscene)
                else:
                    if not cutscene:
                        selectedChoice = draw_default_continue("You are hurt and frustrated at the injustice, and yell "
                                                               "that you will prove him wrong by finding success "
                                                               "working in the industry.")
            elif textStage == 6:
                if selectedChoice:
                    if selectedChoice == "Bus ($5)":
                        playerBalance -= 5
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_decision("The next day, you wake up, ready to prove your "
                                                           "worth at the industry. How will you go to work?", ["Walk",
                                                                                                               "Bus ("
                                                                                                               "$5)"])
            elif textStage == 7:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("You arrive right on time. You enter the headquarters and "
                                                           "notice that you rarely come across any females. "
                                                           "You get nervous and anxious.")
            elif textStage == 8:
                if selectedChoice:
                    if selectedChoice == "Greet him":
                        textStage += 1
                    else:
                        textStage = 54
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_decision("Someone bumps into you and you notice that he was your "
                                                           "friend at high school. What do you do?", ["Pretend you "
                                                                                                      "don't know him",
                                                                                                      "Greet him"])
            elif textStage == 9:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("You: Oh hi James! We were friends in high school.")
            elif textStage == 10:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("James: Oh right! I remember you! How are you?")
            elif textStage == 11:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("You: I'm great! It's "
                                                           "my first day at the industry today, "
                                                           "and I'm really excited to work here!")
            elif textStage == 12:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("James: Oh, then you should be going to room 1703 to be "
                                                           "assigned your group. There are 8 groups, and they tend to "
                                                           "put the more experienced people in higher groups. "
                                                           "Hopefully you get put in group 3 with me. Either way, "
                                                           "see you around, I gotta get going now!")
            elif textStage == 13:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("You say bye and rush to room 1703.",
                                                           choice_rectangle_color=[255, 165, 0], choice="Room 1703")
            elif textStage == 14:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("The room is full of people, lining up in front of a table "
                                                           "ahead. You are unsure of what to do, when a speaker "
                                                           "suddenly announces: 'Newcomers, please line up to be "
                                                           "assigned groups.'")
            elif textStage == 15:
                if selectedChoice:
                    if selectedChoice == "Tell the worker":
                        textStage += 1
                    else:
                        textStage = 23
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_decision("You line up anxiously. When it is your turn, you are told "
                                                           "that you will be in group 8. You think that there must "
                                                           "be a mistake, as room 8 is the lowest group.",
                                                           ["Tell the worker", "Leave"])
            elif textStage == 16:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("You: There must be a problem, can you check again just"
                                                           " in case?")
            elif textStage == 17:
                if selectedChoice:
                    if selectedChoice == "Disagree with worker":
                        textStage += 1
                    else:
                        textStage = 23
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_decision("The worker checks again on his computer and confirms that "
                                                           "you are in group 8. He says: 'I'm sorry, but we select "
                                                           "your group based on your experience here. There is nothing "
                                                           "I can do.'", ["Disagree with worker", "Leave"])
            elif textStage == 18:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("You: 'Then I should be assigned to group 1. I received "
                                                           "education in science and engineering fields.")
            elif textStage == 19:
                if selectedChoice:
                    if selectedChoice == "This is outrageous!":
                        textStage += 1
                    else:
                        textStage = 23
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_decision("The worker is irritated and says: 'Miss, there are "
                                                           "other people waiting in line. If you must know, we also "
                                                           "consider other important factors, such as gender, and you "
                                                           "don't fulfill the requirements. Now I'm asking you kindly "
                                                           "to leave the room.'", ["This is outrageous!", "Leave"])
            elif textStage == 20:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("You: 'This is outrageous! How can you judge someone based "
                                                           "on their gender before even meeting them!'")
            elif textStage == 21:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("Worker: 'I see what you mean. I suppose this isn't "
                                                           "exactly moral, however I don't make the rules around here.'"
                                                           )
            elif textStage == 22:
                if selectedChoice:
                    cutscene = 6
                    selectedChoice = False

                    if cutscene not in cutscenesUnlocked:
                        cutscenesUnlocked.append(cutscene)
                else:
                    if not cutscene:
                        selectedChoice = draw_default_continue("After a pause, the worker sighs and says: 'I will speak"
                                                               " to the boss about this later today. In the meantime, "
                                                               "please work with group 8 for now.'", choice="Leave")
            elif textStage == 23:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("You leave the room. You look at the slip given to you:")
            elif textStage == 24:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    draw_apri_slip()
                    selectedChoice = draw_default_continue("APRI SLIP", choice_rectangle_color=[255, 165, 0],
                                                           choice="ROOM 1600")
            elif textStage == 25:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("Your group is experimenting on weaponizing nuclear fission,"
                                                           " by slamming a neutron into an uranium atom.")
            elif textStage == 26:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("You are responsible for calculating the force required for"
                                                           " the uranium atom to split. Based on your research, you"
                                                           " find that powering the machine at 700-800 Volts would"
                                                           " fire the neutron at the exact force required for the "
                                                           "atom to split.")
            elif textStage == 27:
                if selectedChoice:
                    if selectedChoice == "800 Volts":
                        playerBalance -= 130
                        textStage += 1
                    else:
                        textStage = 45
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_decision("It is up to you to decide on the best option to allow"
                                                           " the experiment to be a success", ["700 Volts", "800 Volts"]
                                                           )
            elif textStage == 28:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("The neutron is slightly lighter than expected, and due "
                                                           "to the increased acceleration, hits the atom at a higher"
                                                           " velocity.")
            elif textStage == 29:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("This creates a mini explosion that knocks you off your "
                                                           "feet.")
            elif textStage == 30:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("The electricity in the room is faulty and the machine will"
                                                           " fire another neutron in one minute at 800 Volts. Knowing"
                                                           " this will result in a second explosion, you get up to your"
                                                           " feet and open the control panel of the machine, "
                                                           "desperately attempting to prevent the explosion.")
            elif textStage == 31:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                    minigame = "Wire"

                    # setup for wire minigame
                    wireLives = 3
                    wireCount = 8
                    leftWiresActive = []
                    rightWiresActive = []
                    leftWireColors = []
                    rightWireColors = []
                    for i in range(wireCount):
                        leftWiresActive.append(False)
                        rightWiresActive.append(False)
                        wire_color = wireColorPossibilities[i]
                        leftWireColors.append(wire_color)
                        rightWireColors.append(wire_color)
                        random.shuffle(leftWireColors)
                        random.shuffle(rightWireColors)
                    wireCircleY_Starting = (screenHeight / 2) / wireCount
                    wireCircleY_Distance = screenHeight / wireCount

                    if "Wire" not in minigamesUnlocked:
                        minigamesUnlocked.append("Wire")
                else:
                    selectedChoice = draw_default_continue("Connect the wires to the corresponding color",
                                                           choice="START", choice_rectangle_color=[0, 180, 0])
            elif textStage == 32 and not minigame:
                if wireLives > 0:
                    if selectedChoice:
                        playerBalance += 1200
                        textStage += 1
                        selectedChoice = False
                    else:
                        selectedChoice = draw_default_continue("You managed to save your colleagues and yourself, "
                                                               "earning a reputation in the industry.")
                else:
                    if selectedChoice:
                        textStage = 43
                        selectedChoice = False
                    else:
                        selectedChoice = draw_default_continue("In your rush to disarm the bomb, you mess up the "
                                                               "wire configuration. The explosion knocks you off your "
                                                               "feet and you have no choice but to call for the "
                                                               "professional engineers to help.")
            elif textStage == 33:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("The APRI headquarters quickly becomes your favorite place "
                                                           "to "
                                                           "be, as everyone respects you, despite being female. "
                                                           "Even your husband is impressed when he hears this, "
                                                           "but he doesn't show this.")
            elif textStage == 34:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("The boss personally comes to your home, and apologizes "
                                                           "for putting you in group 8. He promotes you to group 1 "
                                                           "after realising your potential in science and engineering")
            elif textStage == 35:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("A few days pass, and thanks to your research, the industry"
                                                           " can accurately predict the voltage required for nuclear"
                                                           " fission with any atom and neutron.")
            elif textStage == 36:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("This has allowed the industry to begin designing atomic "
                                                           "bombs, and you are in charge of assembling the pieces "
                                                           "together. The bomb structure has already been built, "
                                                           "however, you now need to insert the metal cell containing "
                                                           "the helium neutrons into the atomic bomb without "
                                                           "detonating it.")
            elif textStage == 37:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                    minigame = "Wire"

                    # setup for wire minigame
                    wireLives = 5
                    wireCount = 10
                    leftWiresActive = []
                    rightWiresActive = []
                    leftWireColors = []
                    rightWireColors = []
                    for i in range(wireCount):
                        leftWiresActive.append(False)
                        rightWiresActive.append(False)
                        wire_color = wireColorPossibilities[i]
                        leftWireColors.append(wire_color)
                        rightWireColors.append(wire_color)
                        random.shuffle(leftWireColors)
                        random.shuffle(rightWireColors)
                    wireCircleY_Starting = (screenHeight / 2) / wireCount
                    wireCircleY_Distance = screenHeight / wireCount

                    if "Wire" not in minigamesUnlocked:
                        minigamesUnlocked.append("Wire")
                else:
                    selectedChoice = draw_default_continue("Connect the wires to the corresponding color",
                                                           choice="START", choice_rectangle_color=[0, 180, 0])
            elif textStage == 38 and not minigame:
                if wireLives > 0:
                    if selectedChoice:
                        playerBalance += 2200
                        textStage += 1
                        selectedChoice = False
                    else:
                        selectedChoice = draw_default_continue("To everyone's amazement, you successfully "
                                                               "constructed the bomb and it works on the first try.")
                else:
                    if selectedChoice:
                        textStage = 37
                        selectedChoice = False
                    else:
                        selectedChoice = draw_default_continue("I'm pretty sure you died along with the entire "
                                                               "APRI HQ, however, I will grant you another chance "
                                                               "because I feel extra nice today.",
                                                               choice="Time Travel",
                                                               choice_rectangle_color=[215, 170, 20])
            elif textStage == 39:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("Your husband doesn't know what to say, and admits that he "
                                                           "shouldn't have treated you unfairly, understanding that "
                                                           "everyone has the same rights and potential to make a "
                                                           "difference.")
            elif textStage == 40:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("After dropping two atomic bombs on the country of Japan, "
                                                           "your Allied powers has won the war against the Axis powers,"
                                                           " thanks to you and your amazing research.")
            elif textStage == 41:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("You were able to make a significant impact and become"
                                                           " a role model and symbol of hope for females across the"
                                                           " world, showing men and women that everyone has the same"
                                                           " potential to accomplish anything, whether they are female"
                                                           " or male.")
            elif textStage == 42:
                if playerBalance > playerBalanceHighscore:
                    playerBalanceHighscore = playerBalance
                drawWW2Return = draw_ww2_end()
                if drawWW2Return:
                    if drawWW2Return == 1:
                        running = False
                        break
                    elif drawWW2Return == 2:
                        centralizeBalance = False
                        textStage = 0
                        scenario = 1
                        playerBalance = 100
                else:
                    centralizeBalance = True
            elif textStage == 43:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("The squad of professional engineers manage to disarm "
                                                           "the bomb, and you and your group thank them for helping.")
            elif textStage == 44:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("You analyze the results of the experiment and realise "
                                                           "that using 700 Volts to power the machine would perfectly "
                                                           "split the atom. You report this to your group and "
                                                           "decide to redo the experiment using 700 Volts the next day."
                                                           )
            elif textStage == 45:
                if selectedChoice:
                    playerBalance += 1200
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("You power on the machine and the neutron is fired at a "
                                                           "slightly lower initial velocity than expected, however, "
                                                           "the lightness of the neutron compensates for it and the "
                                                           "increase in acceleration allows the neutron to perfectly "
                                                           "split the atom apart.")
            elif textStage == 46:
                if selectedChoice:
                    textStage = 33
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("Your colleagues are impressed, "
                                                           "and you earn a reputation in the industry.")
            elif textStage == 47:
                if selectedChoice:
                    cutscene = 5
                    selectedChoice = False

                    if cutscene not in cutscenesUnlocked:
                        cutscenesUnlocked.append(cutscene)
                else:
                    if not cutscene:
                        selectedChoice = draw_default_continue("Your husband doesn't approve of this, as working at a "
                                                               "power plant is a job traditionally belonging to men "
                                                               "only.")
            elif textStage == 48:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("As a result, you argue with your husband every day and you"
                                                           " don't sleep together anymore. You are upset by his"
                                                           " behaviour and realise that the only way to fix the"
                                                           " relationship is by proving that you are capable of working"
                                                           " at the power plant.")
            elif textStage == 49:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("The next day, you are tested at the power plant industry"
                                                           " on your engineering skills")
            elif textStage == 50:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                    minigame = "Wire"

                    # setup for wire minigame
                    wireLives = 1
                    wireCount = 4
                    leftWiresActive = []
                    rightWiresActive = []
                    leftWireColors = []
                    rightWireColors = []
                    for i in range(wireCount):
                        leftWiresActive.append(False)
                        rightWiresActive.append(False)
                        wire_color = wireColorPossibilities[i]
                        leftWireColors.append(wire_color)
                        rightWireColors.append(wire_color)
                        random.shuffle(leftWireColors)
                        random.shuffle(rightWireColors)
                    wireCircleY_Starting = (screenHeight / 2) / wireCount
                    wireCircleY_Distance = screenHeight / wireCount

                    if "Wire" not in minigamesUnlocked:
                        minigamesUnlocked.append("Wire")
                else:
                    selectedChoice = draw_default_continue("Connect the wires to the corresponding color",
                                                           choice="START", choice_rectangle_color=[0, 180, 0])
            elif textStage == 51 and not minigame:
                if wireLives > 0:
                    if selectedChoice:
                        playerBalance += 200
                        textStage = 6
                        selectedChoice = False
                    else:
                        selectedChoice = draw_default_continue("Your coworkers are impressed that you were able to "
                                                               "complete the minigame so easily. Your boss immediately"
                                                               " promotes you to work at the Atomic Physics Research"
                                                               " Industry (APRI).")
                else:
                    if selectedChoice:
                        playerBalance -= 150
                        textStage += 1
                        selectedChoice = False
                    else:
                        selectedChoice = draw_default_continue("Your coworkers are disappointed that you messed up on "
                                                               "such an easy task. The boss fires you, and you have "
                                                               "no choice but to leave and seek a new place to earn "
                                                               "money.")
            elif textStage == 52:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("You come across a large and attractive industrial building."
                                                           " The building seems to be calling out to you, and you "
                                                           "wonder if you can work there.")
            elif textStage == 53:
                if selectedChoice:
                    textStage = 6
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("You learn that the name of the industry is APRI, short for"
                                                           "Atomic Physics Research Industry, and after a few "
                                                           "interviews, you are told that you can start working there "
                                                           "tomorrow.")
            elif textStage == 54:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("You: Oh sorry!")
            elif textStage == 55:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("You walk away before he has the chance to look back.")
            elif textStage == 56:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_decision("You suddenly remember that you are meant to be in room "
                                                           "1703 in 5 minutes. You enter the lift. The man next to "
                                                           "you sees that you pressed 17th floor. He asks: 'Are you "
                                                           "going to room 1703?'", ["Yes", "Yah"])
            elif textStage == 57:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("He says: 'Oh, then it must be your first day here. You will"
                                                           " be assigned your group, there are 8 groups, and they tend "
                                                           "to put the more experienced people in higher groups. "
                                                           "Hopefully you get put in group 2 with me. The people there "
                                                           "are very friendly.'")
            elif textStage == 58:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("The elevator dings just as he finishes his sentence.")
            elif textStage == 59:
                if selectedChoice:
                    textStage += 1
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("He says: 'Oh well, I gotta go now. Either way, see you "
                                                           "around!'")
            elif textStage == 60:
                if selectedChoice:
                    textStage = 14
                    selectedChoice = False
                else:
                    selectedChoice = draw_default_continue("You try to smile, however, what he said only makes you more"
                                                           " nervous.", choice_rectangle_color=[255, 165, 0],
                                                           choice="Room 1703")

    if minigame == 'Wire':
        blit_lives(screenWidth - (wireLives * 32), 0)

    # THEME TRACK VOLUME SETTINGS
    hills_of_radiant_winds_sound_file.set_volume(0)
    cipher_sound_file.set_volume(0)
    basketball_minigame_theme_track_sound_file.set_volume(0)
    math_minigame_theme_track_sound_file.set_volume(0)
    wire_minigame_theme_track_sound_file.set_volume(0)
    if not minigame and not cutscene:
        if scenario == 1:
            hills_of_radiant_winds_sound_file.set_volume(1)

        elif scenario == 2:
            cipher_sound_file.set_volume(1)
    elif minigame:
        if minigame == "Basketball":
            basketball_minigame_theme_track_sound_file.set_volume(0.4)

        elif minigame == "Math":
            math_minigame_theme_track_sound_file.set_volume(1)

        elif minigame == "Wire":
            wire_minigame_theme_track_sound_file.set_volume(1)

    mouseDown = False
    keyEnterDown = False

    display.flip()

    clock.tick(gameSpeed)

# REFERENCE CODE (FOR COPY AND PASTE WHEN YOU CAN'T PUT IT IN A FUNCTION)
# # setup for wire minigame
# wireLives = 3
# wireCount = 4
# leftWiresActive = []
# rightWiresActive = []
# leftWireColors = []
# rightWireColors = []
# for i in range(wireCount):
#   leftWiresActive.append(False)
#   rightWiresActive.append(False)
#   wire_color = wireColorPossibilities[i]
#   leftWireColors.append(wire_color)
#   rightWireColors.append(wire_color)
#   random.shuffle(leftWireColors)
#   random.shuffle(rightWireColors)
# wireCircleY_Starting = (screenHeight / 2) / wireCount
# wireCircleY_Distance = screenHeight / wireCount

# # default continue
# if selectedChoice:
#     textStage += 1
#     selectedChoice = False
# else:
#     selectedChoice = draw_default_continue("")
