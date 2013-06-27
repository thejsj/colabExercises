"""
Problem:

Given a set number of points in space, a base position and a radius, find Which of these points are within the radius of that circle.

Radius is really nothing more than the distance of the farthest point inside the diameter of the circle so just calculate the distance between the two points. 

If the distances is less than the radius then the point is within the diameter of that circle.

"""

import random, math

# Set Field Size
widthOfSpace  = 1000
heightOfSpace = 1000

# Create 100 Random Points
positions = []
for i in range(100):
	thisPosition      = {}
	thisPosition["x"] = random.randint(0,widthOfSpace)
	thisPosition["y"] = random.randint(0,heightOfSpace)
	positions.append(thisPosition)

# Create Base Point and Radius
basePoint = {
	"x": random.randint(0,widthOfSpace),
	"y": random.randint(0,heightOfSpace),
	"r": 100 # arbitrary radius set by me 
}

# Define Funciton to see if they were withhin a set distance
def calculateDistance(x1,y1, x2,y2):
	return math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )

# Go through Each Random Point
pointsWithinRadius    = []
pointsNotWithinRadius = []
for position in positions:
	position["distanceToBasePoint"] = calculateDistance(position["x"],position["y"],basePoint["x"],basePoint["y"])
	if(position["distanceToBasePoint"] < basePoint["r"]):
		# this points is whithin the diameter of that circle
		pointsWithinRadius.append(position)
	else:
		# This point is not within the diamter of the circle
		pointsNotWithinRadius.append(position)
# Conclusion
print pointsWithinRadius
print basePoint
print "Points within Raidus    : ", len(pointsWithinRadius)
print "Points NOT within Raidus: ", len(pointsNotWithinRadius)