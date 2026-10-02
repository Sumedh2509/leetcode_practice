'''
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Example 1:

Input: nums = [3,4,5,6,1,2]

Output: 1
Example 2:

Input: nums = [4,5,0,1,2,3]

Output: 0
Example 3:

Input: nums = [4,5,6,7]

Output: 4
Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000

'''

class Solution:
    def findMin(self, nums: List[int]) -> int:

        #thoughts- the sequence is preserved
        #we can split this in two lists, [3,4,5,6] and [1,2] the first element of last/right half will always be minimum
        #[3, 4, 5, 6, 1, 2], l = 0, r = 5, and mid = 2
        # l = 3, r = 2, mid = 5 , at least 2 of them will lie in the same list
        # if l<mid l and mid lie in the same part , if r>mid r and mid lie in the same part

        res = nums[0]
        l, r = 0, len(nums)-1

        while l<=r:
            if nums[l] <= nums[r]: #this just means that the array is already sorted, so we just gotta print the left most value
                res = min(res, nums[l])
                break

            m = (l+r) //2  #mid pointer
            res = min(res, nums[m]) #find the minimum and store it
            if nums[l] <= nums[m]: #if the left pointer is less that means, mid and l belong to same chunk
                #that means we wanna check the right part 
                #as the left part is sorted 

                l = m+1 
            else:
                r= m-1
        return res


