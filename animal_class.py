import random
from settings import *

class Animal:
    def __init__(self, speed, gender, reproduct, sight, hunger, thirst, age, pos, grid):
        self.speed = speed
        self.gender = gender
        self.reproduct = reproduct
        self.sight = sight
        self.hunger = hunger
        self.thirst = thirst
        self.age = age
        self.pos = pos
        self.grid = grid
    
    #Fills every square that a wolf can see
    def draw_sight_circle(self, seen_squares):
        for point in seen_squares:
            for row in range(X_SIZE):
                for col in range(Y_SIZE):
                    if (row, col) == point:
                        self.grid.matrix[row][col] = 2

    def mutate(self):
        pass

    #Make animal move over grid
    def wander(self):
        #Make old position empty
        self.grid.matrix[self.pos[1]][self.pos[0]] = 0

        #Wander randomly 
        self.pos[0] += self.speed * random.randint(-1, 1) - random.randrange(0, 3) + random.randrange(0, 3)
        self.pos[1] += self.speed * random.randint(-1, 1) - random.randrange(0, 3) + random.randrange(0, 3)
        
        #Check if still in grid
        if self.pos[0] >= X_SIZE :
            self.pos[0] = X_SIZE -1
        if self.pos[1] >=Y_SIZE :
            self.pos[1] = Y_SIZE -1

        #Tell the grid where the animal is
        self.grid.matrix[self.pos[1]][self.pos[0]] = 1
    
    #Calculates squares in sight of animal [point in circle][1]
    def calculate_sight(self):
        seen_squares = []
        for x in range(X_SIZE):
                for y in range(Y_SIZE):
                    dx = abs(x - self.pos[0])
                    dy = abs(y - self.pos[1])
                    
                    if dx + dy < self.sight:
                        seen_squares.append((x,y))

                    if dx**2 + dy**2 <= self.sight ** 2:
                        seen_squares.append((x,y))
        return seen_squares







""" Also an option for calculating sight:
    #using this algorithm: https://en.wikipedia.org/wiki/Midpoint_circle_algorithm
    def calculate_sight(self):
        seen_squares = []
    
        d = 3 - 2 * self.sight
        x = 0
        y = self.sight

        while x < y:
            seen_squares.append((x + self.pos[0], y + self.pos[1]))
            seen_squares.append((x + self.pos[0], -y + self.pos[1]))
            seen_squares.append((-x + self.pos[0], -y + self.pos[1]))
            seen_squares.append((-x + self.pos[0], y + self.pos[1]))
            seen_squares.append((y + self.pos[0], x + self.pos[1]))
            seen_squares.append((y + self.pos[0], -x + self.pos[1]))
            seen_squares.append((-y + self.pos[0], -x + self.pos[1]))
            seen_squares.append((-y + self.pos[0], x + self.pos[1]))

            if d < 0:
                d = d + 4*x + 6
                x += 1
            elif d >= 0:
                d = d + 4 * (x-y) + 10
                x += 1
                y -= 1

        return seen_squares
    """

   #[1]: https://stackoverflow.com/questions/481144/equation-for-testing-if-a-point-is-inside-a-circle