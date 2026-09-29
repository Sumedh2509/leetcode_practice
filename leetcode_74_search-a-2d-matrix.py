'''
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1:



Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

Output: true
Example 2:



Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15

Output: false
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10000 <= matrix[i][j], target <= 10000
'''

#idea-  we can just iterate through each row and perform binary search on each of them
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_list = [item for sublist in matrix for item in sublist]
        for row in matrix: #selects one of the list

            l ,r = 0 , len(row)-1
            while l<=r:
                m = (l+r)//2
                if row[m] < target:
                    l = m+1
                elif row[m] > target:
                    r = m-1
                else:
                    return True
        return False


#trying another approach
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_list = [item for sublist in matrix for item in sublist]
        # for row in matrix: #selects one of the list

        l ,r = 0 , len(flat_list)-1
        while l<=r:
            m = (l+r)//2
            if flat_list[m] < target:
                l = m+1
            elif flat_list[m] > target:
                r = m-1
            else:
                return True
        return False
            

#using double binary search, first on the whole matrix -we find the optimal row 
#then on the row itself 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0]) 

        l, r = 0, ROWS * COLS - 1 #setting up pointers
        while l <= r: 
            m = l + (r - l) // 2 #setting up middle for binary search 
            row, col = m // COLS, m % COLS 
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False


def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    ROWS, COLS = len(matrix), len(matrix[0])  # no of rows is just amount of lists , length of one list is amount of coloumns

#given - The first integer of every row is greater than the last integer of the previous row.

    #finding the optimal row/array first 
    top, bot = 0, ROWS - 1 #top and bottom row 
    while top <= bot: 
        row = (top + bot) // 2  #getting to the middle of rows
        if target > matrix[row][-1]:  #checks the last element of the row that we selected , if it is greater than target 
            #that means the left half of the search is useless 
            top = row + 1
        elif target < matrix[row][0]: #checks the first element of the row that we selected , if it is greater than target 
            #that means the right half of the search is useless
            bot = row - 1
        else:
            break

    #if we don't find anything , that just means it doesn't exist 
    if not (top <= bot):
        return False

    #after obtaining the optimal row
    row = (top + bot) // 2 #know this value is what we found after finding up 
    l, r = 0, COLS - 1 #setting up the pointers for that row 

    #just binary search 
    while l <= r:
        m = (l + r) // 2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True
    return False