################################################
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
    app.r = 3

#################################################
# Room Num
#################################################

def drawRoomNum(app, canvas, x, y, num):
    canvas.create_text(x, y + 10, text = num, font = 'Times 8 bold', \
        fill = 'black', anchor='n')
  
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
    canvas.create_text(x, y, text = num, font = 'Times 12', fill = 'white', anchor='n')    
                        
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

def drawRoom(app, canvas, roomNum, roomEnergy, num, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY):
    # Availability
    drawAvailability(app, canvas, roomAvail, leftUpperX, leftUpperY, rightBottomX, rightBottomY)
    # People Num 
    drawPeopleNum(app, canvas, (rightBottomX - leftUpperX)* 0.5 + leftUpperX, (rightBottomY - leftUpperY) * 0.22 + leftUpperY, num)  
    # Energy Use
    drawEnergy(app, canvas, (rightBottomX - leftUpperX)* 0.8 + leftUpperX, (rightBottomY - leftUpperY) * 0.32 + leftUpperY, roomEnergy) 
    # Room Num
    drawRoomNum(app, canvas, (rightBottomX - leftUpperX)* 0.5 + leftUpperX, (rightBottomY - leftUpperY) * 0.32 + leftUpperY, roomNum)

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
        for index, row in df.iterrows():
            drawRoom(app, canvas, row['Room'], row['EnergyUse'], row['PeopleNum'], row['Availability'], row['leftUpperX'], row['leftUpperY'], row['rightBottomX'], row['rightBottomY'])
        drawLocationPoint(app, canvas)
        drawEnergyLegend(app, canvas)
        drawAvailLegend(app, canvas)

def runViewer():
    runApp(width = 1500, height = 800)
    
runViewer()