'''question - Given an integer array nums, 
return true if any value appears more than once in the array, 
otherwise return false.
example1- 
Input: nums = [1, 2, 3, 3]

Output: true
example 2 - 
Input: nums = [1, 2, 3, 4]

Output: false
'''

#plan - take input from user , append the values in a list and a set 
# list can have duplicates, sets cant
#if length of list> length of set - return true, else return false


#my attempt
'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        is_running = True
        arr = [] #list
        numbers = set()
        
        while is_running:
            
            array = input("Enter the numbers(q to quit):")

            if not array.isdigit():
                print("Wrong input")
                
            elif array == "q":
                is_running = False
            else:
                array = int(array)
                arr.append(array)
                numbers.add(array)
        if len(arr) > len(numbers):
            return True
        else:
            return False
'''
#solution 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        arr = [] #list
        numbers = set()
        for val in nums:
            arr.append(val)
            numbers.add(val)
        if len(arr) > len(numbers):
            return True
        else:
            return False

#mistakes 
'''
1. you do not take input from user - the input is already given to you in competitive questions
2. sets are created as --> variable = set()
3. You add value to sets using .add() not .append()
            

'''

#best solution - 

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = set() #creates a set - set can't have duplicate values
        for val in nums: #iterating over the values in nums
            if val in numbers: #if value is already in numbers set
                return True  
            numbers.add(val) #if it isn't in numbers- we add that value
        return False #if the whole for loop executes- that means there were no duplicates- hence return false
    
#brute force solution  - 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)): #iterating over the given list
            for j in range(i+1 , len(nums)): #iteratres from the next number of till the end of array(list)
                if nums[i] == nums[j]: #checks if they are equal  
                    return True #returns true if they are equal 
        return False
#at i = 0--> inner loop starts at j = 1 and goes till j = n(n = length of the array), and then it goes back to outer loop 
        
#sort method - better than brute force method cuz, u have to only check everything once
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()  #you can directly sort it 
        for i in range(1, len(nums)): 
            if nums[i] == nums[i - 1]: #checks adjacent values 
                return True
        return False