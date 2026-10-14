class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        sett = set()
        max_len = 0

        for right in range(len(s)):
             while s[right] in sett:
                 sett.remove(s[left])
                 left += 1
                 
             if s[right] not in sett:
                sett.add(s[right])
                max_len = max(max_len, len(sett))
        return max_len