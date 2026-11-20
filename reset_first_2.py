#group anagrams

#core idea was to create a frequency map and use that frequency map as the key in our hashmap
#and store the words as value


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list) #a hashmap where each key stores a list

        #to count frequency 
        for str in strs:
            freq = [0]*26
            for s in str:
                freq[ord(s)- ord('a')] += 1
            hashmap[tuple(freq)].append(str)

        return list(hashmap.values())