
# Modules:

import pygame




# Define Colors

BLACK = (0,0,0)

WHITE = (255,255,255)

RED = (255,0,0)

GREEN = (0,255,0)

BLUE = (0,0,255)


# Make the Map Components

def draw_map_comps(screen, screen_height, screen_width):
    # The bottom component of the map

    bottom_comp = pygame.Rect(0, 300, 450, 100)

    # Draw the Bottom Comp: 
    
    pygame.draw.rect(screen, BLUE, bottom_comp)

    # The Top Component: 

    top_comp = pygame.Rect(0, 0, 450, 60)

    # Draw the Top Comp

    pygame.draw.rect(screen, BLUE, top_comp)





