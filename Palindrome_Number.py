class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Convert the number to a string to check palindrome property
        x_str = str(x)
        return x_str == x_str[::-1]
sol = Solution()
print(sol.isPalindrome(121))  
print(sol.isPalindrome(-121)) 
print(sol.isPalindrome(10))   
