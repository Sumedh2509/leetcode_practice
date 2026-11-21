#valid sudoku 
#core idea was to create hashamps which had values in set  , we use sets cuz they can't have duplicates
#after that we loop through the entire board , skip over the empty spaces and add and check the valid elements 


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                #checking if the element already exists
                if (board[i][j] in rows[i] or 
                    board[i][j] in cols[j] or 
                    board[i][j] in box[i//3, j//3]):
                        return False
                cols[j].add(board[i][j])
                rows[i].add(board[i][j])
                box[i//3, j//3].add(board[i][j])
        return True