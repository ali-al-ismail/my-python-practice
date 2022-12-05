import math
import matplotlib.pyplot # use for plotting
import numpy


# takes the angle in degrees and velocity in m/s of the projectile and plots the trajectory

def trajectory(throwAngle,throwVelocity):
  
    g = 9.81
    initialVelocity = throwVelocity
    angleRadians = math.radians(throwAngle) # convert to radians for math functions
    timeOfFlight = 2*initialVelocity*math.sin(angleRadians)/g # formula for time of flight
    time = numpy.linspace(0,timeOfFlight,1000) # create evenly spaced list of 1000 numbers for time from 0s to timeOfFlight 


    # x = Vx * time / Vx = initialVelocity * cos(theta)
    # y = initialHeight + (Vy * time - ((g*time*time)/2))
    newXPos = (initialVelocity * math.cos(angleRadians) * time) # calculate the x, y positions for each value of time calculated in the previous line
    newYPos =  (initialVelocity * math.sin(angleRadians)* time) - 0.5*g*time**2
    
    matplotlib.pyplot.plot(newXPos,newYPos) # use the x and y positions to plot the trajectory
    matplotlib.pyplot.xlabel("Distance") # add labels to the axes in meters
    matplotlib.pyplot.ylabel("Height")
    matplotlib.pyplot.show() # show the plot window




# example usage: trajectory(45, 10) # 45 degree angle, 10 m/s velocity