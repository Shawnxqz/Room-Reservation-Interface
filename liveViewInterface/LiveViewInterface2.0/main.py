#################################################
# Porter Hall Live View Interface
#################################################

import math, random
import pandas as pd
from PIL import ImageTk, Image
import pygame
from cmu_112_graphics import * 
import numpy as np
import pandas as pd

#################################################
# Draw Initial Components
#################################################
# Import data 
df = pd.read_csv('roomInfo.csv')
print(df)

def appStarted(app):
    app.height = 800
    app.width = 1000
    # background
    app.image1 = app.loadImage('floor1.png')
    app.image2 = app.scaleImage(app.image1, 0.8)
    # cmu logo
    app.image3 = app.loadImage('cmu.png')
    app.image4 = app.scaleImage(app.image3, 0.04)
    # Availability
    app.unavailColor = 'red4'
    app.availColor = 'goldenrod1'
    # Energy Use
    app.highColor = 'snow3'
    app.mediumaColor = 'SteelBlue1'
    app.lowColor = 'green4'
    app.r = 8

    # canvas.create_polygon(rightBowTopX, rightBowTopY, cx, cy, \
    #                 rightBowBottomX, rightBowBottomY, \
    #                 fill = app.bowColor, outline = 'DarkOrchid4', width = 3)
 
#################################################
# Room Num
#################################################

def drawRoomNum(app, canvas, x, y, num):
    canvas.create_text(x, y + 10, text = num, font = 'Times 15', \
        fill = 'white', anchor='n')
  
#################################################
# Energy Use
#################################################

def drawEnergy(app, canvas, x0, y0, roomEnergy):
    if roomEnergy == 'H':
        canvas.create_oval(x0 - app.r, y0 - app.r, x0 + app.r, y0 + app.r, 
            fill = app.highColor, outline = app.highColor)
    elif roomEnergy == 'M':
        canvas.create_oval(x0 - app.r, y0 - app.r, x0 + app.r, y0 + app.r, 
            fill = app.mediumaColor, outline = app.mediumaColor)
    elif roomEnergy == 'L':
        canvas.create_oval(x0 - app.r, y0 - app.r, x0 + app.r, y0 + app.r, 
            fill = app.lowColor, outline = app.lowColor)

#################################################
# People Num
#################################################

def drawPeopleNum(app, canvas, x, y, num):
    canvas.create_text(x, y, text = num, font = 'Times 25', \
                fill = 'white', anchor='n')    
                        
#################################################
# Availability
#################################################

def drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY):
    if roomAvail == 'N':
        canvas.create_rectangle(leftUpperX, leftUpperY, rightBottomX, \
            rightBottomY, fill = app.unavailColor, outline = 'black', width = 3)
    elif roomAvail == 'Y':
        canvas.create_rectangle(leftUpperX, leftUpperY, rightBottomX, \
            rightBottomY, fill = app.availColor, outline = 'black', width = 3)

#################################################
# Draw Each Room in PH
#################################################
# 107E
def draw107E(app, canvas):
    roomNum = df.iat[1,0]
    roomEnergy = df.iat[1,1]
    num107E = df.iat[1,2]
    roomAvail = df.iat[1,3]
    leftUpperX = app.width * 0.075
    leftUpperY = app.height * 0.7
    rightBottomX = leftUpperX + 160
    rightBottomY = leftUpperY + 130
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX, textY, num107E)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 30, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 25, leftUpperY + 10, roomNum)

# 100
def draw100(app, canvas):
    roomNum = df.iat[2,0]
    roomEnergy = df.iat[2,1]
    num100 = df.iat[2,2]
    roomAvail = df.iat[2,3]
    leftUpperX = app.width * 0.64
    leftUpperY = app.height * 0.7
    rightBottomX = leftUpperX + 160
    rightBottomY = leftUpperY + 130
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX, textY, num100)
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 30, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 25, leftUpperY + 10, roomNum) 

# 125C
def draw125C(app, canvas):
    roomNum = df.iat[1,0]
    roomEnergy = df.iat[1,1]
    num125C = df.iat[0,2]
    roomAvail = df.iat[1,3]
    leftUpperX = app.width * 0.68
    leftUpperY = app.height * 0.4
    rightBottomX = leftUpperX + 115
    rightBottomY = leftUpperY + 70
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    roomAvail = df.iat[0,3]
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX, textY, num125C)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 30, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 25, leftUpperY + 10, roomNum) 

# 121
def draw121(app, canvas):
    roomNum = df.iat[3,0]
    roomEnergy = df.iat[3,1]
    num121 = df.iat[3,2]
    roomAvail = df.iat[3,3]
    leftUpperX = app.width * 0.44
    leftUpperY = app.height * 0.4 + 26
    rightBottomX = leftUpperX + 80
    rightBottomY = app.height * 0.4 + 70
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX, textY, num121)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 30, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 20, leftUpperY + 5, roomNum)

#################################################
# Draw Background and Other Components 
#################################################

def drawFloorPlan(app, canvas):
    canvas.create_image(app.width * 0.45, app.height * 0.6, \
    image = ImageTk.PhotoImage(app.image2))

def drawCMU(app, canvas):
    canvas.create_image(app.width * 0.075, app.height * 0.08, \
    image = ImageTk.PhotoImage(app.image4))

def drawLocationPoint(app, canvas):
    canvas.create_text(app.width * 0.5, app.height * 0.08, \
            text = 'Real-time View of Rooms on the 1st Floor of Porter Hall', \
            font = 'Times 30 bold', fill = 'black', anchor='n')   

def drawEnergyLegend(app, canvas):
    # title
    canvas.create_text(app.width * 0.9, app.height * 0.9 - 25, \
            text = 'Energy Efficiency', \
            font = 'Times 15 bold', fill = 'black', anchor='n')   
    X1 = app.width * 0.9
    X2 = X1 + 50
    Y1 = app.height * 0.9
    Y2 = Y1 + 20
    Y3 = Y2 + 20
    Y4 = Y3 + 20
    # high
    canvas.create_rectangle(X1, Y1, X2, Y2, fill = 'green4')
    canvas.create_text(X1 - 20, Y1, text = 'High',
            font = 'Times 10 bold', fill = 'black', anchor='n')   
    # medium
    canvas.create_rectangle(X1, Y2, X2, Y3, fill = 'SteelBlue1')
    canvas.create_text(X1 - 20, Y2, text = 'Medium',
            font = 'Times 10 bold', fill = 'black', anchor='n')   
    # low
    canvas.create_rectangle(X1, Y3, X2, Y4, fill = 'snow3') 
    canvas.create_text(X1 - 20, Y3, text = 'Low',
            font = 'Times 10 bold', fill = 'black', anchor='n')   

def drawAvailLegend(app, canvas):
    # title
    canvas.create_text(app.width * 0.9, app.height * 0.8 - 25, \
            text = 'Availability', \
            font = 'Times 15 bold', fill = 'black', anchor='n')   
    X1 = app.width * 0.9
    X2 = X1 + 50
    Y1 = app.height * 0.8
    Y2 = Y1 + 20
    Y3 = Y2 + 20
    Y4 = Y3 + 20
    # avail
    canvas.create_rectangle(X1, Y1, X2, Y2, fill = app.availColor)
    canvas.create_text(X1 - 38, Y1, text = 'Availability',
            font = 'Times 10 bold', fill = 'black', anchor='n')   
    # unavail
    canvas.create_rectangle(X1, Y2, X2, Y3, fill = app.unavailColor)
    canvas.create_text(X1 - 38, Y2, text = 'Unavailability',
            font = 'Times 10 bold', fill = 'black', anchor='n')   # title
    canvas.create_text(app.width * 0.9, app.height * 0.9 - 25, \
            text = 'Energy Efficiency', \
            font = 'Times 15 bold', fill = 'black', anchor='n')   

#################################################
# Run the Interface
#################################################
   
def redrawAll(app, canvas):
        drawCMU(app, canvas)
        drawFloorPlan(app, canvas)
        draw107E(app, canvas)
        draw100(app, canvas)
        draw125C(app, canvas)
        draw121(app, canvas)
        drawLocationPoint(app, canvas)
        drawEnergyLegend(app, canvas)
        drawAvailLegend(app, canvas)

def runViewer():
    runApp(width = 1000, height = 800)

runViewer()