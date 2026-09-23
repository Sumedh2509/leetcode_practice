'''
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in 
O
(
l
o
g
n
)
O(logn) time.

Example 1:

Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3
Example 2:

Input: nums = [-1,0,2,4,6,8], target = 3

Output: -1
Constraints:

1 <= nums.length <= 10000.
-10000 < nums[i], target < 10000
All the integers in nums are unique.


'''
#the basic O(n) method
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i 
        return -1

#in binary search , we keep tearing the list into half 
#check middle value, if greater than target, cut the right part
#check middle value, if less than target, cut the left part
class Solution:
    def search(self, nums: List[int], target:int) -> int:
        l , r = 0 , len(nums) - 1  #initializing pointers
        
        while l<=r : #we nee that equal ,, just in case there is only single element left
            m = (l+r)//2
            
            if nums[m] > target: #cutting the right part out
                r = m-1
            elif nums[m] < target: #cutting the left part out
                l = m+1
            else:
                return m
        return -1 #in case we don't find anything, return -1