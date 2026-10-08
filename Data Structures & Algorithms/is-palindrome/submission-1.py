class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        rev = ""

        for c in s:
            if c.isalnum():
                rev = rev + c.lower()
        
        if rev == rev[::-1]:
            return True
        else:
            return False
        
