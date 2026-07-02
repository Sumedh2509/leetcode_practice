class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #sorted array method
        array = sorted(nums)
        i,j  = 0 , len(nums) -1
        curr = array[i] + array[j]
        while True:
            if curr > target:
                j -=1 
            elif curr< target:
                i+=1 
            else:
                return [min(nums.index(array[i] ), nums.index(array[j] )) , max(nums.index(array[i] ), nums.index(array[j] ))] 
            
#problem with index ---


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqS= [0]* 26 #creating an array with 26 values set to 0
        for i in range(len(s)):
            freqS[ord(s[i])- ord('a')] +=1 
            freqS[ord(t[i])- ord('a')] -=1 
            
        for val in freqS:
            if val != 0:
                return False
        return True
#i can do freq method? , already in dict method? 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        storage = []
        for num in nums: 
            if num in storage:
                return True
            storage.append(num)
        return False

#using ord func? and creating an array of 26? 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_table = [0] *26
        for i in range(len(s)):
            freq_table[ord[i]- ord['a']] +=1 
            freq_table[ord[i]- ord['a']] -=1 
        for val in freq_table:
            if val != 0:
                return False
        return True
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i,j = 0 , len(nums)-1
        sorted_nums = nums.sort()
        curr = sorted_nums[i]+ sorted_nums[j]
        while curr != target:
            if curr > target:
                j -=1 
            elif curr< target: 
                i+=1 
        return [nums.index(sorted_nums[i]), nums.index(sorted_nums[j])] 
    


        