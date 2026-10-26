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
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")":"(", "]":"[", "}":"{"}
        for char in s:
            if char in hashmap:
                if stack and stack[-1] == hashmap[char]:
                    stack.pop()
            else:
                stack.append(char)
        return True if not stack else False

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i , n in enumerate(nums):
            diff = target - n
            if diff in map:
                return [map[diff], i]
            map[n] = i 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #creating a dict where values will be lists
        for char in strs:
            count = [0]*26 #creating an array for each character 
            for c in char:
                count[ord[c]-ord["a"]] +=1
            res[tuple(count)].append(char)
        return list(res.values())

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i , n in enumerate(nums):
            diff = target - n 
            if diff in map:
                return [map[diff], i ]
            map[n] = i 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_list = []
        for i in range(len(nums)):
            prev_prod = 1
            for num in nums[:i]:
                prev_prod *= num

            forw_prod = 1
            for num in nums[i+1:]:
                forw_prod *= num

            final_prod = prev_prod*forw_prod
            product_list.append(final_prod)
        return product_list


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a>0:
                break

            if i>0 and a == nums[i-1]:
                continue

            l, r = 0, len(nums)-1
            while l<r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0 :
                    r-=1 
                elif threesum < 0 :
                    l+=1
                else:
                    res.append([a, nums[l], nums[r]])
                    r-=1 
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1 
        return res


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areas = []
        for i in range(len(heights)):
            for j in range(i+1 , len(heights)):
                height = heights[i]
                width = j-i
                area = height*width
                areas.append(area)
        return max(areas)

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l= 0 , r = len(heights)-1
        while l < r:
            area = min(heights[r], heights[l]) * (r-l)
            res = max(res, area)

            if heights[l] > heights[r]:
                r-=1
            elif heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return res

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevmap = {}
        
        for ind, val in enumerate(nums):
            diff = target-val
            if diff in prevmap:
                return [prevmap[diff], ind]
            prevmap[val] = ind

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums): #iterating 
            diff = target - n #find complement 
            if diff in prevMap: 
                return [prevMap[diff], i] #return if we find it 
            prevMap[n] = i #store the index of that number and that number as the key 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = {}
        final_list = []
        for i in nums:
            freqmap[i] = freqmap.get(i, 0) + 1  # Fix 1
        sorted_list = sorted(freqmap.items(), key=lambda x:x[1], reverse=True)
        for i in range(k):
            final_list.append(sorted_list[i][0])  # Fix 2
        return final_list

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final_list= []
        for i in range(len(nums)):
            prevprod =1 
            for i in range(nums[:i]):
                prevprod *= i

            forwprod = 1
            for i in range(nums[i+1:len(nums)-1]):
                forwprod *= i

        totalprod = prevprod*forwprod
        final_list.append(totalprod)

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
        pdt_list = []
        for i in range(len(nums)):
            product_prev = 1  
            for num in nums[0:i]:
                product_prev *= num
            
            product_forw = 1 
            for num in nums[i+1::]:
                product_forw *= num
            
            final_ans = product_prev * product_forw
            pdt_list.append(final_ans)
        return pdt_list

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l ,r = 0, len(heights)-1 #setting the pointers upp
        res = 0 
        while l<r:
            width = r-l
            length = min(heights[r], heights[l])
            area= length*width
            res = max(res, area)

            if heights[l] > heights[r]:
                r-=1
            elif heights[l] < heights[r]:
                l+=1
            else:
                r-=1 
        return res

class Solution:
    def search(self, nums: List[int], target:int) -> int:
        l,r = 0, len(nums)-1

        while l<=r:
            m = (l+r)//2
            if nums[m]> target:
                r = m-1
            else:
                l = m+1
        return m


def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    top , bot = 0 , len(matrix)-1

    while top<=bot:
        row = (top+bot)//2
        if matrix[row][-1] < target:
            top = row+1
        elif matrix[row][0] > target:
            bot = row-1
        else:
            break #we also have to search withing this row 

    if not (top<=bot):
        return False
    
    row = (top+bot)//2
    l ,r = 0, len(matrix[row])-1

    while l<=r:
        m = (l+r)//2
        if matrix[row][m]==target:
            return True
        elif matrix[row][m]>target:
            r = m-1
        else:
            l= m+1
        
    return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            row = (top + bot) // 2
            # BUG: You wrote "if row[-1]>target" but row is an INDEX (integer), not the actual row data!
            if matrix[row][-1] < target:  # FIXED: Use matrix[row][-1]
                top = row + 1
            # BUG: You wrote "elif row[0] < target" same issue
            elif matrix[row][0] > target:  # FIXED: Use matrix[row][0]
                bot = row - 1
            else:
                break  # BUG: You wrote "return False" but should break to search within this row!

        # BUG: You didn't check if the row is valid after the loop
        if not (top <= bot):
            return False

        row = (top + bot) // 2
        l, r = 0, len(matrix[row]) - 1  # FIXED: Added matrix[row] to get actual row

        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] == target:  # FIXED: Check if EQUAL first
                return True
            elif matrix[row][m] < target:
                l = m + 1
            else:
                r = m - 1
        
        # BUG: You wrote "return True" but should return False (didn't find target!)
        return False  # FIXED: Return False if not found


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in prevmap:
                return [prevmap[diff] , index]
            prevmap[value] = index


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums): #iterating 
            diff = target - n #find complement 
            if diff in prevMap: 
                return [prevMap[diff], i] #return if we find it 
            prevMap[n] = i #store the index of that number and that number as the key 


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0 , len(s)-1 
        while l<r:
            #inner loops are for skipping junk
            while l<r and not self.isalnum(s[l]):
                l+=1
            while l<r and not self.isalnum(s[r]):
                l+=1
            if s[l].lower() != s[r].lower():
                return False
            l , r = l+1, r+1
        return True


    def isalnum(self, c):
        return(ord('A')<ord(c)<ord('Z')) or (ord('a')<ord(c)<ord('z')) or (ord('0')<ord(c)<ord('9'))

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0 , len(numbers)-1
        #return 1-indexed list
        while l<=r:
            if numbers[l] + numbers[r] > target:
                r -=1
            else:
                l+=1
        return [l+1 , r+1]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #remember we can't have duplicates in it , so find a way to eliminate when shit duplicates
        res =[]
        nums.sort()

        
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue #this will remove the duplicate pivotes
            l , r = i+1 , len(nums)-1
            target = 0 - nums[i]
            while l<=r:
                #there might be duplicates in poniters themselves tho
                
                if nums[l]+ nums[r] > target:
                    r-=1
                elif nums[l] + nums[r] < target:
                    l+=1
                else:
                    res.append(nums[i] , nums[l], nums[r])
                    l +=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1

        return res 
'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #the idea was to count frequency and store similar words using frequency
        #frequency was counted using ord function
        #you used a hashmap , which had the sorted word as the key , and u assigned that word as the value to that key
        #what I don't recall is how do you even make the key 

        hashmap = defaultdict(list) 

        #trying to make keys - 
        for str in strs:
            sorted_str = ''.join(sorted(str)) #creating the key for each string
            hashmap[sorted_str].append(str) #hashmap mai , sorted_str naam ki key banao , aur usme orignal string store karo
        return list(hashmap.values())


#the best method , make frequency tables - use them as the keys and store string that match similar frequency in list of that key

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap= defaultdict(list)

        for str in strs:
            count = [0]*26 #creating a big ahh list
            for char in str:
                count[ord[char]- ord['a']] +=1  
            hashmap[tuple(count)].append(str)
        return list(hashmap.values())

class Solution:
    def search(self, nums: List[int], target:int) -> int:

        l , r = 0 , len(nums)-1

        while l<=r:
            m = (l+r)//2
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1


# Example 1:

# Input: nums = [3,4,5,6,1,2]

# Output: 1
# Example 2:

# Input: nums = [4,5,0,1,2,3]

# Output: 0
# Example 3:

# Input: nums = [4,5,6,7]

# Output: 4

class Solution: #return the minimum in rotated sorted array
    def findMin(self, nums: List[int]) -> int:
        #the concep was to find where things break  
        #the concept - we wanna find, if we are left portion or right portion of the rotated sorted array
        
        #if we are in left portion - we search the right portion 
        #in a rotated sorted array (rsa) it makes sense that in this case, the min will lie in the right portion
        #as when we rotate, we take the max value and put it in the first 
        #so minimum becomes the left most value of our right portion 

        #if we are in right portion - we search in left portion 
        #by being in right portion it just means (our pivot exists in left portion)
        #our middle value is in right portion so anything that is to the right of it will be greater than it is
        #so we search to the left


        res = nums[0]
        l , r = 0 , len(nums)-1

        

        while l<=r:
            if nums[l] <= nums[r]: #condition that the array is already sorted
                return min(res, nums[l])
            m = (l+r)//2
            res = min(res, nums[m])

            if nums[l] <= nums[m]:
                l = m+1
            else:
                r = m-1
        return res


class Solution:
    def search(self, nums: List[int], target: int) -> int: