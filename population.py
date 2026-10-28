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

    def calculate_fitness_all(self, maze):
        """
        Calls the fitness calculation for every agent in the population.
        """
        # The 'for' loop must be indented INSIDE the function (1 level right)
        for agent in self.agents:
            # The action must be indented INSIDE the 'for' loop (2 levels right)
            agent.calculate_fitness(maze)

    def natural_selection(self, start_pos):
        """
        Creates the next generation with Elitism: the best agent survives untouched.
        """
        new_agents = []
        fitnesses = [agent.fitness for agent in self.agents]
        
        # --- ELITISM ---
        # Find the index of the agent with the highest fitness
        best_idx = fitnesses.index(max(fitnesses))
        best_agent = self.agents[best_idx]
        
        # Clone the champion's DNA without mutating it
        champion_dna = best_agent.dna.__class__(len(best_agent.dna.instructions)) # Or simply DNA(LIFESPAN) if imported
        # Copy the instructions list explicitly to avoid referencing issues
        champion_dna.instructions = list(best_agent.dna.instructions)
        
        champion = Entity(start_pos)
        champion.dna = champion_dna
        new_agents.append(champion)
        
        # --- REST OF THE POPULATION ---
        # Generate the rest (-1 because the champion took 1 spot)
        for _ in range(len(self.agents) - 1):
            parent_a = random.choices(self.agents, weights=fitnesses, k=1)[0]
            parent_b = random.choices(self.agents, weights=fitnesses, k=1)[0]
            
            child_dna = parent_a.dna.crossover(parent_b.dna)
            child_dna.mutate(MUTATION_RATE)
            
            child = Entity(start_pos)
            child.dna = child_dna
            
            new_agents.append(child)
            
        self.agents = new_agents
        self.generation += 1