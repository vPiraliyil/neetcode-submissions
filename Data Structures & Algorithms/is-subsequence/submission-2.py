class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        string = 0
        sub = 0
        if not s:
            return True
        while string < len(t) and sub < len(s):
            if t[string] == s[sub]:
                sub += 1
                string += 1
            else:
                string += 1
            if sub == len(s):
                return True
            
        return False