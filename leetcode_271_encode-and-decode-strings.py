'''
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

String encode(List<String> strs) {
    // ... your code
    return encoded_string;
}
Machine 2 (receiver) has the function:

List<String> decode(String encoded_string) {
    // ... your code
    return decoded_strs;
}
So Machine 1 does:

String encoded_string = encode(strs);
and Machine 2 does:

List<String> decoded_strs = decode(encoded_string);
decoded_strs in Machine 2 should be the same as the input strs in Machine 1.

Implement the encode and decode methods.

Example 1:

Input: strs = ["Hello","World"]

Output: ["Hello","World"]
Explanation:

Solution solution = new Solution();
String encoded_string = solution.encode(strs);

// Machine 1 ---encoded_string---> Machine 2

List<String> decoded_strs = solution.decode(encoded_string);

Example 2:

Input: strs = [""]

Output: [""]

Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains any possible characters out of 256 valid ASCII characters.
Follow up: Could you write a generalized algorithm to work on any possible set of characters?
'''

class Solution:
    import random
    import string
    chars = " " + string.ascii_letters + string.digits + string.punctuation
    chars = list(chars)
    key = chars.copy()
    random.shuffle(key)
    def encode(self, strs: List[str]) -> str:
        # encoded_text = ""
        result= []
        for word in strs:
            encoded_text = ""
            for letter in word:
                index = self.chars.index(letter)
                encoded_text+= self.key[index]
            result.append(encoded_text)
        return " ".join(result)
            
            
    def decode(self, s: str) -> List[str]:
        to_decode = s.split()
        decoded_list = []
        if len(to_decode) == 0:
            return [""]
        else:
            for  word in to_decode:
                decoded_text = ""
                for letter in word:
                    index = self.key.index(letter)
                    decoded_text += self.chars[index]
                decoded_list.append(decoded_text)
            return decoded_list
                
#this is way too unnecessary - doesn't make much secure either - waste
# test = "cats are gods"
# test_list = []
# for i in test:
#     test_list.append(i)
# print(test_list)

#idea is to create a delimiter and having the length of string in order to encode it 
#knowing this we can decode properly - encoded string will have - length followed by our delimeter , ex - 6#sumedh
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+= str(len(s))+"#"+s
        return res
    def decode(self, s: str) -> List[str]:
        res =[]
        i= 0 
        while i< len(s):
            j = i
            while s[j] != "#":
                j +=1
            length = int(s[i:j]) #j is exclusive 
            res.append(s[j+1:j+1+length])
            i = j+1+length
        return res

