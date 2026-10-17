WIDTH, HEIGHT = 800, 600
FPS = 60
TILE_SIZE = 40  # Block size (wall or empty space)

# Colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)  # Fro the target
BLUE = (0, 0, 255)   # For the departure

RED = (255, 0, 0)
LIFESPAN = 400       # max number of instractions (step) per entity 
ENTITY_RADIUS = 4    # Size of our point
MAX_SPEED = 4        # Maximum speed to prevent it from passing through walls (glitch)