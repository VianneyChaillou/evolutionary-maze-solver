import pygame
from entity import Entity
from settings import POPULATION_SIZE

class Population:
    def __init__(self, start_pos):
        """
        Initializes the population with a given number of entities.
        """
        # Create a list containing multiple Entity objects
        self.agents = [Entity(start_pos) for _ in range(POPULATION_SIZE)]
        
        # Keep track of which generation we are on
        self.generation = 1

    def update(self, maze):
        """
        Updates the physics and collisions for every agent in the population.
        """
        for agent in self.agents:
            agent.update(maze)

    def draw(self, surface):
        """
        Draws every agent on the screen.
        """
        for agent in self.agents:
            agent.draw(surface)

    def all_agents_dead(self):
        """
        Checks if all agents have either hit a wall or reached the target.
        Returns True if the generation is over, otherwise False.
        """
        for agent in self.agents:
            # If at least one agent is still alive and hasn't reached the target
            if not agent.dead and not agent.reached_target:
                return False
        
        # If the loop finishes, everyone is dead or at the target
        return True