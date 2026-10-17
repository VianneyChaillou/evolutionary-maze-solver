import pygame
import random
from settings import RED, GREEN, LIFESPAN, ENTITY_RADIUS, MAX_SPEED

class DNA:
    def __init__(self, lifespan):
        """
        Creates a random sequence of 2D vectors (forces) representing the entity's instructions.
        """
        self.instructions = []
        for _ in range(lifespan):
            # Generate a random 2D vector for direction (x and y between -1 and 1)
            force = pygame.math.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
            
            # Normalize the vector so every instruction has the same magnitude/strength
            if force.length() > 0:
                force = force.normalize()
            
            self.instructions.append(force)

class Entity:
    def __init__(self, start_pos):
        """
        Initializes the agent with its physics properties and its DNA.
        """
        self.pos = pygame.math.Vector2(start_pos)
        self.vel = pygame.math.Vector2(0, 0)
        self.acc = pygame.math.Vector2(0, 0)
        
        self.dna = DNA(LIFESPAN)
        self.step = 0  # Current instruction index
        
        self.dead = False
        self.reached_target = False
        
        # Collision rectangle around the entity
        self.rect = pygame.Rect(self.pos.x - ENTITY_RADIUS, self.pos.y - ENTITY_RADIUS, 
                                ENTITY_RADIUS * 2, ENTITY_RADIUS * 2)

    def update(self, maze):
        """
        Reads the DNA, applies physics, and checks for collisions.
        """
        # Stop moving if dead or if the target is reached
        if self.dead or self.reached_target:
            return

        # 1. Read instruction from DNA
        if self.step < len(self.dna.instructions):
            self.acc = self.dna.instructions[self.step]
            self.step += 1
        else:
            # If the entity runs out of instructions, it dies
            self.dead = True
            return

        # 2. Apply Physics (Euler integration)
        self.vel += self.acc
        
        # Limit speed to prevent passing through walls (tunneling effect)
        if self.vel.length() > MAX_SPEED:
            self.vel.scale_to_length(MAX_SPEED)
            
        self.pos += self.vel
        
        # Update the collision rectangle's position
        self.rect.center = (int(self.pos.x), int(self.pos.y))

        # 3. Check Collisions
        # Using collidelist() which returns -1 if no collision, or the index of the wall hit
        if self.rect.collidelist(maze.walls) != -1:
            self.dead = True
            
        # Check if target is reached
        if maze.target_rect and self.rect.colliderect(maze.target_rect):
            self.reached_target = True

    def draw(self, surface):
        """
        Draws the entity on the screen.
        Turns green if it reached the target, otherwise red.
        """
        color = GREEN if self.reached_target else RED
        pygame.draw.circle(surface, color, (int(self.pos.x), int(self.pos.y)), ENTITY_RADIUS)