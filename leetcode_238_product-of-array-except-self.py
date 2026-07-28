'''
Given an integer array nums, return an array output where output[i] 
is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O(n)
O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
Constraints:

2 <= nums.length <= 1000
-20 <= nums[i] <= 20

'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pdt_list =[] #creating a list to return at the end
        for i in range(len(nums)): #going thru the given list of nums
            answer = 1 
            for num in nums[0:i]:
                product_prev = answer*num
                answer = product_prev
            answer2 =1
            for num in nums[i+1::]:
                product_forw = answer2*num
                answer2 = product_forw
            final_ans = product_prev*product_forw
            pdt_list.append(final_ans)
        return pdt_list


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pdt_list = []
        for i in range(len(nums)):
            product_prev = 1  #we have to initialize this otherwise the loop doesn't run 
            for num in nums[0:i]:
                product_prev *= num
            
            product_forw = 1 
            for num in nums[i+1::]:
                product_forw *= num
            
            final_ans = product_prev * product_forw
            pdt_list.append(final_ans)
        return pdt_list
    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res