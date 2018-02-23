import random
from math import sqrt

def generate_random_points(n):
	""" 
		Generate random n points 
	"""
	points = []
	for i in range(n):
		x = random.uniform(0,n)
		y = random.uniform(0,n)
		point = [x,y]
		points.append(point)
	return points

def get_points_location(point_1,point_n,points_list):
	"""
		Get points location (left/right)
		Will be used in get left/right points
	"""
	left_points = []
	right_points = []
	for point in points_list:
		determinant = get_determinant(point_1,point_n,point)
		if ( determinant > 0):
			left_points.append(point)
		elif (determinant < 0):
			right_points.append(point)
	return (left_points, right_points)

def get_determinant(point_1,point_n,point_x):
	"""
		point_1 = (x1,y1)
		point_2 = (x2,y2)
		point_x = (x3,y3)
		Get the determinant of a matrix:
		| x1 y1 1 |
		| x2 y2 1 |
		| x3 y3 1 |
	"""
	x1,y1 = point_1
	x2,y2 = point_n
	x3,y3 = point_x

	return (x1*y2 + x3*y1 + x2*y3 - x3*y2 - x2*y1 - x1*y3) 

def get_left_points_from_line(point_1,point_n,points_list):
	""" 
		Return points that located on the 'left' of the line (counter-clockwise)
	"""
	return get_points_location(point_1,point_n,points_list)[0]

def get_right_points_from_line(point_1,point_n,points_list):
	""" 
		Return points that located on the 'right' of the line (clockwise)
	"""
	return get_points_location(point_1,point_n,points_list)[1]

def get_line_equation(point_1,point_2):
	""" 
		Get line equation (ax+by+c=0) where :
		[0] = a
		[1] = b
		[2] = c
	"""
	a = (point_2[1]-point_1[1]) 
	b = (point_1[0]-point_2[0]) 
	c = (point_2[0]*point_1[1]) - (point_1[0]*point_2[1])

	return a,b,c

def get_point_distance_from_line(point,line):
	""" 
		Returns the distance from line to point
	"""
	a = line[0]
	b = line[1]
	c = line[2]

	x = point[0]
	y = point[1]

	return ( abs(a*x + b*y + c) / sqrt(a**2 + b**2) )

def get_point_distance_from_point(point_1,point_2):
	"""
		Returns the distance from point to point
	"""
	x1,y1 = point_1
	x2,y2 = point_2
	return sqrt((x2-x1)**2 + (y2-y1)**2)

def make_polygon(points):
	""" make the polygon from point so pyplot can plot it correctly """
	
	# Get the leftmost and rightmost points
	points.sort()
	leftmost = points[0]
	rightmost = points[-1]

	# Get the left points based on the line made from leftmost and rightmost points
	left_points = get_left_points_from_line(leftmost,rightmost, points)
	right_points = get_right_points_from_line(leftmost,rightmost,points)

	# Sort clockwise
	left_points.sort()  # Sort based on ascending x
	right_points.sort(reverse=True) # Sort based on descending x 
	
	result = left_points +  right_points + [left_points[0]]

	return result
