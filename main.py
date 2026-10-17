import pygame
import sys
from population import Population

# Import our constants and classes
from settings import WIDTH, HEIGHT, FPS, WHITE
from environment import Maze

def main():
    # Initialize all imported Pygame modules
    pygame.init()
    
    # Set up the display surface
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Evolutionary AI Maze Solver")
    
    # Set up the clock to control the framerate
    clock = pygame.time.Clock()
    
    # Instantiate our environment (the maze)
    maze = Maze()

    # Creation of our first population 
    population = Population(maze.start_pos)

    # Main application loop
    running = True
    while running:
        # Event handling (inputs, window closing)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear the screen for the new frame
        screen.fill(WHITE)
        
        # Render the environment (walls, start, target)
        maze.draw(screen)

        # Update and draw the population
        population.update(maze)
        population.draw(screen)
        
        # Check if the generation is over
        if population.all_agents_dead():
            print(f"Generation {population.generation} is dead. Time to evolve!")
            # We will call our genetic algorithm here
            
            # For now, let's just reset a new random population to see it loop
            population = Population(maze.start_pos)
        
        # Swap the buffers to display the new frame
        pygame.display.flip()
        
        # Control the framerate
        clock.tick(FPS)

        
        
    # Clean up and exit
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()