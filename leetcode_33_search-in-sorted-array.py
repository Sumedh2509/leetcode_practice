'''
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

You may assume all elements in the sorted rotated array nums are unique,

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Example 1:

Input: nums = [3,4,5,6,1,2], target = 1

Output: 4
Example 2:

Input: nums = [3,5,6,0,1,2], target = 4

Output: -1
Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-1000 <= target <= 1000
All values of nums are unique.
nums is an ascending array that is possibly rotated.
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        
        
        l, r = 0, len(nums) - 1 #setting up pointers
        
        while l <= r:  # equal in case that our list only contains one value 
            mid = (l + r) // 2  #setting up mid value
            if target == nums[mid]: 
                return mid
            
            # left sorted portion
            if nums[l] <= nums[mid]:  #this means m belong to left portion
                if target > nums[mid] or target < nums[l]: 
                    #first cond - simply means our target lies in the right portion
                    #second cond - in this case, there are 2 possibilites - when our mid is in left portion and target is less than mid
                    #our answer is either in left part (elements in the left portion which are ofc less than mid) or to the right after the pivot
                    #so we compare with our left most value if it is less than target we just move to right 
                    l = mid + 1

                else: #targete is smaller than mid and greater than left most value nums[l]
                    r = mid - 1

            # right sorted portion
            else: #when our mid is in the right portion - pivot lies in the left portion
                if target < nums[mid] or target > nums[r]: 
                    #first cond - our target lies in the left portion
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1