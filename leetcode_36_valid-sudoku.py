'''
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.

Example 1:



Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: true
Example 2:

Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: false
Explanation: There are two 1's in the top-left 3x3 sub-box.

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.

'''

#thoughts - it'll be easy to check duplicates in a row and in column ,difficult to do so in the box - 3x3
#for checking duplicates in row , we could just run a nested for loop to compare each item in the list -use len set and len list?- won't work cuz of them dots- use .isdigit()?        
#for checking duplicates in col , we could run a nested for loop for i'th element in each list and compare - -just brute force - 
#for checking duplicates in box - 
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #checking for duplicates in row-
        # row_list =[] #shouldn't be here 
        # col_list =[]
        for row in board:
            row_list =[] #need to make it here , so that the list resets for every row
            for element in row:
                if element.isdigit(): #to eliminate the dots
                    row_list.append(element)
                row_set = set(row_list)
            if len(row_set) != len(row_list):
                return False
            
        #checking for duplicates in col- 
        for i in range(9):
            col_list =[] 
            for row in board:
                if row[i].isdigit(): #to eliminate dots
                    col_list.append(row[i])
            col_set = set(col_list)
            if len(col_set) != len(col_list):
                return False
            
        #checking for duplicates in sub-box
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #making dicts whose default value will be a set- it can be a list/array too 
        rows = defaultdict(set)  #for checking duplicates in rows
        cols = defaultdict(set)  #for checking duplicates in cols
        box = defualtdict(set)   #for checking duplicates in sub-boxes

        for i in range(9):       #iterating over the lists in big list
            for j in range(9):   #iterating over the elements in the lists(inside ones)
                if board[i][j] == ".":  #ignore if the element is blank/. 
                    continue                 
                if (board[i][j] in rows[i] or   #checking if that element is already stored in our i'th dict of rows 
                    board[i][j] in cols[j] or   #checking if that element is already stored in our j'th dict of cols
                    board[i][j] in box[i//3 , j//3]): #checking if that element is already in our sub-box,  dividing by three makes it 0,1,2
                        return False  
                cols[j].add(board[i][j])           #add that element in if it isn't in it 
                rows[i].add(board[i][j])
                box[i//3 , j//3].add(board[i][j])
        return True  #if it executes completely , then it is a valid sudoku 




           