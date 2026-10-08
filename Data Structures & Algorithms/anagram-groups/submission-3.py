class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        states = {}
        for word in strs:
            count = 26*[0]
            for s in word:
                count[ord(s)-ord('a')] += 1
            key = tuple(count)
            if key in states:
                states[key].append(word)
            else:
                states[key] = [word]
        return list(states.values()) 



        