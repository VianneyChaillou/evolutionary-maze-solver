import pygame
from settings import TILE_SIZE, BLACK, GREEN, BLUE, YELLOW

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
    "X  1        X      X",  # Checkpoint 1: Forces them to go left and down
    "X  XXXXXXX  X  XXXXX",
    "X      X       X   X",  # Checkpoint 2: Guides them to the final corridor
    "XXXX   X2XXXXXXX   X",
    "X      X           X",
    "XXXXXXXXXXXXXXXXXXTX"
]

class Maze:
    def __init__(self, grid=DEFAULT_MAP):
        self.walls = []
        self.start_pos = (0, 0)
        self.target_rect = None
        self.checkpoints = []
        
        # Temporary dict to sort checkpoints dynamically based on the digit
        temp_checkpoints = {}

        for row_idx, row in enumerate(grid):
            for col_idx, cell in enumerate(row):
                x = col_idx * TILE_SIZE
                y = row_idx * TILE_SIZE

                if cell == "X":
                    self.walls.append(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
                elif cell == "S":
                    self.start_pos = (x + TILE_SIZE // 2, y + TILE_SIZE // 2)
                elif cell == "T":
                    self.target_rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                elif cell.isdigit(): # If the cell is a number ("1", "2"...)
                    temp_checkpoints[int(cell)] = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        
        # Convert dict to sorted list so index 0 is Checkpoint 1, index 1 is Checkpoint 2, etc.
        for key in sorted(temp_checkpoints.keys()):
            self.checkpoints.append(temp_checkpoints[key])

    def draw(self, surface):
        for wall in self.walls:
            pygame.draw.rect(surface, BLACK, wall)
            
        # Draw checkpoints in yellow to see them
        for cp in self.checkpoints:
            pygame.draw.rect(surface, YELLOW, cp)
            
        if self.target_rect:
            pygame.draw.rect(surface, GREEN, self.target_rect)
        pygame.draw.circle(surface, BLUE, self.start_pos, TILE_SIZE // 4)