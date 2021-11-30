import pygame
from settings import *
import grid_class
import random
import sheep_class

class Game:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()

        #Used to check if game loop should be stopped
        self.running = True 

        #Init screen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  

        #Create grid object
        self.grid = grid_class.Grid(self)

        self.create_sheep()

        
        self.sheep_to_grid()
        
    #Game loop
    def run(self):
        while self.running:
            self.get_events()
            
            self.update()
            self.clock.tick(150)
            self.draw()
        pygame.quit()
    
    #Check for events
    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        for sheep in self.sheep_list:
            sheep.wander()
            seen_squares = sheep.calculate_sight()
            sheep.draw_sight_circle(seen_squares)
        

    #Draw everything to screen
    def draw(self):
        self.screen.fill(BG_COLOUR)
        self.grid.draw_grid()
        pygame.display.update()

    def create_sheep(self):
        self.sheep_list = []
        self.sheep_amount = random.randint(1, 1)

        #Generate random sheep list
        for s in range(self.sheep_amount):
            speed = random.randint(1, 3)
            gender = random.randint(0, 1)
            reproduct = random.randint(1, 10)
            sight = random.randint(23, 23)
            hunger = 0
            thirst = 0
            age = 0
            pos = [random.randint(25, 26 - 1), random.randint(25, 26 - 1)]

            sheep = sheep_class.Sheep(speed, gender, reproduct, sight, hunger, thirst, age, pos, self.grid)
            self.sheep_list.append(sheep)
        for sheep in self.sheep_list:
            print(sheep.pos)
    
    #Add sheep to grid we generated
    def sheep_to_grid(self):
        for sheep in self.sheep_list:
            sheep_x = sheep.pos[0]
            sheep_y = sheep.pos[1]
            self.grid.matrix[sheep_y][sheep_x] = 1
    
