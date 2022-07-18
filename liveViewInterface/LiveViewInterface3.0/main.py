#################################################
# Porter Hall Live View Interface
#################################################

import math, random
import pandas as pd
from PIL import ImageTk, Image
from cmu_112_graphics import * 
import numpy as np
import pandas as pd

#################################################
# Draw Initial Components
#################################################
# Import data 
df = pd.read_csv('roomInfo.csv')

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
    app.r = 4

    # canvas.create_polygon(rightBowTopX, rightBowTopY, cx, cy, \
    #                 rightBowBottomX, rightBowBottomY, \
    #                 fill = app.bowColor, outline = 'DarkOrchid4', width = 3)
 
#################################################
# Room Num
#################################################

def drawRoomNum(app, canvas, x, y, num):
    canvas.create_text(x, y + 10, text = num, font = 'Times 10', \
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
    canvas.create_text(x, y, text = num, font = 'Times 12', \
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
    num = df.iat[1,2]
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
    drawPeopleNum(app, canvas, textX, textY, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 30, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 25, leftUpperY + 10, roomNum)

# 100
def draw100(app, canvas):
    roomNum = df.iat[2,0]
    roomEnergy = df.iat[2,1]
    num = df.iat[2,2]
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
    drawPeopleNum(app, canvas, textX, textY, num)
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 30, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 25, leftUpperY + 10, roomNum) 

# 125C
def draw125C(app, canvas):
    roomNum = df.iat[0,0]
    roomEnergy = df.iat[0,1]
    num = df.iat[0,2]
    roomAvail = df.iat[0,3]
    leftUpperX = app.width * 0.68
    leftUpperY = app.height * 0.4
    rightBottomX = leftUpperX + 115
    rightBottomY = leftUpperY + 70
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX, textY, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 30, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 25, leftUpperY, roomNum) 

# 121
def draw121(app, canvas):
    roomNum = df.iat[3,0]
    roomEnergy = df.iat[3,1]
    num = df.iat[3,2]
    roomAvail = df.iat[3,3]
    leftUpperX = app.width * 0.44
    leftUpperY = app.height * 0.2 + 188
    rightBottomX = leftUpperX + 80
    rightBottomY = app.height * 0.4 + 70
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX, textY, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 30, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 20, leftUpperY + 5, roomNum)

# 123E
def draw123E(app, canvas):
    roomNum = df.iat[4,0]
    roomEnergy = df.iat[4,1]
    num = df.iat[4,2]
    roomAvail = df.iat[4,3]
    leftUpperX = app.width * 0.4 + 65
    leftUpperY = app.height * 0.2
    # rightBottomX = app.width * 0.44+ 80
    rightBottomX = leftUpperX + 40
    rightBottomY = app.height * 0.2 + 45
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX, textY, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 12, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 18, leftUpperY - 5, roomNum)

# 123F
def draw123F(app, canvas):
    roomNum = df.iat[5,0]
    roomEnergy = df.iat[5,1]
    num = df.iat[5,2]
    roomAvail = df.iat[5,3]
    leftUpperX = app.width * 0.4 + 105
    leftUpperY = app.height * 0.2
    rightBottomX = leftUpperX + 50
    rightBottomY = app.height * 0.2 + 35
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX, textY, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 12, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 18, leftUpperY - 5, roomNum)

# 123G
def draw123G(app, canvas):
    roomNum = df.iat[6,0]
    roomEnergy = df.iat[6,1]
    num = df.iat[6,2]
    roomAvail = df.iat[6,3]
    leftUpperX = app.width * 0.4 + 155
    leftUpperY = app.height * 0.2
    rightBottomX = leftUpperX + 40
    rightBottomY = app.height * 0.2 + 45
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX, textY, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 12, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 18, leftUpperY - 5, roomNum)

# 123H
def draw123H(app, canvas):
    roomNum = df.iat[7,0]
    roomEnergy = df.iat[7,1]
    num = df.iat[7,2]
    roomAvail = df.iat[7,3]
    leftUpperX = app.width * 0.4 + 140
    leftUpperY = app.height * 0.2 + 45
    rightBottomX = app.width * 0.4 + 195
    rightBottomY = app.height * 0.2 + 83
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX, textY, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 12, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 18, leftUpperY - 5, roomNum)

# 123J
def draw123J(app, canvas):
    roomNum = df.iat[8,0]
    roomEnergy = df.iat[8,1]
    num = df.iat[8,2]
    roomAvail = df.iat[8,3]
    leftUpperX = app.width * 0.4 + 140
    leftUpperY = app.height * 0.2 + 83
    rightBottomX = app.width * 0.4 + 195
    rightBottomY = app.height * 0.2 + 121
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX, textY, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 12, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 18, leftUpperY - 5, roomNum)

# 123K
def draw123K(app, canvas):
    roomNum = df.iat[9,0]
    roomEnergy = df.iat[9,1]
    num = df.iat[9,2]
    roomAvail = df.iat[9,3]
    leftUpperX = app.width * 0.4 + 140
    leftUpperY = app.height * 0.2 + 121
    rightBottomX = app.width * 0.4 + 195
    rightBottomY = app.height * 0.2 + 159
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX, textY, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 12, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 18, leftUpperY - 5, roomNum)

# 123L
def draw123L(app, canvas):
    roomNum = df.iat[10,0]
    roomEnergy = df.iat[10,1]
    num = df.iat[10,2]
    roomAvail = df.iat[10,3]
    leftUpperX = app.width * 0.4 + 140
    leftUpperY = app.height * 0.2 + 159
    rightBottomX = app.width * 0.4 + 195
    rightBottomY = app.height * 0.2 + 192
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX, textY, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 12, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 18, leftUpperY - 7, roomNum)

# 123D
def draw123D(app, canvas):
    roomNum = df.iat[11,0]
    roomEnergy = df.iat[11,1]
    num = df.iat[11,2]
    roomAvail = df.iat[11,3]
    leftUpperX = app.width * 0.4 + 65
    leftUpperY = app.height * 0.2 + 45
    rightBottomX = app.width * 0.4 + 120
    rightBottomY = app.height * 0.2 + 83
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX, textY, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 12, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 18, leftUpperY - 7, roomNum)

# 123C
def draw123C(app, canvas):
    roomNum = df.iat[12,0]
    roomEnergy = df.iat[12,1]
    num = df.iat[12,2]
    roomAvail = df.iat[12,3]
    leftUpperX = app.width * 0.4 + 65
    leftUpperY = app.height * 0.2 + 83
    rightBottomX = app.width * 0.4 + 120
    rightBottomY = app.height * 0.2 + 121
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX, textY, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 12, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 18, leftUpperY - 7, roomNum)

# 123B
def draw123B(app, canvas):
    roomNum = df.iat[13,0]
    roomEnergy = df.iat[13,1]
    num = df.iat[13,2]
    roomAvail = df.iat[13,3]
    leftUpperX = app.width * 0.4 + 65
    leftUpperY = app.height * 0.2 + 121
    rightBottomX = app.width * 0.4 + 120
    rightBottomY = app.height * 0.2 + 159
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX, textY, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 12, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 18, leftUpperY - 7, roomNum)

# 123A
def draw123A(app, canvas):
    roomNum = df.iat[14,0]
    roomEnergy = df.iat[14,1]
    num = df.iat[14,2]
    roomAvail = df.iat[14,3]
    leftUpperX = app.width * 0.4 + 65
    leftUpperY = app.height * 0.2 + 159
    rightBottomX = app.width * 0.4 + 120
    rightBottomY = app.height * 0.2 + 188
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX, textY, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 12, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 18, leftUpperY - 7, roomNum)

# 125B
def draw125B(app, canvas):
    roomNum = df.iat[15,0]
    roomEnergy = df.iat[15,1]
    num = df.iat[15,2]
    roomAvail = df.iat[15,3]
    leftUpperX = app.width * 0.68 - 58
    leftUpperY = app.height * 0.4
    rightBottomX = app.width * 0.68
    rightBottomY = leftUpperY + 70
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX, textY, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 15, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 25 , leftUpperY, roomNum) 

# 125E
def draw125E(app, canvas):
    roomNum = df.iat[16,0]
    roomEnergy = df.iat[16,1]
    num = df.iat[16,2]
    roomAvail = df.iat[16,3]
    leftUpperX = app.width * 0.68 + 115
    leftUpperY = app.height * 0.4 + 33
    rightBottomX = app.width * 0.68 + 150
    rightBottomY = app.height * 0.4 + 70
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX, textY, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 10, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 20, leftUpperY - 8, roomNum)

# 125A
def draw125A(app, canvas):
    roomNum = df.iat[17,0]
    roomEnergy = df.iat[17,1]
    num = df.iat[17,2]
    roomAvail = df.iat[17,3]
    leftUpperX = app.width * 0.68 - 109
    leftUpperY = app.height * 0.4 + 33
    rightBottomX = app.width * 0.68 - 58
    rightBottomY = app.height * 0.4 + 70
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX, textY, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 10, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 20, leftUpperY - 8, roomNum) 

# 123M
def draw123M(app, canvas):
    roomNum = df.iat[18,0]
    roomEnergy = df.iat[18,1]
    num = df.iat[18,2]
    roomAvail = df.iat[18,3]
    leftUpperX = app.width * 0.68 - 140
    leftUpperY = app.height * 0.4 + 33
    rightBottomX = app.width * 0.68 - 109
    rightBottomY = app.height * 0.4 + 70
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX, textY, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 8, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum) 

# 120
def draw120(app, canvas):
    roomNum = df.iat[19,0]
    roomEnergy = df.iat[19,1]
    num = df.iat[19,2]
    roomAvail = df.iat[19,3]
    leftUpperX = app.width * 0.5 + 20
    leftUpperY = app.height * 0.4 + 33
    rightBottomX = app.width * 0.68 - 140
    rightBottomY = app.height * 0.4 + 56
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 8, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 8, leftUpperY - 8, roomNum) 

# 107D
def draw107D(app, canvas):
    roomNum = df.iat[20,0]
    roomEnergy = df.iat[20,1]
    num = df.iat[20,2]
    roomAvail = df.iat[20,3]
    leftUpperX = app.width * 0.075 + 160
    leftUpperY = app.height * 0.7 + 80
    rightBottomX = app.width * 0.075 + 190
    rightBottomY = app.height * 0.7 + 130
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 8, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum) 

# 107C
def draw107C(app, canvas):
    roomNum = df.iat[21,0]
    roomEnergy = df.iat[21,1]
    num = df.iat[21,2]
    roomAvail = df.iat[21,3]
    leftUpperX = app.width * 0.075 + 190
    leftUpperY = app.height * 0.7 + 80
    rightBottomX = app.width * 0.075 + 260
    rightBottomY = app.height * 0.7 + 130
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 8, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum) 

# 107B
def draw107B(app, canvas):
    roomNum = df.iat[22,0]
    roomEnergy = df.iat[22,1]
    num = df.iat[22,2]
    roomAvail = df.iat[22,3]
    leftUpperX = app.width * 0.075 + 260
    leftUpperY = app.height * 0.7 + 80
    rightBottomX = app.width * 0.075 + 300
    rightBottomY = app.height * 0.7 + 130
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 8, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum) 

# 107A
def draw107A(app, canvas):
    roomNum = df.iat[23,0]
    roomEnergy = df.iat[23,1]
    num = df.iat[23,2]
    roomAvail = df.iat[23,3]
    leftUpperX = app.width * 0.075 + 300
    leftUpperY = app.height * 0.7 + 80
    rightBottomX = app.width * 0.075 + 345
    rightBottomY = app.height * 0.7 + 130
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 8, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum) 

# 103
def draw103(app, canvas):
    roomNum = df.iat[24,0]
    roomEnergy = df.iat[24,1]
    num = df.iat[24,2]
    roomAvail = df.iat[24,3]
    leftUpperX = app.width * 0.075 + 345
    leftUpperY = app.height * 0.7 + 80
    rightBottomX = app.width * 0.075 + 390
    rightBottomY = app.height * 0.7 + 110
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 8, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum) 

# 101
def draw101(app, canvas):
    roomNum = df.iat[25,0]
    roomEnergy = df.iat[25,1]
    num = df.iat[25,2]
    roomAvail = df.iat[25,3]
    leftUpperX = app.width * 0.075 + 390
    leftUpperY = app.height * 0.7 + 80
    rightBottomX = app.width * 0.075 + 435
    rightBottomY = app.height * 0.7 + 120
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 8, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum) 

# 100A
def draw100A(app, canvas):
    roomNum = df.iat[26,0]
    roomEnergy = df.iat[26,1]
    num = df.iat[26,2]
    roomAvail = df.iat[26,3]
    leftUpperX = app.width * 0.075 + 470
    leftUpperY = app.height * 0.7 + 80
    rightBottomX = app.width * 0.075 + 515
    rightBottomY = app.height * 0.7 + 120
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 8, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum) 

# 100B
def draw100B(app, canvas):
    roomNum = df.iat[27,0]
    roomEnergy = df.iat[27,1]
    num = df.iat[27,2]
    roomAvail = df.iat[27,3]
    leftUpperX = app.width * 0.075 + 515
    leftUpperY = app.height * 0.7 + 80
    rightBottomX = app.width * 0.075 + 565
    rightBottomY = app.height * 0.7 + 105
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum) 

# 111
def draw111(app, canvas):
    roomNum = df.iat[28,0]
    roomEnergy = df.iat[28,1]
    num = df.iat[28,2]
    roomAvail = df.iat[28,3]
    leftUpperX = app.width * 0.075 + 390
    leftUpperY = app.height * 0.7 + 5
    rightBottomX = app.width * 0.075 + 435
    rightBottomY = app.height * 0.7 + 45
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum) 

# 113
def draw113(app, canvas):
    roomNum = df.iat[29,0]
    roomEnergy = df.iat[29,1]
    num = df.iat[29,2]
    roomAvail = df.iat[29,3]
    leftUpperX = app.width * 0.075 + 390
    leftUpperY = app.height * 0.7 - 30
    rightBottomX = app.width * 0.075 + 435
    rightBottomY = app.height * 0.7 + 5
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 115
def draw115(app, canvas):
    roomNum = df.iat[30,0]
    roomEnergy = df.iat[30,1]
    num = df.iat[30,2]
    roomAvail = df.iat[30,3]
    leftUpperX = app.width * 0.075 + 390
    leftUpperY = app.height * 0.7 - 90
    rightBottomX = app.width * 0.075 + 435
    rightBottomY = app.height * 0.7 - 30
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 117
def draw117(app, canvas):
    roomNum = df.iat[31,0]
    roomEnergy = df.iat[31,1]
    num = df.iat[31,2]
    roomAvail = df.iat[31,3]
    leftUpperX = app.width * 0.075 + 365
    leftUpperY = app.height * 0.7 - 135
    rightBottomX = app.width * 0.075 + 435
    rightBottomY = app.height * 0.7 - 90
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 112
def draw112(app, canvas):
    roomNum = df.iat[32,0]
    roomEnergy = df.iat[32,1]
    num = df.iat[32,2]
    roomAvail = df.iat[32,3]
    leftUpperX = app.width * 0.075 + 470
    leftUpperY = app.height * 0.7 - 5
    rightBottomX = app.width * 0.075 + 520
    rightBottomY = app.height * 0.7 + 45
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 114
def draw114(app, canvas):
    roomNum = df.iat[33,0]
    roomEnergy = df.iat[33,1]
    num = df.iat[33,2]
    roomAvail = df.iat[33,3]
    leftUpperX = app.width * 0.075 + 470
    leftUpperY = app.height * 0.7 - 45
    rightBottomX = app.width * 0.075 + 520
    rightBottomY = app.height * 0.7 - 5
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 116
def draw116(app, canvas):
    roomNum = df.iat[34,0]
    roomEnergy = df.iat[34,1]
    num = df.iat[34,2]
    roomAvail = df.iat[34,3]
    leftUpperX = app.width * 0.075 + 470
    leftUpperY = app.height * 0.7 - 90
    rightBottomX = app.width * 0.075 + 520
    rightBottomY = app.height * 0.7 - 45
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 110B
def draw110B(app, canvas):
    roomNum = df.iat[35,0]
    roomEnergy = df.iat[35,1]
    num = df.iat[35,2]
    roomAvail = df.iat[35,3]
    leftUpperX = app.width * 0.075 + 470
    leftUpperY = app.height * 0.7 - 135
    rightBottomX = app.width * 0.075 + 550
    rightBottomY = app.height * 0.7 - 90
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 126A
def draw126A(app, canvas):
    roomNum = df.iat[36,0]
    roomEnergy = df.iat[36,1]
    num = df.iat[36,2]
    roomAvail = df.iat[36,3]
    leftUpperX = app.width * 0.075 + 550
    leftUpperY = app.height * 0.7 - 135
    rightBottomX = app.width * 0.075 + 605
    rightBottomY = app.height * 0.7 - 65
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 126B
def draw126B(app, canvas):
    roomNum = df.iat[37,0]
    roomEnergy = df.iat[37,1]
    num = df.iat[37,2]
    roomAvail = df.iat[37,3]
    leftUpperX = app.width * 0.075 + 605
    leftUpperY = app.height * 0.7 - 135
    rightBottomX = app.width * 0.075 + 660
    rightBottomY = app.height * 0.7 - 65
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 126C
def draw126C(app, canvas):
    roomNum = df.iat[38,0]
    roomEnergy = df.iat[38,1]
    num = df.iat[38,2]
    roomAvail = df.iat[38,3]
    leftUpperX = app.width * 0.075 + 660
    leftUpperY = app.height * 0.7 - 135
    rightBottomX = app.width * 0.075 + 720
    rightBottomY = app.height * 0.7 - 65
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 126D
def draw126D(app, canvas):
    roomNum = df.iat[39,0]
    roomEnergy = df.iat[39,1]
    num = df.iat[39,2]
    roomAvail = df.iat[39,3]
    leftUpperX = app.width * 0.075 + 720
    leftUpperY = app.height * 0.7 - 135
    rightBottomX = app.width * 0.075 + 760
    rightBottomY = app.height * 0.7 - 87
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 119D
def draw119D(app, canvas):
    roomNum = df.iat[40,0]
    roomEnergy = df.iat[40,1]
    num = df.iat[40,2]
    roomAvail = df.iat[40,3]
    leftUpperX = app.width * 0.3 - 20
    leftUpperY = app.height * 0.2 + 188
    rightBottomX = app.width * 0.3 + 20
    rightBottomY = app.height * 0.2 + 260
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 119
def draw119(app, canvas):
    roomNum = df.iat[41,0]
    roomEnergy = df.iat[41,1]
    num = df.iat[41,2]
    roomAvail = df.iat[41,3]
    leftUpperX = app.width * 0.3 + 20
    leftUpperY = app.height * 0.2 + 188
    rightBottomX = app.width * 0.3 + 100
    rightBottomY = app.height * 0.2 + 260
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 175
def draw175(app, canvas):
    roomNum = df.iat[42,0]
    roomEnergy = df.iat[42,1]
    num = df.iat[42,2]
    roomAvail = df.iat[42,3]
    leftUpperX = app.width * 0.3 + 100
    leftUpperY = app.height * 0.4 + 45
    rightBottomX = app.width * 0.44
    rightBottomY = app.height * 0.4 + 70
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 5, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 10, roomNum)

# 119C
def draw119C(app, canvas):
    roomNum = df.iat[43,0]
    roomEnergy = df.iat[43,1]
    num = df.iat[43,2]
    roomAvail = df.iat[43,3]
    leftUpperX = app.width * 0.3 - 20
    leftUpperY = app.height * 0.2 + 260
    rightBottomX = app.width * 0.3 + 20
    rightBottomY = app.height * 0.2 + 310
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 119B
def draw119B(app, canvas):
    roomNum = df.iat[44,0]
    roomEnergy = df.iat[44,1]
    num = df.iat[44,2]
    roomAvail = df.iat[44,3]
    leftUpperX = app.width * 0.3 + 20
    leftUpperY = app.height * 0.2 + 260
    rightBottomX = app.width * 0.3 + 60
    rightBottomY = app.height * 0.2 + 310
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 119A
def draw119A(app, canvas):
    roomNum = df.iat[45,0]
    roomEnergy = df.iat[45,1]
    num = df.iat[45,2]
    roomAvail = df.iat[45,3]
    leftUpperX = app.width * 0.3 + 60
    leftUpperY = app.height * 0.2 + 260
    rightBottomX = app.width * 0.3 + 100
    rightBottomY = app.height * 0.2 + 310
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 172C
def draw172C(app, canvas):
    roomNum = df.iat[46,0]
    roomEnergy = df.iat[46,1]
    num = df.iat[46,2]
    roomAvail = df.iat[46,3]
    leftUpperX = app.width * 0.075 + 48
    leftUpperY = app.height * 0.7 - 88
    rightBottomX = app.width * 0.075 + 75
    rightBottomY = app.height * 0.7 - 50
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 118J
def draw118J(app, canvas):
    roomNum = df.iat[47,0]
    roomEnergy = df.iat[47,1]
    num = df.iat[47,2]
    roomAvail = df.iat[47,3]
    leftUpperX = app.width * 0.075 + 75
    leftUpperY = app.height * 0.7 - 88
    rightBottomX = app.width * 0.075 + 100
    rightBottomY = app.height * 0.7 - 50
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 118K
def draw118K(app, canvas):
    roomNum = df.iat[48,0]
    roomEnergy = df.iat[48,1]
    num = df.iat[48,2]
    roomAvail = df.iat[48,3]
    leftUpperX = app.width * 0.075 + 100
    leftUpperY = app.height * 0.7 - 88
    rightBottomX = app.width * 0.075 + 125
    rightBottomY = app.height * 0.7 - 50
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 118L
def draw118L(app, canvas):
    roomNum = df.iat[49,0]
    roomEnergy = df.iat[49,1]
    num = df.iat[49,2]
    roomAvail = df.iat[49,3]
    leftUpperX = app.width * 0.075 + 125
    leftUpperY = app.height * 0.7 - 88
    rightBottomX = app.width * 0.075 + 150
    rightBottomY = app.height * 0.7 - 50
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 118M
def draw118M(app, canvas):
    roomNum = df.iat[50,0]
    roomEnergy = df.iat[50,1]
    num = df.iat[50,2]
    roomAvail = df.iat[50,3]
    leftUpperX = app.width * 0.075 + 150
    leftUpperY = app.height * 0.7 - 88
    rightBottomX = app.width * 0.075 + 175
    rightBottomY = app.height * 0.7 - 50
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 118N
def draw118N(app, canvas):
    roomNum = df.iat[51,0]
    roomEnergy = df.iat[51,1]
    num = df.iat[51,2]
    roomAvail = df.iat[51,3]
    leftUpperX = app.width * 0.075 + 175
    leftUpperY = app.height * 0.7 - 88
    rightBottomX = app.width * 0.075 + 215
    rightBottomY = app.height * 0.7 - 50
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 118P
def draw118P(app, canvas):
    roomNum = df.iat[52,0]
    roomEnergy = df.iat[52,1]
    num = df.iat[52,2]
    roomAvail = df.iat[52,3]
    leftUpperX = app.width * 0.075 + 215
    leftUpperY = app.height * 0.7 - 88
    rightBottomX = app.width * 0.075 + 240
    rightBottomY = app.height * 0.7 - 50
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 12, leftUpperY - 8, roomNum)

# 118Q
def draw118Q(app, canvas):
    roomNum = df.iat[53,0]
    roomEnergy = df.iat[53,1]
    num = df.iat[53,2]
    roomAvail = df.iat[53,3]
    leftUpperX = app.width * 0.075 + 240
    leftUpperY = app.height * 0.7 - 88
    rightBottomX = app.width * 0.075 + 275
    rightBottomY = app.height * 0.7 - 50
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 12, leftUpperY - 8, roomNum)

# 118A
def draw118A(app, canvas):
    roomNum = df.iat[54,0]
    roomEnergy = df.iat[54,1]
    num = df.iat[54,2]
    roomAvail = df.iat[54,3]
    leftUpperX = app.width * 0.075 + 275
    leftUpperY = app.height * 0.7 - 88
    rightBottomX = app.width * 0.075 + 325
    rightBottomY = app.height * 0.7
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 118R
def draw118R(app, canvas):
    roomNum = df.iat[55,0]
    roomEnergy = df.iat[55,1]
    num = df.iat[55,2]
    roomAvail = df.iat[55,3]
    leftUpperX = app.width * 0.075 + 325
    leftUpperY = app.height * 0.5 + 25
    rightBottomX = app.width * 0.075 + 365
    rightBottomY = app.height * 0.5 + 90
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 118H
def draw118H(app, canvas):
    roomNum = df.iat[56,0]
    roomEnergy = df.iat[56,1]
    num = df.iat[56,2]
    roomAvail = df.iat[56,3]
    leftUpperX = app.width * 0.075 + 48
    leftUpperY = app.height * 0.7 - 40
    rightBottomX = app.width * 0.075 + 85
    rightBottomY = app.height * 0.7 
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 118G
def draw118G(app, canvas):
    roomNum = df.iat[57,0]
    roomEnergy = df.iat[57,1]
    num = df.iat[57,2]
    roomAvail = df.iat[57,3]
    leftUpperX = app.width * 0.075 + 85
    leftUpperY = app.height * 0.7 - 40
    rightBottomX = app.width * 0.075 + 120
    rightBottomY = app.height * 0.7 
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 118E
def draw118E(app, canvas):
    roomNum = df.iat[58,0]
    roomEnergy = df.iat[58,1]
    num = df.iat[58,2]
    roomAvail = df.iat[58,3]
    leftUpperX = app.width * 0.075 + 120
    leftUpperY = app.height * 0.7 - 40
    rightBottomX = app.width * 0.075 + 175
    rightBottomY = app.height * 0.7 
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 118D
def draw118D(app, canvas):
    roomNum = df.iat[59,0]
    roomEnergy = df.iat[59,1]
    num = df.iat[59,2]
    roomAvail = df.iat[59,3]
    leftUpperX = app.width * 0.075 + 175
    leftUpperY = app.height * 0.7 - 40
    rightBottomX = app.width * 0.075 + 205
    rightBottomY = app.height * 0.7 
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 118B
def draw118B(app, canvas):
    roomNum = df.iat[60,0]
    roomEnergy = df.iat[60,1]
    num = df.iat[60,2]
    roomAvail = df.iat[60,3]
    leftUpperX = app.width * 0.075 + 205
    leftUpperY = app.height * 0.7 - 40
    rightBottomX = app.width * 0.075 + 275
    rightBottomY = app.height * 0.7 
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 107H
def draw107H(app, canvas):
    roomNum = df.iat[61,0]
    roomEnergy = df.iat[61,1]
    num = df.iat[61,2]
    roomAvail = df.iat[61,3]
    leftUpperX = app.width * 0.075 + 190
    leftUpperY = app.height * 0.7 
    rightBottomX = app.width * 0.075 + 342
    rightBottomY = app.height * 0.7 + 53
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# 107
def draw107(app, canvas):
    roomNum = df.iat[62,0]
    roomEnergy = df.iat[62,1]
    num = df.iat[62,2]
    roomAvail = df.iat[62,3]
    leftUpperX = app.width * 0.075 + 160
    leftUpperY = app.height * 0.7 
    rightBottomX = app.width * 0.075 + 190
    rightBottomY = app.height * 0.7 + 45
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX - 5, textY + 12, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

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
        draw123E(app, canvas)
        draw123F(app, canvas)
        draw123G(app, canvas)
        draw123H(app, canvas)
        draw123J(app, canvas)
        draw123K(app, canvas)
        draw123L(app, canvas)
        draw123D(app, canvas)
        draw123C(app, canvas)
        draw123B(app, canvas)
        draw123A(app, canvas)
        draw125B(app, canvas)
        draw125E(app, canvas)
        draw125A(app, canvas)
        draw123M(app, canvas)
        draw120(app, canvas)
        draw107D(app, canvas)
        draw107C(app, canvas)
        draw107B(app, canvas)
        draw107A(app, canvas)
        draw103(app, canvas)
        draw101(app, canvas)
        draw100A(app, canvas)
        draw100B(app, canvas)
        draw111(app, canvas)
        draw113(app, canvas)
        draw115(app, canvas)
        draw117(app, canvas)
        draw112(app, canvas)
        draw114(app, canvas)
        draw116(app, canvas)
        draw110B(app, canvas)
        draw126A(app, canvas)
        draw126B(app, canvas)
        draw126C(app, canvas)
        draw126D(app, canvas)
        draw119D(app, canvas)
        draw119(app, canvas)
        draw175(app, canvas)
        draw119C(app, canvas)
        draw119B(app, canvas)
        draw119A(app, canvas)
        draw172C(app, canvas)
        draw118J(app, canvas)
        draw118K(app, canvas)
        draw118L(app, canvas)
        draw118M(app, canvas)
        draw118N(app, canvas)
        draw118P(app, canvas)
        draw118Q(app, canvas)
        draw118A(app, canvas)
        draw118R(app, canvas)
        draw118H(app, canvas)
        draw118G(app, canvas)
        draw118E(app, canvas)
        draw118D(app, canvas)
        draw118B(app, canvas)
        draw107H(app, canvas)
        draw107(app, canvas)
        drawLocationPoint(app, canvas)
        drawEnergyLegend(app, canvas)
        drawAvailLegend(app, canvas)

def runViewer():
    runApp(width = 1000, height = 800)

runViewer()