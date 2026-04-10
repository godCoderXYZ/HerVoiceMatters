import pygame
from pygame import display
import time

pygame.init()

screenWidth = 800
screenHeight = 600

screen = display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
minigame = 'Math'
gameSpeed = 100
text_string = ""
mouseDown = False
running = True

# math minigame settings
mathMinigameFont = pygame.font.SysFont("Arial", 20)
coverSize = (621, 877)
questionSize = (800, 269)
coverY = 0
scrollSpeed = 0.3
Course = "Basic"
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


# don't copy and paste the two functions below. Already included in pythonProject - main.py
def check_string_length(string, color, font, max_width):
    text_image = font.render(string, True, color)

    # delete a character if text image is longer than question box
    if text_image.get_width() > max_width:
        string = string[:-1]
        text_image = font.render(string, True, color)
        return [text_image, string]
    else:
        return [text_image, string]


def blit_text(string, color, font, position):
    text_image = font.render(string, True, color)
    screen.blit(text_image, position)


while running:
    # if minigame == 'Math':
    screen.fill('black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouseDown = True

        if minigame == "Math":
            if Course:
                if event.type == pygame.KEYDOWN:
                    if not answerDisplayTimeStart and mathQuestion:
                        if event.key == pygame.K_BACKSPACE:
                            text_string = text_string[:-1]
                        elif event.key == pygame.K_RETURN:
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
                        else:
                            text_string += event.unicode

    if minigame == "Math":
        if Course == "Basic":
            if mathQuestion:
                # if player is answering math question then blit the current question
                screen.blit(basicQuestions[mathQuestion - 1], ((screenWidth - questionSize[0]) / 2,
                                                               (screenHeight - questionSize[1]) / 2))
                # check
                returnList = check_string_length(text_string, 'black', mathMinigameFont, questionBoxWidth)
                text_string = returnList[1]

                # blit player answer input
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
                screen.blit(returnList[0], (answerInputPosition[0], answerInputPosition[1]))
            else:
                # if player is not currently answering a math question, then blit the cover instead of the question
                screen.blit(advancedCourseCover, ((screenWidth - coverSize[0]) / 2, - coverY))

        if coverY < maximumCoverY:
            coverY = round((coverY + scrollSpeed) * 10) / 10
            if coverY >= maximumCoverY:
                mathQuestion = 1

        if answerDisplayTimeStart:
            if time.time() >= answerDisplayTimeStart + answerDisplayDelay:
                if Course == "Advanced":
                    if mathQuestion == 3:
                        if advancedCorrectAnswerCount > 0:
                            advancedWin = True
                            print("WIN ADVANCED")
                        else:
                            advancedWin = False
                            print("LOSE ADVANCED")
                        minigame = False
                        mathQuestion = False
                        Course = False
                    else:
                        mathQuestion += 1

                elif Course == "Basic":
                    mathQuestion += 1

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
                        print("WIN BASIC")
                        minigame = False
                        mathQuestion = False
                        Course = False

                        text_string = ""
                        answerDisplayTimeStart = False
                    else:
                        blit_text(("WRONG - ANSWER: " + basicAnswers[mathQuestion - 1][0]), 'red',
                                  mathMinigameFont, answerDisplayPosition)

    mouseDown = False
    display.flip()

    clock.tick(gameSpeed)
