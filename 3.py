import pygame
import math

# Define the size of the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Define the colors used for the shapes
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the size and spacing of the shapes
SHAPE_SIZE = 150
SHAPE_SPACING = 200

def draw_diamond(surface, color, center_x, center_y, size):
    # Define the vertices of the diamond shape
    vertices = [
        (center_x, center_y - size / 2),
        (center_x + size / 2, center_y),
        (center_x, center_y + size / 2),
        (center_x - size / 2, center_y)
    ]
    
    # Draw the diamond shape
    pygame.draw.polygon(surface, color, vertices)

def draw_heart(surface, color, center_x, center_y, size):
    # Define the vertices of the heart shape
    vertices = []
    for i in range(360):
        t = math.radians(i)
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        vertices.append((center_x + size * x / 20, center_y + size * y / 20))

    # Draw the heart shape
    pygame.draw.polygon(surface, color, vertices)

def draw_club(surface, color, center_x, center_y, size):
    # Draw the center shape of the club
    center_size = size / 3
    center_rect = pygame.Rect(center_x - center_size / 2, center_y - center_size / 2, center_size, center_size)
    pygame.draw.rect(surface, color, center_rect)
    
    # Draw the three circles of the club
    circle_size = size / 5
    circle_offset = size / 3
    left_circle_center = (center_x - circle_offset, center_y)
    right_circle_center = (center_x + circle_offset, center_y)
    top_circle_center = (center_x, center_y - circle_offset)
    pygame.draw.circle(surface, color, left_circle_center, circle_size)
    pygame.draw.circle(surface, color, right_circle_center, circle_size)
    pygame.draw.circle(surface, color, top_circle_center, circle_size)

def draw_shapes(window):
    # Draw the diamond, heart, and club shapes
    draw_diamond(window, BLUE, WINDOW_WIDTH // 4, WINDOW_HEIGHT // 2, SHAPE_SIZE)
    draw_heart(window, RED, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, SHAPE_SIZE)
    draw_club(window, GREEN, WINDOW_WIDTH * 3 // 4, WINDOW_HEIGHT // 2, SHAPE_SIZE)
    
    # Draw the shapes with increased spacing
    draw_diamond(window, BLUE, WINDOW_WIDTH // 4 - SHAPE_SPACING, WINDOW_HEIGHT // 2, SHAPE_SIZE)
    draw_heart(window, RED, WINDOW_WIDTH // 2 - SHAPE_SPACING, WINDOW_HEIGHT // 2, SHAPE_SIZE)
    draw_club(window, GREEN, WINDOW_WIDTH * 3 // 4 - SHAPE_SPACING, WINDOW_HEIGHT // 2, SHAPE_SIZE)

def main():
    # Initialize the Pygame library
    pygame.init()
    
    # Create the window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Shape Visualization')
    
    # Set the background color of the window
    window.fill(WHITE)
    
    # Draw the shapes
    draw_shapes(window)
    
    # Update the display
    pygame.display.update()
    
    # Wait for the user to close the window
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    # Quit the Pygame library
    pygame.quit()

# Call the main function to run the program
if __name__ == '__main__':
    main()

