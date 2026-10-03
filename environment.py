import pygame
from settings import TILE_SIZE, BLACK, GREEN, BLUE

# A simple default map to test our environment (20x15 grid for 800x600 resolution)
DEFAULT_MAP = [
    "XXXXXXXXXXXXXXXXXXXX",
    "XS     X           X",
    "X  XXX X  XXXXXX   X",
    "X    X X       X   X",
    "X  XXX XXXXX   X   X",
    "X        X         X",
    "XXXXXX   X  XXXX   X",
    "X        X     X   X",
    "X  XXXXXXX  XXXX   X",
    "X           X      X",
    "X  XXXXXXX  X  XXXXX",
    "X      X       X   X",
    "XXXX   X  XXXXXX   X",
    "X      X           X",
    "XXXXXXXXXXXXXXXXXXTX"
]

class Maze:
    def __init__(self, grid=DEFAULT_MAP):
        """
        Initializes the maze by parsing the grid layout.
        Extracts wall positions, start position, and target area.
        """
        self.walls = []
        self.start_pos = (0, 0)
        self.target_rect = None

        # Parse the grid string to build the environment
        for row_idx, row in enumerate(grid):
            for col_idx, cell in enumerate(row):
                # Calculate absolute pixel coordinates
                x = col_idx * TILE_SIZE
                y = row_idx * TILE_SIZE

                if cell == "X":
                    # Store walls as pygame.Rect for easy collision detection later
                    self.walls.append(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
                elif cell == "S":
                    # Center the start position within its tile
                    self.start_pos = (x + TILE_SIZE // 2, y + TILE_SIZE // 2)
                elif cell == "T":
                    # Store target as a Rect to detect when entities reach it
                    self.target_rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)

    def draw(self, surface):
        """
        Renders the walls, target, and start position on the given surface.
        """
        # Draw all walls
        for wall in self.walls:
            pygame.draw.rect(surface, BLACK, wall)
        
        # Draw the target
        if self.target_rect:
            pygame.draw.rect(surface, GREEN, self.target_rect)
        
        # Draw a small indicator for the start position (optional, good for visual debugging)
        pygame.draw.circle(surface, BLUE, self.start_pos, TILE_SIZE // 4)