class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        countsS = {}
        for char in s:
            countsS[char] = countsS.get(char, 0) + 1

        countsT = {}
        for char in t:
            countsT[char] = countsT.get(char, 0) + 1

        if countsS == countsT:
            return True


        return False