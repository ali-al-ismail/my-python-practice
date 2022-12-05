import math
import matplotlib.pyplot # use for plotting
import numpy



def trajectory(throwAngle,throwVelocity):
  
    g = 9.81
    initialVelocity = throwVelocity
    angleRadians = math.radians(throwAngle)
    timeOfFlight = 2*initialVelocity*math.sin(angleRadians)/g
    time = numpy.linspace(0,timeOfFlight,1000) # create evenly spaced list of 1000 numbers for time from 0s to timeOfFlight 


    # x = Vx * time / Vx = initialVelocity * cos(theta)
    # y = initialHeight + (Vy * time - ((g*time*time)/2))
    newXPos = (initialVelocity * math.cos(angleRadians) * time) # calculate the x position for each value of time calculated in the previous line
    newYPos =  (initialVelocity * math.sin(angleRadians)* time) - 0.5*g*time**2
    
    matplotlib.pyplot.plot(newXPos,newYPos) # use the x and y positions to plot the trajectory
    matplotlib.pyplot.xlabel("Distance") # add labels to the axes in meters
    matplotlib.pyplot.ylabel("Height")
    matplotlib.pyplot.show() # show the plot window