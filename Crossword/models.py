import time
class Space:

	HORIZONTAL = 1
	VERTICAL = 2

	def __init__(self, start, end):
		self.start = start
		self.word = ''
		self.end = end
		self.intersection = set()
		self.orientation = 0

	def get_length(self):
		if (self.start[0]==self.end[0]):
			return abs(self.start[1]-self.end[1])+1
		else:
			return abs(self.start[0]-self.end[0])+1

	def get_intersection(self):
		return self.intersection

	def get_relative_position(self,position):

		if (self.start[0] == position[0]):
			return (position[1]-self.start[1])
		elif (self.start[1] == position[1]):
			return (position[0]-self.start[0])
		else:
			return None

class Board:
	'Crossword Board model'

	black = '#'
	white = '-'

	def __init__(self,size,table = []):
		self.size = size
		self.space_list_horizontal = []
		self.space_list_vertical = []
		self.table = table

	def set_board(self,table):
		self.table = table
		self.default = table

	def reset_board(self):
		self.table = self.default

	def print_board(self):
		for rows in self.table:
			for item in rows:
				print(item,end="")
			print('')



	def set_space_list(self,length_list):
		# horizontal
		self.space_list_horizontal = self.parse_space_list(self.table,Space.HORIZONTAL,length_list)
		self.space_list_vertical = self.parse_space_list(Board.transpose_board(self),Space.VERTICAL,length_list)
		
		# swap for vertical space_list
		for space in self.space_list_vertical:
			i,j = space.start
			k,l = space.end
			space.start = j,i
			space.end = l,k

		self.get_intersections()

		print ('Getting grids...')


	def transpose_board(board):
		return([ ''.join([row[i] for row in board.table]) for i in range(board.size)])


	def parse_space_list(self,table,orientation,length_list):
		space_list = []
		join_table = []

		for i,row in enumerate(table):
			rows = ''.join(table[i])
			join_table.append(rows)

		for i,line in enumerate(join_table):
			spaces = line.split('#')
			if ' ' in spaces:
				spaces.remove(' ')
			count = 0
			j=0
			for space in spaces:
				if (space!=''):
					space_obj = Space((i,j+count), (i,j+count+len(space)-1))
					space_obj.orientation = orientation
					count+=1
					j+=len(space)
					if(space_obj.end[1]-space_obj.start[1]>=1):
						space_list.append(space_obj)
				else:
					j+=1

		return space_list

				
	def get_intersections(self):
		for space_h in self.space_list_horizontal:
			for space_v in self.space_list_vertical:
				for i in range(space_h.start[1],space_h.end[1]+1):
					for j in range(space_v.start[0], space_v.end[0]+1):
						if ((space_h.start[0],i) == (j,space_v.start[1])):
							space_v.intersection.add((j,i))
							space_h.intersection.add((j,i))



	# Class functions
	def is_white(self,row,column):
		return (self.table[row][column] == Board.white)
	
	def is_black(self,row,column):
		return (self.table[row][column] == Board.black)

