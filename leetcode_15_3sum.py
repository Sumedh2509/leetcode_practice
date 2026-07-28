'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, 
and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:

Input: nums = [0,1,1]

Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

3 <= nums.length <= 1000
-10^5 <= nums[i] <= 10^5

'''
#thoughts - first make an compliment- like subtract 1st element from 0 and let that be the target
#           and then use two pointer method to reach that target
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res =[]
        for num in nums:
            complement = 0 - num
            i ,j = nums.index(num), len(nums)-1 
            while i<j:
                curr = nums[i] + nums[j]
                if curr< complement:
                    j -=1  
                elif curr> complement:
                    i+=1 
                else:
                    res.append([nums.index(num),i, j ])
                    break
        return res
    
#mistakes- didn't sort the array....... and we aren't supposed to return index, return the numbers themselves 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums2 = sorted(nums) #we could've just done , nums.sort() , that'd be better, les mmemory
        res = [] #list to store answers
        for i in range(len(nums)): #iterating over nums2
            if i > 0 and nums2[i] == nums2[i-1]:
                continue
            complement = 0 - nums2[i] #creating a complement basically turns it into a 2 sum questions , just the target is diff everytime
            l, r = i+1 , len(nums)-1 # intializing our pointers , we need i+1 cuz checking previous ones is useless and will cause potential errors
            while l < r:            #breaks when they meet 
                #same logic as two sum question
                curr_sum = nums2[l] + nums2[r] 
                if curr_sum < complement:
                    l+=1
                elif curr_sum> complement:
                    r-=1 
                else:
                    res.append([nums2[i],nums2[l], nums2[r]] )
                    l+=1 #we need to increment this pointers otherwise curr_same becomes same and cuases it to keep appending the res 
                    r-=1 # which makes it an infinite loop
        if len(res)>1:
            res.pop()
        return res

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums2 = sorted(nums)
        res = []
        for i in range(len(nums)):
            complement = 0 - nums2[i]
            l, r = i+1 , len(nums)-1
            while l < r:
                curr_sum = nums2[l] + nums2[r]
                if curr_sum < complement:
                    r-=1
                elif curr_sum> complement:
                    l+=1
                else:
                    res.append([nums2[i],nums2[l], nums2[r]] )
                    l+=1
                    r-=1
        res_set = set(res)
        list_res = list(res_set)
        return list_res

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]: #removes duplicate complements
                continue
            complement  = 0 - nums[i]
            l, r = i+1 , len(nums)-1
            while l < r: 
                curr_sum = nums[l] + nums[r]
                if curr_sum>complement:
                    r-=1
                elif curr_sum<complement:
                    l+=1
                else:
                    res.append([nums[i],nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l+=1
                    while l<r and nums[r] == nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return res



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res