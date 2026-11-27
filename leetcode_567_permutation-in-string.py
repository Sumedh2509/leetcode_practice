'''
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Example 1:

Input: s1 = "abc", s2 = "lecabee"

Output: true
Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

Example 2:

Input: s1 = "abc", s2 = "lecaabee"

Output: false
Constraints:

1 <= s1.length, s2.length <= 10000
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)

        #if s1 is greater than s2 there is no way to find a permutation in s2
        if n > len(s2):
            return False

        # frequency map of s1
        freqs1 = {}
        for ch in s1:
            freqs1[ch] = 1 + freqs1.get(ch, 0)

        #frequency map till the first n letter (len of s1)
        winfreq = {}
        for i in range(n):
            ch = s2[i]
            winfreq[ch] = 1 + winfreq.get(ch, 0)


        #if we find it right here just return truee
        if winfreq == freqs1:
            return True

        #untill this part and above it we defined our window, this window moves rigidly 
        #both the pointers move together
        
        #making the window move
        for r in range(n, len(s2)):
            
            ch_in = s2[r]
            winfreq[ch_in] = 1 + winfreq.get(ch_in, 0)

            
            ch_out = s2[r - n]
            winfreq[ch_out] -= 1

            #this basically deletes that key 
            if winfreq[ch_out] == 0:
                del winfreq[ch_out]

            if winfreq == freqs1:
                return True

        return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False

        #freq map of s1 
        freqs1 = {}

        #building the window itself
        window = {}
        for i in range(n):
            freqs1[s1[i]] = 1 + freqs1.get(s1[i] , 0)
            window[s2[i]] = 1 + window.get(s2[i] , 0) #this is our window 

        if freqs1 == window: return True

        #moving the window and adjusting frequencies while doing that 
        for i in range(n , len(s2)):
            #adjusting frequency of the element that gets in 
            window[s2[i]] = 1 + window.get(s2[i] , 0)

            #adjusting frequency of the element that goes out 
            window[s2[i - n ]] -= 1 

            #deleting the keys 
            if window[s2[i-n]] == 0:
                del window[s2[i-n]]

            if window == freqs1:
                return True
        return False



        