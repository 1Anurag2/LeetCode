class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(s: str, left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # Odd length palindrome
            pal1 = expand_around_center(s, i, i)
            # Even length palindrome
            pal2 = expand_around_center(s, i, i + 1)
            
            # Update the longest palindrome found
            if len(pal1) > len(longest):
                longest = pal1
            if len(pal2) > len(longest):
                longest = pal2

        return longest


solution = Solution()
s1 = "babad"
s2 = "cbbd"
print(solution.longestPalindrome(s1))  
print(solution.longestPalindrome(s2))  