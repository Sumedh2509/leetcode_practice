'''
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.


Example 1:

Input: s = "zxyzxyz"

Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.


Example 2:

Input: s = "xxxx"

Output: 1

Constraints:

0 <= s.length <= 50,000
s may consist of printable ASCII characters.

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l , r = 0 , 1
        maxint = 0 
        seen_by_r = []
        while r < len(s):
            
            if s[l] != s[r] and s[r] not in seen_by_r:
                seen_by_r.append(s[r])
                r+=1 
                
            else:
                maxint = max(maxint, r-l)
                seen_by_r = []
                l = r 
                r+=1 
            
        return maxint