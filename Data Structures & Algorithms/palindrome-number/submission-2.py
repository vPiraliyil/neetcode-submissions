class Solution:
    def isPalindrome(self, x: int) -> bool:
      y = 0
      og = x

      if x < 0:
        return False

      while x > 0:
        digit  = x % 10
        y = y * 10 + digit
        x = x // 10

      if y == og:
        return True

      return False 