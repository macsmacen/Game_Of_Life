import pygame
import numpy as np

# Define the size of the grid
grid_size = 50
cell_size = 10

# Initialize Pygame
pygame.init()

# Set the size of the screen
screen = pygame.display.set_mode((grid_size*cell_size, grid_size*cell_size))

# Initialize the grid
grid = np.zeros((grid_size, grid_size))

# Define a variable to keep track of whether the simulation is running or paused
paused = True

# Define a function to update the grid
def update_grid(grid):
    # Copy the grid
    new_grid = grid.copy()
    # Iterate over each cell in the grid
    for i in range(grid_size):
        for j in range(grid_size):
            # Count the number of live neighbors
            num_neighbors = np.sum(grid[max(0, i-1):min(i+2, grid_size), max(0, j-1):min(j+2, grid_size)]) - grid[i, j]
            # Apply the rules of the Game of Life
            if grid[i, j] == 1 and (num_neighbors < 2 or num_neighbors > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and num_neighbors == 3:
                new_grid[i, j] = 1
    # Update the grid
    grid[:] = new_grid[:]

# Define a function to draw the grid
def draw_grid(grid):
    # Clear the screen
    screen.fill((255, 255, 255))
    # Draw the cells
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i, j] == 1:
                pygame.draw.rect(screen, (0, 0, 0), (j*cell_size, i*cell_size, cell_size, cell_size))
    # Update the screen
    pygame.display.flip()

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Place initial points on the grid
            if paused:
                x, y = pygame.mouse.get_pos()
                i, j = y // cell_size, x // cell_size
                grid[i, j] = 1
        elif event.type == pygame.KEYDOWN:
            # Pause or restart the simulation
            if event.key == pygame.K_SPACE:
                paused = not paused
            elif event.key == pygame.K_r:
                grid[:] = 0
                paused = True
    # Update the grid if the simulation is running
    if not paused:
        update_grid(grid)
    # Draw the grid
    draw_grid(grid)
    # Delay to control the speed of the simulation
    pygame.time.delay(100)
    
# Quit Pygame
pygame.quit()