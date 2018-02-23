import operator
from operations import *
import matplotlib.pyplot as plt

class ConvexHull:
	"""
	 Make an object that generates the ConvexHull 
	"""
	def __init__(self, point_list):
		self.point_list = point_list
		self.convex_hull = []
		self.__get_convex_hull()

	def __add_convex_hull_point(self,point):
		self.convex_hull.append(point)

	def print_convex_hull(self):
		print("Convex hulls :")
		for hull in self.convex_hull:
			print(hull)
		print()

	def print_points(self):
		print("Points :")
		for point in self.point_list:
			print(point)
		print()

	def __get_left_convex_hull(self,point_1,point_n,points):
		if (len(points)!=0):
			# Sort by distance from line and get the farthest point
			line = get_line_equation(point_1,point_n)
			points = sorted(points, key=lambda x: get_point_distance_from_line(x,line), reverse=True)
			farthest_point = points[0]
			# Add the farthest point to the solution set
			self.__add_convex_hull_point(farthest_point)
			points.remove(farthest_point)
			# Recurse 
			left_points_1 = get_left_points_from_line(point_1,farthest_point,points)
			self.__get_left_convex_hull(point_1,farthest_point,left_points_1)
			left_points_2 = get_left_points_from_line(farthest_point,point_n,points)
			self.__get_left_convex_hull(farthest_point,point_n,left_points_2)
		
	def __get_right_convex_hull(self,point_1,point_n,points):
		if (len(points)!=0):
			line = get_line_equation(point_1,point_n)
			# Sort by distance from line and get the farthest point
			points = sorted(points, key=lambda x: get_point_distance_from_line(x,line), reverse=True)
			farthest_point = points[0]
			# Add the farthest point to the solution set
			self.__add_convex_hull_point(farthest_point)
			points.remove(farthest_point)
			# Recurse
			right_points_1 = get_right_points_from_line(point_1,farthest_point,points)
			self.__get_right_convex_hull(point_1,farthest_point,right_points_1)
			right_points_2 = get_right_points_from_line(farthest_point,point_n,points)
			self.__get_right_convex_hull(farthest_point,point_n,right_points_2)

	def __get_convex_hull(self):
		# Sort the points based on the absis value
		points = self.point_list
		points.sort()
		# Get the leftmost and the rightmost point
		point_1 = points[0]
		point_n = points[-1]
		# Add the leftmost and rightmost point to the solution set
		self.__add_convex_hull_point(point_1)
		self.__add_convex_hull_point(point_n)

		# DIVIDE AND CONQUER
		# Solve left and right points 
		left_points = get_left_points_from_line(point_1,point_n,points)
		right_points = get_right_points_from_line(point_1,point_n,points)
		self.__get_left_convex_hull(point_1,point_n,left_points)
		self.__get_right_convex_hull(point_1,point_n,right_points)

		return self.convex_hull

	def draw_graph(self):
		points = self.point_list
		convex_hull  = self.convex_hull
		x_points = [item[0] for item in points]
		y_points = [item[1] for item in points]
		
		# Create polygon to plot
		polygon = make_polygon(convex_hull)
		polygon_x = [item[0] for item in polygon]
		polygon_y = [item[1] for item in polygon]

		# Plot points, convex hull and line that the convex hull makes
		plt.title("Convex Hull")
		plt.plot(x_points,y_points,'bo')
		plt.plot(polygon_x ,polygon_y,'k-')
		plt.plot(polygon_x ,polygon_y,'ro',markersize=3)
		plt.show()
