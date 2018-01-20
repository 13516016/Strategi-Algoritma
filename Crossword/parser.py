from models import Board, Space

def parse_file(file):
	file_content = file.read().splitlines()
	size = file_content[0]
	size = int(size)

	board = parse_board(file_content, size)
	word_list = parse_word(file_content,size)

	return board, word_list



def parse_board(file_content,size):
	board = Board(size)
	rows = []
	table = []
	for i in range(1,board.size+1):
		rows.append(file_content[i])

	table = [[item for item in row] for row in rows]

	for line in table:
		if (' ' in line):
			line.remove(' ')
	
	board.set_board(table)

	return board


def parse_word(file_content, size):
	words = file_content[size+1]
	word_list = words.split(";")

	return word_list