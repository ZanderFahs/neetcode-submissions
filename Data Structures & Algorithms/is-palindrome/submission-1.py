class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = "".join([c for c in s.lower() if c.isalnum()])
        rev = result[::-1]
        if rev == result:
            return True
        else:
            return False