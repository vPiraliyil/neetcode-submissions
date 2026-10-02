class Solution:
    def isPalindrome(self, s: str) -> bool:
       left = 0
       right = len(s) - 1 
       s = s.lower()

       while left < right:
            if self.is_alphanum(s[left]) == False:
                left += 1
                continue
            if self.is_alphanum(s[right]) == False:
                right -= 1
                continue
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            else:
                return False

       return True

    def is_alphanum(self, char):
        if char >= '0' and char <= '9':
            return True
        if char >= 'a' and char <= 'z':
            return True
        return False
            


