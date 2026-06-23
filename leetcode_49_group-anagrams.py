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
#my_plan  = idea 1  - separate strings of equal length --> make hashmaps (frequency tables) --> append in the list those who have equal hashmaps
#my solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_list = []
        equal_len = []
        for i in strs:
            length = len(i)
            for j in range(len(strs)):
                if length == len(strs[j+1]):
                    equal_len.append([strs[i], strs[j+1]]) 

                    
# strs = ["act","pots","tops","cat","stop","hat"]  
# equal_len = []
# for i in strs:
#     length = len(i)
#     for j in range(len(strs)):
#         if length == len(strs[j+1]):
#             equal_len.append([strs[i], strs[j+1]])
# print(equal_len)
'''
strs = ["act","pots","tops","cat","stop","hat"]
equal_len = []

for i, word in enumerate(strs):
    for j in range(i + 1, len(strs)):
        if len(word) == len(strs[j]):
            equal_len.append([word, strs[j]])

print(equal_len)
# '''

# Hint 1
# A naive solution would be to sort each string and group them using a hash map. 
# This would be an O(m * nlogn) solution

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_list = defaultdict(list) #creates a dict - with empty list for keys- keys:[] for every key it creates an empty list 
        for str in strs: #iterating over the given list of strs
            sortedS = ''.join(sorted(str))  #we use ''.join method cuz sorted() gives a list - we are converting it back to a string using .join
            final_list[sortedS].append(str)  #creates the sorted string -as a key- and appends any string that on sorting gives this key as the value of that key
            #Use the sorted string as a key, and append the original string to its list.
        return list(final_list.values()) #return values 
    

#best solution - 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #same as above
        for s in strs: #iterating through each string
            count = [0] * 26 #creating an array of 26 - every value at the beginning is 0 
            for c in s: #going over the character in the string which we are currently iterating 
                count[ord(c) - ord('a')] += 1  #ord - coverts a character to its ASCII number- 'a' - 97 , 'b' - 98 ...., 'z' = 122 - subtracting ord(a)  - to match 
                #the index of our count array 
            res[tuple(count)].append(s)  #making it a tuple  -cuz list can't play the role of key in a dict/hashmap
            #above line is like saying - assign s (as value) to the tuple of count
        return list(res.values())  #returning the list
        
                
            
        