# Pictionary


# Important: 
This is the new repo for the game since I fucked the other one up real bad. 
Push ALL changes onto sub-main and make a PR. Pushing into main just breaks everything




# TODO: 
  Create a interactive task giving system. It should give a task after the user submits their first drawing. 
  Get The server sorted out for the drawing submit.
  Actualy figure out a way to get AI to mark it

 # The Game: 
 The user will be given a item to draw from a array of items. The user then draws 
 this item and submits it. Once the marking has been complete the user will be 
 given their score and a new task from the array will be chosen. A more complex 
 approach in the future will be to make the tasks get harder and harder as you go
 but this is more a of a end of project goal.


 # Submit System: 
 The end goal of the submit system is for AI to try and guess what the drawing is.
 The user will submit a drawing which will then be passed to a server. 
 The server will carry that drawing and deliver it to the AI endpoint for marking.
 Once the AI is complete marking it returns the result to the user

 # File Layout: 
 The main script 'game_core.py' hosts the game loop and other core components for pygame. 
 Map functions are stored in 'map_functions.py'
 Task functions are stored in 'new_task.py'
 ...


 
 

