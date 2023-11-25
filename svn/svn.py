import pygame
from sklearn import svm

radius = 3
screen = pygame.display.set_mode((600, 400), pygame.RESIZABLE)
flag = True
points = []
clusters = []
mouse_button_down = False
screen.fill("white")
pygame.display.update()
mode = 'Input'
class_color_map = {
    0: 'Red',
    1: 'Green'
}

classes = [0, 1]
# clf = svm.SVC()
# clf.fit(X, y)
clf = None
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                mode = 'Input' if 'Predict' == mode else 'Predict'
            if event.key == pygame.K_SPACE:

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_button_down = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_button_down = False

        if mouse_button_down and event.dict.get("pos"):
            pos = event.pos
            x, y = pos
            color = 'black'
            if mode == 'Predict':
                clf = svm.SVC()
                clf.fit(points, classes)
                prediction = clf.predict([[x, y]])[0]
                color = class_color_map[prediction]
            points.append([x, y])
            pygame.draw.circle(screen, color, pos, radius=radius)

        pygame.display.update()
