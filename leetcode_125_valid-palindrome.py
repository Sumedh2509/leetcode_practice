'''
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. 
It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", 
which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.
'''

#thoughts- I could just make s a single string and reverse it and compare with original
# could I use two pointers? one at the beginning and one at the end? that too would need making it a single string
# stop the loop when their index is same

#I need to also make sure that every letter is small (not capital)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = []
        for char in s:
            lower_char = char.lower()
            if lower_char.isalnum():
                s_list.append(lower_char)
        new_s = ""
        for char in s_list:
            new_s += char
        reversed_s = new_s[::-1]
        if new_s == reversed_s:
            return True
        else:
            return False
        

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1 #two pointers , one at beginning and one at end 

        while l < r: 
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
    #creating a function yourselves that checks if the char is alphanum instead of using a .isalnum()
    def alphaNum(self, c):
        #ord gives index of that char in ASCII
        return (ord('A') <= ord(c) <= ord('Z') or  #checking if it comes between capital letters
                ord('a') <= ord(c) <= ord('z') or  #checking if it comes between smaller letters 
                ord('0') <= ord(c) <= ord('9'))    #checking if it comes between digits
        