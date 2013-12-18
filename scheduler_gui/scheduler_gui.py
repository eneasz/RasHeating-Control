#!/usr/bin/python
"""
Code for displaying a 2x 12hr grid for hourly configuration of Scheduling of a subtask.
ie. 2x 12hrs for Monday, Tuesday... etc.

To supply a backend with "Should I be running right now?"

Initial plan is to have this running fullscreen on a 2.8" Touchscreen
attached to a RasberryPi, to allow a user to configure Central Heating Schedules
on a per-day, per-hour, basis.

Base code and learning from: http://programarcadegames.com/index.php?chapter=array_backed_grids

Revised code written by Darren Gibbard
"""
# Import pygame libraries
try:
    import pygame
except ImportError as err:
    print("Failed to load the pygame Python library. Error:\n\n" + str(err))

import sys, os

# Define some basic colours
black = (   0,   0,   0)
white = ( 255, 255, 255)
green = (   0, 255,   0)
#red   = ( 255,   0,   0) # We're not using red at the moment.

# Set the width and height of each grid location/cell
# On a screen of 320x240 (Small 2.8" Touchscreen on Raspberry Pi) - 24 squares @ 20px + 3px margins / 2 rows = 276px; leaving 22px at the start and end of the row.
width  = 20
height = 20

# Set the margin between cells, at the start of a row (sidemargin) and at the top of the display (topmargin).
margin = 3
sidemargin = 22
topmargin = 30

# Statically assign the number of columns/rows
colnum = 12
rownum = 2

# Create a 2 dimensional array. ie. List of lists.
grid = []
for row in range(rownum):
    # Add empty array that will hold each cell in this row.
    grid.append([])
    for column in range(colnum):
        grid[row].append(0) # Append a cell

## Debug - Set row1 (Mon-PM), cell5 (17:00) to One.
# grid[1][5] = 1

## DEBUG - Print list:
#print grid

# Initialise pygame
try:
    pygame.init()
except KeyboardInterrupt:
    print("Stopping initialisation...")
    try:
        pygame.quit()
        sys.exit(0)
    except:
        sys.exit(0)
except Exception as err:
    print("Encountered an error initialising. Error:\n\n", err)

size = [320, 240] ## Eventually, this will become "FULLSCREEN"  in the display definition for small touchscreen LCDs.
screen = pygame.display.set_mode(size)

# Set title of Window (becomes irrelevant when we switch to FULLSCREEN.)
pygame.display.set_caption("Scheduler GUI")

# Setup "done" to be False. If set True during our run, we will quit.
done = False

# Setup clock to manage how fast the screen updates
clock = pygame.time.Clock()

### MAIN LOOP
try:
    while not done:
        for event in pygame.event.get(): #User did something...
            if event.type == pygame.QUIT: #If user clicked close.
                done = True #Now done is true, we'll exit in a second.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicked the mouse, get the position of the cursor
                pos = pygame.mouse.get_pos()
                # Change x/y to screen co-ords in comparison to our grid.
                #column = (pos[0] // ((sidemargin - margin) + width + margin))
                #row = (pos[1] // ((topmargin - margin) + height + margin))
                ### We remove our initial gap from the mouse position first,
                ### So that we're dealing entirely with the grid
                column = (pos[0] - sidemargin) // (width + margin)
                row = (pos[1] - topmargin) // (height + margin)
                # Change that location's value in the grid:
                try:
                    grid[row][column] = 0 if grid[row][column] == 1 else 1
                except IndexError:
                    continue

        # Now we've evaluate our current situation, lets draw the screen:
        # Fill it black first:
        screen.fill(black)

        # Draw the grid
        for row in range(rownum):
            for column in range(colnum):
                colour = green if grid[row][column] == 1 else white
                pygame.draw.rect(screen,
                                 colour,
                                 [((sidemargin - margin) + ((margin+width) * column + margin)),
                                  ((topmargin - margin) + ((margin+height) * row + margin)),
                                 #[((margin+width) * column + margin),
                                 # ((margin+height) * row + margin),
                                  width,
                                  height])
        # Limit to 20fps
        clock.tick(20)

        # Update the screen with what we've got:
        pygame.display.flip()

except KeyboardInterrupt:
    print("Quitting...")
    pygame.quit()

# Quit line - hit once "done" == True
pygame.quit()
