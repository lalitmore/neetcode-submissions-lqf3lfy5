class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        s = "".join(char for char in s if char.isalnum())
        print(s)
        reversed_s = "".join((reversed(s)))
        print(reversed_s)
        if s == reversed_s:
            return True
        return False
        