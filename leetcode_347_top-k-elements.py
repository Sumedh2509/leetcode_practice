'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.
'''

#ideas - 
#idea 1 - create a hashmap - which stores frequencies - key(numbers) : value(freuqencies) - get k(amount) keys whose frequency is higher
#idea 2 -to create keys - first convert our list to tuple and then covert the tuple back to list 
# this will remove the duplicates -covert back to list cuz tuples are unordered
#first create a dict with all the keys - and give them value of 0 - so we can later add
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqN= {} 
        my_list = list(set(nums)) #set deletes duplicates - converting to list makes it iterable -set isn't iterable
        final_list = [] 
        for item in my_list:
            freqN[item] = 0  #setting initial frequency of each key to 0 
        for i in range(len(nums)):
            freqN[nums[i]] = 1+ freqN.get(nums[i], 0 ) #making real frequency tables
        sorted_dict = dict(sorted(freqN.items(), key= lambda x:x[1])) #sorting the dictionairy w.r.t values
        sorted_list= list(sorted_dict.items()) #coverting the dict to list
        sorted_list.reverse() #reversing
        
        for freq in range(k): 
            final_list.append(sorted_list[freq][0]) #appending keys to the list
        return final_list


