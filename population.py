import pygame
import random
from entity import Entity
from settings import POPULATION_SIZE
from settings import MUTATION_RATE

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

    def calculate_fitness_all(self, target_rect):
        """
        Calls the fitness calculation for every agent in the population.
        """
        for agent in self.agents:
            agent.calculate_fitness(target_rect)

    def natural_selection(self, start_pos):
        """
        Creates the next generation of agents based on the fitness of the current one.
        """
        new_agents = []
        
        # Extract the fitness of every agent to use as weights for the selection
        fitnesses = [agent.fitness for agent in self.agents]
        
        for _ in range(len(self.agents)):
            # Select two parents. random.choices picks based on the weights (fitness)
            # The higher the fitness, the more likely they are to be chosen!
            parent_a = random.choices(self.agents, weights=fitnesses, k=1)[0]
            parent_b = random.choices(self.agents, weights=fitnesses, k=1)[0]
            
            # Combine their DNA
            child_dna = parent_a.dna.crossover(parent_b.dna)
            
            # Mutate the child's DNA
            child_dna.mutate(MUTATION_RATE)
            
            # Create a new entity with this new DNA
            child = Entity(start_pos)
            child.dna = child_dna
            
            new_agents.append(child)
            
        # Replace the old population with the new generation
        self.agents = new_agents
        self.generation += 1