class Solution:
    def findMin(self, nums: List[int]) -> int:

        res = nums[0]

        l , r = 0 , len(nums)-1 

        while l<=r:
            if nums[l] <= nums[r]:
                return min(res, nums[l])
            m = (l+r)//2 
            res = min(res, nums[m])

            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1

        return res

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l , r = 0 , len(nums)-1
        while l<=r:
            if nums[l] <= nums[r]: #condition that the array is already sorted
                return min(res , nums[l])
            m = (l+r)//2
            res = min(res, nums[m])

            if nums[l] <= nums[m]:
                l = m+1
            else:
                r = m-1
        return res