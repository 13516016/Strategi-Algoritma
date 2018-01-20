from models import Board,Space
import copy 
class CrosswordSolver:

    def __init__(self,word_list):
        self.word_list = word_list
        self.size = len(word_list)
        

    def solve_board(self,board):
        print('Solving....')
        space_list = board.space_list_horizontal + board.space_list_vertical
        word_list = self.word_list
        space_list.sort(key=lambda x:x.get_length(), reverse=True)
        word_list.sort(key = lambda x: len(x), reverse=True)
        words = [i.word for i in space_list]


        board = self.backtrack(board,space_list,word_list,0)  
        if (board==False):
            print('cant')    
        # board.print_board()

    def backtrack(self,board,space_list,word_list,idx):   
        
        if (len(word_list)==0):
            board.print_board()
            return True

        new_word_list = copy.deepcopy(word_list)
        new_board = copy.deepcopy(board)
        for word in new_word_list:
            if(self.fillable(new_board,space_list[idx],word)):
                word_list = new_word_list.remove(word)
                idx+=1
                if(self.backtrack(new_board,space_list,new_word_list,idx)):
                    return True   
            new_board = copy.deepcopy(board)
            # new_word_list = copy.deepcopy(word_list)


        return False


    def fillable(self,board,space,word):
        return (space.get_length()==len(word) and self.check_boards(board,space,word))

    def check_boards(self,board,space,word):
        if(space.orientation == Space.HORIZONTAL):
            return CrosswordSolver.fill_horizontal(board,space,word)
        else:
            return CrosswordSolver.fill_vertical(board,space,word)

    def fill_horizontal(board,space,word):
        idx = 0
        row = space.start[0]
        for col in range(space.start[1],space.end[1]+1):
            if ((board.table[row][col] == Board.white) or (board.table[row][col] == word[idx])):
                board.table[row][col] = word[idx]
                idx+=1
            else:
                return False
        return True

    def fill_vertical(board,space,word):
        idx = 0
        col = space.start[1]

        for row in range(space.start[0],space.end[0]+1):
            if ((board.table[row][col] == Board.white) or (board.table[row][col] == word[idx])):
                board.table[row][col] = word[idx]
                idx+=1
            else:
                return False
        return True
