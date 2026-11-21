#container with most water 
#the core idea was somehow using 2 pointers and finiding area , what I don't properly 
#remember was the condition to move pointers


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0 , len(heights)-1 
        maxA = 0
        while l<r: 
            area = min(heights[l], heights[r])*(r-l)
            maxA = max(maxA , area)

            if heights[l] > heights[r]:
                r-=1
            elif heights[l] < heights[r]:
                l+=1
            else:
                l+=1

        return maxA

