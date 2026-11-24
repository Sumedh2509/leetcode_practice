'''
You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:

Input: s = "AAABABB", k = 1

Output: 5
Constraints:

1 <= s.length <= 100,000
0 <= k <= s.length
s consists of only uppercase english characters.

'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l , r = 0 , 1
        maxv = 0 
        maxfreq = {}
        while r<len(s):
            lenwid = r - l + 1

            #counting the frequency in current window 
            for i in range(r-l+1):
                maxfreq[i] = 1 + maxfreq.get(maxfreq[i], 0)

            freq = max(maxfreq.values()) 

            cost = lenwid - freq
            while cost<=k:
                if cost<=k:
                    r+=1
                    maxv = max(maxv , lenwid) 
                else:
                    l+=1 

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0 
        l = 0 
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while r-l+1 -max(count.values())>k:
                count[s[l]] -=1 
                l+=1 
            res = max(res, r-l+1)
        return res            


