import math

class Solution:
    def isPerfectSquare(self, num) -> bool:
        if not isinstance(num, int) or num < 0:
            return False  
        value = math.isqrt(num)
        return value * value == num

sol = Solution()
print(sol.isPerfectSquare(16))    
print(sol.isPerfectSquare(21))    
print(sol.isPerfectSquare(98.4))  
