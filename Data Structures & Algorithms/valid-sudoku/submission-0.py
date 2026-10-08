class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        help_row = []
        help_column = []

        for row in board:
            for num in row:
                if num>="1" and num<="9":
                    help_row.append(num)
            help_row_set = set(help_row)
            if len(help_row_set) != len(help_row):
                return False
            help_row = []
        
        for i in range(9):
            for row in board:
                if row[i]>="1" and row[i]<="9":
                    help_column.append(row[i])
            help_column_set = set(help_column)
            if len(help_column_set) != len(help_column):
                return False
            help_column = []

        box = dict()   
        for i in range(9):
            for j in range(9):
                a = i//3
                b = j//3
                c = [a,b]
                c = tuple(c)
                if (a,b) in box:
                    if board[i][j] != ".":
                        box[c].append(board[i][j])
                else:
                    box[c] = []
                    if board[i][j] != ".":
                        box[c].append(board[i][j])

        for key, value in box.items():
            value_help = list(value)
            value_help_set = set(value_help)
            if len(value_help_set)!= len(value_help):
                return False
        
        return True

