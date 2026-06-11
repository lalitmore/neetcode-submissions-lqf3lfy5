class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum())
        no_space_s = s.replace(" ", "").lower()
        for index, val in enumerate(no_space_s):
            if val != no_space_s[len(no_space_s) - index - 1]:
                return False
        return True
        