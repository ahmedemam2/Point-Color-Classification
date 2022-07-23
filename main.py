import pygame
import PerceptronC
import Training
import sys

trainingIndex = 0
brain = PerceptronC.Perceptron()
listPts = []
listcolor = []
def createPts():
    for i in range(100):
        temp = Training.Point()
        listPts.append(temp)

def setup():
    inputs = [-1,0.5]
    guess = brain.guess(inputs)
    print(guess)
    pygame.init()
    White = (255, 255, 255)
    winW = 400
    winH = 400
    wn = pygame.display.set_mode((winW, winH))
    # circle
    startx = winW
    starty = winH
    endx = 0
    endy = 0
    radius = 5
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for pt in listPts:
                    inputs = [pt.x, pt.y]
                    target = pt.label
                    brain.train(inputs,target)

        wn.fill(White)

        width = 5
        pygame.draw.line(wn, (0,0,0,), (startx, starty), (endx, endy))
        for pt in listPts:
            pygame.draw.circle(wn, pt.color, (pt.x ,pt.y), radius)
        for pt in listPts:
            inputs = [pt.x,pt.y]
            target = pt.label
            guess = brain.guess(inputs)
            if guess == target:
                pt.color = (0,255,0)
            else:
                pt.color = (255,0,0)

        pygame.display.update()

createPts()
setup()
def show():
    pass

