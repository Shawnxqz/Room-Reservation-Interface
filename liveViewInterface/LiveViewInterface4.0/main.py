#################################################
# Porter Hall Live View Interface
#################################################

import pandas as pd
from PIL import ImageTk
from cmu_112_graphics import * 
import pandas as pd

#################################################
# Draw Initial Components
#################################################
# Import data 
df = pd.read_csv('roomInfo.csv')

def appStarted(app):
    app.height = 800
    app.width = 1500
    # background
    app.image1 = app.loadImage('floor.png')
    app.image2 = app.scaleImage(app.image1, 0.5)
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

#################################################
# Room Num
#################################################

def drawRoomNum(app, canvas, x, y, num):
    canvas.create_text(x, y + 10, text = num, font = 'Times 8', \
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

#################################################
# Floor 1
#################################################
# 107E
def draw107E(app, canvas):
    roomNum = df.iat[1,0]
    roomEnergy = df.iat[1,1]
    num = df.iat[1,2]
    roomAvail = df.iat[1,3]
    leftUpperX = app.width * 0.01
    leftUpperY = app.height * 0.735
    rightBottomX = leftUpperX + 133
    rightBottomY = leftUpperY + 115
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
    leftUpperX = app.width * 0.01 + 490
    leftUpperY = app.height * 0.735 
    rightBottomX = app.width * 0.01 + 632
    rightBottomY = app.height * 0.735 + 115
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
    leftUpperX = app.width * 0.01 + 525
    leftUpperY = app.height * 0.735 - 207
    rightBottomX = app.width * 0.01 + 625
    rightBottomY = app.height * 0.735 - 145
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
    leftUpperX = app.width * 0.01 + 315
    leftUpperY = app.height * 0.735 - 182
    rightBottomX = app.width * 0.01 + 384
    rightBottomY = app.height * 0.735 - 145
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX, textY, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 10, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 10, leftUpperY - 5, roomNum)

# 123E
def draw123E(app, canvas):
    roomNum = df.iat[4,0]
    roomEnergy = df.iat[4,1]
    num = df.iat[4,2]
    roomAvail = df.iat[4,3]
    leftUpperX = app.width * 0.01 + 338
    leftUpperY = app.height * 0.735 - 346
    rightBottomX = app.width * 0.01 + 373
    rightBottomY = app.height * 0.735 - 305
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX, textY, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 10, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 18, leftUpperY - 5, roomNum)

# 123F
def draw123F(app, canvas):
    roomNum = df.iat[5,0]
    roomEnergy = df.iat[5,1]
    num = df.iat[5,2]
    roomAvail = df.iat[5,3]
    leftUpperX = app.width * 0.01 + 373
    leftUpperY = app.height * 0.735 - 346
    rightBottomX = app.width * 0.01 + 413
    rightBottomY = app.height * 0.735 - 315
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num
    drawPeopleNum(app, canvas, textX, textY, num)
    # Energy Efficiency 
    drawEnergy(app, canvas, textX + 12, textY + 10, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 18, leftUpperY - 5, roomNum)

# 123G
def draw123G(app, canvas):
    roomNum = df.iat[6,0]
    roomEnergy = df.iat[6,1]
    num = df.iat[6,2]
    roomAvail = df.iat[6,3]
    leftUpperX = app.width * 0.01 + 413
    leftUpperY = app.height * 0.735 - 346
    rightBottomX = app.width * 0.01 + 450
    rightBottomY = app.height * 0.735 - 305
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
    leftUpperX = app.width * 0.01 + 405
    leftUpperY = app.height * 0.735 - 305
    rightBottomX = app.width * 0.01 + 450
    rightBottomY = app.height * 0.735 - 275
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

# 123J
def draw123J(app, canvas):
    roomNum = df.iat[8,0]
    roomEnergy = df.iat[8,1]
    num = df.iat[8,2]
    roomAvail = df.iat[8,3]
    leftUpperX = app.width * 0.01 + 405
    leftUpperY = app.height * 0.735 - 275
    rightBottomX = app.width * 0.01 + 450
    rightBottomY = app.height * 0.735 - 245
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

# 123K
def draw123K(app, canvas):
    roomNum = df.iat[9,0]
    roomEnergy = df.iat[9,1]
    num = df.iat[9,2]
    roomAvail = df.iat[9,3]
    leftUpperX = app.width * 0.01 + 405
    leftUpperY = app.height * 0.735 - 245
    rightBottomX = app.width * 0.01 + 450
    rightBottomY = app.height * 0.735 - 215
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

# 123L
def draw123L(app, canvas):
    roomNum = df.iat[10,0]
    roomEnergy = df.iat[10,1]
    num = df.iat[10,2]
    roomAvail = df.iat[10,3]
    leftUpperX = app.width * 0.01 + 405
    leftUpperY = app.height * 0.735 - 215
    rightBottomX = app.width * 0.01 + 450
    rightBottomY = app.height * 0.735 - 182
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
    leftUpperX = app.width * 0.01 + 338
    leftUpperY = app.height * 0.735 - 305
    rightBottomX = app.width * 0.01 + 384
    rightBottomY = app.height * 0.735 - 275
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
    leftUpperX = app.width * 0.01 + 338
    leftUpperY = app.height * 0.735 - 275
    rightBottomX = app.width * 0.01 + 384
    rightBottomY = app.height * 0.735 - 245
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
    leftUpperX = app.width * 0.01 + 338
    leftUpperY = app.height * 0.735 - 245
    rightBottomX = app.width * 0.01 + 384
    rightBottomY = app.height * 0.735 - 215
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
    leftUpperX = app.width * 0.01 + 338
    leftUpperY = app.height * 0.735 - 215
    rightBottomX = app.width * 0.01 + 384
    rightBottomY = app.height * 0.735 - 182
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
    leftUpperX = app.width * 0.01 + 475
    leftUpperY = app.height * 0.735 - 207
    rightBottomX = app.width * 0.01 + 525
    rightBottomY = app.height * 0.735 - 145
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
    leftUpperX = app.width * 0.01 + 625
    leftUpperY = app.height * 0.735 - 180
    rightBottomX = app.width * 0.01 + 658
    rightBottomY = app.height * 0.735 - 145

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
    leftUpperX = app.width * 0.01 + 430
    leftUpperY = app.height * 0.735 - 182
    rightBottomX = app.width * 0.01 + 475
    rightBottomY = app.height * 0.735 - 145
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
    leftUpperX = app.width * 0.01 + 405
    leftUpperY = app.height * 0.735 - 182
    rightBottomX = app.width * 0.01 + 430
    rightBottomY = app.height * 0.735 - 145
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
    leftUpperX = app.width * 0.01 + 384
    leftUpperY = app.height * 0.735 - 182
    rightBottomX = app.width * 0.01 + 405
    rightBottomY = app.height * 0.735 - 160
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

    leftUpperX = app.width * 0.01 + 133
    leftUpperY = app.height * 0.735 + 70
    rightBottomX = app.width * 0.01 + 165
    rightBottomY = app.height * 0.735 + 115
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
    leftUpperX = app.width * 0.01 + 165
    leftUpperY = app.height * 0.735 + 70
    rightBottomX = app.width * 0.01 + 225
    rightBottomY = app.height * 0.735 + 115
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
    leftUpperX = app.width * 0.01 + 225
    leftUpperY = app.height * 0.735 + 70
    rightBottomX = app.width * 0.01 + 260
    rightBottomY = app.height * 0.735 + 115
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
    leftUpperX = app.width * 0.01 + 260
    leftUpperY = app.height * 0.735 + 70
    rightBottomX = app.width * 0.01 + 298
    rightBottomY = app.height * 0.735 + 115
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
    leftUpperX = app.width * 0.01 + 298
    leftUpperY = app.height * 0.735 + 70
    rightBottomX = app.width * 0.01 + 336
    rightBottomY = app.height * 0.735 + 95
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

# 101
def draw101(app, canvas):
    roomNum = df.iat[25,0]
    roomEnergy = df.iat[25,1]
    num = df.iat[25,2]
    roomAvail = df.iat[25,3]
    leftUpperX = app.width * 0.01 + 336
    leftUpperY = app.height * 0.735 + 70
    rightBottomX = app.width * 0.01 + 379
    rightBottomY = app.height * 0.735 + 102
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
    leftUpperX = app.width * 0.01 + 412
    leftUpperY = app.height * 0.735 + 70
    rightBottomX = app.width * 0.01 + 450 
    rightBottomY = app.height * 0.735 + 102
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
    leftUpperX = app.width * 0.01 + 450
    leftUpperY = app.height * 0.735 + 70
    rightBottomX = app.width * 0.01 + 490 
    rightBottomY = app.height * 0.735 + 95
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
    leftUpperX = app.width * 0.01 + 338
    leftUpperY = app.height * 0.735 
    rightBottomX = app.width * 0.01 + 379
    rightBottomY = app.height * 0.735 + 40
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
    leftUpperX = app.width * 0.01 + 338
    leftUpperY = app.height * 0.735 - 30
    rightBottomX = app.width * 0.01 + 379
    rightBottomY = app.height * 0.735 
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
    leftUpperX = app.width * 0.01 + 338
    leftUpperY = app.height * 0.735 - 80
    rightBottomX = app.width * 0.01 + 379
    rightBottomY = app.height * 0.735 - 30
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
    leftUpperX = app.width * 0.01 + 313
    leftUpperY = app.height * 0.735 - 115
    rightBottomX = app.width * 0.01 + 379
    rightBottomY = app.height * 0.735 - 80
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
    leftUpperX = app.width * 0.01 + 409
    leftUpperY = app.height * 0.735 - 3 
    rightBottomX = app.width * 0.01 + 450
    rightBottomY = app.height * 0.735 + 40
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
    leftUpperX = app.width * 0.01 + 409
    leftUpperY = app.height * 0.735 - 40 
    rightBottomX = app.width * 0.01 + 450
    rightBottomY = app.height * 0.735 - 3
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
    leftUpperX = app.width * 0.01 + 409
    leftUpperY = app.height * 0.735 - 80 
    rightBottomX = app.width * 0.01 + 450
    rightBottomY = app.height * 0.735 - 40
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
    leftUpperX = app.width * 0.01 + 409
    leftUpperY = app.height * 0.735 - 115
    rightBottomX = app.width * 0.01 + 475
    rightBottomY = app.height * 0.735 - 80
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
    leftUpperX = app.width * 0.01 + 475
    leftUpperY = app.height * 0.735 - 115
    rightBottomX = app.width * 0.01 + 525  
    rightBottomY = app.height * 0.735 - 55
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
    leftUpperX = app.width * 0.01 + 525
    leftUpperY = app.height * 0.735 - 115
    rightBottomX = app.width * 0.01 + 575  
    rightBottomY = app.height * 0.735 - 55
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
    leftUpperX = app.width * 0.01 + 575
    leftUpperY = app.height * 0.735 - 115
    rightBottomX = app.width * 0.01 + 625  
    rightBottomY = app.height * 0.735 - 55
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
    leftUpperX = app.width * 0.01 + 625
    leftUpperY = app.height * 0.735 - 115
    rightBottomX = app.width * 0.01 + 658  
    rightBottomY = app.height * 0.735 - 75
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
    leftUpperX = app.width * 0.01 + 175
    leftUpperY = app.height * 0.735 - 185
    rightBottomX = app.width * 0.01 + 215
    rightBottomY = app.height * 0.735 - 120
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
    leftUpperX = app.width * 0.01 + 215
    leftUpperY = app.height * 0.735 - 185
    rightBottomX = app.width * 0.01 + 284
    rightBottomY = app.height * 0.735 - 120
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
    leftUpperX = app.width * 0.01 + 284
    leftUpperY = app.height * 0.735 - 167
    rightBottomX = app.width * 0.01 + 315
    rightBottomY = app.height * 0.735 - 145
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
    leftUpperX = app.width * 0.01 + 175
    leftUpperY = app.height * 0.735 - 120
    rightBottomX = app.width * 0.01 + 215
    rightBottomY = app.height * 0.735 - 76
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
    leftUpperX = app.width * 0.01 + 215
    leftUpperY = app.height * 0.735 - 120
    rightBottomX = app.width * 0.01 + 250
    rightBottomY = app.height * 0.735 - 76
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
    leftUpperX = app.width * 0.01 + 250
    leftUpperY = app.height * 0.735 - 120
    rightBottomX = app.width * 0.01 + 284
    rightBottomY = app.height * 0.735 - 76
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
    leftUpperX = app.width * 0.01 + 40
    leftUpperY = app.height * 0.735 - 76
    rightBottomX = app.width * 0.01 + 63
    rightBottomY = app.height * 0.735 - 44
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

# 118J
def draw118J(app, canvas):
    roomNum = df.iat[47,0]
    roomEnergy = df.iat[47,1]
    num = df.iat[47,2]
    roomAvail = df.iat[47,3]
    leftUpperX = app.width * 0.01 + 63
    leftUpperY = app.height * 0.735 - 76
    rightBottomX = app.width * 0.01 + 85
    rightBottomY = app.height * 0.735 - 44
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

# 118K
def draw118K(app, canvas):
    roomNum = df.iat[48,0]
    roomEnergy = df.iat[48,1]
    num = df.iat[48,2]
    roomAvail = df.iat[48,3]
    leftUpperX = app.width * 0.01 + 85
    leftUpperY = app.height * 0.735 - 76
    rightBottomX = app.width * 0.01 + 107
    rightBottomY = app.height * 0.735 - 44
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

# 118L
def draw118L(app, canvas):
    roomNum = df.iat[49,0]
    roomEnergy = df.iat[49,1]
    num = df.iat[49,2]
    roomAvail = df.iat[49,3]
    leftUpperX = app.width * 0.01 + 107
    leftUpperY = app.height * 0.735 - 76
    rightBottomX = app.width * 0.01 + 130
    rightBottomY = app.height * 0.735 - 44
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

# 118M
def draw118M(app, canvas):
    roomNum = df.iat[50,0]
    roomEnergy = df.iat[50,1]
    num = df.iat[50,2]
    roomAvail = df.iat[50,3]
    leftUpperX = app.width * 0.01 + 130
    leftUpperY = app.height * 0.735 - 76
    rightBottomX = app.width * 0.01 + 153
    rightBottomY = app.height * 0.735 - 44
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

# 118N
def draw118N(app, canvas):
    roomNum = df.iat[51,0]
    roomEnergy = df.iat[51,1]
    num = df.iat[51,2]
    roomAvail = df.iat[51,3]
    leftUpperX = app.width * 0.01 + 153
    leftUpperY = app.height * 0.735 - 76
    rightBottomX = app.width * 0.01 + 187
    rightBottomY = app.height * 0.735 - 44
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
    leftUpperX = app.width * 0.01 + 187
    leftUpperY = app.height * 0.735 - 76
    rightBottomX = app.width * 0.01 + 210
    rightBottomY = app.height * 0.735 - 44
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
    leftUpperX = app.width * 0.01 + 210
    leftUpperY = app.height * 0.735 - 76
    rightBottomX = app.width * 0.01 + 237
    rightBottomY = app.height * 0.735 - 44
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
    leftUpperX = app.width * 0.01 + 237
    leftUpperY = app.height * 0.735 - 76
    rightBottomX = app.width * 0.01 + 284
    rightBottomY = app.height * 0.735  
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
    leftUpperX = app.width * 0.01 + 284
    leftUpperY = app.height * 0.735 - 115
    rightBottomX = app.width * 0.01 + 313
    rightBottomY = app.height * 0.735 - 60
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
    leftUpperX = app.width * 0.01 + 40
    leftUpperY = app.height * 0.735 - 33
    rightBottomX = app.width * 0.01 + 72
    rightBottomY = app.height * 0.735
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
    leftUpperX = app.width * 0.01 + 72
    leftUpperY = app.height * 0.735 - 33
    rightBottomX = app.width * 0.01 + 99
    rightBottomY = app.height * 0.735 
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
    leftUpperX = app.width * 0.01 + 99
    leftUpperY = app.height * 0.735 - 33
    rightBottomX = app.width * 0.01 + 150
    rightBottomY = app.height * 0.735 
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
    leftUpperX = app.width * 0.01 + 150
    leftUpperY = app.height * 0.735 - 33
    rightBottomX = app.width * 0.01 + 180
    rightBottomY = app.height * 0.735  
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
    leftUpperX = app.width * 0.01 + 180
    leftUpperY = app.height * 0.735 - 33
    rightBottomX = app.width * 0.01 + 237
    rightBottomY = app.height * 0.735  
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
    leftUpperX = app.width * 0.01 + 163
    leftUpperY = app.height * 0.735 
    rightBottomX = app.width * 0.01 + 298
    rightBottomY = app.height * 0.735 + 46
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
    leftUpperX = app.width * 0.01 + 133
    leftUpperY = app.height * 0.735
    rightBottomX = app.width * 0.01 + 163
    rightBottomY = app.height * 0.735 + 40
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
# Floor A
#################################################
# A7C
def drawA7C(app, canvas):
    roomNum = df.iat[63,0]
    roomEnergy = df.iat[63,1]
    num = df.iat[63,2]
    roomAvail = df.iat[63,3]
    leftUpperX = app.width * 0.01 + 677
    leftUpperY = app.height * 0.735 + 3
    rightBottomX = app.width * 0.01 + 743
    rightBottomY = app.height * 0.735 + 115
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX, textY, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 10, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 25, leftUpperY + 10, roomNum)

# A7BB
def drawA7BB(app, canvas):
    roomNum = df.iat[64,0]
    roomEnergy = df.iat[64,1]
    num = df.iat[64,2]
    roomAvail = df.iat[64,3]
    leftUpperX = app.width * 0.01 + 743
    leftUpperY = app.height * 0.735 + 60
    rightBottomX = app.width * 0.01 + 802
    rightBottomY = app.height * 0.735 + 115
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX, textY, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 10, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A7B
def drawA7B(app, canvas):
    roomNum = df.iat[65,0]
    roomEnergy = df.iat[65,1]
    num = df.iat[65,2]
    roomAvail = df.iat[65,3]
    leftUpperX = app.width * 0.01 + 802
    leftUpperY = app.height * 0.735 + 60
    rightBottomX = app.width * 0.01 + 890
    rightBottomY = app.height * 0.735 + 115
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX, textY, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 10, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A7A
def drawA7A(app, canvas):
    roomNum = df.iat[66,0]
    roomEnergy = df.iat[66,1]
    num = df.iat[66,2]
    roomAvail = df.iat[66,3]
    leftUpperX = app.width * 0.01 + 890
    leftUpperY = app.height * 0.735 + 67
    rightBottomX = app.width * 0.01 + 960
    rightBottomY = app.height * 0.735 + 115
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX, textY, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 10, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A1
def drawA1(app, canvas):
    roomNum = df.iat[67,0]
    roomEnergy = df.iat[67,1]
    num = df.iat[67,2]
    roomAvail = df.iat[67,3]
    leftUpperX = app.width * 0.01 + 960
    leftUpperY = app.height * 0.735 + 67
    rightBottomX = app.width * 0.01 + 1015
    rightBottomY = app.height * 0.735 + 100
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX, textY, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 10, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A7D
def drawA7D(app, canvas):
    roomNum = df.iat[68,0]
    roomEnergy = df.iat[68,1]
    num = df.iat[68,2]
    roomAvail = df.iat[68,3]
    leftUpperX = app.width * 0.01 + 743
    leftUpperY = app.height * 0.735 + 3
    rightBottomX = app.width * 0.01 + 775
    rightBottomY = app.height * 0.735 + 43
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX, textY + 8, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 10, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A7E
def drawA7E(app, canvas):
    roomNum = df.iat[69,0]
    roomEnergy = df.iat[69,1]
    num = df.iat[69,2]
    roomAvail = df.iat[69,3]
    leftUpperX = app.width * 0.01 + 775
    leftUpperY = app.height * 0.735 + 3
    rightBottomX = app.width * 0.01 + 863
    rightBottomY = app.height * 0.735 + 43
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX, textY + 8, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 10, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A7F
def drawA7F(app, canvas):
    roomNum = df.iat[70,0]
    roomEnergy = df.iat[70,1]
    num = df.iat[70,2]
    roomAvail = df.iat[70,3]
    leftUpperX = app.width * 0.01 + 863
    leftUpperY = app.height * 0.735 + 3
    rightBottomX = app.width * 0.01 + 960
    rightBottomY = app.height * 0.735 + 50
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX, textY + 8, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 10, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A18B
def drawA18B(app, canvas):
    roomNum = df.iat[71,0]
    roomEnergy = df.iat[71,1]
    num = df.iat[71,2]
    roomAvail = df.iat[71,3]
    leftUpperX = app.width * 0.01 + 880
    leftUpperY = app.height * 0.735 - 53
    rightBottomX = app.width * 0.01 + 960
    rightBottomY = app.height * 0.735 + 3
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX, textY + 8, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 10, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A18D
def drawA18D(app, canvas):
    roomNum = df.iat[72,0]
    roomEnergy = df.iat[72,1]
    num = df.iat[72,2]
    roomAvail = df.iat[72,3]
    leftUpperX = app.width * 0.01 + 960
    leftUpperY = app.height * 0.735 - 71
    rightBottomX = app.width * 0.01 + 997
    rightBottomY = app.height * 0.735 + 45
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX, textY + 8, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 10, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A11
def drawA11(app, canvas):
    roomNum = df.iat[73,0]
    roomEnergy = df.iat[73,1]
    num = df.iat[73,2]
    roomAvail = df.iat[73,3]
    leftUpperX = app.width * 0.01 + 997
    leftUpperY = app.height * 0.735 - 29
    rightBottomX = app.width * 0.01 + 1036
    rightBottomY = app.height * 0.735 + 45
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX, textY + 8, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 10, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A15
def drawA15(app, canvas):
    roomNum = df.iat[74,0]
    roomEnergy = df.iat[74,1]
    num = df.iat[74,2]
    roomAvail = df.iat[74,3]
    leftUpperX = app.width * 0.01 + 997
    leftUpperY = app.height * 0.735 - 71
    rightBottomX = app.width * 0.01 + 1036
    rightBottomY = app.height * 0.735 - 29
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX, textY + 8, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 10, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A17
def drawA17(app, canvas):
    roomNum = df.iat[75,0]
    roomEnergy = df.iat[75,1]
    num = df.iat[75,2]
    roomAvail = df.iat[75,3]
    leftUpperX = app.width * 0.01 + 974
    leftUpperY = app.height * 0.735 - 106
    rightBottomX = app.width * 0.01 + 1036
    rightBottomY = app.height * 0.735 - 71
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX, textY + 8, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 10, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A44
def drawA44(app, canvas):
    roomNum = df.iat[76,0]
    roomEnergy = df.iat[76,1]
    num = df.iat[76,2]
    roomAvail = df.iat[76,3]
    leftUpperX = app.width * 0.01 + 714
    leftUpperY = app.height * 0.735 - 70
    rightBottomX = app.width * 0.01 + 735
    rightBottomY = app.height * 0.735 - 25
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 5, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 10, leftUpperY - 5, roomNum)

# A18C
def drawA18C(app, canvas):
    roomNum = df.iat[77,0]
    roomEnergy = df.iat[77,1]
    num = df.iat[77,2]
    roomAvail = df.iat[77,3]
    leftUpperX = app.width * 0.01 + 735
    leftUpperY = app.height * 0.735 - 70
    rightBottomX = app.width * 0.01 + 800
    rightBottomY = app.height * 0.735 - 13
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 5, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A18A
def drawA18A(app, canvas):
    roomNum = df.iat[78,0]
    roomEnergy = df.iat[78,1]
    num = df.iat[78,2]
    roomAvail = df.iat[78,3]
    leftUpperX = app.width * 0.01 + 800
    leftUpperY = app.height * 0.735 - 70
    rightBottomX = app.width * 0.01 + 864
    rightBottomY = app.height * 0.735 - 13
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 5, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A19
def drawA19(app, canvas):
    roomNum = df.iat[79,0]
    roomEnergy = df.iat[79,1]
    num = df.iat[79,2]
    roomAvail = df.iat[79,3]
    leftUpperX = app.width * 0.01 + 842
    leftUpperY = app.height * 0.735 - 110
    rightBottomX = app.width * 0.01 + 910
    rightBottomY = app.height * 0.735 - 70
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 5, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A19A
def drawA19A(app, canvas):
    roomNum = df.iat[80,0]
    roomEnergy = df.iat[80,1]
    num = df.iat[80,2]
    roomAvail = df.iat[80,3]
    leftUpperX = app.width * 0.01 + 910
    leftUpperY = app.height * 0.735 - 110
    rightBottomX = app.width * 0.01 + 948
    rightBottomY = app.height * 0.735 - 70
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 5, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A19B
def drawA19B(app, canvas):
    roomNum = df.iat[81,0]
    roomEnergy = df.iat[81,1]
    num = df.iat[81,2]
    roomAvail = df.iat[81,3]
    leftUpperX = app.width * 0.01 + 842
    leftUpperY = app.height * 0.735 - 129
    rightBottomX = app.width * 0.01 + 870
    rightBottomY = app.height * 0.735 - 110
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 5, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 10, roomNum)

# A19C
def drawA19C(app, canvas):
    roomNum = df.iat[82,0]
    roomEnergy = df.iat[82,1]
    num = df.iat[82,2]
    roomAvail = df.iat[82,3]
    leftUpperX = app.width * 0.01 + 842
    leftUpperY = app.height * 0.735 - 172
    rightBottomX = app.width * 0.01 + 896
    rightBottomY = app.height * 0.735 - 129
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 5, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A19D
def drawA19D(app, canvas):
    roomNum = df.iat[83,0]
    roomEnergy = df.iat[83,1]
    num = df.iat[83,2]
    roomAvail = df.iat[83,3]
    leftUpperX = app.width * 0.01 + 896
    leftUpperY = app.height * 0.735 - 172
    rightBottomX = app.width * 0.01 + 950
    rightBottomY = app.height * 0.735 - 129
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 5, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A46
def drawA46(app, canvas):
    roomNum = df.iat[84,0]
    roomEnergy = df.iat[84,1]
    num = df.iat[84,2]
    roomAvail = df.iat[84,3]
    leftUpperX = app.width * 0.01 + 975
    leftUpperY = app.height * 0.735 - 170
    rightBottomX = app.width * 0.01 + 995
    rightBottomY = app.height * 0.735 - 133
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 5, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 10, leftUpperY - 5, roomNum)

# A17C
def drawA17C(app, canvas):
    roomNum = df.iat[85,0]
    roomEnergy = df.iat[85,1]
    num = df.iat[85,2]
    roomAvail = df.iat[85,3]
    leftUpperX = app.width * 0.01 + 995
    leftUpperY = app.height * 0.735 - 170
    rightBottomX = app.width * 0.01 + 1015
    rightBottomY = app.height * 0.735 - 133
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 5, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 10, leftUpperY - 5, roomNum)

# A17B
def drawA17B(app, canvas):
    roomNum = df.iat[86,0]
    roomEnergy = df.iat[86,1]
    num = df.iat[86,2]
    roomAvail = df.iat[86,3]
    leftUpperX = app.width * 0.01 + 1015
    leftUpperY = app.height * 0.735 - 170
    rightBottomX = app.width * 0.01 + 1040
    rightBottomY = app.height * 0.735 - 133
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 5, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A23
def drawA23(app, canvas):
    roomNum = df.iat[87,0]
    roomEnergy = df.iat[87,1]
    num = df.iat[87,2]
    roomAvail = df.iat[87,3]
    leftUpperX = app.width * 0.01 + 995
    leftUpperY = app.height * 0.735 - 225
    rightBottomX = app.width * 0.01 + 1040
    rightBottomY = app.height * 0.735 - 170
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 5, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A21A
def drawA21A(app, canvas):
    roomNum = df.iat[88,0]
    roomEnergy = df.iat[88,1]
    num = df.iat[88,2]
    roomAvail = df.iat[88,3]
    leftUpperX = app.width * 0.01 + 995
    leftUpperY = app.height * 0.735 - 255
    rightBottomX = app.width * 0.01 + 1040
    rightBottomY = app.height * 0.735 - 225
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 5, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A21
def drawA21(app, canvas):
    roomNum = df.iat[89,0]
    roomEnergy = df.iat[89,1]
    num = df.iat[89,2]
    roomAvail = df.iat[89,3]
    leftUpperX = app.width * 0.01 + 995
    leftUpperY = app.height * 0.735 - 325
    rightBottomX = app.width * 0.01 + 1040
    rightBottomY = app.height * 0.735 - 255
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 5, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A20
def drawA20(app, canvas):
    roomNum = df.iat[90,0]
    roomEnergy = df.iat[90,1]
    num = df.iat[90,2]
    roomAvail = df.iat[90,3]
    leftUpperX = app.width * 0.01 + 1060
    leftUpperY = app.height * 0.735 - 325
    rightBottomX = app.width * 0.01 + 1103
    rightBottomY = app.height * 0.735 - 255
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 5, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A20A
def drawA20A(app, canvas):
    roomNum = df.iat[91,0]
    roomEnergy = df.iat[91,1]
    num = df.iat[91,2]
    roomAvail = df.iat[91,3]
    leftUpperX = app.width * 0.01 + 1060
    leftUpperY = app.height * 0.735 - 255
    rightBottomX = app.width * 0.01 + 1103
    rightBottomY = app.height * 0.735 - 225
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 5, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A22
def drawA22(app, canvas):
    roomNum = df.iat[92,0]
    roomEnergy = df.iat[92,1]
    num = df.iat[92,2]
    roomAvail = df.iat[92,3]
    leftUpperX = app.width * 0.01 + 1060
    leftUpperY = app.height * 0.735 - 225
    rightBottomX = app.width * 0.01 + 1103
    rightBottomY = app.height * 0.735 - 170
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 5, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A27
def drawA27(app, canvas):
    roomNum = df.iat[93,0]
    roomEnergy = df.iat[93,1]
    num = df.iat[93,2]
    roomAvail = df.iat[93,3]
    leftUpperX = app.width * 0.01 + 1065
    leftUpperY = app.height * 0.735 - 170
    rightBottomX = app.width * 0.01 + 1125
    rightBottomY = app.height * 0.735 - 133
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 5, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A27B
def drawA27B(app, canvas):
    roomNum = df.iat[94,0]
    roomEnergy = df.iat[94,1]
    num = df.iat[94,2]
    roomAvail = df.iat[94,3]
    leftUpperX = app.width * 0.01 + 1125
    leftUpperY = app.height * 0.735 - 195
    rightBottomX = app.width * 0.01 + 1270
    rightBottomY = app.height * 0.735 - 133
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 5, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A27C
def drawA27C(app, canvas):
    roomNum = df.iat[95,0]
    roomEnergy = df.iat[95,1]
    num = df.iat[95,2]
    roomAvail = df.iat[95,3]
    leftUpperX = app.width * 0.01 + 1270
    leftUpperY = app.height * 0.735 - 170
    rightBottomX = app.width * 0.01 + 1305
    rightBottomY = app.height * 0.735 - 133
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 5, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A27E
def drawA27E(app, canvas):
    roomNum = df.iat[96,0]
    roomEnergy = df.iat[96,1]
    num = df.iat[96,2]
    roomAvail = df.iat[96,3]
    leftUpperX = app.width * 0.01 + 1270
    leftUpperY = app.height * 0.735 - 105
    rightBottomX = app.width * 0.01 + 1305
    rightBottomY = app.height * 0.735 - 67
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 5, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A27F
def drawA27F(app, canvas):
    roomNum = df.iat[97,0]
    roomEnergy = df.iat[97,1]
    num = df.iat[97,2]
    roomAvail = df.iat[97,3]
    leftUpperX = app.width * 0.01 + 1160
    leftUpperY = app.height * 0.735 - 105
    rightBottomX = app.width * 0.01 + 1270
    rightBottomY = app.height * 0.735 - 47
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 5, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 5, roomNum)

# A27H
def drawA27H(app, canvas):
    roomNum = df.iat[98,0]
    roomEnergy = df.iat[98,1]
    num = df.iat[98,2]
    roomAvail = df.iat[98,3]
    leftUpperX = app.width * 0.01 + 1127
    leftUpperY = app.height * 0.735 - 105
    rightBottomX = app.width * 0.01 + 1160
    rightBottomY = app.height * 0.735 - 80
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 8, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# A27G
def drawA27G(app, canvas):
    roomNum = df.iat[99,0]
    roomEnergy = df.iat[99,1]
    num = df.iat[99,2]
    roomAvail = df.iat[99,3]
    leftUpperX = app.width * 0.01 + 1127
    leftUpperY = app.height * 0.735 - 65
    rightBottomX = app.width * 0.01 + 1160
    rightBottomY = app.height * 0.735 - 47
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 8, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# A43
def drawA43(app, canvas):
    roomNum = df.iat[100,0]
    roomEnergy = df.iat[100,1]
    num = df.iat[100,2]
    roomAvail = df.iat[100,3]
    leftUpperX = app.width * 0.01 + 1065
    leftUpperY = app.height * 0.735 - 105
    rightBottomX = app.width * 0.01 + 1127
    rightBottomY = app.height * 0.735 - 71
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 8, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# A14A
def drawA14A(app, canvas):
    roomNum = df.iat[101,0]
    roomEnergy = df.iat[101,1]
    num = df.iat[101,2]
    roomAvail = df.iat[101,3]
    leftUpperX = app.width * 0.01 + 1065
    leftUpperY = app.height * 0.735 - 71
    rightBottomX = app.width * 0.01 + 1105
    rightBottomY = app.height * 0.735 - 32
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 8, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# A12
def drawA12(app, canvas):
    roomNum = df.iat[102,0]
    roomEnergy = df.iat[102,1]
    num = df.iat[102,2]
    roomAvail = df.iat[102,3]
    leftUpperX = app.width * 0.01 + 1065
    leftUpperY = app.height * 0.735 - 32
    rightBottomX = app.width * 0.01 + 1105
    rightBottomY = app.height * 0.735 + 5
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 8, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# A10
def drawA10(app, canvas):
    roomNum = df.iat[103,0]
    roomEnergy = df.iat[103,1]
    num = df.iat[103,2]
    roomAvail = df.iat[103,3]
    leftUpperX = app.width * 0.01 + 1065
    leftUpperY = app.height * 0.735 + 5
    rightBottomX = app.width * 0.01 + 1105
    rightBottomY = app.height * 0.735 + 40
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 8, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# A4A
def drawA4A(app, canvas):
    roomNum = df.iat[104,0]
    roomEnergy = df.iat[104,1]
    num = df.iat[104,2]
    roomAvail = df.iat[104,3]
    leftUpperX = app.width * 0.01 + 1087
    leftUpperY = app.height * 0.735 + 40
    rightBottomX = app.width * 0.01 + 1140
    rightBottomY = app.height * 0.735 + 70
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 8, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# A2
def drawA2(app, canvas):
    roomNum = df.iat[105,0]
    roomEnergy = df.iat[105,1]
    num = df.iat[105,2]
    roomAvail = df.iat[105,3]
    leftUpperX = app.width * 0.01 + 1087
    leftUpperY = app.height * 0.735 + 70
    rightBottomX = app.width * 0.01 + 1140
    rightBottomY = app.height * 0.735 + 100
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 8, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# A4B
def drawA4B(app, canvas):
    roomNum = df.iat[106,0]
    roomEnergy = df.iat[106,1]
    num = df.iat[106,2]
    roomAvail = df.iat[106,3]
    leftUpperX = app.width * 0.01 + 1140
    leftUpperY = app.height * 0.735 + 3
    rightBottomX = app.width * 0.01 + 1180
    rightBottomY = app.height * 0.735 + 38
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 8, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

# A4C
def drawA4C(app, canvas):
    roomNum = df.iat[107,0]
    roomEnergy = df.iat[107,1]
    num = df.iat[107,2]
    roomAvail = df.iat[107,3]
    leftUpperX = app.width * 0.01 + 1140
    leftUpperY = app.height * 0.735 + 38
    rightBottomX = app.width * 0.01 + 1180
    rightBottomY = app.height * 0.735 + 110
    textX = (leftUpperX + rightBottomX) * 0.5
    textY = (leftUpperY + rightBottomY) * 0.49
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, textX - 3, textY + 8, num)  
    # Energy Efficiency
    drawEnergy(app, canvas, textX + 5, textY + 12, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, leftUpperX + 15, leftUpperY - 8, roomNum)

#################################################
# Draw Background and Other Components 
#################################################

def drawFloorPlan(app, canvas):
    canvas.create_image(app.width * 0.45, app.height * 0.55, \
    image = ImageTk.PhotoImage(app.image2))

def drawCMU(app, canvas):
    canvas.create_image(app.width * 0.075, app.height * 0.07, \
    image = ImageTk.PhotoImage(app.image4))

def drawLocationPoint(app, canvas):
    canvas.create_text(app.width * 0.5, app.height * 0.05, \
            text = 'Real-time View of Rooms in Porter Hall', \
            font = 'Times 30 bold', fill = 'black', anchor='n') 
    canvas.create_text(app.width * 0.2, app.height * 0.15, \
            text = ' Floor 1', \
            font = 'Times 25 bold', fill = 'black', anchor='n')   
    canvas.create_text(app.width * 0.75, app.height * 0.15, \
            text = ' Floor A', \
            font = 'Times 25 bold', fill = 'black', anchor='n')   

def drawEnergyLegend(app, canvas):
    # title
    canvas.create_text(app.width * 0.95, app.height * 0.9 - 25, \
            text = 'Energy Use', \
            font = 'Times 15 bold', fill = 'black', anchor='n')   
    X1 = app.width * 0.95
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
    canvas.create_text(app.width * 0.95, app.height * 0.8 - 25, \
            text = 'Availability', \
            font = 'Times 15 bold', fill = 'black', anchor='n')   
    X1 = app.width * 0.95
    X2 = X1 + 50
    Y1 = app.height * 0.8
    Y2 = Y1 + 20
    Y3 = Y2 + 20
    # avail
    canvas.create_rectangle(X1, Y1, X2, Y2, fill = app.availColor)
    canvas.create_text(X1 - 38, Y1, text = 'Availability',
            font = 'Times 10 bold', fill = 'black', anchor='n')   
    # unavail
    canvas.create_rectangle(X1, Y2, X2, Y3, fill = app.unavailColor)
    canvas.create_text(X1 - 38, Y2, text = 'Unavailability',
            font = 'Times 10 bold', fill = 'black', anchor='n')   # title

#################################################
# Run the Interface
#################################################
   
def redrawAll(app, canvas):
        drawCMU(app, canvas)
        drawFloorPlan(app, canvas)
        # FLOOR 1
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
        # FLOOR A
        drawA7C(app, canvas)
        drawA7BB(app, canvas)
        drawA7B(app, canvas)
        drawA7A(app, canvas)
        drawA1(app, canvas)
        drawA7D(app, canvas)
        drawA7E(app, canvas)
        drawA7F(app, canvas)
        drawA18B(app, canvas)
        drawA18D(app, canvas)
        drawA11(app, canvas)
        drawA15(app, canvas)
        drawA17(app, canvas)
        drawA44(app, canvas)
        drawA18C(app, canvas)
        drawA18A(app, canvas)
        drawA19(app, canvas)
        drawA19A(app, canvas)
        drawA19B(app, canvas)
        drawA19C(app, canvas)
        drawA19D(app, canvas)
        drawA46(app, canvas)
        drawA17C(app, canvas)
        drawA17B(app, canvas)
        drawA23(app, canvas)
        drawA21A(app, canvas)
        drawA21(app, canvas)
        drawA20(app, canvas)
        drawA20A(app, canvas)
        drawA22(app, canvas)
        drawA27(app, canvas)
        drawA27B(app, canvas)
        drawA27C(app, canvas)
        drawA27E(app, canvas)
        drawA27F(app, canvas)
        drawA27H(app, canvas)
        drawA27G(app, canvas)
        drawA27(app, canvas)
        drawA43(app, canvas)
        drawA14A(app, canvas)
        drawA12(app, canvas)
        drawA10(app, canvas)
        drawA4A(app, canvas)
        drawA2(app, canvas)
        drawA4B(app, canvas)
        drawA4C(app, canvas)
        drawLocationPoint(app, canvas)
        drawEnergyLegend(app, canvas)
        drawAvailLegend(app, canvas)

def runViewer():
    runApp(width = 1500, height = 800)

runViewer()