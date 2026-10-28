WIDTH, HEIGHT = 800, 600
FPS = 60
TILE_SIZE = 40  # Block size (wall or empty space)

# Colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)  # Fro the target
BLUE = (0, 0, 255)   # For the departure
YELLOW = (255, 255, 0) # Color for our checkpoints

RED = (255, 0, 0)   # For the entity
LIFESPAN = 400       # max number of instractions (step) per entity 
ENTITY_RADIUS = 4    # Size of our point
MAX_SPEED = 4        # Maximum speed to prevent it from passing through walls (glitch)

POPULATION_SIZE = 150  # Number of entities in our swarm

MUTATION_RATE = 0.01 # 1% chance for a gene to mutate

CYCLES_PER_FRAME = 50 # Increase this to speed up simulation time (e.g., 10 or 50)

YELLOW = (255, 255, 0) # Color for our checkpoints