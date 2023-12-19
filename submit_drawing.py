# Modules:

import pygame
import random
import threading

# Global Variables: 



#FIXME: These Defo are not working at the moment: 
# Output: 
''' 
These are the previous tasks you have done: ['Cup', 'Cup', 'Cup']
You Have done:  0 Tasks
'''
prev_tasks = []
amount_task = len(prev_tasks)


# Function to submit drawing: 

def submit_drawing(pictures, picture_to_draw): 
 
   

    prev_tasks.append(picture_to_draw)


    # Make the next task
   
    next_task = random.choice(pictures)
    while next_task in prev_tasks: 
        next_task = random.choice(pictures)
        

    
    picture_to_draw = next_task
    

    return next_task








    




