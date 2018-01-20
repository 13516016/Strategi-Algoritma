from models import Board, Space
from solver import CrosswordSolver
from parser import parse_file
import time, sys, os

def main():

	filename = sys.argv[1] 
	fpath = os.path.join('testcase',filename)
	
	f = open(fpath,"r")
	board, word_list = parse_file(f)
	length_list = set([len(word) for word in word_list])
	solver = CrosswordSolver(word_list)


	# get time

	pre_millis = int(round(time.time() * 1000))
	board.set_space_list(length_list)
	print()
	solver.solve_board(board) #solve board and print (not returning anything)
	post_millis = int(round(time.time() * 1000))

	print('\nSolved in', post_millis-pre_millis, 'ms')
main()