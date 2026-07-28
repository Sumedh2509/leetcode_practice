'''
You are given an integer array heights where heights[i] represents the height of the 
i
t
h
i 
th
  bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:



Input: height = [1,7,2,5,4,7,3,6]

Output: 36
Example 2:

Input: height = [2,2,2]

Output: 4
Constraints:

2 <= height.length <= 1000
0 <= height[i] <= 1000

'''
#ideas- we could brute force by checking multiplications and compare them (use max function)
#I am assuming that the distance between per bar is 1 unit, 
#while finding the area , height must be that of the smaller bar amonngst the picked ones 
#note - while iterating through the list the width is ever increasing 
#maybe we can use the principal of minima maxima 

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areas = [] #list to append all the areas that we find 
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                width = j-i
                height = min(heights[i], heights[j])
                area = height*width
                areas.append(area)
        return max(areas)

#the two pointer appraoch 
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1 #creating the pointers
        res = 0   #to store areas

        while l < r:
            area = min(heights[l], heights[r]) * (r - l) 
            res = max(res, area) #updating the value of res 

            #we know shifting pointers means reducing the width-
            #so we shift the pointer which will cause the least change in height 
            if heights[l] < heights[r]:  
                l += 1           
            elif heights[l] > heights[r]:
                r -=1
            else: #any 1 works
                r -= 1
        return res


