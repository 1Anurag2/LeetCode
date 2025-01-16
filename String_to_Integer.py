class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        i = 0
        n = len(s)
        while i < n and s[i].isspace():
            i += 1
        
        if i == n:
            return 0
        
        sign = 1
        if s[i] == '+' or s[i] == '-':
            if s[i] == '-':
                sign = -1
            i += 1
        
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            # Check for overflow and underflow conditions
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1
        
        return sign * result
sol = Solution()
result = sol.myAtoi(" -042")
print(result)  
