# Initiate pygame program
import pygame
pygame.init()

# Background fill
#   size
screen = pygame.display.set_mode([1200, 750])
#   color
screen.fill((79, 121, 66))

#TODO: Make a coordinate system with 8 rows and columns

# Coordinate system
# from dataclasses import dataclass
# @dataclass
# class Coordinate:
#     row: str
#     column: int
#
# rows = ["A", "B", "C", "D", "E", "F", "G", "H"]
# columns = [1, 2, 3, 4, 5, 6, 7, 8]

#Define squares
class Square:
    def __init__(self, width, height, color, x_pos, y_pos):
        self.square_width = 80
        self.square_height = 80


x_pos = 0
y_pos = 0

for row in rows:
    x_pos += square_width
    for column in columns:
        y_pos += square_height
        pygame.Rect(x_pos, y_pos, square_width, square_height)

#White squares
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(275, 55, 80, 80))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(275+160, 55, 80, 80))



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
