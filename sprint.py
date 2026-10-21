class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        frequency = [[] for i in range(len(list)+ 1)]

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        for val, cnt in hashmap.items(): #this gives key value pair
            frequency[cnt].append(val)

        res = [] 
        for i in range(len(frequency)-1, 0, -1):
            res.append(frequency[i])
            if  len(res) == k:
                return res
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            row_list = []
            for element in row:
                if element.isdigit():
                    row_list.append(element)
            row_set = set(row_list)
            if row_list!= row_set:
                return False

        for row in board:
            col_list = [] 
            for i in range(len(row)-1):
                if row[i].isdigit():
                    col_list.append(i)
            col_set = set(col_list)
            if col_set != col_list:
                return False

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row  = defaultdict(set)
        col  = defaultdict(set)
        square  = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in row[i] or
                   board[i][j] in col[j] or
                   board[i][j] in square[i//3, j//3]):
                    return False
                row[i].append(board[i][j])
                col[j].append(board[i][j])
                square[i//3 , j//3].append(board[i][j])
        return True

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


def is_prime(n):
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
    
    # 2 is the only even prime number
    if n == 2:
        return True
        
    # Exclude all other even numbers
    if n % 2 == 0:
        return False
        
    # Check odd factors up to the square root of n
    # The loop condition i * i <= n is equivalent to i <= sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2  # Skip even numbers
        
    return True



        

