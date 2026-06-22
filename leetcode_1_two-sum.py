'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
Constraints:

2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000
Only one valid answer exists.
'''

#my_plan - run nested loops - check if the sum of i + j = target , if yes then add to list 

#my solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = [] #creating list to store the answer #index of numbers 
        for i in range(len(nums)):
            for j in range (i+1 , len(nums)):
                if nums[i] + nums[j] == target:
                    answer.append(i)
                    answer.append(j)
                else:
                    continue
        return answer
    

#hash-map 2 pass 
#plan - sort the array , put a point at start one at end (i,j) , if sum of i and j is > target , move j to left , if< taret , move i to right

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = nums
        sorted_nums.sort()
        i = 0 
        j = len(nums) -1
        while True:
            if sorted_nums[i] + sorted_nums[j] > target:
                j -= 1
            elif sorted_nums[i] + sorted_nums[j] < target:
                i+=1 
            else:
                return [nums.index(sorted_nums[i]),nums.index(sorted_nums[j])] #this is a problem - .index() always returns
            #the closest index - so if list is like [5,5 ] it will return  [0,0] instead of [0,1]

#plan - create a sort of hashmap - where index and value are stored together              
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_array = []
        for i, val in  enumerate(nums):
            # sorted_array.append(i, val) #Python sorts tuples/lists lexicographically - it compares the first element first, then the second if needed.
            #we want to sort w.r.t val thus we use: 
            sorted_array.append([val, i]) #storing lists
        sorted_array.sort() 
        i,j = 0 , len(nums) -1 
        while True:
            if sorted_array[i][0] + sorted_array[j][0] > target: #accessing the first element of the list 
                j -=1 
            elif sorted_array[i][0] + sorted_array[j][0] < target:
                i +=1
            else:
                #return [sorted_array[i][1], sorted_array[j][1]] #i and j are indices in the sorted array, not the original array!
            
                return [min(sorted_array[i][1], sorted_array[j][1]) , 
                        max(sorted_array[i][1], sorted_array[j][1])]
# nums = [3, 6, 4], target = 7
# sorted_array = [[3, 0], [4, 2], [6, 1]]
                #    ↑ original index


#hasmap - one pass
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums): #iterating 
            diff = target - n #find complement 
            if diff in prevMap: 
                return [prevMap[diff], i] #return if we find it 
            prevMap[n] = i #store if we don't find it 


        