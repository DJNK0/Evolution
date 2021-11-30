from settings import *
import pygame
import numpy as np

"""
0: Empty square
1: Sheep
"""

class Grid:
    def __init__(self, game):
        #initialize the game
        self.game = game
        #initialize the grid
        self.matrix = self.create_2d_arr()

    #Create a matrix size of [X_SIZE, Y_SIZE]
    def create_2d_arr(self):
        print(np.zeros([X_SIZE, 1], dtype=int))
        return np.zeros([X_SIZE, 1], dtype=int)

    def update(self):
        pass
    
    #Draws grid to the screen
    def draw_grid(self):
        for row in range(X_SIZE):
            for col in range(Y_SIZE):
                #If it is a sheep, draw a (color) square
                if self.matrix[row][col] == 1:
                    color = BLACK
                elif self.matrix[row][col] == 2:
                    color = (225, 255, 100)
                else:
                    color = RED

                #Draw rectangle to screen
                pygame.draw.rect(self.game.screen,
                                color,
                                [(MARGIN + WIDTH) * col + MARGIN,
                                (MARGIN + HEIGHT) * row + MARGIN,
                                WIDTH, HEIGHT])
