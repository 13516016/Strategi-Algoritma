from operations import *
from ConvexHull import ConvexHull
import time

def main():
	n = int(input("Enter the number of points: "))
	try:
		points = generate_random_points(n) # Generate random points
		
		pre_run = time.process_time()*1000 
		hull = ConvexHull(points) # Make a convex hull object that solves the convex hull
		post_run = time.process_time()*1000
		runtime = post_run - pre_run # Get the algorithm runtime

		print("Solved in", format(runtime,'.2f'), "ms")
		hull.draw_graph() # Draw convex hull
	except Exception as e:
		print("Point invalid")
	
	
	
if __name__ == '__main__':
	main()
