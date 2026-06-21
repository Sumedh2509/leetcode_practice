'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string,
but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
'''

#plan/idea - iterate over s and compare every value with every value in t - using nested loops? 
#my solution 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_list = list(s)
        for letter in t:
            if letter in s_list:
                s_list.remove(letter)
            else:
                return False
        return True
# s= racecar, t = carrace 
#s = jam , t = jar
# string = "Sumedh"
# print(string[0])

#sorting method 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): #first check if their length are equal 
            return False

        return sorted(s) == sorted(t)  #sorts them in alphabetical order - works cuz there is no capital letters
    
# string1 = "sumedh" 
# string2 = "edhmus"

# print(sorted(string1), sorted(string2)) 
'''-----------------------------------------------------'''
#hasmap - dictionairy method (the best method)

#plan - check frequencies and store them , if the dicts end up equal , it is an anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = {}
        freqT = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)): #len of s or t
            freqS[s[i]] = 1 + freqS.get(s[i], 0)
            freqT[s[i]] = 1 + freqT.get(s[i], 0)
        return freqT == freqS
    
    
