#################################################
# Name: Jiayu Li
# Andrew id: jiayul2
#################################################

import math, random
from PIL import ImageTk, Image
import pygame
from cmu_112_graphics import * 
import numpy as np
import pandas as pd

#################################################
# Porter Hall Live View Interface
#################################################

def rgbString(r, g, b):
    # This helper function aims to convert rgb value to its color which is from:
    # https://www.cs.cmu.edu/~112/notes/notes-graphics.html#customColors
    return f'#{r:02x}{g:02x}{b:02x}'

def appStarted(app):
    app.height = 800
    app.width = 1000
    # background
    app.image1 = app.loadImage('floor1.png')
    app.image2 = app.scaleImage(app.image1, 0.8)

    # canvas.create_polygon(rightBowTopX, rightBowTopY, cx, cy, \
    #                 rightBowBottomX, rightBowBottomY, \
    #                 fill = app.bowColor, outline = 'DarkOrchid4', width = 3)
    
#################################################

def drawFloorPlan(app, canvas):
    canvas.create_image(app.width * 0.45, app.height * 0.6, image = ImageTk.PhotoImage(app.image2))

def drawLocationPoint(app, canvas):
    canvas.create_text(app.width * 0.5, app.height * 0.08, \
                text = 'Real-time View of Rooms on the 1st Floor of Porter Hall', font = 'Times 30', \
                fill = 'black', anchor='n')   
    
def redrawAll(app, canvas):
        drawFloorPlan(app, canvas)
        drawLocationPoint(app, canvas)

def runViewer():
    runApp(width = 1000, height = 800)

runViewer()