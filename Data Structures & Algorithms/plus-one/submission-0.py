class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        num = 0
        for i in range(len(digits)):
            num = num * 10 + digits[i] 
        
        num = num + 1
        
        while num > 0:
            ans.append(num % 10)
            num = num // 10
        
        ans.reverse()
            
        return ans