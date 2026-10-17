import pygame
import sys
from entity import Entity

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

    # Creation of our first entity 
    agent = Entity(maze.start_pos)

    # Main application loop
    running = True
    while running:
        # 1. Event handling (inputs, window closing)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # 2. Clear the screen for the new frame
        screen.fill(WHITE)
        
        # 3. Render the environment (walls, start, target)
        maze.draw(screen)

        agent.update(maze)
        agent.draw(screen)
        
        # 4. Swap the buffers to display the new frame
        pygame.display.flip()
        
        # 5. Control the framerate
        clock.tick(FPS)

        
        
    # Clean up and exit
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()