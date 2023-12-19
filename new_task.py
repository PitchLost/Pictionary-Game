# Modules:

import pygame
import random
import threading

from submit_drawing import submit_drawing

delay = 4


#* Define Colors

BLACK = (0,0,0)

WHITE = (255,255,255)

RED = (255,0,0)

GREEN = (0,255,0)

BLUE = (0,0,255)





# Function to assign a new task to the user:

def new_task(screen, screen_height, screen_width, picture_to_draw): 
   
  
    # Font: 

   # Set up fonts
   font = pygame.font.Font(None, 36)  # You can choose the font and size here

   # Render text 
   text = font.render("Draw Me a " + picture_to_draw, True, WHITE)  # Text, anti-aliasing, color

      
    # Display text
   text_rect = text.get_rect(midtop=(screen_width // 2, 0))# Position of the text
   screen.blit(text, text_rect)

   
# Function to update text

def update_text(next_task):
   
    current_picture_to_draw = submit_drawing(pictures, picture_to_draw)
    
    return current_picture_to_draw






# Create a array for the objects

pictures = ['Duck','Chair','Table','Skateboard','Gun','Cup','Car','Bike','Person', 'Laptop']


picture_to_draw = random.choice(pictures)





    