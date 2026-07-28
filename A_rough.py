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
            freq_table[ord[i]- ord['a']] +=1  #wronggg
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
    

#valid anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0]*26
        for i in range(len(s)):
            freq[ord(s[i])-ord('a')]+=1
            freq[ord(t[i])-ord('a')]-=1
        for val in freq:
            if val!= 0:
                return False
        return True

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map ={}

        for i , n in enumerate(nums):
            diff = target -n 
            if diff in map:
                return [map[diff], i]
            map[n] = i 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for str in strs:
            a= [0]*26
            for c in str:
                a[ord(c)-ord('a')] +=1 
            res[tuple(a)].append(s)

        return list(res.values())
    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #making hashmap to store freq
        buckets = [[] for i in range(len(nums)+1)] #create that many lists inside a list making it a 2d list

        for num in nums: #this loop will create frequency table
            count[num] = 1 + count.get(num, 0) 
        for num, cnt in count.items():
            buckets[cnt].append(num)
        
        res =[]
        for i in range(len(buckets)-1 , 0 , -1):
            res.append(buckets[i])
            if len(res) == k:
                return res

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
