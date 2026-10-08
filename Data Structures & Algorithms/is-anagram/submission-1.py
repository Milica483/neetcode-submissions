class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_set = set(s)
        for letter in anagram_set:
            if s.count(letter) != t.count(letter):
                return False
        if len(s) != len(t):
            return False
        else:
            return True