# IMPORT APPROPIATE LIBRARIES
import random

# CREATING THE DRUNK CLASS
class Drunk:
    # Constructor of Drunk
    def __init__(self, density, drunk_ID, start_x, start_y):
        self.density = density      # used for creating density definition
        self.drunk_ID = drunk_ID    # drunk_ID defined in the model, assigns number to drunks to find their home
        self.x = start_x            # start_x is defined in the model, starting coordinates from the pub
        self.y = start_y            # start_y is defined in the model, starting coordinates from the pub
        self.alcohol_levels = 100   # starting alcohol_levels, used in the sick definition
    
    # Defining movement patterns
    def move(self):
        # If the person is drunk, make their movement staggered by moving at random integers between 1-3
        if self.alcohol_levels > 0:
            if random.random() < 0.5:
                self.x = (self.x + (random.randint(1,3))) % 300    # if random number is <0.05, add 1 to the x-axis of the agent
            else:
                self.x = (self.x - (random.randint(1,3))) % 300    # if random number is >0.05, subtract 1 to the x-axis of the agent
            if random.random() < 0.5:
                self.y = (self.y + (random.randint(1,3))) % 300    # if random number is <0.05, add 1 to the y-axis of the agent
            else:
                self.y = (self.y - (random.randint(1,3))) % 300    # if random number is >0.05, subtract 1 to the y-axis of the agent
                
        if self.alcohol_levels == 0: # once drunk's alcohol level is 0, stop staggering
            if random.random() < 0.5:
                self.x = (self.x + 1) % 300 # if random number is <0.05, add 1 to the x-axis of the agent
            else:
                self.x = (self.x - 1) % 300 # if random number is >0.05, subtract 1 to the x-axis of the agent
            if random.random() < 0.5:
                self.y = (self.y + 1) % 300 # if random number is <0.05, add 1 to the y-axis of the agent
            else:
                self.y = (self.y - 1) % 300 # if random number is >0.05, subtract 1 to the y-axis of the agent
    
    # Defining sick condition
    def sick(self):
        # If the drunk still has some alcohol levels in their body
        if self.alcohol_levels > 0:
            # Gives the drunks a 1% of being sick
            if random.random() < 0.01:
                # Make them sick and subtract 25 from alcohol_levels
                self.alcohol_levels = self.alcohol_levels - 25

    # Defining the density condition    
    def add_density(self):
        # Add 1 to the density list, with the drunk location
        self.density[self.x][self.y] += 1  

