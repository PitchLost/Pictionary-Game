# Modules:

import pygame
import random
import threading



#Import the task function 
from new_task import new_task, pictures, picture_to_draw, update_text


from map_functions import draw_map_comps


# Import the submit script: 
from submit_drawing import submit_drawing, amount_task





pygame.init()

#** Window Config

#* Define the size of the game window

screen_width = 400
screen_height = 400

#* Define the screen: 

screen = pygame.display.set_mode((screen_width,screen_height))


#* Define Colors

BLACK = (0,0,0)

WHITE = (255,255,255)

RED = (255,0,0)

GREEN = (0,255,0)

BLUE = (0,0,255)





run = True

# Define a array for the drawn Rectangles: 
drawn_rectangles =[]

# Create a boolien to track if a task has been given or not

task_given = False

#** Game Functions: 


# Submit Button: 

def draw_submit(screen, screen_height, screen_width): 
    global submit_btn
    submit_btn = pygame.Rect(150, 350, 100, 20)
    pygame.draw.rect(screen, RED, submit_btn)

# Function To clear the drawn rectangles
def remove_rects(): 
    global drawn_rectangles
    drawn_rectangles = []

# Function to color create a rectangle when clicked or 'draw'

def colorTile(event): 

    # Get the coords of the click event
    cursorX, cursorY = event.pos
    
    # I found it easier to make a variable containing both the coords in one

    new_pos = cursorX, cursorY

    # Draw the rect on the click
    rect = pygame.Rect((cursorX - 10, cursorY - 10), (20, 20))


    # Add the current drawn rectangles to the drawn_rectangles array
    # This is important to retaining the position of them each game tick

    drawn_rectangles.append(rect)  # Store the rectangles in a list
    print(new_pos)
    
    # Update the display
    pygame.display.flip()



#** Main Game Loop

while run == True: 
    # Update the background 
    screen.fill(WHITE)


     
    #** Functions to be called upon loop: 
    
    # Draw the map components: 
    draw_map_comps(screen, screen_height, screen_width)

    # Give a task

    new_task(screen, screen_height, screen_width, picture_to_draw)
    task_given = True
        
    # Draw all the rectangles each tick

    for drawn_rect in drawn_rectangles:  
        pygame.draw.rect(screen, RED, drawn_rect)



    # Draw the submit button: 
    draw_submit(screen, screen_height, screen_width)

    # Set the application name: 

    pygame.display.set_caption('Pictionary Game')

    #** Event Listner: 


    #FIXME: Make this less bleh.. Remove the if else shit and replace it with some better code

    for event in pygame.event.get(): 
       
       # If the event is a exit event
        if event.type == pygame.QUIT: 
            print('Terminating Game Window')
            run = False

        # If the user clicks. (Call color function)
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            global mouse_pos
            mouse_pos = pygame.mouse.get_pos() 
            print('Mouse Pos', mouse_pos)

            # Check if the click is on top of the submit button: 
            if submit_btn.collidepoint(mouse_pos): 
                submit_drawing(pictures, picture_to_draw)
                # Remove the drawn rectangles
                remove_rects()
                picture_to_draw = update_text(picture_to_draw)

            

            #FIXME: Check if the click was on the drawing pad instead of the sides and bottom:
            else:
               colorTile(event)


    

    #** Update the display
    pygame.display.update()



pygame.quit()
