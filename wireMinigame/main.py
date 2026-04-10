import pygame
import random

pygame.init()

screenWidth = 800
screenHeight = 600

screen = pygame.display.set_mode(size=(screenWidth, screenHeight))
minigame = 'Wire'
clock = pygame.time.Clock()
gameSpeed = 100
running = True

# text settings
heart_img = pygame.transform.scale(pygame.image.load('heart.png'), (32, 32))

# wire variables
wireCount = 9
wireLives = 3
leftWireSelected = False
rightWireSelected = False
leftWiresActive = []
rightWiresActive = []
wireColorPossibilities = ['red', 'yellow', 'magenta', 'blue', 'green', 'orange', 'indigo', 'aquamarine', 'brown',
                          'silver', 'ivory', 'darkgreen']
leftWireColors = []
rightWireColors = []

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

wireCircleY_Starting = (screenHeight/2)/wireCount
wireCircleY_Distance = screenHeight/wireCount
wireCircleRadius = 16
wireCircleBorderSize = 4
wireCircleScreenEdgeOffset = 100
wireCircleX_Left = wireCircleScreenEdgeOffset
wireCircleX_Right = screenWidth - wireCircleScreenEdgeOffset
wireMinigameWin = False

# mouse
mouseDown = False
mousePos = False


def blit_lives(x, y):
    for iteration in range(wireLives):
        screen.blit(heart_img, (x + (32 * iteration), y))


def draw_wire_circle(side, row, mouse_pos):
    if side == "left":
        border = pygame.draw.circle(screen,
                                    wireCircleBorderColor,
                                    (wireCircleX_Left, wireCircleY_Starting + wireCircleY_Distance * (row - 1))
                                    , wireCircleRadius + wireCircleBorderSize)
        if border.collidepoint(mouse_pos):
            pygame.draw.circle(screen, wireCircleHoverColor,
                               (wireCircleX_Left, wireCircleY_Starting + wireCircleY_Distance * (row - 1)),
                               wireCircleRadius)
            if mouseDown:
                return "left " + str(row)
        else:
            pygame.draw.circle(screen, leftWireColors[row - 1],
                               (wireCircleX_Left, wireCircleY_Starting + wireCircleY_Distance * (row - 1)),
                               wireCircleRadius)
            return False
    else:
        border = pygame.draw.circle(screen,
                                    wireCircleBorderColor,
                                    (wireCircleX_Right, wireCircleY_Starting + wireCircleY_Distance * (row - 1))
                                    , wireCircleRadius + wireCircleBorderSize)
        if border.collidepoint(mouse_pos):
            pygame.draw.circle(screen, wireCircleHoverColor,
                               (wireCircleX_Right, wireCircleY_Starting + wireCircleY_Distance * (row - 1)),
                               wireCircleRadius)
            if mouseDown:
                return "right " + str(row)
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


while running:
    mousePos = pygame.mouse.get_pos()
    if minigame == 'Wire':
        screen.fill("darkgrey")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouseDown = True

    if minigame == 'Wire':
        # draw wire circles
        returnValues = []
        for i in range(wireCount):
            returnValues.append(draw_wire_circle("left", i+1, mousePos))
            returnValues.append(draw_wire_circle("right", i+1, mousePos))

        for i in returnValues:
            if i:
                wireRow = int(i.split()[1])
                if not leftWireSelected and not rightWireSelected:
                    if i.find("left") != -1:
                        if leftWiresActive[wireRow - 1]:  # if wire clicked is already active do nothing
                            pass
                        else:  # if wire clicked is not already active and no other wires are selected, then select wire
                            leftWireSelected = wireRow

                    elif i.find("right") != -1:
                        if rightWiresActive[wireRow - 1]:  # if wire clicked is already active do nothing
                            pass
                        else:  # if wire clicked is not already active and no other wires are selected, then select wire
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

    if minigame == 'Wire':
        blit_lives(screenWidth - 96, 0)

    mouseDown = False

    pygame.display.flip()

    clock.tick(gameSpeed)
