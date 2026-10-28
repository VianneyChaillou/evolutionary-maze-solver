import pygame
import sys
from entity import Entity
from population import Population
from environment import Maze

# Make sure all these are in your settings.py
from settings import WIDTH, HEIGHT, FPS, WHITE, CYCLES_PER_FRAME, RENDER_EVERY_N_GEN

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Evolutionary AI Maze Solver")
    clock = pygame.time.Clock()
    maze = Maze()
    
    population = Population(maze.start_pos)
    
    # --- NEW: State Machine Variables ---
    state = "TRAINING"  # Can be "TRAINING" or "REPLAY"
    winning_dna = None
    replayer = None
    
    running = True
    while running:
        # 1. Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if state == "TRAINING":
            # --- TRAINING MODE ---
            
            # Do we draw this generation?
            should_render = (population.generation % RENDER_EVERY_N_GEN == 0)
            
            # If we don't render, we remove the cycle limit and blast through calculations
            cycles = CYCLES_PER_FRAME if should_render else 20
            
            for _ in range(cycles):
                pygame.event.pump() 

                population.update(maze)
                                
                # Check if ANY agent reached the final target this frame!
                for agent in population.agents:
                    if agent.reached_target:
                        print(f"VICTORY! Target reached at generation {population.generation}!")
                        state = "REPLAY"
                        winning_dna = agent.dna
                        
                        # Create our single replay entity
                        replayer = Entity(maze.start_pos)
                        replayer.dna = winning_dna
                        break # Stop checking agents
                        
                if state == "REPLAY":
                    break # Stop the fast-forward loop immediately
                    
                # Evolution step
                if population.all_agents_dead():
                    population.calculate_fitness_all(maze)
                    population.natural_selection(maze.start_pos)
            
            # Render only if it's a designated rendering generation
            if should_render:
                screen.fill(WHITE)
                maze.draw(screen)
                population.draw(screen)
                pygame.display.flip()
                clock.tick(FPS)
                
        elif state == "REPLAY":
            # --- REPLAY MODE ---
            # Update at normal speed (1 cycle per frame) without fast-forward
            replayer.update(maze)
            
            # If the replay finishes, restart it indefinitely to loop the victory
            if replayer.dead or replayer.reached_target:
                replayer = Entity(maze.start_pos)
                replayer.dna = winning_dna
            
            # Always render the replay smoothly
            screen.fill(WHITE)
            maze.draw(screen)
            replayer.draw(screen)
            pygame.display.flip()
            
            # Cap the framerate to normal speed
            clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()