#!/usr/bin/python

# Questions:
# How do I specify an optional property of a class instance
# ie optional intersection human description


class Segment:
	'This is a line between two points or intersections. It may or may not represent a straight as-the-crow-flies segment'
	count = 0
	fakeMax = "3:30"
	fakeMin = "1:45"

	def __init__(self, intersection1, intersection2, numLanes):
		self.intersection1 = intersection1
		self.intersection2 = intersection2
		self.numLanes = numLanes
		Segment.count += 1

	def getDescription(self):
		print "This segment goes from", self.intersection1,"to", self.intersection2,"and is", self.numLanes, "lane(s) wide."

	def getMaxTime(self):
		print "STUB: The max recorded time for this segment is", fakeMax

	def getMinTime(self):
		print "STUB: The max recorded time for this segment is _____"


class Intersection:
	'This is an intersection. Or from another point of view, this is a point of decision.'
	count = 0

	def __init__(self, lat, lon, type):
		Intersection.count += 1
		self.lat = lat
		self.lon = lon
		self.type = type

	def getCoords(self):
		print "Lat:", self.lat, "Lon:", self.lon


class IntersectionType:
	'This decribes intersection types, ie stoplight, 4-way stop, yield, interchange, etc'
	count = 0
	STOPLIGHT = "STOPLIGHT"
	FOURWAY = "Four way stop"


	def __init__(self, type):
		IntersectionType.count += 1
		self.type = type


class Route:
	'This represents a series of segments chained together constituting a definite route from a place to another place.'
	count = 0

	def __init__(self, Segment): #not sure how to do this... an array of segments?
		self.Segment = Segment
		Segment.count += 1

	def getSegments(self):
		fakeStart = "23.23, 43.32"
		fakeDestination = "44.522, 110.234"
		
		print "This route starts at", fakeStart, "then goes to"
		for segment in 'fakeySegs':
			# loop over each intersection in the route
			print "an intersection", segment
		print "then arrives at", fakeDestination

	def getMinTime(self):
		# loop through each segment and get the minimum time and add up
		print "9.49"

	def getMaxTime(self):
		# loop through each segment and get the max time and add up
		print "15.39"

	def getAvgTime(self):
		# loop through each segment and get the average time and add up
		print "12.10"

class GPSFile:
	'A class that represents a gps track to be split into segments'
	count = 0

	def __init__(self, file):
		self.file = file

	def getStartTime(self):
		# TODO load file and read start time/date
		print "STUB: Started 2016-01-01 08:34"

	def getStopTime(self):
		# TODO load file and read stop time/date
		print "STUB: Stoped 2016-01-01 08:34"

 class GPSPoint
 	'This should represent an entry/point/node in a GPS file'
 	def __init__(self):

	
# Examples!

print "----------------[ Some Facts ]-----------------------"
print ""
print "Segment.__doc__: ", Segment.__doc__
print "Intersection.__doc__: ", Intersection.__doc__
print "IntersectionType.__doc__: ", IntersectionType.__doc__
print "Route.__doc__: ", Route.__doc__
print ""
print "----------------[ end Facts ]-----------------------"
print ""

a = Intersection(40.733556, -111.820297, "STOPLIGHT")
print "a.getCoords: ", a.getCoords()

x = Segment("21st","17th",1)
y = Segment("13th","Foothill",1)
z = Segment("Foothill","17th",1)

print "Segment x: ", x.getDescription()
print "Segment y: ", y.getDescription()
print "Segment z: ", z.getDescription()
print "There are now", x.count, "segments"

print "IntersectionType.STOPLIGHT:", IntersectionType.STOPLIGHT