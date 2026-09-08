'''
You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the total amount of water that can be trapped between the bars.


Example 1:



Input: height = [0,2,0,3,1,0,1,3,2,1]

Output: 9
Constraints:

1 <= height.length <= 20,000
0 <= height[i] <= 100,000

'''


#idea - iterate over the whole array , keep pointers for left and right of the iteration (i-1 and i+1)
# to calc the water stored- (min(height[i-1], height[i+1])) - height[i] --> we subtract height of i cuz that iteration could have a solid block 
#have to think on how to handle edge cases

#ineffieceint solution 
class Solution: 
    def trap(self, height: List[int]) -> int:
    
        if not height:  #to avoid running into an infinite loop
            return 0
        count = 0 #to store water
        for i in range(len(height)): #iterating over the array 
            leftmax= rightmax = height[i] #intializing
            for l in range(0,i): #finding the leftmax value/height
                leftmax = max(leftmax, height[l])
            for r in range(i+1 , len(height)): #finding the rightmax value/height
                rightmax = max(rightmax, height[r])
            count += min(leftmax, rightmax) - height[i] #formula
        return count

            
#making 2 arrays which store max left and max right
#using min(leftmax, rightmax) - height[i] [remember to not add values which are negative]

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n== 0: #if there i nothing in list return 0 
            return 0 
        #intializing the arrays
        leftmax =[0]*n
        rightmax = [0]*n

        #setting the first value to first value of height
        leftmax[0] = height[0]
        #filling the array 
        for i in range(1,n):
            leftmax[i] = max(leftmax[i-1], height[i])
        rightmax[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            rightmax[i] = max(rightmax[i+1], height[i])
        
        count = 0
        for i in range(n):
            count += min(leftmax[i] , rightmax[i]) - height[i]
        return count

