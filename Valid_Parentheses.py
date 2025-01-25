class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to hold matching pairs of brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        # Stack to hold opening brackets
        stack = []
        
        for char in s:
            if char in bracket_map:
                
                top_element = stack.pop()  if stack else '#'

                if bracket_map[char] != top_element:
                    return False
            else:

                stack.append(char)
        return not stack

solution = Solution()
print(solution.isValid("()"))      
print(solution.isValid("()[]{}"))  
print(solution.isValid("(]"))      
